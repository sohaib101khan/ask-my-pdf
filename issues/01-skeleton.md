## Goal
Get the project running on your machine and understand the layout.

## Steps
1. Clone the repo, create a virtualenv, `pip install -r requirements.txt`.
2. Copy `.env.example` to `.env`. Pick a provider (ask Sohaib which key you get).
3. Run `uvicorn app.main:app --reload` and open http://127.0.0.1:8000/docs.
4. Run `pytest` and watch the one test pass.
5. Add a `app/config.py` that reads `LLM_PROVIDER` and the keys from `.env` with `python-dotenv`, and fails with a clear message if the chosen provider has no key.

## Acceptance criteria
- [ ] `pytest` passes.
- [ ] `/health` returns `{"status": "ok"}`.
- [ ] `app/config.py` exists and `python -c "from app.config import settings; print(settings.provider)"` prints your provider.
- [ ] README has a line with your name under "Built by".

## Hints
- `python-dotenv`: `load_dotenv()` then `os.getenv("LLM_PROVIDER")`.
- Keep secrets out of git. `git status` must never show `.env`.
