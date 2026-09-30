---
name: tdd
description: "Implement requested behavior using test-first red-green-refactor cycles. Use when the user requests TDD; adding tests for existing behavior alone does not require this skill."
---

# Test-Driven Development

Complete the requested behavior in small verified slices. Reuse agreed requirements and test boundaries; clarify only ambiguities that would change observable behavior.

For new behavior or a reproduced bug, write a focused test, observe it fail for the intended reason, implement enough to pass, then simplify the changed code where useful. Rerun affected tests after refactoring. Continue through the requested scope rather than stopping at the first green test.

Test observable contracts at an appropriate public boundary. Expected results must come from the specification or independently worked examples, not a copy of implementation logic. Prefer tests that survive internal restructuring. Existing working behavior may pass on its first characterization test; never break production code to manufacture a red step.

Use `codebase-design` only if interface design itself needs work. Domain documentation is relevant when it resolves behavior or terminology, not a prerequisite to every cycle.

Run checks relevant to the changes and required repository checks. Repeat or broaden verification after further changes, failures, or incomplete evidence; avoid redundant runs for unchanged code. Finish with implemented behavior, verification evidence, and any unmet criteria.
