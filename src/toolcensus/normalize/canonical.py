"""RFC 8785 JSON Canonicalization Scheme (JCS).

Implemented here (rather than via a dependency) so the hashing that every published number
depends on is small, auditable, and tested against the RFC's own vectors.
"""

from __future__ import annotations

import hashlib
import json
import math
from decimal import Decimal
from typing import Any


def _es_number(value: float) -> str:
    """Serialize like ECMAScript ``Number.prototype.toString`` (RFC 8785 section 3.2.2.3)."""
    if math.isnan(value) or math.isinf(value):
        raise ValueError("NaN and Infinity are not valid JSON numbers")
    if value == 0:
        return "0"
    sign = "-" if value < 0 else ""
    # repr() yields the shortest round-tripping digits, which is exactly what ES requires.
    tup = Decimal(repr(abs(value))).normalize().as_tuple()
    digits = "".join(map(str, tup.digits))
    assert isinstance(tup.exponent, int)
    k = len(digits)
    # value = 0.<digits> * 10**n, i.e. n is the decimal point position relative to `digits`.
    n = k + tup.exponent
    if k <= n <= 21:
        out = digits + "0" * (n - k)
    elif 0 < n <= 21:
        out = digits[:n] + "." + digits[n:]
    elif -6 < n <= 0:
        out = "0." + "0" * (-n) + digits
    else:
        e = n - 1
        exp = f"e{'+' if e >= 0 else '-'}{abs(e)}"
        out = digits[0] + ("." + digits[1:] if k > 1 else "") + exp
    return sign + out


def _serialize(value: Any, out: list[str]) -> None:
    if value is None:
        out.append("null")
    elif value is True:
        out.append("true")
    elif value is False:
        out.append("false")
    elif isinstance(value, int):
        if abs(value) > 2**53:
            # Outside the IEEE-754 safe range: serialize as the double JSON parsers would see.
            out.append(_es_number(float(value)))
        else:
            out.append(str(value))
    elif isinstance(value, float):
        out.append(_es_number(value))
    elif isinstance(value, str):
        out.append(json.dumps(value, ensure_ascii=False))
    elif isinstance(value, (list, tuple)):
        out.append("[")
        for i, item in enumerate(value):
            if i:
                out.append(",")
            _serialize(item, out)
        out.append("]")
    elif isinstance(value, dict):
        out.append("{")
        # Keys are sorted by their UTF-16 code units.
        for i, key in enumerate(sorted(value, key=lambda k: str(k).encode("utf-16-be"))):
            if not isinstance(key, str):
                raise TypeError("JSON object keys must be strings")
            if i:
                out.append(",")
            out.append(json.dumps(key, ensure_ascii=False))
            out.append(":")
            _serialize(value[key], out)
        out.append("}")
    else:
        raise TypeError(f"cannot canonicalize {type(value).__name__}")


def canonicalize(value: Any) -> bytes:
    out: list[str] = []
    _serialize(value, out)
    return "".join(out).encode("utf-8")


def jcs_sha256(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonicalize(value)).hexdigest()
