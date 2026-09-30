# Waiting for delegated work

Use the delegation system's blocking, event-driven wait for the assigned agent. Defaults below may be overridden by the user's request or Orbit Forge settings in `AGENTS.md`, within tool limits.

- Wait window: 45–60 seconds (default 60). Completion, a relevant message, or new user input may wake the wait earlier.
- Silence threshold: 5 minutes since the last meaningful task progress or status response.
- Correction limit: two consecutive rounds without measurable progress on confirmed failures.

## Event loop

1. Dispatch work and record the agent ID and time of the last meaningful signal.
2. If no independent work remains, block on the agent's wait tool. With the collaboration tools, use `wait_agent(timeout_ms=60000)`; consume its notifications/messages when it wakes. If the wait returns only a summary, fetch only the indicated result as necessary.
3. On a timeout, wait again. Do not call list/status tools, inspect the evolving diff, read logs, or send a check-in just because a window expired. Events from other agents do not reset this task's silence clock. Routine "still working" replies may defer a check-in but are not evidence of implementation progress.
4. On completion, collect the result and perform the acceptance gate. On a question or blocker, resolve it immediately within scope or ask the user for the missing decision. Incorporate new user input before continuing.
5. After the silence threshold, send one concise request for the current result, remaining work, and any blocker, then continue event-driven waiting. Record the check-in time; do not repeat it before another full silence interval. Assess the response before deciding the next action.

A timeout, silence, or a slow build does not itself authorize cancellation, duplicate implementation, or model substitution. If successive check-ins show no substantive progress, investigate the reported blocker instead of indefinitely repeating check-ins. A task-wide deadline, if the user supplies one, is separate from these wait windows; surface unfinished work when it is reached.

If no event-driven wait exists, use the available interruptible wait/sleep for up to 60 seconds before a bounded status check. Do not use a busy loop or a long blocking shell sleep. Report meaningful changes to the user and obey the host's communication requirements; avoid repeating unchanged status when not required.
