# CHORD Skills — Master Plan

Status: active working plan  
Last updated: 2026-11-24  
Scope: `chord-ai-skills` repository only  
Source of category taxonomy: `from the start.md` (2026-11-23 diary entry)  
Website: https://chord-ai-org.github.io/

---

## 1. Current baseline

### 1.1 Tracked files

| Path | State | Note |
| --- | --- | --- |
| `.gitignore` | committed | Ignores agent scratch, virtualenvs, env files, build output, OS files |
| `LICENSE` | committed | MIT, copyright CHORD-ai-org |
| `README.md` | committed | Category index, add-a-skill steps, status values, open license question |
| `from the start.md` | committed | Source diary; keep untranslated |
| `skills/01-metacognition/README.md` | committed | 1 skill listed |
| `skills/02-engineering/README.md` | committed | 0 skills listed |
| `skills/03-visual/README.md` | committed | 0 skills listed |
| `skills/04-foundations/README.md` | committed | 0 skills listed |
| `skills/05-domain/README.md` | committed | 0 skills listed |
| `skills/06-interaction/README.md` | committed | 1 skill listed |
| `skills/07-narrative/README.md` | committed | 0 skills listed |
| `skills/08-specific/README.md` | committed | 0 skills listed |
| `research/SOURCES.md` | committed | 10 candidate repositories |
| `research/QUERIES.md` | committed | 8 category queries plus CLI discovery commands |
| `research/log/2026-11-24.md` | committed | Daily research log |
| `templates/SKILL.md` | committed | 8-field template |
| `scripts/check_skills.py` | committed | Frontmatter validator |
| `skills/01-metacognition/fundemetal/SKILL.md` | committed | `status: referenced` pointer |
| `skills/06-interaction/grill-me/SKILL.md` | committed | `status: blocked` on Thylas session state |

### 1.2 Verified working state

- `python scripts/check_skills.py` passes for both existing skills.
- All README files are English.
- Working tree is clean at the time this plan was written.
- Nothing has been pushed in this session. Push stays with the user.

### 1.3 Open conflicts

| Conflict | Current fact | Action |
| --- | --- | --- |
| License | Repo `LICENSE` is MIT; CHORD website footer says GPL-3.0 | Open an issue with CHORD. Do not change `LICENSE` until answered. |
| Skill package layout | This repo uses `skills/<category>/<skill>/SKILL.md`; `npx skills add` expects `skills/<name>/SKILL.md` | Decide between generated release artifacts or a layout change. Do not silently reorganize. |
| `grill-me` dependency | Needs Thylas customizable persistent session state | Keep `blocked`; unblock only when the dependency exists. |

---

## 2. Principles

1. **Evidence before entry.** A repository becomes a source only after README and license are opened directly.
2. **Pointer before copy.** Prefer a pointer `SKILL.md` over copying an upstream skill folder.
3. **One skill, one directory, one commit.** Every new `SKILL.md` is its own commit.
4. **No bulk install.** Add one skill, run it once on a real task, then decide.
5. **Scripts are code.** Any source with `scripts/` gets a code read before reuse.
6. **Status must be honest.** `referenced` is not `ready`; `blocked` must name the blocker.
7. **Category is stable; content moves.** Keep the 8 categories from the diary. Put cross-category skills under a primary category and name secondary categories in the body.
8. **Research stays separate.** `research/` is staging. `skills/` is curated.
9. **No vanity metrics.** Stars are not a quality signal. Multiple sources disagree on star counts.
10. **Reversible changes.** Keep source files small and references explicit so a bad source can be removed in one commit.

---

## 3. Target structure

```text
chord-ai-skills/
├── LICENSE
├── README.md
├── PLAN.md
├── from the start.md
├── .gitignore
├── templates/
│   └── SKILL.md
├── scripts/
│   ├── check_skills.py
│   └── build_release_index.py          # proposed
├── research/
│   ├── SOURCES.md
│   ├── QUERIES.md
│   ├── LICENSES.md                     # proposed
│   └── log/
│       ├── 2026-11-24.md
│       └── YYYY-MM-DD.md
├── skills/
│   ├── 01-metacognition/
│   │   ├── README.md
│   │   ├── fundemetal/
│   │   ├── superpowers-brainstorming/   # proposed
│   │   └── superpowers-verification/     # proposed
│   ├── 02-engineering/
│   │   ├── README.md
│   │   ├── superpowers-tdd/              # proposed
│   │   └── vercel-react-best-practices/  # proposed
│   ├── 03-visual/
│   │   ├── README.md
│   │   ├── anthropics-frontend-design/   # proposed
│   │   └── jakubkrehel-better-ui/        # proposed, license gate
│   ├── 04-foundations/
│   │   ├── README.md
│   │   └── scientific-skills/            # proposed, license gate
│   ├── 05-domain/
│   │   ├── README.md
│   │   └── security-audit/               # proposed, legal gate
│   ├── 06-interaction/
│   │   ├── README.md
│   │   ├── grill-me/
│   │   ├── anthropics-webapp-testing/    # proposed
│   │   └── jakubkrehel-interface-review/ # proposed, license gate
│   ├── 07-narrative/
│   │   ├── README.md
│   │   ├── story-worldbuilding/          # proposed
│   │   └── story-init/                   # proposed
│   └── 08-specific/
│       ├── README.md
│       └── find-skills/                  # proposed
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── source-candidate.md           # proposed
│   │   └── skill-proposal.md             # proposed
│   ├── PULL_REQUEST_TEMPLATE.md          # proposed
│   └── workflows/
│       └── check-skills.yml              # proposed
└── releases/                             # generated, not committed
    └── skills/<skill-id>/SKILL.md
```

Items marked proposed are not created yet.

---

## 4. Stage A — Freeze the baseline

### Goal

Make the current state auditable before adding more content.

### Actions

