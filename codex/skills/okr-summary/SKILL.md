---
name: okr-summary
description: Draft a leadership-facing quarterly or closing comment from a GitHub OKR, its descendants and comments. For a closure spanning several workstreams, delegate the evidence read before writing. Return copyable Markdown in chat.
---

# OKR Summary

Write one quarterly or closing comment for a leader outside the team. Use the requested language, otherwise the language of the reporting template or parent issue. Use GitHub read-only. Deliver the comment in the current chat.

## Read the evidence

Read the parent, criteria, milestone, reporting template and comments. Collect every descendant's body, state and complete discussion, including open work and cross-repository children. [scripts/read_issue_tree.py](scripts/read_issue_tree.py) takes the issue URL, uses paginated `gh` GET requests and emits JSON Lines. For a large tree, capture it once in a temporary file. A nonzero exit signals incomplete collection. An equivalent complete, read-only source works too.

The session asked for the final comment is the **writer**, including when invoked as a subagent. For a closure spanning several workstreams, once the snapshot is available, call the subagent tool to start **one independent evidence analyst**. In Codex use `spawn_agent` with `fork_turns="none"`, `model="gpt-6.2-sol"` and `reasoning_effort="high"` when available. Pass the objective, period, snapshot path and material linked decisions. Assign the analyst a read-only evidence task. Ask them to reconcile native children with explicit task lists, read additional child tasks and return:

- The final state of each principal commitment and its practical consequence. Distinguish this period's delivery from capabilities inherited from earlier or neighboring OKRs.
- A short result and its source links for each distinct outcome, plus the decisions and owners of remaining work.
- Private qualifications that prevent a factual mistake, such as the different scope of two dates or who owns an unfinished change. Keep these separate from publishable results.

The analyst reads all issue bodies and comments in batches and delivers one final brief with actual coverage, without drafting or delegating. The writer can verify decisive claims in the original issues while the analyst works. Wait for the analyst's completed response before drafting. Reuse a completed brief when the caller already supplied one. For a simple update, an explicit solo request or unavailable delegation, the writer does the full read directly. Follow extra references when they could change a reported outcome or scope boundary. If a needed source remains inaccessible after a read-only retry, identify the material gap to the user. An unavailable incidental link can be omitted when the necessary evidence is complete.

Use the earlier quarter as a baseline. Ground each material claim in an observed result, its population or environment and its source. A plan or a closed issue alone cannot establish deployment, resolution of every defect or adoption by another team.

## Write the comment

Follow the requested template. For the usual quarterly format use `## Summary – <quarter and year>` and the three level-three headings below. When the user supplies an accepted example, follow its emphasis and level of detail. Verify the facts for the current OKR independently.

**Technical solution – output.** In the first two sentences, account for **each principal commitment** in the parent objective. For a replacement and retirement, name what moved, where the replacement works and where the old service was switched off. In a second short paragraph, explain the dependency removed and the status of the risk that motivated the change. If historical retention was a commitment, name what information was kept here. Keep implementation details in the tickets and routine remaining cleanup in the scope section. Cite repeated facts once, in the evidence bullets below. Use the team's voice.

For **Key criteria**, write one sentence that connects the capability's verified operation in its intended setting with its practical value. Take that value from the parent's reason for doing the work, such as making future changes to this capability easier. A predecessor's completed work belongs in the quarter context only if needed. Leave the list of user actions in the user-experience bullet. Reserve grades for a requested or recorded assessment.

**Outcome evidence – metrics, data and documents.** Give each material result a short bold label, one or two sentences and representative sources. For a migration with evidence for these groups, use the following order. For other OKRs, derive the groups from the objective.

- **Creation or delivery process** — Trace the path from the user's initial choice through provisioning to the result they receive. If the team migrated an existing set of user-facing assets, say explicitly which assets moved and which users kept using them. Selection or availability describes a different fact.
- **User experience** — Give checks before starting, what users see as work progresses, and how they can recover or look up past work. This merits its own bullet when the user interface changed.
- **Production rollout** — Give the decisive date with its year, population reached and transition safeguard. A leadership summary generally needs only the milestone that changed production coverage.
- **Testing and fixes** — Describe production verification, fixes collectively and the reported result for that phase. Leave examples of individual incidents and test dates in the source unless they change the conclusion. A phase end date does not establish when every fix shipped.
- **Historical data** — State which business or audit records moved, their count or time span and what the source could reliably preserve. An internal identifier conversion or repair count is a different population and usually adds nothing to this outcome.
- **Integrations** — Describe support for affected teams, responsibility transferred and any adoption still pending. Aggregate individual clients unless a named exception changes the conclusion.
- **Legacy shutdown** — Give the environments, monitoring or controls retired and the risk actually resolved. Use a deadline only when the source records it as such.
- **Supporting documents** — Link the named research, proposal or decision directly, preserving its status.

Put clickable links at the end of the point they support. Use `[#123](issue-url)` for tickets and descriptive labels for documents. Highlight the few figures that establish reach, timing or impact. Preserve material limitations. Omit speculative gains, lists of missing measurements and incidental engineering metrics from a normal closing comment.

**Task scope description.** Give the earlier quarter's baseline, then name each material delivery in the closing period, including any transfer of historical records and retirement of the old service. When the sources establish which work will continue outside the OKR, say so explicitly before the follow-up bullets. Give residual cleanup, selected improvements and any separate deliverable their own short bullets and owning links. Use the tracker's exact name for the remaining item and explain an unfamiliar acronym alongside it. When an assessment selected follow-ups, one sentence can report the decision and link the assessment and selected tasks. Describe individual changes only when a sponsor needs to act on one.

## Check and deliver

For English, read [Simple English](../simple-english/SKILL.md) and edit in Plain mode unless the user requests Strict. Preserve the actors, scope of dates and counts, qualifications, headings and links.

Read the opening alone as a sponsor. Keep a technology name there only if it identifies a commitment or the risk resolved. Check that every evidence bullet proves a distinct result and that dates qualify the right event. During the plain-language edit, verify each named actor and action against the source. A system that displays an error can report a failure originating elsewhere. Keep a limitation where it changes the meaning of a reported fact. Keep the analyst's cautions about unrelated measurements private unless the user asks for a criteria audit. A complex closing note will often fit in 300–400 words of prose, excluding links.

For a complex closure, make one last pass over the **finished text** with the analyst's findings beside it. For each relevant group, point to the words that describe the user's initial choice, what existing assets moved, which resources or configuration the process creates, and what the user receives. Check how the rollout started, whom it reached and what safeguard was available. Check what help affected teams received, what ownership moved and what remains with others. If a material, source-backed detail dropped out during editing, restore it in the shortest clause that preserves its meaning. Keep the rest of the draft intact. This is the writer's own check using evidence already collected.

For a complete read, return only one fenced `markdown` block containing the literal, unescaped comment.
