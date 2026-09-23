# Focused experiments

For intermittent failures, record attempts, failures, conditions, and seeds where possible. Use bounded repeated runs or isolated stress to increase the signal, with a time/attempt limit and a stopping condition. Do not infer reliability from one successful run. Avoid load or destructive replay against shared systems without authorization.

For performance, establish comparable before/after conditions and measure the reported bottleneck. Use timings, profiles, or query plans as appropriate; account for warmup and natural variance. Bisection is useful when a known-good revision or dataset exists, but preserve unrelated work in an isolated checkout.

When reproduction needs human interaction, adapt [hitl-loop.template.sh](../scripts/hitl-loop.template.sh) if it helps. Inspect it before running; use only the required steps and protect captured credentials. A human-driven reproduction is evidence, even when it cannot be automated.

Choose the next experiment for the information it can add. If additional runs cannot distinguish the remaining hypotheses, report the missing evidence instead of increasing the loop indefinitely.
