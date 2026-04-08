# Agent Prompts Used During This Run

These are the working prompts applied while completing this repository task:

1. Inspect the repository before editing anything so inherited upstream files are not overwritten blindly.
2. Keep one authoritative documentation location under `docs/` and remove stale duplicates when they would create drift.
3. Treat the BDD suite as a contract test layer for principal user flows, not as fake device integration.
4. Prefer maintainable GitHub Actions primitives over custom shell installs when an official action exists.
5. Do not revert unrelated user changes; work around them unless they directly block the requested task.
6. Verify locally after edits so the committed workflow configuration matches a passing repository state.
