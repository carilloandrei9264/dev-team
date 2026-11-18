#!/usr/bin/env python3
"""Helpers for the visual style catalog in design-ui/references/styles/.

Used by the tests, and as a small command-line tool:

    python tools/style_catalog.py --gallery [out.html]

builds a single HTML page that shows every style (its real tokens and starter
CSS) side by side, so the styles can be judged by eye. Web fonts are not loaded
in the gallery; the fallback stacks are shown.
"""
from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STYLES_DIR = ROOT / "design-ui" / "references" / "styles"
INDEX_FILE = STYLES_DIR / "index.md"

REQUIRED_SECTIONS = (
    "Signature traits",
    "Fits",
    "Avoid when",
    "Tokens",
    "Starter CSS",
    "Accessibility traps",
    "Pairs with",
)
COLOR_TOKENS = ("--bg", "--surface", "--text", "--muted", "--primary", "--on-primary", "--accent", "--focus")
OTHER_TOKENS = ("--radius", "--shadow", "--font-display", "--font-body")
HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")


def style_files() -> list[Path]:
    return sorted(p for p in STYLES_DIR.glob("*.md") if p.name != "index.md")


def sections(text: str) -> dict[str, str]:
    """Split a Markdown file into {heading: body} for its '## ' sections.

    Lines inside fenced code blocks are never treated as headings, so a template
    that contains '## ' lines in a code fence stays in one piece.
    """
    result: dict[str, list[str]] = {}
    current: str | None = None
    in_fence = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        if not in_fence and line.startswith("## "):
            current = line[3:].strip()
            result[current] = []
        elif current is not None:
            result[current].append(line)
    return {heading: "\n".join(body) + "\n" for heading, body in result.items()}


def css_block(section_body: str) -> str:
    match = re.search(r"```css\n(.*?)```", section_body, re.S)
    return match.group(1) if match else ""


def parse_tokens(css: str) -> dict[str, str]:
    """Read '--name: value;' declarations from a :root block."""
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"(--[\w-]+)\s*:\s*([^;]+);", css)}


def parse_style(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    secs = sections(text)
    tokens_css = css_block(secs.get("Tokens", ""))
    return {
        "name": path.stem,
        "title": text.splitlines()[0].lstrip("# ").strip(),
        "sections": secs,
        "tokens_css": tokens_css,
        "tokens": parse_tokens(tokens_css),
        "starter_css": css_block(secs.get("Starter CSS", "")),
        "traps": [l for l in secs.get("Accessibility traps", "").splitlines() if l.startswith("- ")],
    }


def luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    channels = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    lin = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]


def contrast(a: str, b: str) -> float:
    """WCAG contrast ratio between two #RRGGBB colors."""
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def index_links() -> list[str]:
    """Style file names linked from index.md, in order."""
    text = INDEX_FILE.read_text(encoding="utf-8")
    return re.findall(r"\]\(([a-z0-9-]+\.md)\)", text)


SAMPLE = """<main style="padding:24px;box-sizing:border-box">
<h1>{title}</h1>
<p>Sample copy to judge type, spacing, and contrast.</p>
<div class="demo-stack bento">
<div class="card wide"><h2>Weekly summary</h2><p>Your monstera grew 2 cm this week.</p>
<p><label for="plant">Plant name</label><br><input id="plant" class="input" placeholder="Monstera"></p>
<p><button class="button" type="button">Add plant</button></p></div>
<div class="card"><h2>Next watering</h2><p>Tomorrow morning</p></div>
</div></main>"""


def demo_document(style: dict) -> str:
    """A full HTML page for one style: generic layout rules first, then the style's own CSS."""
    return (
        '<!doctype html><html lang="en"><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f"<title>{html.escape(style['title'])}</title>"
        "<style>.demo-stack{display:grid;gap:16px}label{display:inline-block;margin-bottom:6px}</style>"
        f"<style>{style['tokens_css']}\n{style['starter_css']}</style>"
        f"<body>{SAMPLE.format(title=html.escape(style['title']))}</body></html>"
    )


def build_gallery() -> str:
    cards = []
    for path in style_files():
        style = parse_style(path)
        wide = style["name"] == "bento-grid"
        cards.append(
            f'<section class="item{" full" if wide else ""}"><h2>{html.escape(style["title"])}</h2>'
            f'<iframe title="{html.escape(style["title"])} sample" loading="lazy" '
            f'srcdoc="{html.escape(demo_document(style), quote=True)}"></iframe></section>'
        )
    return (
        '<!doctype html><html lang="en"><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        "<title>Style gallery</title><style>"
        "body{margin:0;padding:24px;font:16px/1.5 system-ui,sans-serif;background:#eee;color:#111}"
        "h1{margin:0 0 4px}p.note{margin:0 0 20px;color:#444}"
        ".grid{display:grid;gap:24px;grid-template-columns:repeat(auto-fill,minmax(420px,1fr))}"
        ".item h2{font-size:1rem;margin:0 0 8px}.item.full{grid-column:1/-1}"
        "iframe{width:100%;height:560px;border:1px solid #bbb;background:#fff}"
        "</style><body><h1>Style gallery</h1>"
        '<p class="note">Generated from design-ui/references/styles. Web fonts are not loaded, so fallback fonts are shown.</p>'
        '<div class="grid">' + "".join(cards) + "</div></body></html>"
    )


def main(argv: list[str]) -> int:
    if "--gallery" in argv:
        i = argv.index("--gallery")
        out = Path(argv[i + 1]) if len(argv) > i + 1 else Path("style-gallery.html")
        out.write_text(build_gallery(), encoding="utf-8")
        print(f"wrote {out}")
        return 0
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
