# Assignment 2 — evidence and workflow guide

Student: Vishnu Singh  
URN: 2581358  
Repository: https://github.com/vishnuu01/vishnu-2581358vcs

## Q1 — Remote repository workflow
```bash
git remote add origin https://github.com/vishnuu01/vishnu-2581358vcs.git
git push -u origin main
git remote -v
git clone https://github.com/vishnuu01/vishnu-2581358vcs.git CampusNotes-clone
cd CampusNotes-clone
git pull
```
Record screenshots of remote configuration, push, clone, and pull with actual terminal output.

## Q2 — Fork, feature branch, and pull request
This requires a partner's repository and a genuine fork. After the partner supplies their repository:
1. Fork it using GitHub's Fork button.
2. Clone the fork and add the partner's original repository as upstream.
3. Create `feature/vishnu-improvement`, make a meaningful change, commit and push.
4. Open a pull request from the fork branch to the partner's repository and link a related issue.
Evidence: actual PR link and screenshots of its description and branch details.

## Q3 — Code review and merge
This task depends on a genuine partner PR. Leave at least three constructive inline comments and one suggested change. The partner should reply; then approve or request changes. Push an update and, as PR owner, merge with a documented strategy. Capture actual review, reply and merge links/screenshots. Do not fabricate partner activity.

## Q4 — Commit conventions, tags and release
Use five Conventional Commit messages, e.g. `feat: add note display`, `fix: correct note numbering`, `docs: describe remote setup`, `refactor: simplify output loop`, `chore: add ignore rules`.
Create tags:
```bash
git tag -a v0.1.0 -m "CampusNotes first milestone"
git tag -a v1.0.0 -m "CampusNotes 1.0.0"
git push origin main --tags
git tag -n
git log --oneline
```
Then publish a GitHub Release for tag v1.0.0 with brief release notes.

## Q5 — Hooks
Configure tracked hooks:
```bash
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit .githooks/commit-msg
```
Pre-commit rejects additions containing TODO or FIXME. Commit-msg requires a Conventional Commit prefix and a message longer than 10 characters. Test each with one blocked and one successful commit and capture terminal evidence.

### Hook sharing and bypass analysis
Git does not transmit local hooks in `.git/hooks` when a repository is cloned or pushed. Tracking scripts in `.githooks` makes them shareable, but each contributor must configure `core.hooksPath` and ensure scripts are executable. Hooks can be bypassed with `git commit --no-verify`, so they are a convenience guard, not a security boundary. CI checks and server-side policies are stronger enforcement.

## Evidence checklist
- [ ] Q1 remote, push, clone and pull screenshots
- [ ] Q2 partner fork and PR link/screenshots
- [ ] Q3 genuine inline review, reply, decision, merge link/screenshots
- [ ] Q4 five commits, tag outputs and published release link
- [ ] Q5 both hooks blocked and successful runs
