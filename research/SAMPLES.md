# Upstream SKILL.md samples

Raw files were downloaded to local scratch only. Do not copy them into `skills/` or commit them. This file records what the samples show.

Sampled on: 2026-11-24

| Sample | Upstream path | Frontmatter | Structure lesson |
| --- | --- | --- | --- |
| anthropics/frontend-design | `skills/frontend-design/SKILL.md` | `name`, `description`, `license` | Long brief-level body. Names generic AI design tells. Uses a two-pass plan → review → build → critique flow. |
| anthropics/skill-creator | `skills/skill-creator/SKILL.md` | `name`, `description` | Treats skill authoring as an eval loop: draft, test prompts, evaluate, rewrite, expand. |
| obra/superpowers | `skills/brainstorming/SKILL.md` | `name`, `description` | Hard workflow gates. Forces approach selection, design doc, approval, then handoff to `writing-plans`. |
| danjdewhurst/story-skills | `skills/worldbuilding/SKILL.md` | `name`, `description` | Depends on project files and a CLI. References `story.md`, `_index.md`, and bundled `references/`. |
| zbbsdsb/Fundemetal | `skills/decomposer/SKILL.md` | none | Not an Agent Skills `SKILL.md`. It is an index pointing to `PROTOCOL.md`, `MANIFEST.md`, `FIELD_GUIDE.md`, and `adapters/`. |
| vercel-labs/agent-skills | `skills/web-design-guidelines/SKILL.md` | `name`, `description`, `metadata` | Thin loader. Pins an upstream commit and SHA-256 for bundled `references/command.md`. |

## Findings that change the plan

1. Upstream Agent Skills use `name` + `description` as the real compatibility core. This repo currently requires `name` but not `description`.
2. Our repository-specific fields (`status`, `inputs`, `outputs`, `fails_when`, `verify`, `source`) are curation metadata, not the upstream standard.
3. A pointer skill can keep our curation fields. A copied or generated skill must include `description` and should keep `name` first.
4. Fundemetal skill folders are not directly Agent Skills compatible. Copying one requires adding frontmatter and deciding what stays in `PROTOCOL.md`.
5. Vercel's pinned snapshot pattern is the strongest example for `research/LICENSES.md` and release artifacts.

## Actions

- Add `description` to `templates/SKILL.md` and both existing `SKILL.md` files.
- Extend `scripts/check_skills.py` to require `description`.
- Keep raw samples in local scratch only; link to upstream URLs instead.
- Use the pinned-commit pattern for every promoted pointer.

## Full folder downloads

Downloaded complete skill folders on 2026-11-24 into local scratch only. Raw files are not committed.

| Folder | Upstream path | Files | Scratch path |
| --- | --- | --- | --- |
| `anthropics-frontend-design` | `anthropics/skills` → `skills/frontend-design` | 2 | `.workbuddy/tmp/skill-samples/full/anthropics-frontend-design/` |
| `anthropics-skill-creator` | `anthropics/skills` → `skills/skill-creator` | 18 | `.workbuddy/tmp/skill-samples/full/anthropics-skill-creator/` |
| `superpowers-brainstorming` | `obra/superpowers` → `skills/brainstorming` | 8 | `.workbuddy/tmp/skill-samples/full/superpowers-brainstorming/` |
| `story-worldbuilding` | `danjdewhurst/story-skills` → `skills/worldbuilding` | 10 | `.workbuddy/tmp/skill-samples/full/story-worldbuilding/` |
| `fundemetal-decomposer` | `zbbsdsb/Fundemetal` → `skills/decomposer` | 35 | `.workbuddy/tmp/skill-samples/full/fundemetal-decomposer/` |
| `vercel-web-design-guidelines` | `vercel-labs/agent-skills` → `skills/web-design-guidelines` | 2 | `.workbuddy/tmp/skill-samples/full/vercel-web-design-guidelines/` |

Manifest: `.workbuddy/tmp/skill-samples/MANIFEST.tsv`. Source branch: `main`. Commit SHAs were not captured because the GitHub API was rate-limited; pin before promotion.
