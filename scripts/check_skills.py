#!/usr/bin/env python3
"""Validate SKILL.md frontmatter, body sections, and README counts."""

from __future__ import annotations

import re
import sys
from collections import Counter
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
SECTIONS = ["## Trigger", "## Steps", "## Hard rules", "## Verify"]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CATEGORY_RE = re.compile(r"^\d{2}-[a-z0-9-]+$")
LIST_RE = re.compile(r"^\s*(?:\d+\.|[-*])\s+\S")
GENERIC_TRIGGER = "Use when the task falls under"
VALIDATE_CMD = "python scripts/check_skills.py"


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
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
    return data, lines[end + 1 :]


def section_body(body: list[str], heading: str) -> list[str]:
    start = None
    for index, line in enumerate(body):
        if line.strip() == heading:
            start = index + 1
            break
    if start is None:
        return []
    out = []
    for line in body[start:]:
        if line.startswith("## "):
            break
        out.append(line)
    return out


def find_skill_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target] if target.name == "SKILL.md" else []
    direct = target / "SKILL.md"
    if direct.is_file():
        return [direct]
    return sorted(target.glob("*/*/SKILL.md"))


def validate(path: Path, repo_root: Path) -> list[str]:
    errors: list[str] = []
    try:
        data, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    except ValueError as exc:
        return [f"frontmatter: {exc}"]

    for field in REQUIRED:
        if not data.get(field):
            errors.append(f"missing or empty: {field}")

    name = data.get("name", "")
    status = data.get("status", "")
    description = data.get("description", "")
    source = data.get("source", "")

    if name and not NAME_RE.match(name):
        errors.append(f"invalid name: {name}")
    if description and len(description) > 1024:
        errors.append(f"description too long: {len(description)}")
    if status and status not in STATUSES:
        errors.append(f"invalid status: {status}")
    if source and not (
        source.startswith("http://")
        or source.startswith("https://")
        or source == "from the start.md"
    ):
        errors.append(f"invalid source: {source}")

    skill_dir = path.parent
    category_dir = skill_dir.parent
    if name and name != skill_dir.name:
        errors.append(f"name '{name}' != directory '{skill_dir.name}'")
    category = data.get("category", "")
    if category and category != category_dir.name:
        errors.append(f"category '{category}' != directory '{category_dir.name}'")
    if not CATEGORY_RE.match(category_dir.name):
        errors.append(f"invalid category directory: {category_dir.name}")

    for section in SECTIONS:
        if section not in body:
            errors.append(f"missing section: {section}")

    trigger = " ".join(section_body(body, "## Trigger"))
    if GENERIC_TRIGGER in trigger:
        errors.append("generic trigger text")

    steps = [line for line in section_body(body, "## Steps") if LIST_RE.match(line)]
    if len(steps) < 2:
        errors.append("steps: fewer than 2 list items")

    verify = " ".join(section_body(body, "## Verify"))
    if VALIDATE_CMD not in verify:
        errors.append("verify: missing validator command")

    category_readme = repo_root / "skills" / category_dir.name / "README.md"
    if category_readme.is_file() and name:
        row_re = re.compile(
            rf"\|\s*(?:\[{re.escape(name)}\]\([^)]*\)|{re.escape(name)})\s*\|"
        )
        if not row_re.search(category_readme.read_text(encoding="utf-8")):
            errors.append(f"not listed in {category_readme.relative_to(repo_root)}")

    return errors


def count_errors(files: list[Path], repo_root: Path) -> list[str]:
    errors: list[str] = []
    counts = Counter(path.parent.parent.name for path in files)
    readme = (repo_root / "README.md").read_text(encoding="utf-8")

    total_match = re.search(r"(\d+) SKILL\.md files so far", readme)
    if not total_match:
        errors.append("README.md: missing skill total sentence")
    elif int(total_match.group(1)) != len(files):
        errors.append(f"README.md: skill total {total_match.group(1)} != {len(files)}")

    row_re = re.compile(
        r"^\|\s*\d+\s*\|\s*[^|]+\|\s*\[([^\]]+)\]\([^)]+\)\s*\|.*\|\s*(\d+)\s*\|$"
    )
    for line in readme.splitlines():
        match = row_re.match(line)
        if not match:
            continue
        category, listed = match.group(1), int(match.group(2))
        if counts.get(category, 0) != listed:
            errors.append(
                f"README.md: {category} count {listed} != {counts.get(category, 0)}"
            )

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
        errors = validate(path, repo_root)
        if errors:
            failed += 1
            print(f"FAIL {path.relative_to(repo_root)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK {path.relative_to(repo_root)}")

    if len(sys.argv) == 1:
        for error in count_errors(files, repo_root):
            failed += 1
            print("FAIL README.md")
            print(f"  - {error}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
