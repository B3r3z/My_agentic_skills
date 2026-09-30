---
name: wayfinder
description: "Plan a multi-session effort as a local Markdown map of decision tickets. Use when the route to a spec or approved plan is too uncertain for one conversation, not for implementation task breakdown."
---

# Wayfinder

Find the route through a large, uncertain effort. A **decision ticket** holds a question whose resolution is a decision or fact needed for planning, not a slice of the build. Wayfinder plans by default; do not turn its frontier into implementation work. When the route is clear, hand off to `$to-spec` if a durable spec is needed, then `$to-tickets` for executable tasks. Do not invoke either handoff skill or start implementation unless requested.

All map and ticket state stays in local Markdown. Do not fetch, create, update, assign, close, or label issues in an external tracker. Read `AGENTS.md` for the configured local task directory. For the default `.scratch/<effort>/issues/`, keep `map.md`, `decisions/`, and `research/` as siblings under `.scratch/<effort>/`. If the project has an existing local map, continue it. For a custom task path, use an analogous feature root beside its implementation-ticket directory and report the paths chosen. Reserve `issues/` for the implementation tickets produced by `$to-tickets`; decision tickets live in `decisions/` and are never marked `ready-for-agent` merely because they are well phrased.

## Map and decisions

The map is a low-resolution index, not a second copy of the answers. Keep these sections in `map.md`:

- **Destination:** what clearing this map enables (for example, an approved spec).
- **Notes:** domain context and standing constraints for this effort.
- **Decisions so far:** a one-line gist and relative link to each resolved decision ticket.
- **Not yet specified:** in-scope fog that cannot yet be phrased as a precise question.
- **Out of scope:** deliberate exclusions, with a reason and link if an existing ticket was ruled out.

Store each decision in `decisions/<NN>-<slug>.md`, preserving existing numbers and files:

```markdown
# <NN>: <Decision title>

**Type:** research | prototype | grilling | task
**Blocked by:** <local decision IDs or relative links, or None>
**Status:** open | claimed | resolved | out-of-scope
**Claimed by:** <session or agent identifier, only while claimed>

## Question

<the decision or investigation to resolve>

## Resolution

<the answer and links to evidence or artifacts, once resolved>
```

Use stable local IDs or relative links for blockers; they must resolve and must not form cycles. A decision is on the **frontier** when it is open, unclaimed, and all its blockers are resolved. Keep open tickets out of the map's Decisions-so-far list; inspect the `decisions/` files for the live frontier. Refer to tickets by linked title in user-facing prose, not by bare number. A precise but blocked question is a ticket; a question not yet precise belongs in Not yet specified. Do not duplicate the resolution in the map.

`research` tickets establish facts from sources; `prototype` tickets make a small artifact to react to; `grilling` tickets settle a choice with the human; `task` tickets cover a bounded prerequisite needed to make a decision. That last type is not an implementation task. Use the installed `$grilling` or `$domain-modeling` skills when their workflows genuinely help, after reading their instructions; do not assume a generic Skill tool or an unavailable dependency. For research, use `$research` if available, and link its local note from the decision ticket. Do not create throwaway branches or separate tasks by default.

## Chart a map

With a loose idea, clarify the destination and breadth of the unknowns with the user. If the route is already clear enough to settle in one conversation, say a map is unnecessary and stop. Otherwise create the map, write the questions that are precise now as decision tickets, then add their blocking links. Leave genuinely unformulated questions in Not yet specified. Report the first frontier and stop; charting does not silently resolve decisions or launch implementation.

## Resolve a decision

Open the supplied local map or ticket. If no ticket is named, choose the first frontier ticket in map order. Before working, mark it `claimed` with an identifier and re-read it; if another session has claimed or changed it, coordinate rather than overwriting. Resolve at most one human-in-the-loop decision per session. Research tickets may be investigated in parallel only where delegation is available and within the user's authorization.

Write the answer and evidence links into that ticket's Resolution, change its status to `resolved`, and add a one-line linked gist to Decisions so far. If the answer exposes new precise questions, add tickets and blocking links; move clarified fog out of Not yet specified. If an existing ticket lies beyond the destination, mark it `out-of-scope` and explain why in the map. Preserve other sessions' edits and do not erase unresolved work.

When no decisions or fog remain, report the cleared map and the appropriate handoff; do not create a duplicate implementation backlog in `decisions/`.
