## Goal
Follow-up questions should work: "What does chapter 2 say about X?" then "and chapter 3?".

## Steps
1. Add `conversation_id` to `/ask`. Keep the last 6 turns in memory (a dict is fine; SQLite is a bonus).
2. Before searching, rewrite the follow-up into a standalone question using the LLM ("and chapter 3?" becomes "What does chapter 3 say about X?"). Search with the rewritten question.
3. Return the rewritten question in the response so you can see it.

## Acceptance criteria
- [ ] A two-step conversation from your PDF works and the rewritten question is sensible (paste it).
- [ ] A new `conversation_id` starts clean.
- [ ] Test: the rewrite step is called only when there is history.

## Hints
- Keep the rewrite prompt tiny; it is a cheap call.
