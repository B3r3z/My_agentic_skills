---
name: simple-english
description: Write, rewrite, or review technical English for readers outside the field or readers who use English as a second language. Use for plain-English explanations, clearer instructions, or a requested ASD-STE100 Simplified Technical English review.
license: MIT
---

# Simple English

Write for the person who needs to understand the result or take the next step. Use **Plain** by default. Use **Strict** when the user asks you to apply Simplified Technical English (STE) or check ASD-STE100 compliance. A request to explain what STE means is an ordinary explanation.

## Write or rewrite

- Open an explanation with the answer. For a procedure, give the prerequisite before the first step that needs it. Put a condition before the action it governs. For example, “If the build fails, open the build log.”
- Give one instruction per sentence. Use a direct verb and aim for at most 20 words. For descriptions, aim for at most 25 words per sentence and six sentences per paragraph. Keep each paragraph on one topic. Let the reader see who does what. If the source does not identify the actor, leave that open.
- Use familiar words and simple tenses where the meaning survives. “Before” works for “prior to.” Remove empty claims such as “seamlessly.” Keep distinctions that affect the task. Checking a file exists and validating its signature are different actions.
- Use one name for each concept. Define an unfamiliar term in a few words when the reader first needs it. Keep official labels so the reader can find them. Use American spelling unless the user or project specifies another convention.
- Preserve conditions, order, negation, units, time, and degrees of certainty or obligation. “We recommend” can express advice. “Must” makes it a requirement. Keep a possible cause tentative even when a definite diagnosis would make a shorter sentence.
- Copy commands, flags, identifiers, paths, placeholders, and quoted output exactly. Preserve warnings, their severity, and confirmation text. When drafting a warning, place it before the risky step and state the consequence. Add a host, cause, prerequisite, or recovery action only when the source supports it.

For a runbook, incident report, error message, release note, or other short format, use the matching example in [Writing patterns](references/use-cases.md).

## Review or apply STE

For a review, quote the smallest passage that shows each issue, explain its effect on the reader, and give a replacement. For a Plain review, use the guidance above. If the user asks only for a review, leave the source in place.

For Strict writing or review, use the [Issue 9 rule index](references/rule-catalog.md) and [vocabulary guide](references/strict-vocabulary.md). Verify rule numbers and word approvals against the requested issue before citing them. When only part of the standard is available, deliver the edits you can support and identify what still needs checking.

## Deliver

For a rewrite, return the revised text in the requested format. For a chat explanation, lead with the answer and use prose by default. Number steps when order matters. Use a table when readers need to compare the same attributes. Write out contractions. Split long sentences at semicolons or em dashes. Skip decorative emphasis and stock openings or closings. Keep any surrounding reply in the user's language.

Before delivery, compare the result with the source. Could a reader now run a step in the wrong environment, treat advice as mandatory, or mistake a theory for a fact? Restore the detail that prevents the misreading.
