## Goal
A student can start the application and run repeatable checks.

## Acceptance criteria
- [ ] `python3 server.py` starts the local site at `http://127.0.0.1:8091/`.
- [ ] `python3 -m unittest discover -s backend/tests -v` exits successfully.
- [ ] `python3 -m compileall -q backend server.py` exits successfully.

## Out of scope
- Do not add a framework dependency to the offline runnable path.

## Constraints
- Root scripts, README, and tests.
- Follow `docs/spec.md`, `docs/process.md`, and role instructions.
