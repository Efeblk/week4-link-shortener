---
name: implement-task
description: Implement one Link Shortener task with a failing HTTP-level test first, the smallest change, pytest verification, and a concise risk summary.
---

# Implement a Link Shortener task

Use this workflow for one feature from `docs/TASKS.md`.

1. Read the selected task and all applicable `AGENTS.md` guidance.
2. Inspect the related code and existing HTTP tests.
3. State the expected behavior, affected files, and relevant edge cases.
4. Add a failing behavioral test through `TestClient`.
5. Make the smallest implementation change that satisfies the test and task.
6. Run `python -m pytest` from the repository root and resolve failures.
7. Summarize the change, test result, and remaining risks or limitations.