1. Add this `PLAN.md`.
2. Add `DECISIONS.md` with open decisions and resolved decisions.
3. Add `research/LICENSES.md` with one row per source license.
4. Record the license conflict as an issue draft locally before opening it upstream.
5. Record the package-layout conflict as a decision, not an implementation task.

### Acceptance criteria

- `PLAN.md` exists and links to `README.md`, `research/SOURCES.md`, and `from the start.md`.
- `DECISIONS.md` contains at least three entries: license conflict, package layout, `grill-me` dependency.
- `research/LICENSES.md` lists MIT, Apache 2.0, CC0 1.0, per-skill MIT, CC-BY-SA-4.0, SPDX unknown.
- No existing file is renamed.

### Files

```text
PLAN.md                    new
DECISIONS.md               new
research/LICENSES.md       new
```

---

## 5. Stage B — Harden the research pipeline

### Goal

Turn `research/` into a repeatable intake system.

### Current files

- `research/SOURCES.md` — repository-level candidates.
- `research/QUERIES.md` — discovery queries.
- `research/log/2026-11-24.md` — daily additions.

### Add to `SOURCES.md`

| Field | Rule |
| --- | --- |
| `Repo` | GitHub `owner/repo`, linked |
| `Category` | One or more of `01`–`08` |
| `License` | SPDX ID when known; `unverified` otherwise |
| `Install` | Exact command from upstream README |
| `Scripts` | `yes` / `no` / `unknown` |
| `Evals` | `yes` / `no` / `unknown` |
| `Last commit` | ISO date; `unknown` if not checked |
| `Confidence` | `verified` / `unverified` / `license flag` / `index` |
| `Next` | One concrete next action |
| `Verified on` | Date the README was opened |
| `Verified by` | Session or contributor |

### Verification checklist

For every candidate:

1. Open the GitHub repo page directly.
2. Open `README.md`.
3. Open `LICENSE` or the license field in each `SKILL.md`.
4. Open at least one `SKILL.md`.
5. Check whether `scripts/` exists.
6. Check whether `evals/` exists.
7. Record last commit date.
8. Run `npx skills add <repo> --list` if the repo claims CLI support.
9. Do not run `npx skills use` on untrusted sources.
10. Mark `verified` only after steps 1–4.

### Daily log format

Each day gets `research/log/YYYY-MM-DD.md`. Append only.

```markdown
## 2026-11-24

- Added: owner/repo — category 03 — reason.
- Verified: owner/repo — README + LICENSE opened.
- Rejected: owner/repo — reason.
- Next: read LICENSE for jakubkrehel/skills.
```

### Acceptance criteria

- `SOURCES.md` contains the two new columns.
- `LICENSES.md` exists.
- `QUERIES.md` contains the two discovery surfaces and the verification checklist.
- No candidate is promoted to `skills/` without `Confidence: verified`.

---

## 6. Stage C — Verify the first source set

### Goal

Resolve the ten rows already in `SOURCES.md`.

### Source-by-source tasks

| Source | Category | Required action | Gate |
| --- | --- | --- | --- |
| `anthropics/skills` | 01, 02, 03, 06 | Confirm Apache 2.0 and list exact skill folders | Already verified; add pointer for `frontend-design` |
| `obra/superpowers` | 01, 02 | Map Build chain to pointer skills | MIT confirmed; scripts need read before any reuse |
| `vercel-labs/agent-skills` | 02, 03, 06 | Take `web-design-guidelines` and `react-best-practices` as pointers | MIT confirmed |
| `jakubkrehel/skills` | 03, 06 | Read `LICENSE` and set SPDX | Blocked until license is known |
| `danjdewhurst/story-skills` | 07 | Add `worldbuilding` and `story-init` pointers | MIT confirmed |
| `zbbsdsb/Fundemetal` | 01 | Keep pointer; optionally add one protocol pointer | CC0 + per-skill MIT confirmed |
| `K-Dense-AI/claude-scientific-skills` | 04, 05 | Open README and LICENSE | Blocked until verified |
| `trailofbits/skills` | 02, 05 | Legal review of CC-BY-SA-4.0 | Blocked until decision |
| `ComposioHQ/awesome-claude-skills` | all | Use only as discovery index | Do not promote |
| `VoltAgent/awesome-agent-skills` | all | Use only as discovery index | Do not promote |

### Acceptance criteria

- Every `unverified` row is either verified or rejected.
- Every `license flag` row has a written decision in `DECISIONS.md`.
- `research/LICENSES.md` matches `SOURCES.md`.
- Rejected rows stay in `SOURCES.md` with `Next: rejected — reason`.

---

## 7. Stage D — Skill authoring standard v2

### Goal

Make every `SKILL.md` predictable enough for tooling.

### Required frontmatter fields

Current template already requires:

```yaml
name: skill-id
category: 00-category
status: draft
inputs: what the user gives
outputs: what the skill returns
fails_when: condition under which the result is wrong
verify: python scripts/check_skills.py skills/00-category/skill-id
source: URL or diary entry
```

### Status meanings

| Status | Meaning | Allowed next |
| --- | --- | --- |
| `referenced` | Pointer to an external source; no copied logic | `draft`, `rejected` |
| `draft` | Local spec; validator passes; not used yet | `ready`, `blocked` |
| `ready` | Used once on a real task with evidence recorded | `reused` |
| `reused` | Used in two or more distinct tasks | no change |
| `blocked` | Dependency named in body | `draft` when dependency lands |

### Body sections

Every `SKILL.md` must contain:

1. `# Skill title`
2. `## Trigger`
3. `## Steps`
4. `## Hard rules`
5. `## Verify`

Pointer skills may add:

- `## Source`
- `## Formation map`
- `## Failure conditions`
- `## License`
- `## Why blocked`

### Validator upgrades

`scripts/check_skills.py` currently checks frontmatter only. Add:

