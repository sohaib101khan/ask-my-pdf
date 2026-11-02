## Goal
Make citations trustworthy: the pages reported must be the pages the answer really used, and weak matches must refuse.

## Steps
1. Ask the model to end its answer with a line `PAGES: 3, 7` listing only pages it used. Parse that line, remove it from the answer, return the numbers.
2. If the best search score is below a threshold (find it by trying), skip the LLM and return `"I couldn't find that in the document."` with `pages: []`.
3. Return a short quote (one sentence) from each cited page so the user can verify.

## Acceptance criteria
- [ ] For 5 known questions, every cited page actually contains the answer (check by hand, paste results).
- [ ] An off-topic question never calls the LLM (add a counter or log and prove it).
- [ ] Test: parsing `PAGES: 3, 7` and a missing PAGES line both work.

## Hints
- Models sometimes write `Pages:` or `PAGES 3,7`. Parse with a forgiving regex.
