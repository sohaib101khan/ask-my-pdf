## Goal
Measure quality with numbers instead of feelings. This is the most important habit in AI work.

## Steps
1. Write `eval/questions.json`: 20 questions about your sample PDF, each with the expected answer (short) and the expected page(s).
2. `eval/run.py`: for each question call `/ask`, then score:
   - page hit: is an expected page in the returned pages?
   - answer hit: does the answer contain the expected short answer (case-insensitive)?
3. Print a table and two totals: page accuracy and answer accuracy. Save results to `eval/results-<date>.json`.
4. Change one thing (chunk size, k, or the system prompt), run again, write what happened in the PR.

## Acceptance criteria
- [ ] 20 questions, run completes, both accuracies printed.
- [ ] PR shows before/after numbers for one change and a sentence on why.
- [ ] Script does not need the UI; it talks to the API with `httpx`.
