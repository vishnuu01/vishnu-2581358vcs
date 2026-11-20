# CampusNotes — VCS Assignment 2

**Student:** Vishnu Singh  
**URN:** 2581358  
**Course:** Version Control System (CSE25303) — Assignment 2

A small Python CampusNotes demo used to practice remote repositories, branches, pull requests, review workflow, conventional commits, release tags, and Git hooks.

## Run
```bash
python3 campusnotes.py
```

## Configure Git hooks
```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit .githooks/commit-msg
```
Hooks reject staged TODO/FIXME markers and enforce Conventional Commit-style messages. Git hooks are local and are not automatically transferred by pushes; sharing scripts in this repository and setting `core.hooksPath` is the team setup.

See `docs/assignment-guide.md` for the assignment steps and evidence checklist.
