# Week 4 write-up

## 1. Repository-wide guidance

`AGENTS.md` describes the service's purpose, a short file map, PowerShell
commands for creating the virtual environment, installing development
requirements, running Uvicorn, and running pytest. It also states the product
boundary: this remains a small single-file FastAPI service with local SQLite
state, without authentication, a frontend, a remote database, accounts, or
unrequested layers. Finally, it gives the compact workflow: understand the
task, add a behavioral test, make the smallest change, and verify it. These
facts belong here because they apply before almost any code, documentation, or
test change.

## 2. Scoped guidance

`tests/AGENTS.md` applies to the `tests/` subtree. It requires public HTTP API
tests through `TestClient`, success plus failure or edge-case coverage,
independent state-reset tests, and assertions about observable behavior rather
than SQLite internals. This detail would add noise to a documentation-only or
application-only task, so it is not in the root guide. Codex discovers
`AGENTS.md` files by walking from the repository root to its current working
directory, using the nearest applicable file in each directory. Thus, when
Codex starts work in `tests/` or a child directory, it receives the root guide
and this test-specific guide; the nested guide follows the broader root rules.

## 3. Reusable workflow

`.agents/skills/implement-task/SKILL.md` encodes the seven-step feature
procedure: read the task and guidance; inspect related code and tests; state
behavior, files, and edge cases; add a failing behavioral test; make the
smallest change; run pytest; summarize the result and remaining risks. It
turns the requested development sequence into a reusable instruction instead
of leaving it only in a one-time chat prompt.

## 4. Codex discovery and invocation

Codex loads repository instructions from the root through the current working
directory. It loads the root guide always and the tests guide when started in
that scope. For local skills, Codex scans `.agents/skills` from the current
directory up to the repository root. It initially sees each skill's name,
description, and path, then reads the full `SKILL.md` when selected. The skill
can be selected explicitly with `$implement-task` in Codex CLI or an IDE
extension, or implicitly when a request matches its description. The stage
files under `docs/stages/` are ordinary project documentation: they are not a
special auto-invoked Codex artifact, so the root file map and an explicit task
prompt point an agent to them.

## 5. Planning and review findings

The plan in `docs/stages/01-plan.md` identified a real compatibility concern:
the starter creates a persistent `links.db`, so adding a column required a
migration check rather than assuming a fresh table. It also identified that
redirect tests need `follow_redirects=False` to observe the `307`. The review
in `docs/stages/03-review.md` checked the full diff against those points and
accepted it after confirming all requested counter behaviors had HTTP-level,
order-independent coverage. The final test run was `7 passed, 1 warning`; the
warning is the installed framework's `TestClient` deprecation notice.

<!-- TODO (you): write this yourself. Course policy (Week 1 slides, p.16): no AI for reflections. -->
