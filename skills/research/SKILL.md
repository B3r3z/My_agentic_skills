---
name: research
description: "Investigate a factual question against primary sources and save cited findings in a local Markdown note. Use for standalone research or to inform a local decision ticket; do not make the user's decision for them."
---

# Research

Take a concrete question, optionally linked to a local Wayfinder decision ticket. Investigate against the primary sources that own the facts: official documentation, specifications, source code, or first-party APIs. Trace consequential claims to citations, note the date for time-sensitive facts, and distinguish evidence from inference and remaining uncertainty.

Write one focused Markdown note in the repository's existing research location. If the question comes from a Wayfinder map and no convention exists, use its feature root's `research/<decision-id>-<slug>.md`; otherwise default to `docs/research/YYYY-MM-DD-<slug>.md`. Preserve an existing note for the same question and update it rather than creating duplicates. Include the question, findings with direct citations, limitations or open questions, and the implication for the decision being investigated.

When a local decision ticket is in scope, link the note from that ticket's Resolution. Mark a research ticket resolved only when its factual question is answered; leave it open with the gap recorded otherwise. Research does not decide downstream design choices, turn findings into implementation tickets, or use an external issue tracker as task storage. Source URLs are evidence links, not ticket-state operations.

Delegation is optional: use a background agent only when available and authorized within this task; otherwise research directly. Do not create a new thread, branch, pull request, or external ticket merely to run the research. Finish with the note path, the answer, and any remaining uncertainty.
