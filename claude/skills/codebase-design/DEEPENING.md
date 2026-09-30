# Deepening existing modules

Identify complexity repeated across real callers and propose an interface that contains it. Check invariants, error semantics, and dependency ownership before consolidating behavior; in-process code is not automatically safe to merge.

Choose verification according to the dependency:

- Pure or in-memory behavior: exercise it directly through the proposed interface.
- Local infrastructure: use a realistic test instance or substitute when it preserves the relevant semantics.
- Owned remote services: isolate transport where useful, and retain contract or integration evidence for behavior a fake cannot prove.
- Third-party systems: use controlled boundary doubles for deterministic behavior, with appropriate integration evidence for their real contract.

Introduce a seam for a concrete variation, isolation, or ownership need. The number of adapters alone does not establish whether the seam is useful. Keep test-only configuration from needlessly expanding the caller interface.

Before retiring tests, map their distinct scenarios, edge cases, and invariants to verified replacements. Preserve or port unmatched cases; a new high-level test does not automatically replace existing regression coverage. Remove behavior-specific tests only when that behavior has explicitly left the requirements.
