---
name: to-spec
description: "Synthesize an agreed conversation into a local feature spec for a Markdown-ticket workflow. Use when a durable spec is needed before task breakdown; do not interview or implement."
disable-model-invocation: true
---

# To Spec

Turn the decisions already made in the conversation into one durable local spec. This is synthesis, not another design interview or an implementation pass. Use only the conversation and local project files for task context; do not read, create, label, or publish issues in an external tracker. If the sole input is an external task reference, ask for its text or a local export.

Read relevant code, the project's glossary, and applicable ADRs to ground the spec. Preserve the distinction between confirmed decisions, proposals, and open questions. Identify the highest useful behavioral test seam, preferring an existing seam. If a consequential seam or behavior is unresolved, record it under **Open Decisions** and ask for a targeted decision before calling the spec ready; do not silently choose on the user's behalf.

Save the spec at the plan/spec path configured in `CLAUDE.md`, defaulting to `docs/plan/YYYY-MM-DD-<slug>.md`. If an approved plan or spec for this effort already exists, enrich that document rather than creating a competing source of truth. Preserve its confirmed scope and link to any existing local tasks instead of copying their backlog into the spec. Do not create implementation tickets here; `/to-tickets` handles that when requested.

Use these sections, omitting only ones that are genuinely inapplicable:

## Problem Statement

Describe the problem from the user's perspective.

## Solution

Describe the intended behavior and scope from the user's perspective.

## User Stories

Number the distinct actor goals that clarify the feature. Cover meaningful behavior and edge cases without padding the list to an arbitrary length.

## Implementation Decisions

Record agreed module boundaries, contracts, data changes, and other consequential constraints. Prefer durable decisions over speculative file lists or working code. A short prototype extract is appropriate only when it expresses a decision more precisely than prose.

## Testing Decisions

Name the chosen behavioral seam, relevant prior-art tests, and what observable outcomes will establish success. Avoid testing private implementation details as the contract.

## Out of Scope

State deliberate exclusions.

## Open Decisions

List unresolved choices and the consequence of each. If none remain, say so briefly.

## Further Notes

Link relevant local plans, research, decision records, or tickets without duplicating their content.

Finish with the saved path, any open decisions, and whether the spec is ready for `/to-tickets`. Specification readiness does not itself authorize ticket creation or implementation.
