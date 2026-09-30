# ADR Format

Preserve the project's existing ADR template, metadata, naming, and numbering. Use the defaults below only where no convention exists.

Use the ADR directory configured in `CLAUDE.md` or the context map for the decision's scope. System-wide decisions default to root `docs/adr/`; context-specific decisions use that context's ADR directory (for example `src/ordering/docs/adr/`). Default file names are `0001-slug.md`, `0002-slug.md`, etc.

Create the selected ADR directory lazily, only when its first agreed decision is recorded.

## Template

```md
# {Short title of the decision}

{1-3 sentences: what's the context, what did we decide, and why.}
```

That's it. An ADR can be a single paragraph. The value is in recording *that* a decision was made and *why*, not in filling out sections.

## Optional sections

When no project template applies, include these only when useful.

- **Status** frontmatter (`proposed | accepted | deprecated | superseded by ADR-NNNN`): useful when decisions are revisited
- **Considered Options**: only when the rejected alternatives are worth remembering
- **Consequences**: only when non-obvious downstream effects need to be called out

## Numbering

When using sequential numbering, scan the selected ADR directory for the highest existing number and increment by one. Check that the target filename is unused before writing; do not borrow numbering from a different context or overwrite an existing ADR.

## When to offer an ADR

For unsolicited suggestions, consider these signals rather than requiring all three:

1. **Hard to reverse**: the cost of changing your mind later is meaningful
2. **Surprising without context**: a future reader will look at the code and wonder "why on earth did they do it this way?"
3. **The result of a real trade-off**: there were genuine alternatives and you picked one for specific reasons

Suggest an ADR when preserving the reasoning will help future changes; skip routine choices with no useful context to retain. An explicit request to document a decision does not need to satisfy these signals.

### What qualifies

- **Architectural shape.** "We're using a monorepo." "The write model is event-sourced, the read model is projected into Postgres."
- **Integration patterns between contexts.** "Ordering and Billing communicate via domain events, not synchronous HTTP."
- **Technology choices that carry lock-in.** Database, message bus, auth provider, deployment target. Not every library: just the ones that would take a quarter to swap out.
- **Boundary and scope decisions.** "Customer data is owned by the Customer context; other contexts reference it by ID only." The explicit no-s are as valuable as the yes-s.
- **Deliberate deviations from the obvious path.** "We're using manual SQL instead of an ORM because X." Anything where a reasonable reader would assume the opposite. These stop the next engineer from "fixing" something that was deliberate.
- **Constraints not visible in the code.** "We can't use AWS because of compliance requirements." "Response times must be under 200ms because of the partner API contract."
- **Rejected alternatives when the rejection is non-obvious.** If you considered GraphQL and picked REST for subtle reasons, record it; otherwise someone will suggest GraphQL again in six months.
