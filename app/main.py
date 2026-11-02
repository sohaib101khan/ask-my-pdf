from fastapi import FastAPI

app = FastAPI(title="Ask My PDF")


@app.get("/health")
def health() -> dict:
    """Issue 1: this is the only endpoint for now. Keep it."""
    return {"status": "ok"}
