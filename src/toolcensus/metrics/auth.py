"""Authorization metadata for *remote* servers (phase 2, opt-in; METHODOLOGY.md section 7.6).

Exactly one unauthenticated GET of a public discovery document per server per scan
(RFC 9728 OAuth 2.0 Protected Resource Metadata, as referenced by the MCP authorization spec).
No authentication attempts, no follow-up requests, no crawling.
"""

from __future__ import annotations

from typing import Any
from urllib.parse import urlsplit, urlunsplit

from pydantic import BaseModel

from toolcensus.discovery.http import CachedHttp

WELL_KNOWN = "/.well-known/oauth-protected-resource"
FIELDS = ("resource", "authorization_servers", "scopes_supported", "bearer_methods_supported")


class AuthMetadata(BaseModel):
    url: str
    published: bool
    http_status: int | None
    fields_present: list[str]


def metadata_url(remote_url: str) -> str:
    """RFC 9728 section 3.1: insert the well-known segment between host and path."""
    parts = urlsplit(remote_url)
    path = parts.path.rstrip("/")
    return urlunsplit((parts.scheme, parts.netloc, WELL_KNOWN + path, "", ""))


async def probe_auth_metadata(http: CachedHttp, remote_url: str) -> AuthMetadata:
    url = metadata_url(remote_url)
    status, body = await http.get_json_status(url)
    doc: dict[str, Any] = body if isinstance(body, dict) else {}
    ok = status == 200 and bool(doc)
    return AuthMetadata(
        url=url,
        published=ok,
        http_status=status,
        fields_present=[f for f in FIELDS if f in doc] if ok else [],
    )
