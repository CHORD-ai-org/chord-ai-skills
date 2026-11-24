# chord-ai-skills
The skills best suited for handling complex tasks in the world

A collection of Skills for CHORD AI ORG, built for complex tasks.

Website: https://chord-ai-org.github.io/
Categories from: [from the start.md](<from the start.md>) (diary entry, 2026-11-23)
Research index: [research/SOURCES.md](research/SOURCES.md)
Master plan: [PLAN.md](PLAN.md)
Contribution guide: [CONTRIBUTING.md](CONTRIBUTING.md)
Expert-field candidates: [research/EXPERT_FIELDS.md](research/EXPERT_FIELDS.md)

189 SKILL.md files so far. 180 are domain pointers; 9 are local or source pointers.

## Categories

| # | Category | Directory | Scope | Count |
| --- | --- | --- | --- | --- |
| 1 | Metacognition & Methodology | [01-metacognition](skills/01-metacognition/README.md) | Thinking methods; reference Fundamental | 1 |
| 2 | Engineering | [02-engineering](skills/02-engineering/README.md) | Write code, review code, structure diagrams, tech choices | 2 |
| 3 | Visual Ability | [03-visual](skills/03-visual/README.md) | Aesthetic judgment, style imitation, web pages in any style | 2 |
| 4 | Foundations | [04-foundations](skills/04-foundations/README.md) | Methods specific to each discipline | 1 |
| 5 | Domain Knowledge | [05-domain](skills/05-domain/README.md) | Quantitative trading, surgery, insurance, and similar domains | 180 |
| 6 | Human–Agent Interaction | [06-interaction](skills/06-interaction/README.md) | How humans and agents interact; grill-me | 1 |
| 7 | Creative & Narrative | [07-narrative](skills/07-narrative/README.md) | Worldbuilding and narrative work | 1 |
| 8 | Miscellaneous / Specific / Niche | [08-specific](skills/08-specific/README.md) | Skills that do not fit the first seven | 1 |

## Add a skill

1. Create `<skill-id>/SKILL.md` under the matching category.
2. Fill in 9 fields: `name`, `description`, `category`, `status`, `inputs`, `outputs`, `fails_when`, `verify`, `source`.
3. Keep four body sections: `## Trigger`, `## Steps`, `## Hard rules`, `## Verify`.
4. Update the category README table and the count above.

Allowed `status` values:

| Status | Meaning |
| --- | --- |
| `referenced` | Pointer to an external source |
| `draft` | Local spec, not used yet |
| `ready` | Used once on a real task |
| `reused` | Used in two or more tasks |
| `blocked` | Dependency named in the body |

## Release artifacts

Generate CLI-compatible artifacts without changing the source tree:

```bash
python scripts/build_release_index.py
```

The command writes `releases/skills/<name>/SKILL.md` and `releases/index.json`. Blocked skills are skipped. `releases/` is gitignored.

## To confirm

- `LICENSE` is MIT; the website footer says GPL-3.0. Open an issue before changing it.
