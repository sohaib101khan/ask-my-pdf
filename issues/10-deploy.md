## Goal
Put it online so you can send a link.

## Steps
1. Write a `Dockerfile` that runs the API (and the UI in a second service or the same container; your call, explain it).
2. Deploy to Render, Railway or Hugging Face Spaces (free tiers work). Keys go in the host's secret settings, never in the repo.
3. Add the live link and a short "how it works" diagram (even hand-drawn) to the README.

## Acceptance criteria
- [ ] `docker build` and `docker run` work locally.
- [ ] Live link in README answers a question about the sample PDF.
- [ ] README explains the pipeline in 5 lines: upload, chunk, embed, search, answer with citations.

## Stretch (optional)
- Multiple PDFs with a document filter.
- Streaming answers.
- A re-ranker on the top 20 chunks.
