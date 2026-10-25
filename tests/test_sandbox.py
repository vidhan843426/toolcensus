"""Sandbox configuration (unit) and isolation guarantees (integration, needs Docker)."""

from __future__ import annotations

import json
import shutil
import stat
import subprocess
import sys
import uuid
from dataclasses import replace
from pathlib import Path

import pytest

from toolcensus.config import SandboxSettings
from toolcensus.introspect.collect import introspect_command
from toolcensus.models import Status
from toolcensus.sandbox.docker import INSTALL_SCRIPT, DockerRunner, install_flags, sandbox_flags
from toolcensus.sandbox.runner import (
    PLACEHOLDER,
    LaunchSpec,
    SandboxError,
    UnsafeConfigurationError,
    load_overrides,
    resolve_launch,
)


def _flag(flags: list[str], name: str) -> str:
    return flags[flags.index(name) + 1]


def test_run_flags_enforce_isolation() -> None:
    s = SandboxSettings()
    flags = sandbox_flags(s)
    assert _flag(flags, "--network") == "none"
    assert "--read-only" in flags
    assert _flag(flags, "--cap-drop") == "ALL"
    assert _flag(flags, "--security-opt") == "no-new-privileges"
    assert _flag(flags, "--user") == "1000:1000"
    assert _flag(flags, "--memory") == "512m" and _flag(flags, "--pids-limit") == "256"
    assert _flag(flags, "--cpus") == "1"
    assert "/tmp:" in _flag(flags, "--tmpfs")
    assert "--privileged" not in flags and "-v" not in flags and "--volume" not in flags


def test_run_command_never_forwards_host_env() -> None:
    spec = LaunchSpec("@a/b", "1.0.0", "dist/index.js", env={"API_KEY": PLACEHOLDER})
    cmd = DockerRunner().run_command("vol", spec, "name")
    assert cmd[cmd.index("-v") + 1] == "vol:/app:ro"
    for i, part in enumerate(cmd):
        if part == "-e":
            assert "=" in cmd[i + 1], "a bare `-e NAME` would copy the host value"
    assert cmd[-1] == "/app/node_modules/@a/b/dist/index.js"
    assert f"API_KEY={PLACEHOLDER}" in cmd


def test_cli_env_is_filtered(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "x")
    assert "AWS_SECRET_ACCESS_KEY" not in DockerRunner().cli_env()


def test_install_container_is_locked_down() -> None:
    s = SandboxSettings()
    assert "@sha256:" in s.base_image
    flags = install_flags(s)
    assert _flag(flags, "--cap-drop") == "ALL" and "--read-only" in flags
    assert "--privileged" not in flags
    # The npm cache is written inside the volume and removed before the container exits.
    assert (
        "--cache /app/.npm-cache" in INSTALL_SCRIPT and "rm -rf /app/.npm-cache" in INSTALL_SCRIPT
    )


def _fake_engine(tmp_path: Path, *, fail_on: str = "") -> tuple[SandboxSettings, Path]:
    """A stand-in `docker` binary that logs its argv and prints canned output."""
    log = tmp_path / "calls.jsonl"
    script = tmp_path / "docker"
    script.write_text(
        f"#!{sys.executable}\n"
        "import json, sys\n"
        f"open({str(log)!r}, 'a').write(json.dumps(sys.argv[1:]) + '\\n')\n"
        f"if {fail_on!r} and {fail_on!r} in sys.argv[1:2]: print('npm ERR! 404'); sys.exit(1)\n"
        "if sys.argv[1:3] in (['ps', '-aq'], ['volume', 'ls'], ['images', '-q']): print('abc def')\n"
    )
    script.chmod(script.stat().st_mode | stat.S_IEXEC)
    return replace(SandboxSettings(), engine=str(script)), log


def _calls(log: Path) -> list[list[str]]:
    return [json.loads(line) for line in log.read_text().splitlines()]


async def test_prepare_installs_into_a_volume_and_release_deletes_it(tmp_path: Path) -> None:
    settings, log = _fake_engine(tmp_path)
    runner = DockerRunner(settings)
    spec = LaunchSpec("@a/b", "1.2.3", "cli.js")
    volume = await runner.prepare(spec)
    await runner.release(volume)
    create, install, delete = _calls(log)
    assert create[:2] == ["volume", "create"] and create[-1] == volume
    assert install[0] == "run" and f"{volume}:/app" in install
    assert "PKG=@a/b@1.2.3" in install and "NPM_FLAGS=--ignore-scripts" in install
    assert "--network" not in install  # needs the registry, but nothing else is granted
    assert delete == ["volume", "rm", "-f", volume]


async def test_failed_install_removes_the_volume(tmp_path: Path) -> None:
    from toolcensus.sandbox.runner import InstallFailedError

    settings, log = _fake_engine(tmp_path, fail_on="run")
    with pytest.raises(InstallFailedError, match="404"):
        await DockerRunner(settings).prepare(LaunchSpec("p", "1.0.0", "x.js"))
    calls = _calls(log)
    assert calls[-1][:3] == ["volume", "rm", "-f"]
    assert calls[-2][:2] == ["rm", "-f"]