1. Required body sections.
2. `name` matches directory.
3. `category` matches directory.
4. `status` in allowed set.
5. `source` is either `http...`, `https...`, or `from the start.md`.
6. `verify` is non-empty.
7. Category README contains a row for the skill.
8. No duplicate `name` across the repo.
9. Exit non-zero with file path and field name on failure.
10. Support `--all` and single-path modes without changing output format.

### Acceptance criteria

- `python scripts/check_skills.py` passes.
- Two intentionally broken fixtures fail for the expected reason.
- Validator output stays plain text, one issue per line.
- No external dependencies are added to the validator.

---

## 8. Stage E — Category 01: Metacognition & Methodology

### Current state

- `fundemetal` pointer exists and passes validator.
- `status: referenced`.

### Next skills

| Skill | Source | Status target | Why |
| --- | --- | --- | --- |
| `superpowers-brainstorming` | `obra/superpowers` | `referenced` | Draws intent before build; matches diary category 1 |
| `superpowers-verification` | `obra/superpowers` | `referenced` | Blocks false completion claims |
| `superpowers-writing-skills` | `obra/superpowers` | `referenced` | Method for maintaining this repo |
| `fundemetal-sycophancy-breaker` | `zbbsdsb/Fundemetal` | `draft` | First protocol to localize after pointer is exercised |

### Order

1. Add `superpowers-brainstorming` pointer.
2. Update 01 README row count.
3. Add `superpowers-verification` pointer.
4. Update 01 README row count.
5. Add `superpowers-writing-skills` pointer.
6. Decide whether to localize one Fundemetal protocol.
7. If localizing, run upstream `evals/` first.

### Acceptance criteria

- 01 README count matches actual `SKILL.md` files.
- Each pointer states the upstream folder path.
- No upstream `scripts/` are copied.
- Fundemetal remains one pointer until a real task needs a protocol.

---

## 9. Stage F — Category 02: Engineering

### Current state

- 0 skills.
- Strong sources already verified: `obra/superpowers`, `vercel-labs/agent-skills`.

### Next skills

| Skill | Source | Status target | Gate |
| --- | --- | --- | --- |
| `superpowers-tdd` | `obra/superpowers` | `referenced` | Read `scripts/` before copying anything |
| `superpowers-systematic-debugging` | `obra/superpowers` | `referenced` | Same |
| `vercel-react-best-practices` | `vercel-labs/agent-skills` | `referenced` | Verify folder name |
| `vercel-composition-patterns` | `vercel-labs/agent-skills` | `referenced` | Verify folder name |
| `github-spec-kit` | `github/spec-kit` | `referenced` | Add to `SOURCES.md` first |

### Order

1. Add `superpowers-tdd` pointer.
2. Add `superpowers-systematic-debugging` pointer.
3. Add `vercel-react-best-practices` pointer.
4. Add `vercel-composition-patterns` pointer.
5. Research `github/spec-kit` into `SOURCES.md`.
6. Promote `github-spec-kit` only after license verification.

### Acceptance criteria

- Each skill states whether it enforces a process or only gives advice.
- No skill claims a test passed unless a command is recorded.
- 02 README count matches actual files.

---

## 10. Stage G — Category 03: Visual Ability

### Current state

- 0 skills.
- `anthropics/skills` verified Apache 2.0.
- `vercel-labs/agent-skills` verified MIT.
- `jakubkrehel/skills` license SPDX unknown.

### Next skills

| Skill | Source | Status target | Gate |
| --- | --- | --- | --- |
| `anthropics-frontend-design` | `anthropics/skills` | `referenced` | Confirm folder path |
| `anthropics-canvas-design` | `anthropics/skills` | `referenced` | Confirm folder path |
| `vercel-web-design-guidelines` | `vercel-labs/agent-skills` | `referenced` | Already listed in upstream README |
| `jakubkrehel-better-ui` | `jakubkrehel/skills` | `referenced` | Read LICENSE first |
| `emilkowalski-emil-design-eng` | `emilkowalski/skills` | `referenced` | Add to `SOURCES.md` first |

### Design position

This category should not become a prompt collection. Each skill must state:

- what it changes;
- what it refuses to change;
- what evidence proves the visual result improved.

### Acceptance criteria

- At least one pointer states an explicit anti-generic rule.
- No repository with unknown SPDX is promoted.
- 03 README count matches actual files.

---

## 11. Stage H — Category 04: Foundations

### Current state

- 0 skills.
- No verified source yet.

### Research targets

| Query | Source surface |
| --- | --- |
| `site:github.com agent skills scientific method statistics research` | GitHub search |
| `site:github.com agent skills literature review evidence grading` | GitHub search |
| `npx skills find statistics` | skills CLI |
| `npx skills find research` | skills CLI |

### Candidate

- `K-Dense-AI/claude-scientific-skills` — currently `unverified` in `SOURCES.md`.

### Next skills after verification

| Skill | Source | Status target |
| --- | --- | --- |
| `scientific-skills-index` | `K-Dense-AI/claude-scientific-skills` | `referenced` |
| `source-ledger` | `zbbsdsb/Fundemetal` | `referenced` |
| `disconfirmation-hunt` | `zbbsdsb/Fundemetal` | `referenced` |

Note: the two Fundemetal protocols may be dual-listed here and in 01. Primary category stays 01; 04 README may link back.

### Acceptance criteria

- At least one source in 04 is `verified`.
- LICENSE is recorded in `research/LICENSES.md`.
- 04 README count matches actual files.

---

## 12. Stage I — Category 05: Domain Knowledge

### Current state

- 0 skills.
- No trustworthy medical, legal, or insurance skill found in the first search.
- `trailofbits/skills` is license-flagged CC-BY-SA-4.0.

### Research targets

