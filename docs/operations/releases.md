# Releases

Generate CLI-compatible artifacts:

```bash
python scripts/build_release_index.py
```

Output:

```text
releases/skills/<name>/SKILL.md
releases/index.json
```

`releases/` is gitignored. Blocked skills are skipped.
