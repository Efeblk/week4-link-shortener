# Stage 1: Click counter plan

**Stage boundary:** planning only; do not change application code or tests in
this stage.

## Expected behavior

- Every successful `GET /{code}` increments that link's click count once and
  still returns the existing `307` redirect.
- `GET /stats/{code}` returns `200` and
  `{ "url": "<stored URL>", "clicks": <integer> }`.
- A new shortened link reports `clicks: 0` before it is visited.
- Statistics reads do not increment the counter.
- Unknown codes return `404` from both the redirect and statistics endpoints.
- Counts belong to their individual links; visiting one link cannot change
  another link's count.

## Affected files

- `main.py`: add a non-null `clicks` column with a zero default, make database
  initialization work for an existing `links.db`, increment during a successful
  redirect, and add `GET /stats/{code}`.
- `tests/test_main.py`: add HTTP-level tests for initial count, visits,
  statistics reads, unknown statistics code, and independent links.
- `docs/stages/02-implement.md`: record the required red/green test evidence.

## Test plan

Use `TestClient` and the autouse reset fixture. Create links through
`POST /shorten`, request redirects with `follow_redirects=False`, then inspect
the public statistics endpoint. Add one failing test first, then add the rest
of the behavioral coverage once the endpoint exists.

## Edge cases and implementation notes

- The app creates `links.db` at import time, so initialization must migrate the
  existing table instead of assuming a fresh database.
- Use a SQL increment (`clicks = clicks + 1`) only after confirming that the
  code exists. This avoids counting unknown codes and preserves independent
  rows.
- `GET /stats/{code}` must only read state. Redirects need
  `follow_redirects=False` so tests observe the service's `307` response.
- Concurrent requests are outside this homework's tiny local-service scope;
  the increment statement nevertheless avoids a Python read-modify-write step.
