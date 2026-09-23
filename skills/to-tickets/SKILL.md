---
name: to-tickets
description: Split an approved plan, spec, or conversation into local Markdown tasks with acceptance criteria and dependencies. All ticket operations stay local; no external tracker interaction.
---

# To Tickets

Break a plan, spec, or conversation into a set of **tickets**: tracer-bullet vertical slices, each declaring the tickets that **block** it.

Use only the conversation and local project files. Read the local task-directory setting from `AGENTS.md`, defaulting to `.scratch/<feature-slug>/issues/`. No tracker setup, labels, credentials, or external services are needed.

This skill creates and updates local Markdown files only. Do not fetch, create, update, comment on, or close issues in external systems, and do not sync or publish generated tasks. External tracker settings in `AGENTS.md` do not change this local-only workflow. Plan and record tasks; do not implement them.

## Process

### 1. Gather context

Use the requirements already present in the conversation or a local spec/task file. Read relevant local context. If the input is only an external issue number or URL, ask for the needed text in the conversation or a local export; do not retrieve it over the network. A supplied URL may be retained as a plain source reference without opening it.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Ticket titles and descriptions should use the project's domain glossary vocabulary, and respect ADRs in the area you're touching.

Identify any prerequisite refactoring to include as planned tickets. Do not perform that refactoring during ticket creation.

### 3. Draft vertical slices

Break the work into **tracer bullet** tickets.

<vertical-slice-rules>

- Each slice cuts a narrow but COMPLETE path through every layer (schema, API, UI, tests): vertical, NOT a horizontal slice of one layer
- A completed slice is demoable or verifiable on its own
- Each slice is sized to fit in a single fresh context window
- Any prerequisite refactoring should be scheduled before the dependent implementation tickets

</vertical-slice-rules>

Give each ticket its **blocking edges**: the other tickets that must complete before it can start. A ticket with no blockers can start immediately.

**Wide refactors are the exception to vertical slicing.** A **wide refactor** is one mechanical change (rename a column, retype a shared symbol) whose **blast radius** fans across the whole codebase, so a single edit breaks thousands of call sites at once and no vertical slice can land green. Don't force it into a tracer bullet; sequence it as **expand–contract**. First expand: add the new form beside the old so nothing breaks. Then migrate the call sites over in batches sized by blast radius (per package, per directory), each batch its own ticket blocked by the expand, keeping CI green batch to batch because the old form still exists. Finally contract: delete the old form once no caller remains, in a ticket blocked by every migrate batch. When even the batches can't stay green alone, keep the sequence but let them share an integration branch that all block a final integrate-and-verify ticket; green is promised only there.

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each ticket, show:

- **Title**: short descriptive name
- **Blocked by**: which other tickets (if any) must complete first
- **What it delivers**: the end-to-end behaviour this ticket makes work

Ask the user:

- Does the granularity feel right? (too coarse / too fine)
- Are the blocking edges correct: does each ticket only depend on tickets that genuinely gate it?
- Should any tickets be merged or split further?

Iterate until the user approves the breakdown.

### 5. Save the approved tasks locally

Use the configured local task directory (default `.scratch/<feature-slug>/issues/`). Write one file per task as `<NN>-<slug>.md`, numbered in dependency order, starting at `01` only for a new set. Preserve existing files: update matching tasks when revising a plan and allocate unused numbers for additions. Keep stable IDs and use local IDs or relative Markdown links for dependencies.

Store task descriptions, acceptance criteria, dependencies, status, and any requested follow-up notes in those local files. Use the template below. `ready-for-agent` means specified; execution still requires every blocker to be complete. Do not translate local statuses into external labels or tracker updates.

Finish by reporting the file paths and the **frontier**: tasks whose blockers are all complete. Stop after recording and reporting the plan. Do not claim tasks, modify application code, or start implementation unless separately requested.

<local-ticket-template>

# <NN>: <Ticket title>

**What to build:** the end-to-end behaviour this ticket makes work, from the user's perspective, not a layer-by-layer implementation list.

**Blocked by:** the numbers/titles of the tickets that gate this one, or "None (can start immediately)".

**Status:** ready-for-agent

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2

</local-ticket-template>

In task descriptions, avoid specific file paths or code snippets: they go stale fast. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.
