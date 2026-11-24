---
name: okr-summary
description: Draft a leadership-facing quarterly or closing comment for a GitHub OKR from the deliverable, its child issues and their comments. Return copyable Markdown in chat.
---

# OKR Summary

Write one comment that a leader outside the team can read to understand what changed, how the team knows it worked and what is still in scope. Use the requested output language, otherwise the language of the deliverable's reporting template. Use GitHub read-only throughout. The destination is the current chat.

## Read the evidence

1. Read the parent issue, acceptance criteria, milestone, reporting template and comments. Establish the reporting quarter from the request or milestone. An earlier quarterly update gives the starting point for the current period.
2. Read the body, state and complete comment thread of every child issue, recursively, including open children and children in other repositories. [scripts/read_issue_tree.py](scripts/read_issue_tree.py) takes a full GitHub issue URL and uses authenticated `gh` GET requests. It emits one JSON line per issue with its body, milestone, child URLs and dated comments. For large trees, redirect stdout to a temporary file and read it in batches small enough to see every body and comment. A nonzero exit indicates incomplete collection. An equivalent read-only source is fine if needed.
3. Reconcile the native hierarchy with explicit child-task lists in descriptions or comments. Read any additional child tasks and their discussions. Follow links to separately tracked work or decisions when they establish a result or scope boundary. Keep related deliverables distinct. If part of the tree remains inaccessible after a read-only retry, identify the gap to the user before presenting a partial draft.
4. Use completion comments, rollout records, verified counts and explicit decisions to establish what happened. A ticket description may describe a plan. A closed status alone cannot establish a production rollout, a measured improvement or completion of someone else's work. Check the scope of each date, number and result against its source.

## Decide what leadership needs to know

Build the evidence bullets first. Group the work by the results that answer the parent objective. Keep a result when leaving it out would change a reader's understanding of what was delivered, who benefited, how it was verified or what remains. Routine repairs, incidental features and internal record conversions can stay in the child tickets, even when they have precise figures.

For a migration or retirement, use the following as possible labels in the **outcome evidence** section. Include a bullet wherever the source work supports a distinct result. For other OKRs, derive the groups from their own success criteria.

- **Delivered process** — Name a few representative steps and the existing use cases or templates the replacement supports.
- **User experience** — Describe the workflow in the user's usual interface, including checks before they start and how they can follow, recover or look up an operation.
- **Production rollout and testing** — Give the rollout's reach, date and safeguards. Report what testing found and how that phase ended.
- **Historical data** — Give the population, time span, quantity and any limits on what can be recovered.
- **Integrations** — Report the handoff at team level. Look for ownership transfers, support provided to affected consumers and the overall state of their adoption. Identify an individual client or pull request only when leadership needs a decision about it.
- **Legacy shutdown** — Report separately on the operating dependency retired, where it was switched off, which controls could be removed and what risk was resolved.

Use a measurement when it shows reach, timing or impact. In an ordinary closing comment, omit both an unmeasured improvement and commentary about the missing comparison. Discuss measurement gaps when the user requests a criteria audit or when the missing evidence prevents reporting the central result. Keep observed shortfalls and limitations that qualify a fact you do report.

## Write the comment

Return a single fenced `markdown` block with the literal, unescaped comment inside. Follow the supplied template's sections, using clean headings without its prompts or placeholders. Otherwise use the headings below. Put complete clickable Markdown links at the end of the point they support. Use `[#123](actual-issue-url)` for tickets and descriptive labels for documents.

- `## Summary – <quarter and year>`
- `### Technical solution – output` — Introduce the service people now use and the operational problem the change resolves, in one or two short paragraphs. Name a technology when it explains a benefit or a retired risk. Leave implementation details in the linked tickets. In **Key criteria**, state in one sentence what users or operators can rely on now. Reserve grades such as “partially met” for a requested assessment or a documented current verdict.
- `### Outcome evidence – metrics, data and documents` — Give each distinct result a short bold label, one or two plain-language sentences and representative sources. Highlight the few numbers or dates that establish the outcome. When the OKR names supporting documents, give their direct links together in a **Supporting documents** bullet, preserving labels such as research, proposal or decision.
- `### Task scope description` — Include when work crossed quarters, changed scope or continues elsewhere. State what the reporting period delivered. Give each distinct piece of remaining work its owning link. If an assessment selected follow-up tasks, cite that decision alongside the selected tickets so the reader can see why they were deferred. Keep final cleanup here. Call work outside scope when the user or a recorded decision places it there.
