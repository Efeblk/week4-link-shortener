# Tests guidance

This guidance applies to files under `tests/`.

- Test the public FastAPI HTTP API with `TestClient`.
- Cover successful behavior and failures or meaningful edge cases.
- Keep tests independent: use the shared fixture to reset service state; do not
  depend on test ordering or codes created by another test.
- Assert observable status codes, response bodies, headers, and redirects—not
  SQLite queries or other private implementation details.
