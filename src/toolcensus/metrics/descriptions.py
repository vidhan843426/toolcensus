"""Description hygiene (METHODOLOGY.md section 7.5): counts and categories only, never content."""

from __future__ import annotations

import re
import unicodedata
from collections import Counter
from collections.abc import Mapping
from typing import Any

from toolcensus.models import DescriptionMetrics

_ZERO_WIDTH = {0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF, 0x180E}
_BIDI = {0x061C, 0x200E, 0x200F, *range(0x202A, 0x202F), *range(0x2066, 0x206A)}
_ALLOWED_CONTROLS = {0x09, 0x0A, 0x0D}
#: FE0E/FE0F select text/emoji presentation and are ubiquitous in normal emoji.
_COMMON_VARIATION = {0xFE0E, 0xFE0F}

_MARKUP = re.compile(r"</?[A-Za-z][A-Za-z0-9:-]*(?:\s[^<>]*)?/?>")


def char_category(ch: str) -> str | None:
    """Return the hygiene category of an invisible / non-printing code point, else None."""
    cp = ord(ch)
    if cp in _ZERO_WIDTH:
        return "zero_width"
    if cp in _BIDI:
        return "bidi_control"
    if 0xE0000 <= cp <= 0xE007F:
        return "tag"
    if (0xFE00 <= cp <= 0xFE0F and cp not in _COMMON_VARIATION) or 0xE0100 <= cp <= 0xE01EF:
        return "variation_selector"
    cat = unicodedata.category(ch)
    if cat == "Cc" and cp not in _ALLOWED_CONTROLS:
        return "control"
    if cat == "Cf":
        return "other_format"
    if cat in ("Co", "Cn"):
        return "private_or_unassigned"
    return None


def invisible_categories(text: str) -> Counter[str]:
    return Counter(c for c in map(char_category, text) if c is not None)


def has_invisible(text: str) -> bool:
    return any(char_category(c) is not None for c in text)


def description_metrics(definition: Mapping[str, Any]) -> DescriptionMetrics:
    desc = definition.get("description")
    text = desc if isinstance(desc, str) else ""
    cats = invisible_categories(text)
    return DescriptionMetrics(
        length=len(text),
        invisible_char_count=sum(cats.values()),
        invisible_categories=dict(sorted(cats.items())),
        markup_tag_count=len(_MARKUP.findall(text)),
    )


def redact_invisible(value: Any) -> tuple[Any, bool]:
    """Replace every string containing invisible code points with a neutral placeholder.

    Public output must not reproduce such text (ETHICS.md rule 5); the original is routed to
    the git-ignored ``private/`` directory for manual review instead.
    """
    if isinstance(value, str):
        if has_invisible(value):
            cats = invisible_categories(value)
            summary = ", ".join(f"{k}={v}" for k, v in sorted(cats.items()))
            return f"[redacted by toolcensus: contains non-printing code points ({summary})]", True
        return value, False
    if isinstance(value, list):
        items = [redact_invisible(v) for v in value]
        return [v for v, _ in items], any(r for _, r in items)
    if isinstance(value, dict):
        pairs = {k: redact_invisible(v) for k, v in value.items()}
        return {k: v for k, (v, _) in pairs.items()}, any(r for _, r in pairs.values())
    return value, False
