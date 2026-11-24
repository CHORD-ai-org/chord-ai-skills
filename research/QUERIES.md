# Queries

Discovery surfaces: `skills.sh`, `agentskills.io`, GitHub `topic:agent-skills`, the two index repos in [SOURCES.md](SOURCES.md).

Verification per candidate: open README, license file or frontmatter, one `SKILL.md`, `scripts/`, `evals/`, last commit.

| Category | Query |
| --- | --- |
| 01 | `site:github.com agent skills cognitive protocol decision making` |
| 02 | `site:github.com agent skills code review TDD refactoring` |
| 03 | `site:github.com agent skills frontend design typography accessibility` |
| 04 | `site:github.com agent skills scientific method statistics research` |
| 05 | `site:github.com agent skills quantitative trading medical legal insurance` |
| 06 | `site:github.com agent skills human agent interaction` |
| 07 | `site:github.com agent skills worldbuilding narrative storytelling` |
| 08 | `npx skills find <specific need>` |

CLI discovery:

```bash
npx skills find <keyword>
npx skills add <repo> --list
npx skills use <repo>@<skill>
```
