#!/usr/bin/env python3
"""Validate SKILL.md frontmatter in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = [
    "name",
    "description",
    "category",
    "status",
    "inputs",
    "outputs",
    "fails_when",
    "verify",
    "source",
]
STATUSES = {"referenced", "draft", "ready", "reused", "blocked"}
CATEGORY_RE = re.compile(r"^\d{2}-[a-z0-9-]+$")


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening ---")

    end = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = index
            break
    if end is None:
        raise ValueError("missing closing ---")

    data: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line.strip()}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def find_skill_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.name == "SKILL.md" else []
    direct = target / "SKILL.md"
    if direct.is_file():
        return [direct]
    return sorted(target.glob("*/*/SKILL.md"))


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = parse_frontmatter(path.read_text(encoding="utf-8"))
    except ValueError as exc:
        return [f"frontmatter: {exc}"]

    for field in REQUIRED:
        if not data.get(field):
            errors.append(f"missing or empty: {field}")

    status = data.get("status", "")
    if status and status not in STATUSES:
        errors.append(f"invalid status: {status}")

    skill_dir = path.parent
    category_dir = skill_dir.parent
    if data.get("name") and data["name"] != skill_dir.name:
        errors.append(f"name '{data['name']}' != directory '{skill_dir.name}'")
    if data.get("category") and data["category"] != category_dir.name:
        errors.append(f"category '{data['category']}' != directory '{category_dir.name}'")
    if not CATEGORY_RE.match(category_dir.name):
        errors.append(f"invalid category directory: {category_dir.name}")

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else repo_root / "skills"

    if not target.exists():
        print(f"FAIL target not found: {target}")
        return 1

    files = find_skill_files(target)
    if not files:
        print(f"FAIL no SKILL.md found under: {target}")
        return 1

    failed = 0
    for path in files:
        errors = validate(path)
        if errors:
            failed += 1
            print(f"FAIL {path.relative_to(repo_root)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK {path.relative_to(repo_root)}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
