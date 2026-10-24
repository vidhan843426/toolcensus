"""Polite HTTP: identifying User-Agent, per-host rate limiting, SQLite cache with conditional
requests (ETag / Last-Modified), ``Retry-After`` handling and exponential backoff."""

from __future__ import annotations

import asyncio
import json
import sqlite3
import time
from email.utils import parsedate_to_datetime
from pathlib import Path
from types import TracebackType
from typing import Any
from urllib.parse import urlencode, urlsplit

import httpx

from toolcensus import USER_AGENT
from toolcensus.config import HttpSettings

RETRY_STATUSES = {429, 500, 502, 503, 504}


class HttpError(RuntimeError):
    def __init__(self, url: str, status: int) -> None:
        super().__init__(f"GET {url} -> HTTP {status}")
        self.url = url
        self.status = status


class _Cache:
    def __init__(self, path: Path | None) -> None:
        if path is not None:
            path.parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(str(path) if path else ":memory:")
        self.db.execute(
            "CREATE TABLE IF NOT EXISTS http_cache (url TEXT PRIMARY KEY, status INTEGER,"
            " etag TEXT, last_modified TEXT, body BLOB, fetched_at REAL)"
        )

    def get(self, url: str) -> tuple[int, str | None, str | None, bytes, float] | None:
        row = self.db.execute(
            "SELECT status, etag, last_modified, body, fetched_at FROM http_cache WHERE url=?",
            (url,),
        ).fetchone()
        return (row[0], row[1], row[2], row[3], row[4]) if row else None

    def put(self, url: str, status: int, etag: str | None, lm: str | None, body: bytes) -> None:
        self.db.execute(
            "INSERT OR REPLACE INTO http_cache VALUES (?, ?, ?, ?, ?, ?)",
            (url, status, etag, lm, body, time.time()),
        )
        self.db.commit()

    def touch(self, url: str) -> None:
        self.db.execute("UPDATE http_cache SET fetched_at=? WHERE url=?", (time.time(), url))
        self.db.commit()


def retry_after_seconds(value: str | None, default: float) -> float:
    if not value:
        return default
    try:
        return max(0.0, float(value))
    except ValueError:
        try:
            return max(0.0, parsedate_to_datetime(value).timestamp() - time.time())
        except (TypeError, ValueError):
            return default


class CachedHttp:
    def __init__(
        self,
        settings: HttpSettings | None = None,
        *,
        transport: httpx.AsyncBaseTransport | None = None,
        cache_path: Path | str | None = "default",
        sleep: Any = asyncio.sleep,
    ) -> None:
        self.settings = settings or HttpSettings()
        path: Path | None
        if cache_path == "default":
            path = self.settings.cache_dir / "http.sqlite"
        else:
            path = Path(cache_path) if cache_path else None
        self._cache = _Cache(path)
        self._client = httpx.AsyncClient(
            headers={"User-Agent": USER_AGENT, "Accept": "application/json"},
            timeout=self.settings.timeout_s,
            follow_redirects=True,
            transport=transport,
        )
        self._last: dict[str, float] = {}
        self._locks: dict[str, asyncio.Lock] = {}
        self._sleep = sleep
        self.requests_sent = 0

    async def __aenter__(self) -> CachedHttp:
        return self

    async def __aexit__(
        self, et: type[BaseException] | None, e: BaseException | None, tb: TracebackType | None
    ) -> None:
        await self._client.aclose()
        self._cache.db.close()

    async def _throttle(self, host: str) -> None:
        lock = self._locks.setdefault(host, asyncio.Lock())
        async with lock:
            wait = self._last.get(host, 0.0) + self.settings.min_interval_s - time.monotonic()
            if wait > 0:
                await self._sleep(wait)
            self._last[host] = time.monotonic()

    async def get_raw(self, url: str, params: dict[str, Any] | None = None) -> tuple[int, bytes]:
        if params:
            url = f"{url}?{urlencode({k: v for k, v in params.items() if v is not None})}"
        cached = self._cache.get(url)
        if cached and time.time() - cached[4] < self.settings.fresh_for_s:
            return cached[0], cached[3]
        headers: dict[str, str] = {}
        if cached:
            if cached[1]:
                headers["If-None-Match"] = cached[1]
            if cached[2]:
                headers["If-Modified-Since"] = cached[2]

        host = urlsplit(url).netloc
        for attempt in range(self.settings.max_retries + 1):
            await self._throttle(host)
            self.requests_sent += 1
            try:
                resp = await self._client.get(url, headers=headers)
            except httpx.TransportError:
                if attempt == self.settings.max_retries:
                    raise
                await self._sleep(self.settings.backoff_base_s * 2**attempt)
                continue
            if resp.status_code == 304 and cached:
                self._cache.touch(url)
                return cached[0], cached[3]
            if resp.status_code in RETRY_STATUSES and attempt < self.settings.max_retries:
                delay = retry_after_seconds(
                    resp.headers.get("Retry-After"), self.settings.backoff_base_s * 2**attempt
                )
                await self._sleep(min(delay, 300))
                continue
            if resp.status_code < 500:
                self._cache.put(
                    url,
                    resp.status_code,
                    resp.headers.get("ETag"),
                    resp.headers.get("Last-Modified"),
                    resp.content,
                )
            return resp.status_code, resp.content
        raise AssertionError("unreachable")  # pragma: no cover

    async def get_json_status(
        self, url: str, params: dict[str, Any] | None = None
    ) -> tuple[int, Any]:
        status, body = await self.get_raw(url, params)
        try:
            return status, json.loads(body) if body else None
        except ValueError:
            return status, None

    async def get_json(self, url: str, params: dict[str, Any] | None = None) -> Any:
        status, data = await self.get_json_status(url, params)
        if status != 200:
            raise HttpError(url, status)
        return data
