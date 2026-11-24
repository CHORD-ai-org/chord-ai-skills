# Authoring workflow

1. Open a source-candidate issue.
2. Verify README, license, and one `SKILL.md`.
3. Add a row to [`research/SOURCES.md`](../../research/SOURCES.md).
4. Copy the template into `skills/<category>/<skill-id>/SKILL.md`.
5. Run `python scripts/check_skills.py`.
6. Update category and root README counts.
7. Commit one file at a time.
