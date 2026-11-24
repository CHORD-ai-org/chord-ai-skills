# Metrics

Generated: 2026-11-24

| Metric | Value |
| --- | --- |
| SKILL.md files | 189 |
| 01-metacognition | 1 |
| 02-engineering | 2 |
| 03-visual | 2 |
| 04-foundations | 1 |
| 05-domain | 180 |
| 06-interaction | 1 |
| 07-narrative | 1 |
| 08-specific | 1 |
| `referenced` | 188 |
| `draft` | 0 |
| `ready` | 0 |
| `reused` | 0 |
| `blocked` | 1 |
| Generic trigger files | 0 |
| Missing body sections | 0 |
| Pinned sources | 8 |
| Domain skills sampled for quality | 40 |
| Open decisions | 2 |
| Validator result | 189 OK / 0 FAIL |
| Release artifacts | 188 |

Ignored metrics: GitHub stars, download counts, bulk-install counts.

Review rules:

- Validator runs on every commit through `.github/workflows/check-skills.yml`.
- README counts are checked by `python scripts/check_skills.py`.
- Licenses are rechecked quarterly.
- Domain skills are sampled after every 20 new entries.
- Blocked skills are reviewed when their dependency changes.
