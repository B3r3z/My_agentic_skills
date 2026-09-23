# Local task format

One file per task: `<NN>-<slug>.md` in the configured directory. Start at `01` only for a new set; allocate unused numbers for additions. Update matching tasks rather than duplicating them. Dependencies use stable local IDs or relative links, must resolve, and must not form cycles.

```markdown
# <NN>: <Title>

**What to build:** observable behavior or migration outcome.
**Blocked by:** local task IDs/links, or None.
**Status:** ready-for-agent

- [ ] Verifiable acceptance criterion
```

Keep existing statuses on revision unless the changed requirements justify an explicit transition. `ready-for-agent` means specified; execution also requires every blocker to be complete, except for the explicit integration-group rule below. Record follow-up notes locally when requested.

Prefer durable behavior and contracts over speculative file lists. Include a concrete path, schema, or short prototype extract when it expresses an actual constraint more precisely.

When tasks cannot pass verification independently, define an integration group once in the plan or a member task and link it from the other members. Specify member IDs, implementation order, each member's independently verifiable criteria, and the exact checks deferred until the group is implemented. A member with those individual criteria satisfied may be recorded as `implemented` to unblock the next member. All members remain incomplete until their individual criteria and shared checks pass; dependent work outside the group waits for completion. Do not defer unrelated failures or create cyclic dependencies to express shared verification.