| Domain | Query |
| --- | --- |
| Quantitative trading | `site:github.com agent skills quantitative trading backtesting risk` |
| Medicine | `site:github.com agent skills clinical medical diagnosis evidence` |
| Law | `site:github.com agent skills legal contract review jurisdiction` |
| Insurance | `site:github.com agent skills insurance underwriting claims actuarial` |
| Security | existing `trailofbits/skills` |

### Rules

1. Do not invent domain skills from general knowledge.
2. Do not promote a source that cannot name its domain boundary.
3. Medical and legal sources require a human expert review row in `SOURCES.md`.
4. CC-BY-SA-4.0 requires a written decision before reuse.

### Next skills after gates

| Skill | Source | Status target | Gate |
| --- | --- | --- | --- |
| `security-audit-index` | `trailofbits/skills` | `referenced` | Legal decision |
| `quant-research-index` | to be found | `referenced` | Source verification |
| `clinical-evidence-index` | to be found | `blocked` if no expert review | Source verification |

### Acceptance criteria

- 05 has at least one verified source or a written reason it is still empty.
- No domain skill claims professional authority.
- Each domain pointer names its failure condition.

---

## 13. Stage J — Category 06: Human–Agent Interaction

### Current state

- `grill-me` exists with `status: blocked`.
- Blocker: Thylas customizable persistent session state.

### Next skills

| Skill | Source | Status target | Gate |
| --- | --- | --- | --- |
| `anthropics-webapp-testing` | `anthropics/skills` | `referenced` | Confirm folder path |
| `jakubkrehel-interface-review` | `jakubkrehel/skills` | `referenced` | Read LICENSE first |
| `jakubkrehel-state-machine` | `jakubkrehel/skills` | `referenced` | Same |
| `grill-me` | this repo | stays `blocked` | Unblock only with Thylas state support |

### Interaction rules to preserve

- One question at a time for `grill-me`.
- Interface-review skills report issues; they do not silently rewrite code.
- State ownership must be explicit: agent state vs user state vs run state.

### Acceptance criteria

- `grill-me` stays blocked until the dependency is real.
- Each new pointer states whether it observes or modifies the interface.
- 06 README count matches actual files.

---

## 14. Stage K — Category 07: Creative & Narrative

### Current state

- 0 skills.
- `danjdewhurst/story-skills` verified MIT, 24 skills, CLI needs Node 18+.

### Next skills

| Skill | Source | Status target |
| --- | --- | --- |
| `story-worldbuilding` | `danjdewhurst/story-skills` | `referenced` |
| `story-init` | `danjdewhurst/story-skills` | `referenced` |
| `story-continuity` | `danjdewhurst/story-skills` | `referenced` |
| `story-coach` | `jwynia/agent-skills` | `referenced` after license check |

### Order

1. Add `story-worldbuilding` pointer.
2. Add `story-init` pointer.
3. Add `story-continuity` pointer.
4. Research `jwynia/agent-skills` license before adding `story-coach`.

### Acceptance criteria

- Each pointer states whether it writes prose or checks structure.
- No pointer claims the upstream CLI is installed here.
- 07 README count matches actual files.

---

## 15. Stage L — Category 08: Miscellaneous / Specific / Niche

### Current state

- 0 skills.

### Next skills

| Skill | Source | Status target |
| --- | --- | --- |
| `find-skills` | local workflow around `npx skills find` | `draft` |
| `source-candidate-triage` | local workflow around `research/SOURCES.md` | `draft` |
| `release-index` | local workflow around `scripts/build_release_index.py` | `draft` after script exists |

### Purpose

This category holds workflows that are too specific for the other seven. It is not a dumping ground. Every skill here must name:

- the exact trigger;
- the command or file it operates on;
- the stop condition.

### Acceptance criteria

- No skill here has a vague name like `helper`.
- Each skill has a runnable verify command.
- 08 README count matches actual files.

---

## 16. Stage M — Validation and CI

### Goal

Make validation automatic for every pull request.

### Workflow

Create `.github/workflows/check-skills.yml`:

```yaml
name: check-skills
on:
  pull_request:
  push:
    branches: [main]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.13'
      - run: python scripts/check_skills.py
```

### Additional checks

Add to the same job or a second job:

1. README counts match `SKILL.md` counts.
2. No Chinese characters in README files.
3. `research/SOURCES.md` has no empty required cell.
4. `PLAN.md` links resolve.
5. No skill has `status: ready` without a `verify` command.

### Acceptance criteria

- CI runs on every PR.
- CI fails on a broken frontmatter fixture.
- CI output names the failing file.
- No CI step installs third-party skills.

---

## 17. Stage N — Security and supply chain

### Goal

Prevent a malicious or hollow skill from entering the repo.

### Rules

1. Read every `SKILL.md` in full before promotion.
2. Treat `scripts/` as executable code; review line by line.
3. Do not run `npx skills use` on an unverified source.
4. Keep `skills-lock.json` outside this repo unless the repo becomes a package consumer.
5. Disable CLI telemetry when running discovery in CI:
   ```bash
   DISABLE_TELEMETRY=1 npx skills find <keyword>
   ```
6. Pin upstream commit SHA in `research/SOURCES.md` for every promoted source.
7. Record checksum or commit in `research/LICENSES.md` when copying any file.
8. Prefer pointer skills over copied scripts.
9. Never auto-update from upstream; review updates as PRs.
10. Keep a `rejected` list with reasons.

### Review checklist

```text
[ ] README opened directly
[ ] LICENSE opened directly
[ ] One SKILL.md opened in full
[ ] scripts/ present? yes / no / unknown
[ ] scripts/ reviewed? yes / n/a
[ ] evals/ present? yes / no / unknown
[ ] upstream commit pinned
[ ] license compatible with MIT repo
[ ] pointer written, no files copied
[ ] category README updated
[ ] validator passes
```

### Acceptance criteria

- Every `referenced` skill has a pinned source commit.
- Every copied file, if any, has a checksum row.
- No promoted source has `Confidence: unverified`.

