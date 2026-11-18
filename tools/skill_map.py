#!/usr/bin/env python3
"""Build dev-lead/references/skill-map.md from each skill's Connections block.

Every SKILL.md ends with a "## Connections" section holding three lines:
Needs, Produces, Next. Those lines are the single source of truth. This script
turns them into one overview (a stage table and a "who makes which file" index)
so the router can see the whole pack at once.

Usage:
    python tools/skill_map.py          print the map
    python tools/skill_map.py --write  update dev-lead/references/skill-map.md
    python tools/skill_map.py --check  exit 1 if that file is out of date
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP_FILE = ROOT / "dev-lead" / "references" / "skill-map.md"
FIELDS = ("Needs", "Produces", "Next")
BACKTICKED = re.compile(r"`([^`]+)`")
SKILL_NAME = re.compile(r"^[a-z]+(?:-[a-z]+)+$")


def skill_dirs() -> list[Path]:
    """dev-lead first (the router), then the stage skills alphabetically."""
    dirs = sorted(p.parent for p in ROOT.glob("*/SKILL.md"))
    return sorted(dirs, key=lambda d: (d.name != "dev-lead", d.name))


def parse_connections(skill_dir: Path) -> dict[str, str]:
    """Return {"Needs": ..., "Produces": ..., "Next": ...} for one skill."""
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r"^## Connections\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field = re.match(r"- \*\*(\w+):\*\*\s*(.+\S)\s*$", line)
        if field:
            fields[field.group(1)] = field.group(2)
    return fields


def skill_names_in(text: str) -> list[str]:
    """Backticked, hyphenated lowercase tokens: the skill names mentioned."""
    return [t for t in BACKTICKED.findall(text) if SKILL_NAME.match(t)]


def artifacts_in(text: str) -> list[str]:
    """Backticked Markdown file names mentioned, in order, without repeats."""
    seen: list[str] = []
    for token in BACKTICKED.findall(text):
        if token.endswith(".md") and token not in seen:
            seen.append(token)
    return seen


def load_all() -> dict[str, dict[str, str]]:
    return {d.name: parse_connections(d) for d in skill_dirs()}


def build_map() -> str:
    skills = load_all()
    lines = [
        "# Skill map",
        "",
        "Generated from the Connections block at the end of every SKILL.md by "
        "`tools/skill_map.py`. Do not edit by hand: change a skill's Connections "
        "and run `python tools/skill_map.py --write`.",
        "",
        "How to use it: before a stage, check its **Needs** exist in the repo. If one is "
        "missing, run the skill that produces it (see the file index) or, for a small "
        "clear task, write the minimum yourself and say so. After a stage, offer the "
        "**Next** options whose condition is true now.",
        "",
        "## Stages",
        "",
        "| Skill | Needs | Produces | Next |",
        "|-------|-------|----------|------|",
    ]
    for name, fields in skills.items():
        cells = [fields.get(f, "").replace("|", "\\|") for f in FIELDS]
        lines.append(f"| `{name}` | " + " | ".join(cells) + " |")

    produced: dict[str, list[str]] = {}
    needed: dict[str, list[str]] = {}
    for name, fields in skills.items():
        for artifact in artifacts_in(fields.get("Produces", "")):
            produced.setdefault(artifact, []).append(name)
        for artifact in artifacts_in(fields.get("Needs", "")):
            needed.setdefault(artifact, []).append(name)

    lines += [
        "",
        "## Who makes which file",
        "",
        "| File | Produced or updated by | Needed by |",
        "|------|------------------------|-----------|",
    ]
    for artifact in sorted(set(produced) | set(needed)):
        makers = ", ".join(f"`{s}`" for s in produced.get(artifact, [])) or "-"
        users = ", ".join(f"`{s}`" for s in needed.get(artifact, [])) or "-"
        lines.append(f"| `{artifact}` | {makers} | {users} |")
    return "\n".join(lines) + "\n"


def main(argv: list[str]) -> int:
    expected = build_map()
    if "--write" in argv:
        MAP_FILE.write_text(expected, encoding="utf-8", newline="\n")
        print(f"wrote {MAP_FILE.relative_to(ROOT)}")
        return 0
    if "--check" in argv:
        current = MAP_FILE.read_text(encoding="utf-8") if MAP_FILE.exists() else ""
        if current.replace("\r\n", "\n") != expected:
            print("skill-map.md is out of date; run: python tools/skill_map.py --write")
            return 1
        print("skill-map.md is up to date")
        return 0
    print(expected, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
