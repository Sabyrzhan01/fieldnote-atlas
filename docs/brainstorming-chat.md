# Brainstorming chat record

This file preserves the assignment prompt and the idea-selection notes from before implementation. It is a concise record, not a verbatim export of every assistant turn.

## User's assignment prompt

> Pick a project idea, different from Part I, and come up with a non trivial app (no habit tracker, to-do list, etc). Come up with an idea you will be proud to show off.
>
> If interested in startup and money part, get ideas from: https://trustmrr.com/
>
> Fully follow:
> - https://aishippingblog.com/p/ai-native-development-specifications
> - https://aishippingblog.com/p/build-and-ship-a-full-stack-app-with
>
> I know they start from different places, but think about how can you combine.
> Utilize Github Issues in the first article's workflow. Use non-generic design references (Lovable / v0 / Claude Design) or give the coding agent strong visual references. Close all MVP tags (up to 100 issues is okay). Use SQLite for persistent storage and a DBMS-agnostic ORM. Work in iterations: mock-service frontend → OpenAPI contract → in-memory backend → SQLite storage → connect frontend and backend. Keep Markdown documentation in GitHub and improve it while developing. Save the brainstorming chat as Markdown. Run and thoroughly test the app. If a real user-test bug is found, create a GitHub issue with Goal and Description, ask PM to groom it and QA to add cases, label it `user-test-bug`, then fix and retest. QA should close passing `mvp` and `user-test-bug` issues before the deadline.

## Idea discussion and decision

We considered a neighborhood soundwalk archive, a personal museum of found objects, an oral-history map, and a field-research atlas. The atlas best combined a distinctive map-led portfolio presentation with a meaningful research workflow: a researcher can compare observations, interview excerpts, artifacts, and local signals while keeping each item's place, date, source, and tags attached.

The selected project is **Fieldnote Atlas**: a visual field-research archive seeded with fictional Almaty observations. The first release focuses on browsing and selecting evidence, search, filters, starring, and creating a field note. It does not use live location data or claim real map precision.

The user later supplied `https://github.com/Sabyrzhan01/fieldnote-atlas` as the destination repository and confirmed being signed in. The selected idea should be compared with the student's Part I topic before submission; that topic was not included in the conversation available for this record.

## Follow-up choices

- Visual direction: warm editorial research journal, understated cartography, terracotta markers, serif display type, and monospaced metadata. See `design-system.md` for concrete references and tokens.
- Build loop: mock-backed interactive frontend first, then OpenAPI, in-memory FastAPI, SQLAlchemy/SQLite, and a connected API mode.
- Workflow: groomed GitHub issues with `mvp`, `post-mvp`, and `user-test-bug` labels; PM, engineer, and QA role guides; only QA closes passing MVP/bug issues.
- Startup research was optional in the assignment, so the project stayed focused on the research workflow instead of adding speculative monetization.