---

## 18. Stage O — Package layout and distribution

### Problem

This repo uses category folders for curation. The skills CLI expects `skills/<name>/SKILL.md`.

### Options

| Option | Change | Benefit | Cost |
| --- | --- | --- | --- |
| Keep source tree | none | Stable taxonomy | Not directly installable by CLI |
| Generate release artifacts | add `scripts/build_release_index.py` | Source tree unchanged; CLI-compatible output | Extra build step |
| Flatten `skills/` | rename all folders | Direct CLI compatibility | Breaks current taxonomy and links |

### Recommendation

Generate release artifacts. Keep `skills/<category>/<skill>/SKILL.md` as the source of truth.

### Build script requirements

`scripts/build_release_index.py` must:

1. Read every `skills/*/*/SKILL.md`.
2. Read frontmatter fields.
3. Write `releases/skills/<name>/SKILL.md`.
4. Rewrite `category` field to the human-readable category name.
5. Preserve all other fields.
6. Write `releases/index.json` with name, category, status, source.
7. Skip skills with `status: blocked`.
8. Exit non-zero on duplicate names.
9. Add `releases/` to `.gitignore`.
10. Be runnable with no third-party packages.

### Acceptance criteria

- Generated artifacts pass a basic frontmatter check.
- `releases/` is ignored by git.
- The script never writes into `skills/`.
- The script is documented in `README.md`.

---

## 19. Stage P — Governance and contribution

### Files to add

| File | Content |
| --- | --- |
| `CONTRIBUTING.md` | How to propose a source, add a skill, run validator, write commit |
| `DECISIONS.md` | Resolved and open decisions with date and reason |
| `.github/ISSUE_TEMPLATE/source-candidate.md` | Repo URL, category, license, why, failure condition |
| `.github/ISSUE_TEMPLATE/skill-proposal.md` | Trigger, inputs, outputs, fails_when, verify, source |
| `.github/PULL_REQUEST_TEMPLATE.md` | What changed, which skill, validator result, source license |

### Contribution flow

1. Open a source-candidate issue.
2. Verify README and license.
3. Add a row to `research/SOURCES.md`.
4. Wait for approval if license is not SPDX-clear.
5. Create `SKILL.md` from `templates/SKILL.md`.
6. Run `python scripts/check_skills.py`.
7. Update category README and root README count.
8. Commit one file at a time.
9. Open PR with validator output pasted.

### Commit message pattern

```text
Add <skill-id> pointer skill
Add source row for <owner/repo>
Update <category> README for <skill-id>
Add validator for required sections
Update root README counts
```

### Acceptance criteria

- `CONTRIBUTING.md` links to `PLAN.md`, `templates/SKILL.md`, and `scripts/check_skills.py`.
- Issue templates exist for both sources and skills.
- PR template asks for validator output.
- No commit contains more than one file.

---

## 20. Stage Q — Documentation

### Root README additions

1. Link to `PLAN.md`.
2. Link to `CONTRIBUTING.md`.
3. Document the generated release artifact command.
4. Document the difference between `referenced` and `ready`.
5. Keep the license conflict note until resolved.

### Category README format

Each category README must keep:

```markdown
# <NN> <Category>

Scope: <one sentence>.

Source: diary entry 2026-11-23, category <N>.

## Skills

| Skill | Status | Purpose | Source |
| --- | --- | --- | --- |
| ... | ... | ... | ... |

To add: create `<skill-id>/SKILL.md`. See [root README](../../README.md) for fields.
```

### Research README

Add `research/README.md` explaining:

- `SOURCES.md` is staging;
- `QUERIES.md` is the discovery script;
- `log/` is append-only;
- verification means README and license opened directly;
- scripts are not audited by default.

### Acceptance criteria

- Root README links resolve.
- Every category README row matches a real `SKILL.md`.
- `research/README.md` exists.
- No Chinese characters in README files.

---

## 21. Stage R — Metrics and review

### Metrics that matter

| Metric | How to compute |
| --- | --- |
| Verified sources | Count `Confidence: verified` in `SOURCES.md` |
| Skills per category | Count `SKILL.md` files and compare with README counts |
| Ready ratio | `ready + reused` divided by total skills |
| Blocked with named dependency | Count `status: blocked` with a `Why blocked` section |
| Validator pass rate | CI result |
| Removed sources | Count `rejected` rows with reason |
| License unknowns | Count `SPDX unknown` or `unverified` in `LICENSES.md` |

### Metrics to ignore

- GitHub stars.
- Download counts from aggregator sites.
- Number of skills installed at once.
- Number of categories filled quickly.

### Review cadence

| Action | Frequency |
| --- | --- |
| Run validator | Every commit |
| Reconcile README counts | Every skill change |
| Re-check license of promoted sources | Quarterly |
| Review rejected list | Quarterly |
| Re-open source discovery for empty categories | Monthly |
| Re-evaluate `blocked` skills | When dependency changes |

### Acceptance criteria

- Metrics are computed by a script, not by hand.
- Report output is plain text.
- Review dates are recorded in `research/log/`.

---

## 22. Stage S — First 12 concrete tasks

These are the next actionable items after this plan is accepted.

| # | Task | File(s) | Gate |
| --- | --- | --- | --- |
| 1 | Add the master plan | `PLAN.md` | This file |
| 2 | Add decision log | `DECISIONS.md` | Three open decisions recorded |
| 3 | Add license matrix | `research/LICENSES.md` | Matches `SOURCES.md` |
| 4 | Extend source table | `research/SOURCES.md` | New columns added |
| 5 | Read `jakubkrehel/skills` LICENSE | `research/LICENSES.md`, `research/SOURCES.md` | SPDX recorded |
| 6 | Verify `K-Dense-AI/claude-scientific-skills` | `research/SOURCES.md`, `research/LICENSES.md` | Confidence set |
| 7 | Add `superpowers-brainstorming` pointer | `skills/01-metacognition/superpowers-brainstorming/SKILL.md` | Validator passes |
| 8 | Add `anthropics-frontend-design` pointer | `skills/03-visual/anthropics-frontend-design/SKILL.md` | Validator passes |
| 9 | Add `story-worldbuilding` pointer | `skills/07-narrative/story-worldbuilding/SKILL.md` | Validator passes |
| 10 | Add `find-skills` workflow | `skills/08-specific/find-skills/SKILL.md` | Validator passes |
| 11 | Add CI workflow | `.github/workflows/check-skills.yml` | CI green |
| 12 | Add release index script | `scripts/build_release_index.py` | Generated artifacts valid |

