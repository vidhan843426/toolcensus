"""Runtime configuration. Defaults are deliberately conservative towards upstream services."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path


def _env_path(name: str, default: str) -> Path:
    return Path(os.environ.get(name, default)).expanduser()


@dataclass(frozen=True)
class HttpSettings:
    #: Minimum seconds between two requests to the same host.
    min_interval_s: float = float(os.environ.get("TOOLCENSUS_MIN_INTERVAL", "0.25"))
    max_retries: int = 5
    backoff_base_s: float = 1.0
    timeout_s: float = 30.0
    cache_dir: Path = field(
        default_factory=lambda: _env_path("TOOLCENSUS_CACHE", "~/.cache/toolcensus")
    )
    #: Cached responses younger than this are served without revalidation.
    fresh_for_s: int = 6 * 3600


@dataclass(frozen=True)
class SandboxSettings:
    #: Pinned by digest so every scan installs into the same base image.
    base_image: str = os.environ.get(
        "TOOLCENSUS_BASE_IMAGE",
        # Resolved with `docker buildx imagetools inspect node:22-slim` on 2026-10-24.
        "node:22-slim@sha256:de170b39439eb0e5a3444ad7d60b015614a381e10fecae2e30ec9e735122f38d",
    )
    cpus: str = "1"
    memory: str = "512m"
    #: npm needs more headroom than the server itself.
    install_memory: str = "1g"
    pids: int = 256
    tmpfs_size: str = "64m"
    #: Hard wall-clock limit for one server's introspection.
    timeout_s: float = 60.0
    build_timeout_s: float = 600.0
    #: uid:gid of the non-root user inside the sandbox.
    user: str = "10001:10001"
    engine: str = os.environ.get("TOOLCENSUS_CONTAINER_ENGINE", "docker")
    #: Keep each server's install volume after measuring it (debugging only; uses disk space).
    keep_sandboxes: bool = False


@dataclass(frozen=True)
class Settings:
    http: HttpSettings = field(default_factory=HttpSettings)
    sandbox: SandboxSettings = field(default_factory=SandboxSettings)
    data_dir: Path = field(default_factory=lambda: _env_path("TOOLCENSUS_DATA", "data"))
    private_dir: Path = field(default_factory=lambda: _env_path("TOOLCENSUS_PRIVATE", "private"))
    population_size: int = 200
    concurrency: int = 4
