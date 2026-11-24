# Contributing

Read [PLAN.md](PLAN.md) before changing the repository.

## Add a source

1. Open an issue with the repository URL, category, license, scripts, evals, and verification notes.
2. Add or update a row in [research/SOURCES.md](research/SOURCES.md).
3. Mark `Confidence` as `verified` only after opening the README and license.
4. Record license details in [research/LICENSES.md](research/LICENSES.md).

## Add a skill

1. Copy [templates/SKILL.md](templates/SKILL.md) into `skills/<category>/<skill-id>/SKILL.md`.
2. Fill all nine frontmatter fields.
3. Keep the four body sections: `## Trigger`, `## Steps`, `## Hard rules`, `## Verify`.
4. Update the category README and the root README count.
5. Run the validator:

```bash
python scripts/check_skills.py
```

## Status values

| Status | Meaning |
| --- | --- |
| `referenced` | Pointer to an external source |
| `draft` | Local spec, not used yet |
| `ready` | Used once on a real task |
| `reused` | Used in two or more tasks |
| `blocked` | Dependency named in the body |

## Commit rule

One file per English commit. Do not push from the agent environment.
