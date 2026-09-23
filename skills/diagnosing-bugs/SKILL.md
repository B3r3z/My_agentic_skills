---
name: diagnosing-bugs
description: "Investigate an unexplained failure, intermittent bug, or performance regression. Use when diagnosis is needed; adapt to available logs, code, and reproduction access."
---

# Diagnosing Bugs

Establish what fails, why, and what evidence distinguishes the cause from alternatives. Diagnose without application changes when diagnosis alone is requested; complete and verify a fix when fixing is authorized.

Start from the reported symptom and relevant caller path. Use the smallest useful reproduction or measurement: an existing test, fixture, request replay, or focused harness. Confirm it detects the reported failure rather than an unrelated setup error. Read domain documents only when terminology or a recorded decision affects the investigation.

Let evidence determine the next experiment. State falsifiable predictions for plausible causes; no fixed hypothesis count or mandatory sequence is needed. Reduce the reproduction where this helps distinguish causes. Change one relevant variable at a time and prefer targeted instrumentation over broad logging.

For intermittent or performance failures, consult [experiments.md](references/experiments.md). If reproduction is unavailable, continue with code, logs, dumps, and contracts. Separate established facts from hypotheses, and request only the missing evidence that would resolve material uncertainty. Do not claim runtime verification from static analysis.

For a fix, capture the failure in a regression test when a suitable observable boundary exists, apply the change, and check the original scenario. Explain missing coverage if the real failure cannot be exercised. Run relevant checks and required project checks; repeat or broaden them when changes or evidence justify it.

Remove only temporary instrumentation and artifacts introduced for this investigation. Keep secrets out of commands, displayed output, and shared artifacts. Finish with the cause and supporting evidence, changes if any, validation results, and unresolved limits. Stop an unproductive experiment to reassess; do not run endless retries.
