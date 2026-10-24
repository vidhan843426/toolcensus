"""Discovery against recorded HTTP fixtures (no live network)."""

from __future__ import annotations

import json
from pathlib import Path

import httpx
import pytest
import respx

from toolcensus.config import HttpSettings
from toolcensus.discovery import npm, pypi
from toolcensus.discovery.http import CachedHttp, HttpError, retry_after_seconds
from toolcensus.discovery.population import Candidate, classify, library_name, select_population
from toolcensus.discovery.registry import REGISTRY_BASE, npm_stdio_packages, remotes

from helpers import FIXTURES

HTTP = FIXTURES / "http"


def load(name: str) -> object:
    return json.loads((HTTP / name).read_text())


async def _no_sleep(_: float) -> None:
    return None


def client(tmp_path: Path | None = None, **kw: object) -> CachedHttp:
    settings = HttpSettings(min_interval_s=0, backoff_base_s=0, **kw)  # type: ignore[arg-type]
    return CachedHttp(
        settings, cache_path=(tmp_path / "c.sqlite") if tmp_path else None, sleep=_no_sleep
    )


def mock_ecosystem(router: respx.MockRouter) -> None:
    router.get(f"{REGISTRY_BASE}/v0.1/servers", params={"cursor": "c1"}).respond(
        json=load("registry_page2.json")
    )
    router.get(f"{REGISTRY_BASE}/v0.1/servers").respond(json=load("registry_page1.json"))
    router.get(f"{npm.NPM_REGISTRY}/-/v1/search").respond(json=load("npm_search.json"))
    for name, doc in load("packuments.json").items():  # type: ignore[union-attr]
        router.get(f"{npm.NPM_REGISTRY}/{npm.encode_name(name)}").respond(json=doc)
    router.get(f"{npm.NPM_REGISTRY}/gone-mcp-server").respond(404)
    router.get(url__startswith=f"{npm.NPM_API}/downloads/point/last-week/").mock(
        side_effect=lambda req: httpx.Response(200, json={"downloads": 777})
    )


@respx.mock
async def test_select_population(tmp_path: Path) -> None:
    mock_ecosystem(respx.mock)
    excl = tmp_path / "exclusions.yaml"
    excl.write_text("exclude:\n  - name: excluded-server\n    reason: test\n")
    async with client() as http:
        pop = await select_population(
            http, week="2026-43", top_n=10, exclusions_path=excl, search_limit=250
        )
    names = [p.name for p in pop.packages]
    assert names == ["popular-mcp-server", "@scope/registry-server"]
    reg = pop.packages[1]
    assert reg.registry_listed and reg.registry_name == "io.github.scope/registry-server"
    assert reg.weekly_downloads == 777
    reasons = {e.name: e.reason for e in pop.excluded}
    assert "exclusions.yaml" in reasons["excluded-server"]
    assert "library pattern" in reasons["mcp-client-lib"]
    assert "no bin" in reasons["no-bin-mcp"]
    assert "metadata unavailable" in reasons["gone-mcp-server"]
    assert pop.selection_rule and pop.top_n == 10


@respx.mock
async def test_select_population_without_registry() -> None:
    mock_ecosystem(respx.mock)
    async with client() as http:
        pop = await select_population(
            http, week="2026-43", top_n=5, search_limit=250, include_registry=False
        )
    assert all(not p.registry_listed for p in pop.packages)
    assert "DISABLED" in pop.selection_rule


def test_registry_parsing() -> None:
    page = load("registry_page1.json")
    server = page["servers"][0]["server"]  # type: ignore[index]
    [pkg] = npm_stdio_packages(server)
    assert pkg.package == "@scope/registry-server" and pkg.required_env == ("API_KEY",)
    assert [r.url for r in remotes(server)] == ["https://mcp.example.com/mcp"]


def test_library_names() -> None:
    assert library_name("@modelcontextprotocol/sdk")
    assert library_name("mcp-proxy")
    assert not library_name("server-filesystem")
    cand = Candidate("x")
    assert classify(cand, {"bin": "x.js"}, {}) is not None  # no MCP signal
    for sdk in npm.MCP_SDK_PACKAGES:
        assert classify(cand, {"bin": "x.js", "dependencies": {sdk: "1"}}, {}) is None


@respx.mock
async def test_cache_conditional_and_retry_after(tmp_path: Path) -> None:
    url = "https://example.test/x"
    route = respx.get(url)
    route.side_effect = [
        httpx.Response(429, headers={"Retry-After": "0"}),
        httpx.Response(200, json={"v": 1}, headers={"ETag": '"e1"'}),
        httpx.Response(304),
    ]
    async with client(tmp_path, fresh_for_s=0) as http:
        assert await http.get_json(url) == {"v": 1}
        assert await http.get_json(url) == {"v": 1}  # revalidated with 304
        assert route.calls[-1].request.headers["If-None-Match"] == '"e1"'
        assert route.calls[0].request.headers["User-Agent"].startswith("toolcensus/")
    async with client(tmp_path) as http:  # fresh cache: no request at all
        assert await http.get_json(url) == {"v": 1}
    assert route.call_count == 3


@respx.mock
async def test_errors_and_backoff() -> None:
    respx.get("https://example.test/404").respond(404)
    respx.get("https://example.test/500").respond(503)
    respx.get("https://example.test/bad").respond(200, content=b"not json")
    flaky = respx.get("https://example.test/flaky")
    flaky.side_effect = [httpx.ConnectError("x"), httpx.Response(200, json=[1])]
    async with client(max_retries=2) as http:
        with pytest.raises(HttpError):
            await http.get_json("https://example.test/404")
        assert (await http.get_json_status("https://example.test/500"))[0] == 503
        assert await http.get_json_status("https://example.test/bad") == (200, None)
        assert await http.get_json("https://example.test/flaky") == [1]


def test_retry_after_parsing() -> None:
    assert retry_after_seconds("5", 1) == 5
    assert retry_after_seconds(None, 2) == 2
    assert retry_after_seconds("garbage", 3) == 3
    assert retry_after_seconds("Wed, 21 Oct 2015 07:28:00 GMT", 1) == 0


@respx.mock
async def test_pypi_metadata() -> None:
    respx.get(f"{pypi.PYPI}/mcp-server-x/json").respond(json={"info": {"keywords": "mcp,server"}})
    async with client() as http:
        meta = await pypi.project_metadata(http, "mcp-server-x")
    assert pypi.has_console_scripts_hint(meta)


@respx.mock
async def test_bulk_downloads() -> None:
    respx.get(f"{npm.NPM_API}/downloads/point/last-week/a,b").respond(
        json={"a": {"downloads": 5}, "b": None}
    )
    respx.get(f"{npm.NPM_API}/downloads/point/last-week/@s%2Fc").respond(json={"downloads": 7})
    async with client() as http:
        assert await npm.weekly_downloads(http, ["a", "b", "@s/c"]) == {"a": 5, "b": 0, "@s/c": 7}


def test_npm_helpers() -> None:
    assert npm.encode_name("@a/b") == "@a%2Fb"
    assert npm.bin_entries({"name": "@a/b", "bin": "cli.js"}) == {"b": "cli.js"}
    assert npm.latest_version({"dist-tags": {}, "versions": {"1.0.0": {}, "0.9.0": {}}}) == "1.0.0"
