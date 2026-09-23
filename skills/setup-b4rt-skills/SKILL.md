---
name: setup-b4rt-skills
description: "Set up or migrate this skills collection\u2019s project configuration in AGENTS.md. Use explicitly for setup, not before ordinary development tasks."
---

# Setup B4rt Skills

Produce one concise `## Agent skills` block in root `AGENTS.md`. Preserve unrelated instructions and existing choices. Agent configuration belongs here; domain definitions and decisions remain in linked glossary and ADR files.

Inspect existing `AGENTS.md` settings and documentation paths. Read legacy `CLAUDE.md` or `docs/agents/` settings only when migrating them; do not delete those files or leave the new block dependent on them. Resolve conflicting settings only when the task and repository do not settle them.

Record the settings actually needed:

- Local task directory: default `.scratch/<feature-slug>/issues/`. `to-tickets` stores Markdown tasks there.
- Relevant domain paths: default `CONTEXT.md` and `docs/adr/`, or the existing context map. Build modules do not automatically imply separate domains.

Add conditional documentation guidance: consult the relevant glossary for domain terminology and relevant ADRs for design constraints. Missing documents do not block ordinary work; surface conflicts with recorded decisions rather than silently replacing them. Adapt useful settings directly into `AGENTS.md`; do not copy a CLI manual or instructions for uninstalled workflows.

Proceed under the user's setup authorization once material choices are settled. Update the existing block in place or create it once. Do not create empty glossaries or ADRs. Verify concrete paths/targets, absence of conflicting duplicate configuration, and that documentation is read only when relevant. Report the resulting settings and unresolved choices.
