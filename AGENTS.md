# Link Shortener repository guide

## Purpose

This is a tiny FastAPI link shortener. `POST /shorten` stores a valid HTTP(S)
URL and returns a code; `GET /{code}` redirects to the stored URL.

## File map

- `main.py`: the complete application and local SQLite access.
- `tests/test_main.py`: HTTP-level behavioral tests.
- `tests/conftest.py`: gives each test its own temporary database (never the real `links.db`).
- `docs/TASKS.md`: the available homework features.
- `.agents/skills/implement-task/SKILL.md`: feature implementation workflow.

## Commands (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements-dev.txt
.\.venv\Scripts\python -m uvicorn main:app --reload
.\.venv\Scripts\python -m pytest
```

## Product boundaries

Keep this a small, single-file HTTP service with local SQLite state. Do not add
authentication, a frontend, a remote database, accounts, analytics systems, or
unrequested architectural layers.

## Change workflow

1. Understand the selected task, this guidance, and the affected code/tests.
2. Add a behavioral test that demonstrates the required result.
3. Implement the smallest change that makes the test pass.
4. Run `pytest` and summarize behavior plus any remaining risks.
