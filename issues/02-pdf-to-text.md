## Goal
Upload a PDF and turn it into text, one entry per page, so every later answer can say which page it came from.

## Steps
1. Add `POST /upload` that accepts a PDF file (FastAPI `UploadFile`).
2. Extract text per page with `pypdf`. Build a list like `[{"page": 1, "text": "..."}, ...]`.
3. Save the list as JSON under `data/<document_id>/pages.json`. `document_id` can be a short uuid.
4. Return `{"document_id": ..., "pages": <count>, "chars": <total characters>}`.
5. Put one real PDF (10 to 30 pages, something you like, no personal data) in `sample_pdfs/`.

## Acceptance criteria
- [ ] Uploading the sample PDF returns the right page count.
- [ ] Empty pages are kept (as empty strings), so page numbers stay correct.
- [ ] A non-PDF upload returns HTTP 400 with a clear message.
- [ ] Test: `tests/test_upload.py` uploads the sample PDF and checks the page count.

## Hints
- `from pypdf import PdfReader`, `reader.pages[i].extract_text() or ""`.
- FastAPI `TestClient` can upload files with `files={"file": ("x.pdf", open(path, "rb"), "application/pdf")}`.
