## Goal
Split pages into chunks that are small enough to embed and search, while remembering the page each chunk came from.

## Why
LLMs and embedding models work on pieces of a few hundred tokens. A whole page is too big and too mixed.

## Steps
1. Write `app/chunking.py` with `chunk_pages(pages, size=500, overlap=80) -> list[Chunk]` where a chunk has `text`, `page`, `index`.
2. Count size in words for now (tokens later if you like). Overlap means the last 80 words of one chunk start the next.
3. Never let a chunk span two pages.
4. Save chunks to `data/<document_id>/chunks.json` during upload.

## Acceptance criteria
- [ ] Three tests in `tests/test_chunking.py`:
  - a 1,200-word page gives 3 chunks, all with the same page number;
  - two pages never share a chunk;
  - overlap works: the last words of chunk 1 appear at the start of chunk 2.
- [ ] The sample PDF produces a sensible number of chunks (print it in the upload response).

## Hints
- Write the tests first with made-up text, then the function.
