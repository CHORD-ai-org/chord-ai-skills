# Security review

Reviewed on: 2026-11-24

No upstream executable scripts were copied into this repository. No upstream skill was executed in this repository during import.

## Sampled script review

| Source | Sampled scripts | Findings | Decision |
| --- | --- | --- | --- |
| `anthropics/skills` | `skill-creator/scripts/*.py`, `eval-viewer/generate_review.py` | `subprocess` launches `claude -p`; eval viewer runs a local HTTP server and can terminate a process on a chosen port. | Do not copy or run here. Keep pointer only. |
| `obra/superpowers` | `brainstorming/scripts/helper.js`, `start-server.sh`, `stop-server.sh` | Browser helper opens a WebSocket to the same host; server scripts manage a local companion process. | Do not copy or run here. Keep pointer only. |
| `vercel-labs/agent-skills` | `web-design-guidelines` folder | No scripts in the sampled folder. Bundles pinned `references/command.md`. | Keep pointer. |
| `danjdewhurst/story-skills` | `worldbuilding` folder | No scripts in the sampled folder; skill references an external `story` CLI. | Keep pointer. Do not assume CLI is installed. |
| `zbbsdsb/Fundemetal` | `decomposer` folder | No scripts in the sampled folder; protocol files and evals only. | Keep pointer. |
| `alirezarezvani/claude-skills` | repository-wide scripts present | Scripts exist in upstream; none copied into this repo. Sampled 20 domain pointers are Markdown only. | Keep pointers. Full script audit required before execution. |
| `K-Dense-AI/scientific-agent-skills` | repository-wide scripts present | Scripts exist in upstream; only an index pointer is stored here. | Keep pointer. Full script audit required before execution. |
| `casemark/skills` | scripts status unknown | No scripts copied into this repo. 160 domain pointers are Markdown only. | Keep pointers. Audit before execution. |
| `trailofbits/skills` | security-tooling scripts present | License flag CC-BY-SA-4.0. | Do not reuse in this MIT repo. |

## Rules

- Do not run `npx skills use` on unreviewed sources.
- Disable telemetry during automated discovery:

```bash
DISABLE_TELEMETRY=1 npx skills find <keyword>
```

- Read every `SKILL.md` before promotion.
- Treat `scripts/` as code requiring review.
- Never auto-update promoted sources. Review changes as PRs.
