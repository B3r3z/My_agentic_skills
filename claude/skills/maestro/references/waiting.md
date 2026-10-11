# Waiting for Claude Code subagents

Use Claude Code's foreground result or background completion notification for the assigned subagent. Settings below may be overridden by the user's request or Maestro settings in `CLAUDE.md`, within host limits.

- Silence threshold: 5 minutes since the last meaningful task progress or status response, when the host exposes elapsed time and a message mechanism.
- Correction limit: two consecutive rounds without measurable progress on confirmed failures.

## Event loop

1. Dispatch with `Agent`, then record the returned agent ID and any output-file path. In sequential mode, keep one implementer active and request foreground execution when the host supports it; current interactive sessions may run all subagents in the background. In parallel mode, run implementers in the background up to the concurrency limit.
2. If the call returns a final result, perform the acceptance gate. If it starts background work, complete only independent work, then wait for Claude Code's completion notification. Use an available blocking wait when provided. Do not repeatedly read the output file, inspect the evolving diff or logs, or poll session task lists. In parallel mode, handle each completion as it arrives (accept, merge, dispatch newly ready tasks) while the others continue.
3. On completion, collect the reported result. Read the reported output file once when the notification omits needed details; do not assume an output file means the task finished. A returned partial result remains incomplete and may be continued using the same agent.
4. Resolve reported questions or blockers within scope. Subagents cannot use `AskUserQuestion`; the root handles missing user decisions. Incorporate new user input before continuing.
5. Track silence per agent; another agent's events do not reset it. When the host permits a timed check-in and the silence threshold has passed, use the available subagent messaging mechanism once to request the current result, remaining work, and blocker. Current Claude Code uses `SendMessage` addressed to the recorded agent ID to continue completed subagents; older hosts may offer `Agent` resumption. Do not assume these tools exist or send a message to an unrelated session. Record the check-in and wait for a relevant event before another check-in.

If the host requires yielding to deliver a completion notification, keep the execution record active and report that the assigned task is pending. Continue the same run when its result arrives; a waiting response never marks acceptance or review passed. Do not create cron jobs or another session to emulate a wait.

A timeout, silence, or slow build does not authorize cancellation, duplicate implementation, or model substitution. If successive check-ins show no substantive progress, investigate the reported blocker. A user-supplied task deadline is separate from waiting; report unfinished work when it is reached.
