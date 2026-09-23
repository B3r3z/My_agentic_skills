---
name: setup-b4rt-skills
description: "Configure a project's AGENTS.md with its issue tracker, optional labels, and paths to domain documentation. Use when setting up or migrating this skills collection."
---

# Setup B4rt Skills

Keep agent instructions and configuration in the repository's root `AGENTS.md`. Keep the domain glossary in `CONTEXT.md` (or a context map and per-context glossaries), and decisions in ADR files. `AGENTS.md` points to those documents; it does not duplicate their contents.

## 1. Inspect the existing configuration

Read the existing `AGENTS.md`, relevant `CLAUDE.md` configuration if present, git remotes, domain documentation, and any legacy `docs/agents/` files. Preserve the user's choices and unrelated instructions. Inspect existing module/context boundaries; a multi-module repository is not automatically a multi-context domain. Do not infer the domain layout solely from JavaScript workspace files.

When migrating, bring the relevant tracker, label, and documentation settings into `AGENTS.md`. Resolve conflicting values with the user if the current task does not already settle them. Do not delete legacy files or overwrite unrelated `CLAUDE.md` content. The generated configuration must not depend on either location for its operation.

## 2. Resolve only missing choices

Reuse choices already made in this session or documented in the repo. Ask only when a material decision remains unresolved.

- **Issue tracker:** GitHub, GitLab, local Markdown, or the user's existing tracker. A remote suggests a provider but does not authorize choosing it over an existing setting. Record the target repository/project and how to read and publish tickets.
- **Local tasks:** record the local directory used by `to-tickets`, default `.scratch/<feature-slug>/issues/`. This skill always works locally, regardless of the tracker selected for other workflows; it needs no labels or remote access.
- **Labels:** optional. Record `Labels: none` when the user has no established label workflow. If labels are wanted, record the role-to-label mapping in `AGENTS.md`; do not require the `triage` skill. Verify configured remote labels exist before using them. If one is missing, ask whether to create it or omit it; publishing authorization alone does not require labels.
- **Domain documents:** preserve existing locations and context boundaries. Otherwise use root `CONTEXT.md` and `docs/adr/`. Use `CONTEXT-MAP.md` and per-context paths when actual domain boundaries justify them, regardless of language/build system. Record the paths and when to read the documents.

Use the relevant seed as a reference, adapting its applicable instructions directly into the `AGENTS.md` block rather than generating separate configuration documents:

- [issue-tracker-github.md](issue-tracker-github.md)
- [issue-tracker-gitlab.md](issue-tracker-gitlab.md)
- [issue-tracker-local.md](issue-tracker-local.md)
- [triage-labels.md](triage-labels.md) only if labels are enabled
- [domain.md](domain.md)

Include only the tracker operations and settings needed by the installed workflows. For a different tracker, use the user's workflow and available tools. Keep PR/MR triage off unless already configured or requested.

## 3. Update AGENTS.md

Create root `AGENTS.md` if absent, even when `CLAUDE.md` exists. Update its existing `## Agent skills` block in place, or add one. Preserve other sections. Show the proposed settings; proceed under the user's existing setup authorization once the choices are settled.

The resulting block contains concrete values, not unresolved placeholders:

```markdown
## Agent skills

### Issue tracker

Provider and target repository/project, or local task directory.
Instructions for reading and publishing specs/tickets in workflows that use the tracker.
Local tasks (to-tickets): .scratch/<feature-slug>/issues/ — local Markdown only.

### Labels

Labels: none
Or the configured role-to-label mapping and which roles this project uses.

### Domain docs

Glossary: CONTEXT.md
Decisions: docs/adr/
Read the relevant glossary and ADRs when working in that domain.
If a context map exists, list its path and follow its links to the relevant documents.
Missing glossary/ADR files are created only when a term or decision is resolved during authorized documentation work.
```

Keep all tracker, label, and documentation-consumption instructions in this block. Do not create `docs/agents/issue-tracker.md`, `docs/agents/triage-labels.md`, or `docs/agents/domain.md`. Do not create empty glossary or ADR files during setup.

## 4. Verify and report

Re-read the resulting block. Confirm that tracker operations and label policy are explicit, documentation paths match the repo, there is only one configuration block, and no generated instructions require legacy configuration files. Report what changed and any unresolved choices. Subsequent skills read these settings from `AGENTS.md`; rerunning setup should update the block without duplicating it.
