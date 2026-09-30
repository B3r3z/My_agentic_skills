---
name: codebase-design
description: "Design or simplify module interfaces, choose test seams, or compare alternative designs. Use for structural design work, not routine edits."
---

# Codebase Design

Aim for substantial behavior behind an interface that callers can understand and use correctly. Judge the design by caller complexity, change locality, and verifiability, not line counts or a mandatory abstraction pattern.

An **interface** includes contracts, ordering, errors, configuration, and performance assumptions as well as signatures. A **seam** is a place to vary behavior without changing callers; an **adapter** supplies that behavior. Use the project's established terminology when it differs.

Inspect representative callers and tests before proposing a structure. Show which complexity becomes private, what callers still need to know, and how observable behavior will be tested. Introduce indirection for a concrete variation or isolation need; avoid speculative interfaces. Side effects can be legitimate behavior: isolate or control them where verification requires it.

Load only the applicable guide:

- [DEEPENING.md](DEEPENING.md) when consolidating scattered behavior or moving dependency seams.
- [DESIGN-IT-TWICE.md](DESIGN-IT-TWICE.md) when competing interface designs need comparison.

A design-only request ends with a recommendation, trade-offs, and migration/verification implications. Implement when requested. Preserve behavior and existing regression coverage; retire tests only after their distinct scenarios and invariants have verified replacements.
