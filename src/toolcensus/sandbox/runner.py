"""Sandbox abstraction and launch resolution.

Ground rule (ETHICS.md #2): third-party code only ever runs inside a :class:`SandboxRunner`.
The only implementation shipped for third-party packages is :class:`DockerRunner`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol

import yaml

from toolcensus.discovery import npm

#: Every env value given to a server must be an obviously fake placeholder or a harmless flag.
PLACEHOLDER = "toolcensus-placeholder-not-a-real-secret"
_HARMLESS_VALUES = {"0", "1", "true", "false", "production", "error", "warn", "info", "/tmp"}
_ENV_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_PKG_NAME = re.compile(r"^(?:@[A-Za-z0-9][\w.-]*/)?[A-Za-z0-9][\w.-]*$")
_VERSION = re.compile(r"^[0-9A-Za-z][0-9A-Za-z.+-]*$")
_SAFE_ARG = re.compile(r"^[\w@%+=:,./-]*$")


class SandboxError(RuntimeError):
    pass


class InstallFailedError(SandboxError):
    pass


class UnsafeConfigurationError(SandboxError):
    """Raised when a launch spec would hand something other than a placeholder to a server."""


@dataclass(frozen=True)
class LaunchSpec:
    package: str
    version: str
    bin_path: str
    args: tuple[str, ...] = ()
    env: dict[str, str] = field(default_factory=dict)
    source: str = "bin"  # "bin" | "registry" | "override"
    allow_install_scripts: bool = False

    def __post_init__(self) -> None:
        if not _PKG_NAME.match(self.package):
            raise UnsafeConfigurationError(f"invalid package name {self.package!r}")
        if not _VERSION.match(self.version):
            raise UnsafeConfigurationError(f"invalid version {self.version!r}")
        if self.bin_path.startswith("/") or ".." in Path(self.bin_path).parts:
            raise UnsafeConfigurationError(f"bin path escapes the package: {self.bin_path!r}")
        for arg in self.args:
            if not _SAFE_ARG.match(arg):
                raise UnsafeConfigurationError(f"unsafe launch argument {arg!r}")
        validate_env(self.env)


def validate_env(env: dict[str, str]) -> None:
    for key, value in env.items():
        if not _ENV_NAME.match(key):
            raise UnsafeConfigurationError(f"invalid env name {key!r}")
        if not (value.startswith("toolcensus-placeholder") or value in _HARMLESS_VALUES):
            raise UnsafeConfigurationError(
                f"env {key} must be a toolcensus placeholder; real values are never allowed"
            )


def load_overrides(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return {str(k): dict(v or {}) for k, v in (data.get("packages") or {}).items()}


def resolve_launch(
    version_doc: dict[str, Any],
    *,
    overrides: dict[str, dict[str, Any]] | None = None,
    required_env: tuple[str, ...] = (),
    registry_args: tuple[str, ...] = (),
) -> LaunchSpec:
    name = str(version_doc["name"])
    version = str(version_doc["version"])
    override = (overrides or {}).get(name, {})
    bins = npm.bin_entries(version_doc)
    if override.get("bin"):
        bin_path = str(bins.get(override["bin"], override["bin"]))
    elif bins:
        short = name.split("/")[-1]
        bin_path = bins.get(short) or bins[sorted(bins)[0]]
    else:
        raise SandboxError(f"{name}@{version} declares no bin")
    env = {k: PLACEHOLDER for k in required_env}
    env.update({str(k): str(v) for k, v in (override.get("env") or {}).items()})
    if override.get("args"):
        args = tuple(str(a) for a in override["args"])
    elif registry_args and all(_SAFE_ARG.match(a) for a in registry_args):
        args = registry_args
    else:
        args = ()
    source = "override" if override else "registry" if args else "bin"
    return LaunchSpec(
        package=name,
        version=version,
        bin_path=bin_path.removeprefix("./"),
        args=args,
        env=env,
        source=source,
        allow_install_scripts=bool(override.get("allow_install_scripts", False)),
    )


class SandboxRunner(Protocol):
    async def prepare(self, spec: LaunchSpec) -> str:
        """Install (with network) the package. Returns a reference to the installed copy."""

    def run_command(self, ref: str, spec: LaunchSpec, name: str) -> list[str]:
        """argv that starts the server *without network* and with stdio attached."""

    async def cleanup(self, name: str) -> None:
        """Force-stop and remove a running sandbox (used on timeout)."""

    async def release(self, ref: str) -> None:
        """Delete the installed copy returned by ``prepare`` (frees the disk space)."""

    def cli_env(self) -> dict[str, str]:
        """Environment for the container CLI process itself (never forwarded into the sandbox)."""
