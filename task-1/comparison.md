# Task 1: Subagent vs Agent Team Comparison

**Task**: Build a lead list of 50 contacts at technology/software companies in Dallas, TX.

**Model**: Claude Sonnet 4.6 (Claude Max)

### Technical Performance

| Metric | Subagent | Agent Team |
|---|---|---|
| **Active compute time** | 36.8 min | 21.0 min |
| **Wall-clock time** | ~37 min | 42.1 min |
| Orchestration overhead | ~1 min | 21.1 min |
| Sessions | 1 | 7 |
| API turns | 201 | 197 |
| Peak context window | 166,653 | 74,608 (largest session) |
| Compaction events | 1 (at turn 184) | 0 |
| Output tokens | 10,249 | 4,323 |
| **Est. unique tokens** | **~232k** | **~265k** |

### Task Performance

| Metric | Subagent | Agent Team |
|---|---|---|
| Contacts | 50 | 50 |
| Unique companies | 27 | 30 |
| Emails found | 50 (100%) | 8 (16%) |
| PE-backed companies | 19 (70%) | 20 (67%) |
| Midsized companies (200–5000 emp) | 19 (70%) | 18 (60%) |

**Notes**:
- Subagent ran as a single session and hit the context limit, triggering conversation compaction mid-run. This contributed to its high cache read token count.
- Agent team created 3 parallel agents for research, then consolidated results in follow-up sessions (7 total).
- Agent team only returned 