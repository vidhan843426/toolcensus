"""Docker/Podman sandbox. Two phases, each in its own throwaway container:

1. ``prepare``: ``npm install`` the exact version into a fresh, labelled Docker volume from a
   digest-pinned base image (network on, install scripts *off* unless explicitly overridden).
2. ``run_command``: ``docker run`` with the volume mounted read-only, no network, read-only
   rootfs + tmpfs, non-root user, all capabilities dropped, no-new-privileges, CPU/memory/PID
   limits.

``release`` deletes the volume afterwards, so nothing a scan downloads stays on disk. No images
are built, so there is no image or build cache to accumulate either.
"""

from __future__ import annotations

import asyncio
import os
import uuid

from toolcensus.config import SandboxSettings
from toolcensus.sandbox.runner import InstallFailedError, LaunchSpec

LABEL = "toolcensus.sandbox=1"

#: The npm cache lives inside the volume and is removed before the install container exits.
INSTALL_SCRIPT = (
    "npm init -y >/dev/null"
    ' && npm install --omit=dev --no-package-lock --cache /app/.npm-cache $NPM_FLAGS "$PKG"'
    " && rm -rf /app/.npm-cache"
    " && chmod -R a+rX /app"
)

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
        LABEL,
    ]


def install_flags(settings: SandboxSettings) -> list[str]:
    """The install container has network (to reach npm) but is otherwise locked down too."""
    return [
        "--rm",
        "--read-only",
        "--tmpfs",
        f"/tmp:rw,nosuid,nodev,size={settings.tmpfs_size}",
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges",
        "--cpus",
        settings.cpus,
        "--memory",
        settings.install_memory,
        "--pids-limit",
        str(settings.pids),
        "--workdir",
        "/app",
        "-e",
        "HOME=/tmp",
        "-e",
        "NPM_CONFIG_UPDATE_NOTIFIER=false",
        "-e",
        "NPM_CONFIG_FUND=false",
        "-e",
        "NPM_CONFIG_AUDIT=false",
        "-e",
        "NPM_CONFIG_LOGLEVEL=error",
        "--label",
        LABEL,
    ]


class DockerRunner:
    def __init__(self, settings: SandboxSettings | None = None) -> None:
        self.settings = settings or SandboxSettings()

    def cli_env(self) -> dict[str, str]:
        return {k: os.environ[k] for k in _CLI_ENV_KEYS if k in os.environ}

    async def _run(self, *argv: str, timeout: float) -> tuple[int, str]:
        proc = await asyncio.create_subprocess_exec(
            self.settings.engine,
            *argv,
            stdin=asyncio.subprocess.DEVNULL,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.STDOUT,
            env=self.cli_env(),
        )
        try:
            out, _ = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        except TimeoutError:
            proc.kill()
            await proc.wait()
            return -1, "timeout"
        return proc.returncode or 0, out.decode("utf-8", "replace")

    async def prepare(self, spec: LaunchSpec) -> str:
        """Install the package into a new volume and return the volume name."""
        volume = f"toolcensus-{uuid.uuid4().hex[:12]}"
        code, out = await self._run("volume", "create", "--label", LABEL, volume, timeout=30)
        if code != 0:
            raise InstallFailedError(out[-2000:])
        installer = f"{volume}-install"
        code, out = await self._run(
            "run",
            "--name",
            installer,
            *install_flags(self.settings),
            "-v",
            f"{volume}:/app",
            "-e",
            f"PKG={spec.package}@{spec.version}",
            "-e",
            f"NPM_FLAGS={'' if spec.allow_install_scripts else '--ignore-scripts'}",
            "--entrypoint",
            "sh",
            self.settings.base_image,
            "-c",
            INSTALL_SCRIPT,
            timeout=self.settings.build_timeout_s,
        )
        if code != 0:
            await self.cleanup(installer)
            await self.release(volume)
            raise InstallFailedError(out[-2000:])
        return volume

    def run_command(self, volume: str, spec: LaunchSpec, name: str) -> list[str]:
        env_flags = [x for k, v in sorted(spec.env.items()) for x in ("-e", f"{k}={v}")]
        entry = f"/app/node_modules/{spec.package}/{spec.bin_path}"
        return [
            self.settings.engine,
            "run",
            "--name",
            name,
            *sandbox_flags(self.settings),
            "-v",
            f"{volume}:/app:ro",
            *env_flags,
            "--entrypoint",
            "node",
            self.settings.base_image,
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

    async def release(self, volume: str) -> None:
        await self._run("volume", "rm", "-f", volume, timeout=60)

    async def clean(self, *, base_image: bool = False) -> list[str]:
        """Remove every container, volume (and legacy image) a scan left behind."""
        removed: list[str] = []
        code, out = await self._run("ps", "-aq", "--filter", f"label={LABEL}", timeout=30)
        if code == 0 and out.split():
            await self._run("rm", "-f", *out.split(), timeout=120)
            removed.append(f"{len(out.split())} container(s)")
        code, out = await self._run("volume", "ls", "-q", "--filter", f"label={LABEL}", timeout=30)
        if code == 0 and out.split():
            await self._run("volume", "rm", "-f", *out.split(), timeout=300)
            removed.append(f"{len(out.split())} volume(s)")
        # Images built by toolcensus 0.1.0 before sandboxes moved to volumes.
        code, out = await self._run("images", "-q", "--filter", f"label={LABEL}", timeout=30)
        if code == 0 and out.split():
            await self._run("rmi", "-f", *sorted(set(out.split())), timeout=300)
            removed.append(f"{len(set(out.split()))} legacy image(s)")
        if base_image:
            code, _ = await self._run("rmi", self.settings.base_image, timeout=120)
            if code == 0:
                removed.append(f"base image {self.settings.base_image.split('@')[0]}")
        return removed