async def test_clean_sweeps_everything_labelled(tmp_path: Path) -> None:
    settings, log = _fake_engine(tmp_path)
    removed = await DockerRunner(settings).clean(base_image=True)
    assert removed == [
        "2 container(s)",
        "2 volume(s)",
        "2 legacy image(s)",
        "base image node:22-slim",
    ]
    calls = _calls(log)
    assert ["rm", "-f", "abc", "def"] in calls and ["volume", "rm", "-f", "abc", "def"] in calls
    assert ["rmi", settings.base_image] in calls


@pytest.mark.parametrize(
    "kwargs",
    [
        {"env": {"API_KEY": "sk-live-real"}},
        {"env": {"BAD NAME": PLACEHOLDER}},
        {"package": "evil; rm -rf /"},
        {"version": "1.0.0 && curl x"},
        {"bin_path": "../../etc/passwd"},
        {"bin_path": "/usr/bin/env"},
        {"args": ("--x", "$(whoami)")},
    ],
)
def test_unsafe_specs_rejected(kwargs: dict) -> None:
    base = {"package": "p", "version": "1.0.0", "bin_path": "x.js"}
    base.update(kwargs)
    with pytest.raises(UnsafeConfigurationError):
        LaunchSpec(**base)


def test_resolve_launch(tmp_path) -> None:  # type: ignore[no-untyped-def]
    doc = {"name": "@s/srv", "version": "1.2.3", "bin": {"srv": "./dist/cli.js", "other": "o.js"}}
    spec = resolve_launch(doc, required_env=("TOKEN",))
    assert spec.bin_path == "dist/cli.js" and spec.source == "bin"
    assert spec.env == {"TOKEN": PLACEHOLDER}
    ov = tmp_path / "o.yaml"
    ov.write_text(
        "packages:\n  '@s/srv':\n    bin: other\n    args: ['--stdio']\n    env: {MODE: production}\n"
    )
    spec2 = resolve_launch(doc, overrides=load_overrides(ov))
    assert (spec2.bin_path, spec2.args, spec2.source) == ("o.js", ("--stdio",), "override")
    spec3 = resolve_launch(doc, registry_args=("server", "start"))
    assert (spec3.args, spec3.source) == (("server", "start"), "registry")
    assert resolve_launch(doc, registry_args=("$(id)",)).args == ()  # unsafe -> ignored
    assert resolve_launch(doc, overrides=load_overrides(ov), registry_args=("x",)).args == (
        "--stdio",
    )
    with pytest.raises(SandboxError):
        resolve_launch({"name": "x", "version": "1.0.0"})
    assert load_overrides(tmp_path / "missing.yaml") == {}


def _docker_ok() -> bool:
    if shutil.which("docker") is None:
        return False
    return subprocess.run(["docker", "info"], capture_output=True).returncode == 0


needs_docker = pytest.mark.skipif(not _docker_ok(), reason="Docker daemon not available")
BASE = SandboxSettings().base_image


@pytest.mark.sandbox
@needs_docker
async def test_sandbox_has_no_network() -> None:
    runner = DockerRunner()
    name = f"toolcensus-test-{uuid.uuid4().hex[:8]}"
    probe = (
        "require('https').get('https://registry.npmjs.org/',()=>{console.log('CONNECTED');process.exit(0)})"
        ".on('error',e=>{console.error('BLOCKED '+e.code);process.exit(7)})"
    )
    cmd = runner.raw_command(BASE, name, ["node", "-e", probe])
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    assert "CONNECTED" not in proc.stdout
    assert proc.returncode == 7, proc.stderr
    assert "BLOCKED" in proc.stderr


@pytest.mark.sandbox
@needs_docker
async def test_sandbox_rootfs_read_only_and_non_root() -> None:
    runner = DockerRunner()
    script = "id -u; touch /app/x 2>/dev/null && echo WROTE || echo RO; touch /tmp/ok && echo TMPOK"
    cmd = runner.raw_command(BASE, f"toolcensus-test-{uuid.uuid4().hex[:8]}", ["sh", "-c", script])
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=120).stdout.split()
    assert out == ["1000", "RO", "TMPOK"]


@pytest.mark.sandbox
@needs_docker
async def test_timeout_kills_container() -> None:
    runner = DockerRunner()
    name = f"toolcensus-test-{uuid.uuid4().hex[:8]}"
    cmd = runner.raw_command(BASE, name, ["node", "-e", "setInterval(()=>{},1000)"])
    raw = await introspect_command(
        cmd, env=runner.cli_env(), timeout_s=3, cleanup=lambda: runner.cleanup(name)
    )
    assert raw.status is Status.TIMEOUT
    ps = subprocess.run(
        ["docker", "ps", "-aq", "--filter", f"name={name}"], capture_output=True, text=True
    )
    assert ps.stdout.strip() == ""
