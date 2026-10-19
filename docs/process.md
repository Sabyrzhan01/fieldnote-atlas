# Development process

## Workflow basis
This staged workflow combines the spec-first backlog/PM-engineer-QA loop from [AI-Native Development: Specifications, Loop and Graph Engineering](https://aishippingblog.com/p/ai-native-development-specifications) with the mock-service frontend → OpenAPI → in-memory API → SQLite/SQLAlchemy sequence from [Build and Ship a Full-Stack App with AI Coding Assistants](https://aishippingblog.com/p/build-and-ship-a-full-stack-app-with). The issue tracker is the current source of task status; the local issue files are the groomed source templates. Design inspiration and component references are recorded in `design-system.md`.

## Canonical work
GitHub Issues are the canonical backlog after a GitHub remote is configured. Every MVP issue must be groomed, implemented, independently checked against acceptance criteria, and closed by QA only after PASS. Labels: `mvp`, `post-mvp`, and `user-test-bug`.

## Staged implementation
1. **Frontend + mockService:** Build and inspect the full interactive UI with seeded local mock data. No backend dependency.
2. **OpenAPI:** Describe the frontend service contract in root `openapi.yaml`; treat it as the shared boundary.
3. **In-memory backend:** Implement that contract with FastAPI and an in-memory repository; connect the frontend and validate the contract.
4. **SQLite persistence:** Replace the repository implementation with SQLAlchemy models and SQLite, keeping routes and response shapes stable.
5. **Integrated QA:** Run backend checks, production build, and browser walkthrough against the real backend. Record steps and results.

## Roles
- PM grooms each issue using `docs/team/pm.md` before implementation.
- Engineer implements one groomed issue using `docs/team/software-engineer.md`; never closes it.
- QA checks the running result against acceptance criteria using `docs/team/qa-engineer.md`, posts PASS/FAIL evidence, and closes a passing issue.

## Orchestrator and loop
The main development session coordinates the role handoffs and does not report its implementation work as independent QA. For each issue: (1) choose an open backlog item, (2) PM grooms it, (3) engineer implements and leaves it open, (4) QA independently checks the running result without editing code, (5) FAIL returns to engineering with the QA comment, (6) QA posts a PASS comment and closes only after every criterion passes, (7) repeat until the selected backlog scope is complete. The `/goal` loop stop condition is checkable: every issue in the chosen label/scope is either closed after PASS or explicitly deferred in a linked post-MVP issue.

## Bug loop
When a bug is found during hands-on app use, create a GitHub issue labeled `user-test-bug` with a **Goal** and **Description**, reproduction steps, observed/expected behavior, and environment. PM grooms it; QA adds the missing regression cases to `docs/testing-guidelines.md` and the relevant test suite. Fix, repeat the same user journey, post QA verdict, then close. Do not invent user-test bugs when none were observed.

## Git discipline
Commit at meaningful milestones. Keep all Markdown project artifacts in the repository. Do not mark an issue done until the corresponding code/docs are committed and QA has checked it.
