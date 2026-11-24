#!/usr/bin/env python3
"""Build CLI-compatible release artifacts from category-based skill sources."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASES = ROOT / "releases"


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
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
    data = {}
    for line in lines[1:end]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, "\n".join(lines[end + 1 :])


def main() -> int:
    sources = sorted(ROOT.glob("skills/*/*/SKILL.md"))
    if not sources:
        print("FAIL no source skills found")
        return 1

    if RELEASES.exists():
        shutil.rmtree(RELEASES)
    (RELEASES / "skills").mkdir(parents=True)

    seen: set[str] = set()
    index = []
    for path in sources:
        text = path.read_text(encoding="utf-8")
        try:
            data, body = parse_frontmatter(text)
        except ValueError as exc:
            print(f"FAIL {path.relative_to(ROOT)}: {exc}")
            return 1

        if data.get("status") == "blocked":
            continue
        name = data.get("name", "")
        if not name:
            print(f"FAIL {path.relative_to(ROOT)}: missing name")
            return 1
        if name in seen:
            print(f"FAIL duplicate name: {name}")
            return 1
        seen.add(name)

        out_dir = RELEASES / "skills" / name
        out_dir.mkdir(parents=True)
        (out_dir / "SKILL.md").write_text(text, encoding="utf-8")
        index.append(
            {
                "name": name,
                "description": data.get("description", ""),
                "category": data.get("category", ""),
                "status": data.get("status", ""),
                "source": data.get("source", ""),
            }
        )

    (RELEASES / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"built {len(index)} release skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