Each task is one file or one tightly scoped change. Each change gets its own English commit.

---

## 23. Decision log seed

| ID | Decision | Status | Reason |
| --- | --- | --- | --- |
| D-01 | Keep repo `LICENSE` as MIT | open | Website says GPL-3.0; ask CHORD before changing |
| D-02 | Keep category folder layout | open | CLI compatibility unresolved; prefer generated artifacts |
| D-03 | Keep Fundemetal as one pointer | resolved | Avoid copying 24 protocols before a real need |
| D-04 | Keep `grill-me` blocked | resolved | Thylas session state not available |
| D-05 | Do not bulk-install skills | resolved | Routing degrades with too many installed skills |
| D-06 | Verify README and license before promotion | resolved | Prevents hollow or unsafe sources |
| D-07 | Treat scripts as code | resolved | Supply-chain risk |
| D-08 | Ignore star counts | resolved | Sources disagree; not a quality signal |

---

## 24. Definition of done for the whole plan

The plan is complete when:

1. All 8 categories have at least one `SKILL.md` with `status` not `referenced` only.
2. No category README count disagrees with the filesystem.
3. Every promoted source has a pinned upstream commit.
4. Every promoted source has an SPDX license or a written legal decision.
5. `python scripts/check_skills.py` passes on every commit.
6. CI runs the same validator on every PR.
7. `CONTRIBUTING.md`, `DECISIONS.md`, `research/README.md` exist.
8. Generated release artifacts are installable without changing the source tree.
9. `grill-me` is either unblocked with Thylas state support or remains blocked with the reason still true.
10. The license conflict with the CHORD website is resolved.

---

## 25. Rules for changing this plan

1. Add a dated entry to `DECISIONS.md` when a plan choice changes.
2. Do not rewrite history in this file; append a new section.
3. If a stage is skipped, record the reason.
4. If a source is removed, keep the rejected row with reason.
5. If the category taxonomy changes, open an issue first; it comes from the diary and should not drift silently.
6. Keep this file English.
7. Keep every commit English and one file per commit.
8. Do not push from this environment.

---

## 26. Upstream sample findings and plan correction

Added after downloading six real `SKILL.md` files on 2026-11-24. Raw files stay in local scratch under `.workbuddy/tmp/skill-samples/` and are not committed. Observations are recorded in `research/SAMPLES.md`.

### 26.1 Samples downloaded

| Repo | File | Result |
| --- | --- | --- |
| `anthropics/skills` | `skills/frontend-design/SKILL.md` | Downloaded |
| `anthropics/skills` | `skills/skill-creator/SKILL.md` | Downloaded |
| `obra/superpowers` | `skills/brainstorming/SKILL.md` | Downloaded |
| `danjdewhurst/story-skills` | `skills/worldbuilding/SKILL.md` | Downloaded |
| `zbbsdsb/Fundemetal` | `skills/decomposer/SKILL.md` | Downloaded |
| `vercel-labs/agent-skills` | `skills/web-design-guidelines/SKILL.md` | Downloaded |

### 26.2 What the samples prove

1. The Agent Skills compatibility core is `name` + `description`. Optional upstream fields include `license` and `metadata`.
2. This repo currently requires `name` but not `description`. That blocks clean compatibility with the open format.
3. Our fields `status`, `inputs`, `outputs`, `fails_when`, `verify`, `source` are curation metadata. They are useful here, but they are not a replacement for `description`.
4. `obra/superpowers` uses hard gates. A skill can force a handoff instead of merely advising.
5. `danjdewhurst/story-skills` depends on project files plus a CLI. Pointer skills must state those dependencies.
6. `zbbsdsb/Fundemetal` skill folders are not Agent Skills `SKILL.md` files. They are indexes into `PROTOCOL.md` and adapters. Do not copy one into `skills/` without adding frontmatter.
7. `vercel-labs/agent-skills` pins a source commit and SHA-256 for bundled reference data. This is the model for this repo's release artifacts.

### 26.3 Corrections to earlier stages

Stage D and Stage O are amended as follows:

| Earlier text | Correction |
| --- | --- |
| Required fields are the current 8 fields | Add `description` as field 9. Keep `name` first and `description` second. |
| Validator checks frontmatter only | Validator must also require `description` and enforce `name` as lowercase letters, digits, and hyphens. |
| Template uses 8 fields | Update `templates/SKILL.md` to 9 fields. |
| Existing skills pass as-is | Add `description` to `fundemetal` and `grill-me`, then rerun validator. |
| Fundemetal is ready to localize | Localizing a Fundemetal protocol needs a new frontmatter layer and a decision on where `PROTOCOL.md` content lives. |
| Release artifacts preserve all fields | Release artifacts must emit upstream-compatible frontmatter: `name`, `description`, plus optional `license`. Curation fields may stay but must not break discovery. |

### 26.4 New ordering rule

Before writing more pointer skills:

1. Update the template.
2. Update the validator.
3. Update the two existing skills.
4. Rerun `python scripts/check_skills.py`.
5. Only then add `superpowers-brainstorming`, `anthropics-frontend-design`, `story-worldbuilding`, and the other Stage E–L skills.

