---
name: fundemetal
category: 01-metacognition
status: referenced
inputs: a decision, plan, or claim to stress-test
outputs: constraints, trade-offs, falsifiable claims
fails_when: output is generic agreement, or no evidence gate
verify: run the upstream evals/ suite for the chosen protocol
source: https://github.com/zbbsdsb/Fundemetal
---

# Fundemetal

A pointer to 24 cognitive protocols. Use this as an index. Do not copy the whole upstream repository into this repo.

## When to use

- A decision is already made and needs stress-testing.
- A plan looks plausible but has no falsifiable claims.
- The answer is agreement without evidence.
- A vision needs to become an observable execution path.

## Start here

Use the Build chain first:

1. **Decomposer** — surface unknown unknowns.
2. **Tension Mining** — map latent conflicts and the invariant that holds across them.
3. **Great Expectations** — anti-consensus planning with BANI and integrity gates.
4. **Vision Retrospective** — turn a hollow vision into verifiable claims.

Add the Falsify group when the plan needs pressure:

- **Pre-Mortem** — assume failure, write at least five mechanisms.
- **Outside View** — check the base rate before arguing exception.
- **Resulting** — judge the decision, not the outcome.

## Formation map

| Formation | Protocols | Use |
| --- | --- | --- |
| Build | Decomposer, Tension Mining, Great Expectations, Vision Retrospective | Surface unknowns, find the force, write the plan |
| Falsify | Pre-Mortem, Outside View, Resulting | Stress-test the plan |
| Evidence | Source Ledger, Disconfirmation Hunt | Tag claims, hunt refutation |
| Adversarial | Crux Finder, Red Cell, Silent Start | Disagreement as an asset |
| Single | Question Autopsy, Quantity Quota, Trade-off Ledger, Second-Order, Steelman Forge, Stopping Rule | Targeted cognitive traps |
| AI-native | Sycophancy Breaker, Goal Anchor | LLM-specific failure modes |
| Meta | Taboo, Curator, Insight Crystallizer, Shoulders of Giants | Maintain the protocol library |

## Failure conditions

Do not present a protocol as complete when:

- the output contains no objection, trade-off, or falsifiable claim;
- the user asked for execution, not examination;
- the upstream `evals/` suite has not been run for the chosen protocol.

## Verify

1. Pick one protocol from upstream `skills/`.
2. Copy that single folder into the agent skills directory.
3. Run its `evals/` suite.
4. Pass only if happy path, false positive, and gate-gaming cases all pass.

## License

Repository: CC0 1.0. Individual skill folders: MIT (© CeaserZhao). Cite the source when adapting a protocol.
