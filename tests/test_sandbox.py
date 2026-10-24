"""Sandbox configuration (unit) and isolation guarantees (integration, needs Docker)."""

from __future__ import annotations

import shutil
import subprocess
import uuid

import pytest

from toolcensus.config import SandboxSettings
from toolcensus.introspect.collect import introspect_command
from toolcensus.models import Status
from toolcensus.sandbox.docker import DOCKERFILE, DockerRunner, sandbox_flags
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
    assert _flag(flags, "--user") == "10001:10001"
    assert _flag(flags, "--memory") == "512m" and _flag(flags, "--pids-limit") == "256"
    assert _flag(flags, "--cpus") == "1"
    assert "/tmp:" in _flag(flags, "--tmpfs")
    assert "--privileged" not in flags and "-v" not in flags and "--volume" not in flags


def test_run_command_never_forwards_host_env() -> None:
    spec = LaunchSpec("@a/b", "1.0.0", "dist/index.js", env={"API_KEY": PLACEHOLDER})
    cmd = DockerRunner().run_command("img", spec, "name")
    for i, part in enumerate(cmd):
        if part == "-e":
            assert "=" in cmd[i + 1], "a bare `-e NAME` would copy the host value"
    assert cmd[-1] == "/app/node_modules/@a/b/dist/index.js"
    assert f"API_KEY={PLACEHOLDER}" in cmd


def test_cli_env_is_filtered(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "x")
    assert "AWS_SECRET_ACCESS_KEY" not in DockerRunner().cli_env()


def test_dockerfile_pins_digest_and_ignores_scripts() -> None:
    assert "@sha256:" in SandboxSettings().base_image
    assert "--ignore-scripts" in DOCKERFILE.format(base="b", scripts_flag="--ignore-scripts")
    a = DockerRunner().image_tag(LaunchSpec("p", "1.0.0", "x.js"))
    b = DockerRunner().image_tag(LaunchSpec("p", "1.0.1", "x.js"))
    assert a != b and a.startswith("toolcensus-sbx:")


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
    assert out == ["10001", "RO", "TMPOK"]


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
