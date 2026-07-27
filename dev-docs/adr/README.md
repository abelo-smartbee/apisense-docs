# Architecture Decision Records

One file per decision, named `NNNN-title.md` (`0001-i18n-suffix-structure.md`).
Numbers are sequential and never reused. A record is written once the decision is
settled — open questions being worked out belong in a GitHub issue labelled
`decision`, not here.

These live in `dev-docs/`, not `docs/`, because `docs/` is the published site
root (https://docs.apisense.ai/) — ADRs are internal.

Each record has four sections:

```markdown
# NNNN. Title

## Status

Proposed | Accepted | Superseded by [NNNN](NNNN-other.md)

## Context

What forced the decision. Constraints, alternatives on the table.

## Decision

What was chosen, stated in the active voice.

## Consequences

What becomes easier, what becomes harder, what has to change as a result.
```
