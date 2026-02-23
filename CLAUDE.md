# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repo benchmarks Claude Code's **subagent** approach (single session using the Task tool) against **agent teams** (experimental multi-session feature with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`) on identical tasks. The goal is to compare token usage, compute time, and task quality.

## Repository Structure

- `task-N/subagent/` — prompt and deliverables for the subagent run (single Claude Code session)
- `task-N/team/` — prompt and deliverables for the agent team run (multi-session); includes `.claude/settings.local.json` to enable agent teams
- `task-N/README.md` — evaluation results comparing both approaches
- `evaluate.md` — instructions for analyzing JSONL session logs and generating comparison tables

## Workflow

Each task follows the same pattern:

1. **Run subagent**: Open Claude Code in the repo root, paste `task-N/subagent/prompt.txt`. The subagent prompt tells Claude to complete the task itself (using subagents/Task tool as it sees fit).
2. **Run agent team**: Open Claude Code inside `task-N/team/`, paste `task-N/team/prompt.txt`. The agent team prompt instructs Claude to delegate via agent teams rather than working alone. The `settings.local.json` in that directory enables the experimental agent teams feature.
3. **Evaluate**: Use `evaluate.md` to parse JSONL session logs from `~/.claude/projects/` and produce `task-N/README.md`.

## Evaluation Details

Session logs live in `~/.claude/projects/<project-path-with-dashes>/*.jsonl`. Key metrics extracted from logs:

- **Active compute time**: sum of inter-message gaps, excluding gaps > 120s
- **Peak context window**: max of (input_tokens + cache_creation + cache_read) per turn
- **Compaction events**: turns where context drops > 20% from previous turn
- **Est. unique tokens**: accounts for compaction and cross-session overlap

Cache read tokens are re-reads of the same context — they must not be summed as "total tokens."

## Notes

- Subagent runs produce a single large JSONL file; agent team runs produce multiple
- The subagent prompt says "decide for yourself how to accomplish it"; the agent team prompt says "create an agent team, do not do it alone"
- Task 1 is complete (lead list building). Tasks 2 and 3 have directory scaffolding but no prompts yet
