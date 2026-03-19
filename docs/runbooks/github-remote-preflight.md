# GitHub Remote Preflight

Use this checklist before adding a GitHub remote and pushing the repository.

## What should already be true

- The repository has a root [README.md](../../README.md) and [AGENTS.md](../../AGENTS.md).
- The docs index in [../README.md](../README.md) reflects the current repository layout.
- Repo-local skills and validation tests pass.
- Ignore rules in [../../.gitignore](../../.gitignore) cover local cache and editor files.

## Local checks

1. Run `python -m unittest discover -s tests -p "test_*.py" -v`.
2. Review `git status --short` and make sure only intended files are staged or committed.
3. Confirm there are no secrets, tokens, or machine-specific files in the diff.
4. Ensure the default branch is `main` before the first push.
5. Make the initial local commit before adding the remote.

## When the GitHub URL is available

1. Add the remote:

```powershell
git remote add origin <repo-url>
```

2. Verify it:

```powershell
git remote -v
```

3. Push the current branch and set upstream:

```powershell
git push -u origin main
```

## Post-push checks

- Confirm the README renders correctly on GitHub.
- Confirm the workflow file appears under Actions.
- Confirm no ignored local cache files were uploaded.
