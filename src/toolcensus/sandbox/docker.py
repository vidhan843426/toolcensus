"""Docker/Podman sandbox. Two phases:

1. ``prepare``: ``docker build`` an image from a digest-pinned base, ``npm install`` the exact
   version (network on, install scripts *off* unless explicitly overridden).
2. ``run_command``: ``docker run`` with no network, read-only rootfs + tmpfs, non-root user,
   all capabilities dropped, no-new-privileges, CPU/memory/PID limits.
"""

from __future__ import annotations

import asyncio
import hashlib
import os

from toolcensus.config import SandboxSettings
from toolcensus.sandbox.runner import InstallFailedError, LaunchSpec

DOCKERFILE = """\
FROM {base}
ARG PKG
ENV NODE_ENV=production NPM_CONFIG_UPDATE_NOTIFIER=false NPM_CONFIG_FUND=false \\
    NPM_CONFIG_AUDIT=false NPM_CONFIG_LOGLEVEL=error
WORKDIR /app
RUN npm init -y >/dev/null \\
 && npm install --omit=dev --no-package-lock {scripts_flag} "$PKG" \\
 && chmod -R a+rX /app
"""

#: Only these variables reach the *docker CLI* (never the container).
_CLI_ENV_KEYS = (
    "PATH",
    "HOME",
    "DOCKER_HOST",
    "DOCKER_CONTEXT",
    "DOCKER_CONFIG",
    "XDG_RUNTIME_DIR",
)


def sandbox_flags(settings: SandboxSettings) -> list[str]:
    return [
        "--rm",
        "-i",
        "--network",
        "none",
        "--read-only",
        "--tmpfs",
        f"/tmp:rw,nosuid,nodev,size={settings.tmpfs_size}",
        "--user",
        settings.user,
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges",
        "--cpus",
        settings.cpus,
        "--memory",
        settings.memory,
        "--memory-swap",
        settings.memory,
        "--pids-limit",
        str(settings.pids),
        "--ipc",
        "none",
        "--workdir",
        "/tmp",
        "-e",
        "HOME=/tmp",
        "-e",
        "NODE_ENV=production",
        "--label",
        "toolcensus.sandbox=1",
    ]


class DockerRunner:
    def __init__(self, settings: SandboxSettings | None = None) -> None:
        self.settings = settings or SandboxSettings()

    def cli_env(self) -> dict[str, str]:
        return {k: os.environ[k] for k in _CLI_ENV_KEYS if k in os.environ}

    def image_tag(self, spec: LaunchSpec) -> str:
        key = (
            f"{self.settings.base_image}|{spec.package}@{spec.version}|{spec.allow_install_scripts}"
        )
        return f"{self.settings.image_prefix}:{hashlib.sha256(key.encode()).hexdigest()[:16]}"

    async def _run(self, *argv: str, stdin: bytes | None = None, timeout: float) -> tuple[int, str]:
        proc = await asyncio.create_subprocess_exec(
            self.settings.engine,
            *argv,
            stdin=asyncio.subprocess.PIPE if stdin is not None else asyncio.subprocess.DEVNULL,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
            env=self.cli_env(),
        )
        try:
            out, _ = await asyncio.wait_for(proc.communicate(stdin), timeout=timeout)
        except TimeoutError:
            proc.kill()
            await proc.wait()
            return -1, "timeout"
        return proc.returncode or 0, out.decode("utf-8", "replace")

    async def prepare(self, spec: LaunchSpec) -> str:
        tag = self.image_tag(spec)
        code, _ = await self._run("image", "inspect", tag, timeout=30)
        if code == 0:
            return tag
        dockerfile = DOCKERFILE.format(
            base=self.settings.base_image,
            scripts_flag="" if spec.allow_install_scripts else "--ignore-scripts",
        )
        code, out = await self._run(
            "build",
            "--quiet",
            "-t",
            tag,
            "--build-arg",
            f"PKG={spec.package}@{spec.version}",
            "--label",
            "toolcensus.sandbox=1",
            "-",
            stdin=dockerfile.encode(),
            timeout=self.settings.build_timeout_s,
        )
        if code != 0:
            raise InstallFailedError(out[-2000:])
        return tag

    def run_command(self, image: str, spec: LaunchSpec, name: str) -> list[str]:
        env_flags = [x for k, v in sorted(spec.env.items()) for x in ("-e", f"{k}={v}")]
        entry = f"/app/node_modules/{spec.package}/{spec.bin_path}"
        return [
            self.settings.engine,
            "run",
            "--name",
            name,
            *sandbox_flags(self.settings),
            *env_flags,
            "--entrypoint",
            "node",
            image,
            entry,
            *spec.args,
        ]

    def raw_command(self, image: str, name: str, argv: list[str]) -> list[str]:
        """Sandboxed command with an arbitrary entrypoint (used by the network-isolation test)."""
        return [
            self.settings.engine,
            "run",
            "--name",
            name,
            *sandbox_flags(self.settings),
            image,
            *argv,
        ]

    async def cleanup(self, name: str) -> None:
        await self._run("rm", "-f", name, timeout=30)
