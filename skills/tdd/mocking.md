# Controlling dependencies

Prefer real internal behavior. Introduce a double when it controls a relevant boundary: remote service, clock, randomness, filesystem, or costly infrastructure. Ownership alone does not decide whether to mock; an owned remote service can still need a test double.

Use a test database or realistic local substitute when database semantics are part of the contract. A mock cannot establish transaction, query, or concurrency behavior it does not implement.

Assert externally meaningful outcomes. Calls, counts, or ordering are useful assertions when they are themselves contractual, such as preventing duplicate payments; avoid them for incidental internal choreography.

Inject dependencies where this makes behavior controllable without speculative abstractions. Keep doubles consistent with the real contract, and cover important gaps with contract or integration checks. Choose interface shape for callers rather than solely for mocking convenience.
