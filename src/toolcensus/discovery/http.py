"""Polite HTTP: identifying User-Agent, per-host rate limiting, SQLite cache with conditional
requests (ETag / Last-Modified), ``Retry-After`` handling and exponential backoff."""

from __future__ import annotations

import asyncio
import json
import random
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
CACHEABLE_STATUSES = {200, 404, 410}


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
        self.rate_limited = 0

    async def __aenter__(self) -> CachedHttp:
        return self

    async def __aexit__(
        self, et: type[BaseException] | None, e: BaseException | None, tb: TracebackType | None
    ) -> None:
        await self._client.aclose()
        self._cache.db.close()

    def _throttle_key(self, url: str) -> tuple[str, float]:
        parts = urlsplit(url)
        where = parts.netloc + parts.path
        for prefix, interval in self.settings.slow_paths:
            if where.startswith(prefix):
                return prefix, interval
        return parts.netloc, self.settings.min_interval_s

    async def _throttle(self, url: str) -> None:
        key, interval = self._throttle_key(url)
        lock = self._locks.setdefault(key, asyncio.Lock())
        async with lock:
            wait = self._last.get(key, 0.0) + interval - time.monotonic()
            if wait > 0:
                await self._sleep(wait)
            self._last[key] = time.monotonic()

    def _backoff(self, base: float, attempt: int) -> float:
        delay = min(base * 2.0**attempt, self.settings.max_backoff_s)
        # Jitter so concurrent requests that were limited together don't retry together.
        return delay + random.uniform(0, delay * 0.1)  # noqa: S311 - not security sensitive

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

        errors = limited = 0
        while True:
            await self._throttle(url)
            self.requests_sent += 1
            try:
                resp = await self._client.get(url, headers=headers)
            except httpx.TransportError:
                if errors == self.settings.max_retries:
                    raise
                await self._sleep(self._backoff(self.settings.backoff_base_s, errors))
                errors += 1
                continue
            status = resp.status_code
            if status == 304 and cached:
                self._cache.touch(url)
                return cached[0], cached[3]
            if status == 429 and limited < self.settings.rate_limit_retries:
                fallback = self._backoff(self.settings.rate_limit_backoff_s, limited)
                delay = retry_after_seconds(resp.headers.get("Retry-After"), fallback)
                self.rate_limited += 1
                await self._sleep(min(delay, 2 * self.settings.max_backoff_s))
                limited += 1
                continue
            if status in RETRY_STATUSES and status != 429 and errors < self.settings.max_retries:
                await self._sleep(self._backoff(self.settings.backoff_base_s, errors))
                errors += 1
                continue
            # Only definitive answers are cached; errors (429, 5xx, ...) must be retried later.
            if status in CACHEABLE_STATUSES:
                self._cache.put(
                    url,
                    status,
                    resp.headers.get("ETag"),
                    resp.headers.get("Last-Modified"),
                    resp.content,
                )
            return status, resp.content

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
