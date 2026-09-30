---
name: setup-b4rt-skills
description: "Set up or migrate this skills collection\u2019s project configuration in CLAUDE.md. Use explicitly for setup, not before ordinary development tasks."
disable-model-invocation: true
---

# Setup B4rt Skills

Produce one concise `## Agent skills` block in root `CLAUDE.md`. Preserve unrelated instructions and existing choices. Agent configuration belongs here; domain definitions and decisions remain in linked glossary and ADR files.

Inspect existing `CLAUDE.md` settings and documentation paths. Read `AGENTS.md` or `docs/agents/` settings when migrating them; preserve those files and unrelated instructions. If `CLAUDE.md` imports `AGENTS.md`, account for the imported settings instead of adding a conflicting duplicate block. Resolve conflicting settings only when the task and repository do not settle them.

Record the settings actually needed:

- Local task directory: default `.scratch/<feature-slug>/issues/`. `to-tickets` stores Markdown tasks there.
- Relevant domain paths: default `CONTEXT.md` and `docs/adr/`, or the existing context map. Build modules do not automatically imply separate domains.

Add conditional documentation guidance: consult the relevant glossary for domain terminology and relevant ADRs for design constraints. Missing documents do not block ordinary work; surface conflicts with recorded decisions rather than silently replacing them. Adapt useful settings directly into `CLAUDE.md`; do not copy a CLI manual or instructions for uninstalled workflows.

Proceed under the user's setup authorization once material choices are settled. Update the existing block in place or create it once. Do not create empty glossaries or ADRs. Verify concrete paths/targets, absence of conflicting duplicate configuration, and that documentation is read only when relevant. Report the resulting settings and unresolved choices.
