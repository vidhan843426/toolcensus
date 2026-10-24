"""Static SVG line charts rendered at build time (no JavaScript, no external requests)."""

from __future__ import annotations

from collections.abc import Sequence
from html import escape


def line_chart(
    title: str,
    labels: Sequence[str],
    values: Sequence[float | None],
    *,
    unit: str = "%",
    width: int = 640,
    height: int = 220,
    y_max: float | None = None,
) -> str:
    pad_l, pad_r, pad_t, pad_b = 48, 16, 32, 36
    pts = [(i, v) for i, v in enumerate(values) if v is not None]
    top = y_max if y_max is not None else max([v for _, v in pts] + [1.0]) * 1.1
    iw, ih = width - pad_l - pad_r, height - pad_t - pad_b
    n = max(len(labels) - 1, 1)

    def xy(i: int, v: float) -> tuple[float, float]:
        return pad_l + iw * i / n, pad_t + ih * (1 - v / top if top else 1)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="{escape(title)}" font-family="system-ui, sans-serif" font-size="11">',
        f"<title>{escape(title)}</title>",
        f'<text x="{pad_l}" y="18" font-size="13" font-weight="600" fill="currentColor">{escape(title)}</text>',
    ]
    for frac in (0, 0.5, 1):
        y = pad_t + ih * (1 - frac)
        parts.append(
            f'<line x1="{pad_l}" x2="{width - pad_r}" y1="{y:.1f}" y2="{y:.1f}" stroke="#8884" />'
        )
        parts.append(
            f'<text x="{pad_l - 6}" y="{y + 4:.1f}" text-anchor="end" fill="#888">{top * frac:.0f}{unit}</text>'
        )
    step = max(1, len(labels) // 8)
    for i, label in enumerate(labels):
        if i % step == 0 or i == len(labels) - 1:
            x, _ = xy(i, 0)
            parts.append(
                f'<text x="{x:.1f}" y="{height - 12}" text-anchor="middle" fill="#888">{escape(label)}</text>'
            )
    if pts:
        path = " ".join(f"{x:.1f},{y:.1f}" for x, y in (xy(i, v) for i, v in pts))
        parts.append(
            f'<polyline points="{path}" fill="none" stroke="#3b82f6" stroke-width="2.5" />'
        )
        for i, v in pts:
            x, y = xy(i, v)
            parts.append(
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="#3b82f6"><title>{escape(labels[i])}: {v}{unit}</title></circle>'
            )
    else:
        parts.append(
            f'<text x="{width / 2}" y="{height / 2}" text-anchor="middle" fill="#888">no data yet</text>'
        )
    parts.append("</svg>")
    return "\n".join(parts)
