Analyze the Claude Code session logs for a completed subagent vs agent team comparison and generate a comparison table.

## What to do

1. Find the JSONL session logs in `~/.claude/projects/`. Match the project directory to each run by looking for paths containing the task directory name (e.g. `task-1-agent-team` for the agent team, and the parent repo path for the subagent).

2. For each JSONL file, parse assistant messages that contain `usage` data. Extract per-turn:
   - `input_tokens`
   - `cache_creation_input_tokens`
   - `cache_read_input_tokens`
   - `output_tokens`
   - `timestamp`
   - `model`

3. Compute these metrics for each run:

   **Active compute time**: Sum the gaps between consecutive message timestamps within each session, excluding gaps > 120 seconds (those are idle/user time). This should closely match Claude's "Cooked for" time.

   **Wall-clock time**: First timestamp to last timestamp across all sessions in the run.

   **Orchestration overhead**: Wall-clock time minus active compute time.

   **Sessions**: Number of JSONL files with at least 1 assistant turn.

   **API turns**: Total assistant messages with usage data.

   **Peak context window**: Max of (input_tokens + cache_creation_input_tokens + cache_read_input_tokens) across all turns. For agent teams, report the largest single session.

   **Compaction events**: Count turns where context size drops >20% from the previous turn.

   **Output tokens**: Sum of output_tokens across all turns and sessions.

   **Est. unique tokens**: For subagent: peak context + post-compaction context growth + total output. For agent team: sum of peak contexts across sessions (note overlap from shared system prompt).

4. Write a `comparison.md` in the task directory using this format:

```markdown
# Task N: Subagent vs Agent Team Comparison

**Task**: [one-line description from prompt.txt]

**Model**: [model name from session logs] ([billing type])

| Metric | Subagent | Agent Team |
|---|---|---|
| **Active compute time** | X min | X min |
| **Wall-clock time** | X min | X min |
| Orchestration overhead | X min | X min |
| Sessions | X | X |
| API turns | X | X |
| Peak context window | X | X (largest session) |
| Compaction events | X | X |
| Output tokens | X | X |
| **Est. unique tokens** | **~Xk** | **~Xk** |

### Task Performance

| Metric | Subagent | Agent Team |
|---|---|---|
| [task-specific metric 1] | X | X |
| [task-specific metric 2] | X | X |
| [task-specific metric 3] | X | X |

*Evaluate the deliverables in `task-N/subagent/` and `task-N/agent-team/` against the criteria in `prompt.txt`. Add rows for each measurable criterion. Include percentages where applicable.*

**Notes**:
- [any notable observations: compaction, parallelism, errors, etc.]
```

## Where to look

- Session logs: `~/.claude/projects/<project-path-with-dashes>/*.jsonl`
- Task prompts: `task-N/subagent/prompt.txt` and `task-N/agent-team/prompt.txt`
- The subagent sessions are typically in the parent repo's project directory
- The agent team sessions are in a separate project directory named after the agent-team subdirectory

## Important

- The subagent run is usually a single large JSONL file. The agent team will have multiple.
- Cache read tokens dominate total counts but are re-reads of the same context each turn — do NOT sum them as "total tokens."
- If a conversation was compacted, context size will drop sharply mid-run. Account for this when estimating unique tokens.
