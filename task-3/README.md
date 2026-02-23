# Task 3: Landing Page Build

**Task**: Design and build a landing page for "AI Builder Academy" using FastHTML, custom CSS, and uv — with brand guidelines, waitlist CTA embed, and responsive layout.

**Model**: claude-sonnet-4-6 (Claude Max)

| Metric | Subagent | Agent Team |
|---|---|---|
| **Run time** | 6.3 min | 21.1 min |
| **Total compute time** | 9.3 min | 22.2 min |
| Sessions | 3 | 6 |
| API turns | 47 | 120 |
| Peak context window | 77,598 | 54,745 (largest session) |
| Compaction events | 0 | 0 |
| Output tokens | ~32,500 | ~26,100 |
| **Est. unique tokens** | **~110k** | **~218k** |

### Task Performance

| Criterion | Subagent | Agent Team |
|---|---|---|
| Runs (`uv run python main.py`) | ✓ | ✓ |
| Brand compliance (colors + fonts) | ✓ All 6 colors via CSS vars, Manrope/Libre Franklin | ✓ All 6 colors in CSS file, Manrope/Libre Franklin |
| Waitlist CTA (Kit embed) | ✓ `NotStr()` with fa5023cefd | ✓ `NotStr()` with fa5023cefd |
| Total code | 1,166 lines (single main.py with inline CSS) | 851 lines (293 main.py + 558 style.css) |
| Architecture | All-in-one file | Separate CSS file (better separation) |
| Sections | 10 (hero, stats, problem, benefits, curriculum, instructor, testimonials, waitlist, FAQ, footer) | 9 (hero, social proof, problem, who it's for, curriculum, instructor, testimonials, waitlist, footer) |
| Hero design | Code card visual with syntax highlighting, gradient background effects | Clean centered text, CTA button |
| CSS approach | CSS variables, surface color system, gradients, hover animations | Direct color values, clean borders, simpler transitions |

**Notes**:
- Subagent implementation has better design, but agent team has better copy