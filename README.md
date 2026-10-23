# Link Shortener

A tiny FastAPI + SQLite service for creating short URLs and redirecting them.
Read [AGENTS.md](AGENTS.md) for the repository workflow, commands, and product
boundaries before making a change.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements-dev.txt
.\.venv\Scripts\python -m pytest
.\.venv\Scripts\python -m uvicorn main:app --reload
```

The app runs at `http://localhost:8000`; interactive documentation is at
`/docs`.

## Try it

```bash
curl -X POST localhost:8000/shorten -H 'Content-Type: application/json' \
  -d '{"url":"https://example.com"}'
# -> {"code":"b","short_url":"/b"} then GET /b redirects
```

## API

- `POST /shorten` creates a short code for an HTTP(S) URL.
- `GET /{code}` redirects with `307` and increments that link's click count.
- `GET /stats/{code}` returns `{ "url": "...", "clicks": N }`, or `404` for
  an unknown code.

## Files

- `main.py` - the complete FastAPI application.
- `tests/test_main.py` - the pytest suite.
- `AGENTS.md` - repository guidance for Codex.
- `docs/TASKS.md` - available homework features.
