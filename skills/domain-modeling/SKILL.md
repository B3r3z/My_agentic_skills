---
name: domain-modeling
description: "Clarify domain concepts or write a domain glossary or architecture decision record. Do not invoke merely to read existing domain documentation."
---

# Domain Modeling

Resolve ambiguous terms and relationships using concrete scenarios and relevant code evidence. Distinguish current behavior from proposed future behavior; surface contradictions without assuming either the code or the proposal is automatically correct.

Read configured documentation paths from `AGENTS.md`, and only the glossary/decisions relevant to the topic. Preserve established terminology unless a change is agreed. Discussion alone produces proposed definitions; edit documents when authorized, including agreed documentation under `grill-with-docs`.

- For glossary edits, use [CONTEXT-FORMAT.md](CONTEXT-FORMAT.md). Default: root `CONTEXT.md`. Keep it a domain glossary, not a spec, implementation log, or instruction file.
- For a decision that is costly to reverse, surprising without context, and based on a real trade-off, use [ADR-FORMAT.md](ADR-FORMAT.md). Default: `docs/adr/`. Routine implementation choices do not need ADRs.
- Follow an existing context map for multiple domains; do not equate build modules with domain boundaries.

Create documents only when there is resolved content to record. Keep agent instructions and configuration in `AGENTS.md`, which points to the glossary and ADRs. Preserve unrelated definitions and decisions. Finish with agreed terms/decisions, any updated paths, and the unresolved questions that affect the next step.
