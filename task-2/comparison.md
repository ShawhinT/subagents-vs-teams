
# Task 2: YouTube Course Creator

**Task**: Build a "YouTube Course Creator" web app where users paste a playlist URL and get a distraction-free course page with progress tracking and per-lesson notes.

**Model**: Claude Sonnet 4.6 (Claude Max)

| Metric | Subagent | Agent Team |
|---|---|---|
| **Active compute time** | 13.4 min | 10.9 min |
| **Wall-clock time** | 15.9 min | 17.4 min |
| Orchestration overhead | 2.5 min | 6.5 min |
| Sessions | 1 | 4 (orchestrator + 3 agents) |
| API turns | 44 | 52 (19 + 3 + 3 + 27) |
| Peak context window | 78k | 68k (largest session) |
| Compaction events | 0 | 0 |
| Output tokens | ~21k | ~32k |
| **Est. unique tokens** | **~99k** | **~111k** |

### Task Performance

| Metric | Subagent | Agent Team |
|---|---|---|
| Runs without errors | Yes | Yes |
| Playlist fetch + display | Yes (21 videos) | Yes (21 videos) |
| Notes auto-save persists | Yes | Yes |
| Playlist cache works | Yes | Yes |
| Files produced | 3 (main.py, pyproject.toml, README.md) | 5 (main.py, extractor.py, pyproject.toml, README.md, data.db) |
| Total app code lines | ~416 | ~447 (main.py: 363 + extractor.py: 83) |

### Notes

- **Subagent** worked sequentially in a single session: init project, write the full app, test with curl, fix issues, verify all 6 criteria with an automated end-to-end test. Used raw SQL via fastlite for database operations. Dark-themed UI. Produced a clean, self-contained single-file app.
- **Agent team** split work across 3 agents: Agent 1 (project setup + extractor.py), Agent 2 (main.py with all routes/UI), Agent 3 (testing + bug fixes). However, the agents worked sequentially.
- Agent team UI has strange color combination and side bar text gets cut off. It also doesnt have a progress bar. However, team implementation puts new line between lesson title and duration which is aesthetically more appealing.
