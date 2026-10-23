# Stage 2: Click counter implementation

The `implement-task` skill was followed: guidance and the task were read,
affected behavior was stated in the plan, then an HTTP-level failing test was
added before the application changed.

## Failing test evidence

Command:

```powershell
.\.venv\Scripts\python -m pytest tests/test_main.py::test_new_link_stats_start_at_zero_and_reads_do_not_count_clicks -q
```

Output before implementation:

```text
F                                                                        [100%]
================================== FAILURES ===================================
_______ test_new_link_stats_start_at_zero_and_reads_do_not_count_clicks _______

    def test_new_link_stats_start_at_zero_and_reads_do_not_count_clicks():
        created = client.post("/shorten", json={"url": "https://example.com"})
        code = created.json()["code"]

        first_stats = client.get(f"/stats/{code}")
        second_stats = client.get(f"/stats/{code}")

>       assert first_stats.status_code == 200
E       assert 404 == 200
E        +  where 404 = <Response [404 Not Found]>.status_code

tests\test_main.py:35: AssertionError
=========================== short test summary info ===========================
FAILED tests/test_main.py::test_new_link_stats_start_at_zero_and_reads_do_not_count_clicks
1 failed, 1 warning in 0.15s
```

## Smallest implementation

- Added `clicks INTEGER NOT NULL DEFAULT 0` to the table definition and a
  `PRAGMA table_info` check that migrates an existing local `links.db`.
- Incremented `clicks` only for a successful redirect with
  `clicks = clicks + 1`.
- Added read-only `GET /stats/{code}` returning `url` and `clicks`, with the
  existing `404` behavior for unknown codes.
- Added behavioral tests for visits, unknown stats, and separate counters;
  the first test also verifies a new link starts at zero and stats reads do not
  count as clicks.

## Passing test evidence

Command:

```powershell
.\.venv\Scripts\python -m pytest -q
```

Output after implementation:

```text
.......                                                                  [100%]
7 passed, 1 warning in 0.18s
```

The warning is emitted by the installed FastAPI/Starlette `TestClient` about
its `httpx` compatibility path; it does not indicate a failing test.
