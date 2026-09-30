---
name: code-review
description: "Review changes, selected files, or a repository against standards and requirements. Use for review requests, not implementation."
---

# Code Review

Review is read-only unless fixes are requested. Report two separate assessments: **Standards** and **Spec**. Cover correctness and regressions as well as documented conventions; distinguish actionable defects from design preferences.

Establish the user-selected scope using [scope.md](references/scope.md), including relevant untracked files for WIP. All reviewers must assess the same state. Read applicable repository instructions and standards, then follow affected callers and contracts where needed to establish a finding.

Use the user's requirements first, then relevant local specs or issue descriptions supplied in the task or present in the repository. Base the review on supplied and repository-local evidence; do not retrieve tickets from an external tracker. If no spec is available, complete Standards and explicitly mark Spec unassessed.

Independent parallel reviewers may assess the two axes when useful and available. Otherwise assess them sequentially and disclose shared context. An enclosing orchestrator may require one independent reviewer to cover both axes; do not create another reviewer layer in that case.

For each finding, give the concrete failure or violated rule, evidence, affected location, and severity. Trace enough context to validate it; do not present hypothetical code smells as defects. Repository conventions override general design preferences. Avoid duplicating issues already established by tooling.

Finish with separate Standards and Spec verdicts, actionable findings ordered by severity within each axis, and verification limits. A missing spec or unrun check is not a pass. No findings is a valid result; do not manufacture suggestions.
