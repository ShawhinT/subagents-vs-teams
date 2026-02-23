# Subagents vs Agent Teams

Benchmarking Claude Code's **subagent** approach (single session using the Task tool) against **agent teams** (multi-session via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`) on identical tasks. Compares token usage, compute time, and output quality.

## Results

**Model**: Claude Sonnet 4.6 (Claude Max)

| Task | Metric | Subagent | Agent Team |
|---|---|---|---|
| **Task 1: Lead List** | Run time | 32.6 min | 24.4 min |
| | Est. unique tokens | ~232k | ~265k |
| | Output quality | 50/50 emails | 6/50 emails |
| **Task 2: Web App** | Run time | 13.4 min | 10.9 min |
| | Est. unique tokens | ~99k | ~111k |
| | Output quality | Better design and features | Worse design, no progress bar|
| **Task 3: Landing Page** | Run time | 6.3 min | 21.1 min |
| | Est. unique tokens | ~110k | ~218k |
| | Output quality | Better design | Better copy|

## How to Run

Each task follows the same pattern:

1. **Subagent run** — Open Claude Code in `task-N/subagent/` and paste `prompt.txt`. Claude completes the task in a single session, using the Task tool as it sees fit.
2. **Agent team run** — Open Claude Code in `task-N/team/` and paste `prompt.txt`. The `settings.local.json` in that directory enables the experimental agent teams feature.
3. **Evaluate** — Use `evaluate.md` to parse JSONL session logs from `~/.claude/projects/` and produce `task-N/comparison.md`.

## Structure

- `task-N/subagent/` — prompt and deliverables for the subagent run
- `task-N/team/` — prompt and deliverables for the agent team run
- `task-N/comparison.md` — per-task evaluation
- `evaluate.md` — instructions for log analysis
