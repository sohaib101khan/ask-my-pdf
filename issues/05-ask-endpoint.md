## Goal
Answer a question with the LLM, using only the retrieved chunks.

## Steps
1. `app/llm.py`: one function `complete(system, user) -> str` that works for the provider in `.env` (Anthropic, OpenAI or Ollama). Start with the one you have a key for; leave the others as TODO.
2. `POST /ask` with `{document_id, question}`:
   - search top 5 chunks,
   - build a prompt: system = rules, user = the chunks (each labelled `[page N]`) followed by the question,
   - return `{"answer": ..., "pages": [list of pages used], "chunks": [...]}`.
3. The system prompt must say: answer only from the given text; if the text does not contain the answer, say so.

## Acceptance criteria
- [ ] 5 questions from your sample PDF get correct answers (paste them in the PR).
- [ ] A question about something not in the PDF ("who won the 2018 World Cup?") gets a refusal, not a guess.
- [ ] Test: mock `complete` to return a fixed string and check `/ask` wires search + prompt + answer together.

## Hints
- Log the full prompt once and read it. You learn more from one real prompt than from ten blog posts.
