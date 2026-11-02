# Ask My PDF

A chatbot that answers questions about any uploaded PDF and cites the pages it used.

This is a learning project. Work through the GitHub Issues in order (#1 to #10). Each issue is one pull request:
read the goal, meet every acceptance criterion, make the tests pass, open the PR, ask for review.

## Stack

- Python 3.11+, FastAPI, pypdf
- sentence-transformers (free embeddings), ChromaDB (vector store)
- One LLM: Claude API, OpenAI API, or a free local model through Ollama
- Streamlit for the UI (issue 9)

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows   (source .venv/bin/activate on Mac/Linux)
pip install -r requirements.txt
copy .env.example .env         # then fill in your key
uvicorn app.main:app --reload
```

## Rules of the road

- Small commits with clear messages.
- Every issue adds at least one test in `tests/`.
- Never commit `.env` or API keys.
- If stuck for more than an hour, write what you tried in the issue and ask.
