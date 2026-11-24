# Writing patterns

## Runbooks and API guides

Tell readers where to act and what must be true first. Keep the condition attached to every step it governs. Give the expected result if the source provides it.

Source: “Following a failed deployment, operators should consider inspecting the logs via `svc logs --env test` before initiating another deployment.”

Rewrite: “If the deployment fails, we recommend reading the logs before you deploy again. To read the logs, run `svc logs --env test`.”

## Incidents and errors

For an incident, report the observed impact, the interval, and the recovery state when known. Attribute hypotheses to their source. For an error, keep the literal message for search and give a known next step if one exists.

Source: “Between 10:02 and 10:07 UTC, requests returned `E_TIMEOUT`. Connection pool exhaustion may have been a contributing factor.”

Rewrite: “From 10:02 to 10:07 UTC, requests returned `E_TIMEOUT`. The service may have run out of connections.”

## Release notes and commit messages

Name the change and its scope. For release notes, state what the user can now do or what they need to change. For a commit subject, name the change in one line.

Source: “The CSV export functionality now facilitates the inclusion of archived orders when the `includeArchived` option is enabled.”

Rewrite: “CSV exports now include archived orders if you enable `includeArchived`.”

## UI copy, prompts, and text for translation

In UI instructions, copy the label exactly. In prompts, keep output formats, placeholders, and conditions intact. For translation, replace idioms and name the referent of an ambiguous pronoun.

Source: “Once you have given the preview a once-over, go ahead and hit **Send now**.”

Rewrite: “After you review the preview, select **Send now**.”
