"""RFC 8785 test vectors and hashing invariants."""

from __future__ import annotations

import json
import struct

import pytest

from toolcensus.normalize.canonical import canonicalize, jcs_sha256
from toolcensus.normalize.toolhash import surface_hash, tool_hashes

# RFC 8785 Appendix B: IEEE-754 bit patterns -> expected serialization.
NUMBER_VECTORS = [
    ("0000000000000000", "0"),
    ("8000000000000000", "0"),
    ("0000000000000001", "5e-324"),
    ("8000000000000001", "-5e-324"),
    ("7fefffffffffffff", "1.7976931348623157e+308"),
    ("ffefffffffffffff", "-1.7976931348623157e+308"),
    ("4340000000000000", "9007199254740992"),
    ("c340000000000000", "-9007199254740992"),
    ("4430000000000000", "295147905179352830000"),
    ("44b52d02c7e14af5", "9.999999999999997e+22"),
    ("44b52d02c7e14af6", "1e+23"),
    ("44b52d02c7e14af7", "1.0000000000000001e+23"),
    ("444b1ae4d6e2ef4e", "999999999999999700000"),
    ("444b1ae4d6e2ef4f", "999999999999999900000"),
    ("444b1ae4d6e2ef50", "1e+21"),
    ("3eb0c6f7a0b5ed8c", "9.999999999999997e-7"),
    ("3eb0c6f7a0b5ed8d", "0.000001"),
    ("41b3de4355555553", "333333333.3333332"),
    ("41b3de4355555554", "333333333.33333325"),
    ("41b3de4355555555", "333333333.3333333"),
    ("41b3de4355555556", "333333333.3333334"),
    ("41b3de4355555557", "333333333.33333343"),
    ("becbf647612f3696", "-0.0000033333333333333333"),
    ("43143ff3c1cb0959", "1424953923781206.2"),
]


@pytest.mark.parametrize(("bits", "expected"), NUMBER_VECTORS)
def test_rfc8785_numbers(bits: str, expected: str) -> None:
    value = struct.unpack(">d", bytes.fromhex(bits))[0]
    assert canonicalize(value).decode() == expected


def test_rfc8785_section_3_2_2_example() -> None:
    src = (
        '{"numbers": [333333333.33333329, 1E30, 4.50, 2e-3, 0.000000000000000000000000001],'
        ' "string": "\\u20ac$\\u000F\\u000aA\'\\u0042\\u0022\\u005c\\\\\\"\\/",'
        ' "literals": [null, true, false]}'
    )
    expected = (
        '{"literals":[null,true,false],"numbers":[333333333.3333333,1e+30,4.5,0.002,1e-27],'
        '"string":"€$\\u000f\\nA\'B\\"\\\\\\\\\\"/"}'
    )
    assert canonicalize(json.loads(src)).decode() == expected


def test_rfc8785_key_sorting_by_utf16() -> None:
    src = '{"\\u20ac":"Euro Sign","\\r":"Carriage Return","\\ufb33":"Hebrew Letter Dalet With Dagesh","1":"One","\\ud83d\\ude00":"Emoji: Grinning Face","\\u0080":"Control","\\u00f6":"Latin Small Letter O With Diaeresis"}'
    keys = list(json.loads(canonicalize(json.loads(src))))
    assert keys == ["\r", "1", "\u0080", "ö", "€", "\U0001f600", "דּ"]


def test_invalid_values() -> None:
    for bad in (float("nan"), float("inf"), object(), {1: "x"}):
        with pytest.raises((ValueError, TypeError)):
            canonicalize(bad)


def test_large_ints_and_nesting() -> None:
    assert canonicalize(2**60) == b"1152921504606847000"  # ES Number semantics
    assert canonicalize({"b": [1, 2.0, {"z": None, "a": True}], "a": "x"}) == (
        b'{"a":"x","b":[1,2,{"a":true,"z":null}]}'
    )


TOOL = {
    "name": "search",
    "description": "Search the index.",
    "inputSchema": {"type": "object", "properties": {"q": {"type": "string"}}, "required": ["q"]},
}


def test_key_order_and_whitespace_do_not_change_hash() -> None:
    reordered = json.loads(
        '{ "inputSchema": {"required":["q"], "properties":{"q":{"type":"string"}}, "type":"object"},'
        '  "description" : "Search the index.",   "name":"search" }'
    )
    assert tool_hashes(TOOL) == tool_hashes(reordered)


@pytest.mark.parametrize(
    "mutate",
    [
        lambda t: t.update(description="Search the index!"),
        lambda t: t["inputSchema"]["properties"]["q"].update(type="integer"),
        lambda t: t["inputSchema"].update(required=[]),
        lambda t: t.update(annotations={"readOnlyHint": True}),
        lambda t: t.update(name="search2"),
    ],
)
def test_any_semantic_change_changes_hash(mutate) -> None:  # type: ignore[no-untyped-def]
    changed = json.loads(json.dumps(TOOL))
    mutate(changed)
    assert tool_hashes(changed).tool_hash != tool_hashes(TOOL).tool_hash


def test_component_hashes_isolate_changes() -> None:
    changed = dict(TOOL, description="Different")
    a, b = tool_hashes(TOOL), tool_hashes(changed)
    assert a.description_hash != b.description_hash
    assert a.input_schema_hash == b.input_schema_hash
    assert a.annotations_hash == b.annotations_hash == jcs_sha256(None)


def test_surface_hash_is_order_independent() -> None:
    assert surface_hash([("a", "1"), ("b", "2")]) == surface_hash([("b", "2"), ("a", "1")])
    assert surface_hash([("a", "1")]) != surface_hash([("a", "2")])
