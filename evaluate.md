Analyze the Claude Code session logs for a completed subagent vs agent team comparison and generate a comparison table.

## What to do

1. Find the JSONL session logs in `~/.claude/projects/`. Match the project directory to each run by looking for paths containing the task directory name (e.g. `task-1-team` for the agent team, and the parent repo path for the subagent).

2. For each JSONL file, parse assistant messages that contain `usage` data. Extract per-turn:
   - `input_tokens`
   - `cache_creation_input_tokens`
   - `cache_read_input_tokens`
   - `output_tokens`
   - `timestamp`
   - `model`

3. Compute these metrics for each run:

   **Active compute time**: Sum the gaps between consecutive message timestamps within each session, excluding gaps > 120 seconds (those are idle/user time). For agent teams, sum across all sessions (orchestrator + sub-agents). Compare against the system `turn_duration` entry and the conversation transcript's "Cooked for" / "Baked for" time as sanity checks — the gap method tends to overcount by 10–20% because it includes short tool-execution waits the system doesn't count as model compute.

   **Wall-clock time**: First timestamp to last timestamp across all sessions in the run.

   **Orchestration overhead**: Wall-clock time minus active compute time.

   **Sessions**: Number of JSONL files with at least 1 assistant turn.

   **API turns**: Total unique `requestId` values across all assistant messages (see "JSONL structure" below for why raw message count is wrong).

   **Peak context window**: Max of (input_tokens + cache_creation_input_tokens + cache_read_input_tokens) across all turns. For agent teams, report the largest single session.

   **Compaction events**: Count turns where context size drops >20% from the previous turn.

   **Output tokens**: Estimate from actual content character length (~4 chars/token). Sum text, thinking, and tool_use input JSON across all content blocks per request, then divide by 4. See "JSONL structure" below for why the `output_tokens` usage field cannot be used.

   **Est. unique tokens**: For subagent: peak context + total output. For agent team: sum of peak contexts across sessions (note overlap from shared system prompt, typically ~20k).

4. Write a `comparison.md` in the task directory using this format:

```markdown
# Task N: [3-Word Task Description]

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

*Evaluate the deliverables in `task-N/subagent/` and `task-N/team/` against the criteria in `prompt.txt`. Add rows for each measurable criterion. Include percentages where applicable.*

**Notes**:
- [any notable observations: compaction, parallelism, errors, etc.]
```

## Where to look

- Session logs: `~/.claude/projects/<project-path-with-dashes>/*.jsonl`
- Task prompts: `task-N/subagent/prompt.txt` and `task-N/team/prompt.txt`
- The subagent sessions are typically in a project directory matching the task subdirectory (e.g. `-task-2-subagent`) or the parent repo's project directory
- The agent team orchestrator session is in a project directory named after the team subdirectory
- **Sub-agent session logs** are nested inside the orchestrator's session directory at `<session-id>/subagents/agent-<agent-id>.jsonl` — they are NOT in separate project directories. List the `<session-id>/subagents/` directory to find them.

## JSONL structure

The JSONL format has several gotchas that differ from what you might expect:

### Streaming chunks, not complete responses

Each API call produces **multiple** assistant entries in the JSONL — one per content block (thinking, text, tool_use). These are streaming chunks, not complete responses. To get per-API-call data:

- **Group by `requestId`** — all chunks from the same API call share a `requestId`.
- **API turn count** = number of unique `requestId` values, NOT the number of assistant entries.
- For usage data (context size), take the chunk with the highest context size per `requestId`.

### Output tokens are unreliable

The `output_tokens` field in the `usage` object reflects streaming chunk counts, not cumulative totals. Most chunks report `output_tokens: 0` or single-digit values. A session that builds a 400-line app may report only ~700 total output tokens via usage fields.

**Do not use `usage.output_tokens`.** Instead, estimate output tokens from actual content:
- For `text` blocks: `len(text)`
- For `thinking` blocks: `len(thinking)`
- For `tool_use` blocks: `len(json.dumps(input))`
- Sum character counts per `requestId`, then across all requests. Divide total by 4 for approximate token count.

### System entries

Look for entries with `type: "system"` and `subtype: "turn_duration"` — these contain `durationMs`, the system's own measurement of active compute time. Use this as a sanity check against the gap-based method.

## Important

- The subagent run is usually a single large JSONL file. The agent team will have the orchestrator JSONL plus sub-agent JSONLs in the `<session-id>/subagents/` subdirectory.
- Cache read tokens dominate total counts but are re-reads of the same context each turn — do NOT sum them as "total tokens."
- If a conversation was compacted, context size will drop sharply mid-run. Account for this when estimating unique tokens.
- For agent teams, the orchestrator's gap-based active compute may look low because it spends long stretches (>120s) waiting for sub-agents. Sum the gap-based times across ALL sessions (orchestrator + each sub-agent) for the total active compute figure.
