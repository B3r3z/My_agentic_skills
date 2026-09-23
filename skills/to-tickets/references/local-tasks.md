# Local task format

One file per task: `<NN>-<slug>.md` in the configured directory. Start at `01` only for a new set; allocate unused numbers for additions. Update matching tasks rather than duplicating them. Dependencies use stable local IDs or relative links, must resolve, and must not form cycles.

```markdown
# <NN>: <Title>

**What to build:** observable behavior or migration outcome.
**Blocked by:** local task IDs/links, or None.
**Status:** ready-for-agent

- [ ] Verifiable acceptance criterion
```

Keep existing statuses on revision unless the changed requirements justify an explicit transition. `ready-for-agent` means specified; execution also requires every blocker to be complete. Record follow-up notes locally when requested.

Prefer durable behavior and contracts over speculative file lists. Include a concrete path, schema, or short prototype extract when it expresses an actual constraint more precisely. For an integration-only verification gate, identify which tasks share that gate; do not promise independent green checks for those tasks.