This ordering is now mandatory. The earlier Stage S table is superseded where it conflicts with this rule.

### 26.5 Acceptance criteria for this correction

- `templates/SKILL.md` contains `description`.
- `skills/01-metacognition/fundemetal/SKILL.md` contains `description`.
- `skills/06-interaction/grill-me/SKILL.md` contains `description`.
- `scripts/check_skills.py` fails when `description` is missing.
- `research/SAMPLES.md` exists and links no raw copied files.
- No upstream `SKILL.md` text is committed into this repository.

---

## 27. Next-step plan after the 180-skill import

Added after the 2026-11-24 import and repo audit. This section supersedes earlier task ordering where it conflicts.

### 27.1 Audit baseline

| Check | Result |
| --- | --- |
| `SKILL.md` count | 182 |
| Category coverage | `01` 1, `02` 0, `03` 0, `04` 0, `05` 180, `06` 1, `07` 0, `08` 0 |
| Duplicate names | 0 |
| Descriptions over 1024 chars | 0 |
| Missing required body sections | 183 findings |
| Generic trigger text | 180 files |
| Invalid `source` format | 1 file (`grill-me`) |
| Governance files | 7 proposed files missing |
| READMEs with Chinese characters | 0 |
| Validator | 182 OK / 0 FAIL |

The validator passes, but the content is not yet good enough. The main problem is format consistency, not frontmatter correctness.

### 27.2 Phase N1 — Fix the canonical format

Goal: one `SKILL.md` shape across all 182 files.

Required frontmatter order:

```yaml
name:
description:
category:
status:
inputs:
outputs:
fails_when:
verify:
source:
```

Required body sections for every skill:

```markdown
## Trigger
## Steps
## Hard rules
## Verify
```

Pointer skills may add:

```markdown
## Source notes
## Failure conditions
## License
## Why blocked
```

Rules:

1. `description` stays one line and under 1024 characters.
2. `source` must be an `http...` / `https...` URL or exactly `from the start.md`.
3. `## Trigger` must name the concrete task. Ban the generic sentence `Use when the task falls under ... and the upstream skill matches the request.`
4. `## Steps` must contain at least 2 actionable lines.
5. `## Hard rules` must contain the advisory-only rule for legal, medical, finance, and capital skills.
6. `## Verify` must contain the validator command.
7. Fundemetal must be rewritten to include the four required body sections.
8. `grill-me` source must be changed to `from the start.md`; the date and category belong in the body.

Acceptance criteria:

- `missing_sections` audit result is 0.
- `generic_trigger` audit result is 0.
- `bad_source` audit result is 0.
- Validator still reports 182 OK / 0 FAIL.

Files touched:

```text
templates/SKILL.md
scripts/check_skills.py
skills/01-metacognition/fundemetal/SKILL.md
skills/06-interaction/grill-me/SKILL.md
skills/05-domain/*/SKILL.md    # 180 files
```

### 27.3 Phase N2 — Upgrade the validator

Goal: make format rules executable.

Add checks:

1. Required body sections present.
2. `description` non-empty and <= 1024 chars.
3. `name` uses `^[a-z0-9]+(?:-[a-z0-9]+)*$`.
4. `source` is URL or exactly `from the start.md`.
5. `## Trigger` does not contain the banned generic sentence.
6. `## Steps` has at least 2 non-empty list items.
7. `## Verify` contains `python scripts/check_skills.py`.
8. Category README contains a row for each skill.
9. Counts in root README match filesystem counts.

Do not add third-party dependencies.

Acceptance criteria:

- Validator fails on one intentionally broken fixture per rule.
- Validator output stays plain text with file path and reason.
- Full run reports 182 OK / 0 FAIL after N1.

### 27.4 Phase N3 — Fill the empty categories

Goal: no category except `08` stays empty without a written reason.

| Category | First skill to add | Source | Status |
| --- | --- | --- | --- |
| `02-engineering` | `superpowers-brainstorming` | `obra/superpowers` | `referenced` |
| `02-engineering` | `superpowers-tdd` | `obra/superpowers` | `referenced` |
| `03-visual` | `anthropics-frontend-design` | `anthropics/skills` | `referenced` |
| `03-visual` | `vercel-web-design-guidelines` | `vercel-labs/agent-skills` | `referenced` |
| `04-foundations` | `scientific-skills-index` | `K-Dense-AI` source, after verification | `referenced` |
| `07-narrative` | `story-worldbuilding` | `danjdewhurst/story-skills` | `referenced` |
| `08-specific` | `find-skills` | local workflow around `npx skills find` | `draft` |

Rules:

1. Add one skill at a time.
2. Use the canonical format from N1.
3. Update the category README and root README count in the same change set.
4. Pin the upstream commit in `research/SOURCES.md` before promotion.
5. Do not copy upstream files into the repo.

Acceptance criteria:

- All 8 categories have at least one `SKILL.md`.
- Every new skill has `description`.
- Validator passes.

### 27.5 Phase N4 — Governance files

Goal: make contribution and review explicit.

Create:

```text
CONTRIBUTING.md
DECISIONS.md
research/LICENSES.md
research/README.md
.github/ISSUE_TEMPLATE/source-candidate.md
.github/ISSUE_TEMPLATE/skill-proposal.md
.github/PULL_REQUEST_TEMPLATE.md
.github/workflows/check-skills.yml
```

Content requirements:

| File | Must contain |
| --- | --- |
| `CONTRIBUTING.md` | Source verification, skill creation, validator command, commit rule |
| `DECISIONS.md` | D-01 license conflict, D-02 package layout, D-05 no bulk install, D-07 scripts as code |
| `research/LICENSES.md` | MIT, Apache 2.0, CC0, per-skill MIT, CC-BY-SA-4.0, SPDX unknown |
| `research/README.md` | Meaning of `SOURCES.md`, `QUERIES.md`, `SAMPLES.md`, `EXPERT_FIELDS.md`, `log/` |
| Source-candidate issue | Repo URL, category, license, scripts, evals, verification notes |
| Skill-proposal issue | Trigger, inputs, outputs, fails_when, verify, source |
| PR template | Changed file, validator output, source license, human review status |
| CI workflow | `python scripts/check_skills.py` on PR and push to `main` |

