---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Look up available environmental facts yourself. Delegate an independent lookup only when useful and available; if delegation is absent or a limit is reached, use your own read tools and continue. While a lookup runs, ask questions that do not depend on its result. Ask the user for decisions or facts you cannot obtain from available evidence.

Keep the decision tree within the requested goal. Finish when decisions needed for the next agreed step are settled; list deferred questions and explicit assumptions instead of expanding indefinitely. Confirm the shared understanding before implementation or other follow-on actions. When used by `grill-with-docs`, record agreed documentation during the interview as that skill directs; otherwise do not edit project files merely because an interview occurred.
