# Pre-build brainstorming chat transcript

Messages are copied from the actual Codex task history in chronological order up to the first project-file change. This preserves the brainstorming conversation, not subsequent implementation chatter.

## User

Pick a project idea, different from Part I, and come up with a non trivial app (no habit tracker, to-do list, etc).  Come up with an idea you will be proud to show off. \
\
If interested in startup and money part, get ideas from: [https://trustmrr.com/](https://trustmrr.com/)\
\
\- Fully follow:\
[https://aishippingblog.com/p/ai-native-development-specifications](https://aishippingblog.com/p/ai-native-development-specifications)\
[https://aishippingblog.com/p/build-and-ship-a-full-stack-app-with](https://aishippingblog.com/p/build-and-ship-a-full-stack-app-with)\
\
I know they start from different places, but think about how can you combine. \
\
\- Utilize Github Issues as in ai-native-development-specifications. \
\- Use Non generic design agents like Lovable / v0 / Claude Design. OR at least provide good references for the coding agent. \
\- Close all mvp tags. It can be up to 100 issues. (more is ok)\
\- Use persistent storage as sqlLite. \
\- Use dbms agnostic tools like ORM.\
\- Work in iterations. First front end with mockService -> openapi.yml (describe contract) -> backend in memory story - > backend sqllite storage -> connect frontend + backend. \
\- Add all your .md files to the github repo. Improve them while you develop. \
\- Add your chat history where you brainstormed before creating an app as text file. (.md) \
\- Actually run your app and throughly test it. \
\- If found a bug, create an issue Github describe with Goal and Description and ask pm.md to groom and qa.md to add more test cases. Use tag user-test-bug. So that we know you actually tested. (Overall you will have mvp, post-mvp, user-test-bug tags). \
\- Work and test until it's fully working and well tested. \
\- Submit everything to github repo and close (qa-engineer.md should close it) all issues with mvp and user-test-bug tags before the deadline. 
this my homework, and can you help me with this hw, if it is not rude, can you do it for me as a student?


## Assistant

I’ll help you build this as a complete, reviewable student project. First I’ll inspect the workspace and the two linked guides, then I’ll choose a distinctive idea and turn the requirements into a working app, GitHub issue workflow, project docs, and test evidence.

## Assistant

The guides converge on a useful build sequence: precise spec, interactive mock-backed frontend, OpenAPI contract, in-memory backend, then SQLite through an ORM, followed by end-to-end QA. I’m choosing a “Fieldnote Atlas” concept: a visual field-research workspace that turns observations, places, evidence, and connections into an explorable map and narrative brief—more distinctive than a generic tracker and feasible to demonstrate locally. I’ll check what repo and GitHub access already exist before creating the issue backlog.

## Assistant

The folder is empty, and the GitHub CLI and Node runtime aren’t available in this environment. I can still create the full app, documentation, backlog, and test it with the available Python runtime; to publish issues and the repository, I’ll need to see whether a GitHub connector is available.

## Assistant

I’m going ahead with a polished, runnable local MVP and a repository-ready issue set. The external GitHub submission is the one part this environment cannot perform yet: no remote/repo or authenticated GitHub tool is attached. I’ll make that limitation explicit in the project handoff rather than claim issues were created or closed.