Acceptance criteria:

- All listed files exist.
- CI job runs with Python 3.13 and no extra dependencies.
- `CONTRIBUTING.md` links to `PLAN.md` and `templates/SKILL.md`.

### 27.6 Phase N5 — Source pinning and license hygiene

Goal: every promoted pointer has a traceable upstream state.

Actions:

1. Add `Commit` column to `research/SOURCES.md`.
2. Pin commit SHA for:
   - `anthropics/skills`
   - `obra/superpowers`
   - `vercel-labs/agent-skills`
   - `danjdewhurst/story-skills`
   - `casemark/skills`
   - `alirezarezvani/claude-skills`
   - `zbbsdsb/Fundemetal`
3. Read `LICENSE` for `jakubkrehel/skills` and set SPDX.
4. Decide whether `trailofbits/skills` CC-BY-SA-4.0 is usable in this MIT repo.
5. Resolve the CHORD website GPL-3.0 vs repo MIT conflict.
6. Add one `License` line to each pointer skill body.

Acceptance criteria:

- No promoted source has `Confidence: unverified`.
- No promoted source has empty `Commit`.
- Legal decisions are recorded in `DECISIONS.md`.

### 27.7 Phase N6 — Package layout and release artifacts

Goal: make the repo consumable by `npx skills add` without breaking category folders.

Actions:

1. Add `scripts/build_release_index.py`.
2. Read all `skills/*/*/SKILL.md`.
3. Write `releases/skills/<name>/SKILL.md`.
4. Write `releases/index.json`.
5. Skip `status: blocked`.
6. Preserve `name`, `description`, and other frontmatter.
7. Add `releases/` to `.gitignore`.
8. Document the command in `README.md`.

Acceptance criteria:

- Generated artifacts pass a basic frontmatter check.
- Duplicate names fail the build.
- Script never writes into `skills/`.
- Source tree stays unchanged.

### 27.8 Phase N7 — Expert-field quality pass

Goal: 180 domain pointers become useful, not just present.

Actions:

1. Split review by field: law, medicine, finance, capital.
2. Replace generic trigger text with the first sentence of each upstream description.
3. Add 2–5 steps from the upstream skill where available.
4. Keep the human-expert-review rule in every domain pointer.
5. Mark each skill with one of:
   - `candidate` in `research/EXPERT_FIELDS.md`
   - `referenced` once its body is rewritten
   - `ready` after one real run with evidence
6. Build a random sample audit of 20 skills: 5 per field.
7. Remove or mark `blocked` any skill whose upstream folder cannot be opened.

Acceptance criteria:

- 180 domain pointers have zero generic triggers.
- 20 sampled skills have non-empty, field-specific steps.
- No domain skill claims professional authority.

### 27.9 Phase N8 — Security pass

Goal: no unreviewed executable content.

Actions:

1. List all promoted sources with `scripts/`.
2. Read scripts in `anthropics/skills`, `obra/superpowers`, `vercel-labs/agent-skills`, `danjdewhurst/story-skills`, and `alirezarezvani/claude-skills`.
3. Record audit result in `research/SOURCES.md`.
4. Do not run `npx skills use` on unreviewed sources.
5. Disable telemetry during CLI discovery:

```bash
DISABLE_TELEMETRY=1 npx skills find <keyword>
```

Acceptance criteria:

- Every promoted source with scripts has a review note.
- No external scripts are copied into this repo.
- No CI step installs third-party skills.

### 27.10 Phase N9 — Documentation polish

Goal: README files describe the repo accurately.

Actions:

1. Root README links to `PLAN.md`, `CONTRIBUTING.md`, `research/EXPERT_FIELDS.md`.
2. Replace the skill total sentence after each import.
3. Add a status legend with plain meanings.
4. Add a one-line description of generated release artifacts.
5. Keep the open license conflict visible until resolved.
6. Ensure all README files stay English.

Acceptance criteria:

- No README count disagrees with the filesystem.
- No broken relative links.
- No Chinese characters in README files.

### 27.11 Phase N10 — Metrics and review

Goal: track useful signals only.

Metrics:

| Metric | Source |
| --- | --- |
| Skills by category | filesystem count |
| Referenced / draft / ready / reused / blocked | frontmatter status |
| Generic triggers | validator audit |
| Missing body sections | validator audit |
| Pinned sources | `research/SOURCES.md` |
| Human-reviewed domain skills | `research/EXPERT_FIELDS.md` |
| Open legal decisions | `DECISIONS.md` |

Ignore stars, downloads, and bulk-install counts.

Review cadence:

| Action | When |
| --- | --- |
| Validator | every commit |
| README count check | every skill change |
| License recheck | quarterly |
| Expert-field sample audit | after every 20 new domain skills |
| Review blocked skills | when dependency changes |

### 27.12 Immediate task order

Execute in this order:

| # | Task | Output |
| --- | --- | --- |
| 1 | Fix `grill-me` source field | one modified file |
| 2 | Rewrite fundemetal body sections | one modified file |
| 3 | Rewrite 180 domain pointers to remove generic triggers and add steps | 180 modified files |
| 4 | Upgrade validator with body-section checks | one modified file |
| 5 | Add CONTRIBUTING and DECISIONS | two new files |
| 6 | Add research governance files | four new files |
| 7 | Add GitHub templates and CI | four new files |
| 8 | Pin source commits | one modified file |
| 9 | Add missing category skills | one new skill per commit |
| 10 | Add release index script | one new file |

Commit rule stays unchanged: one file per English commit. No push from this environment.
