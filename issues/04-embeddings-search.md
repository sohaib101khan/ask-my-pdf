## Goal
Turn chunks into vectors and find the chunks most similar to a question.

## Steps
1. `app/embeddings.py`: load `sentence-transformers/all-MiniLM-L6-v2` once, `embed(texts) -> list[list[float]]`.
2. `app/store.py`: ChromaDB persistent client in `chroma_db/`. One collection per document. Add chunks with metadata `{page, index}`.
3. `search(document_id, question, k=5)` returns the top chunks with their page and a similarity score.
4. Call the store from `/upload` so a document is searchable right after upload.
5. Add `GET /search?document_id=...&q=...` for debugging.

## Acceptance criteria
- [ ] For your sample PDF, ask 5 questions whose answers you know, and the right page is in the top 5 at least 4 times. Paste the 5 questions and results in the PR.
- [ ] Test: index 3 tiny fake chunks, search a question, the expected chunk comes first.
- [ ] Re-uploading the same document does not duplicate chunks.

## Hints
- First embed call downloads the model (~90 MB); that's normal.
- Chroma returns distances; convert to a score so higher is better.
