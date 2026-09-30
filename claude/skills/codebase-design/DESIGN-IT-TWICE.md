# Compare interface designs

Use alternatives to resolve an actual design trade-off. Establish the caller needs, constraints, and dependencies from available evidence. Compare meaningfully different options, not cosmetic variants; the useful number depends on the decision.

For each option, show the caller-facing contract, a small usage example, hidden complexity, dependency strategy, and main trade-offs. Consider simplicity for the common caller, future changes already supported by requirements, and where verification belongs. Do not optimize for hypothetical flexibility.

Independent subagents may explore options when useful and available. Give each the same requirements and relevant code, with a distinct design emphasis. Otherwise compare locally and disclose shared context. Never wait for extra agent capacity merely to satisfy an option count.

Recommend a design based on caller complexity, change locality, and testability. Explain migration implications and the evidence that would change the recommendation. Design exploration alone does not authorize implementation.
