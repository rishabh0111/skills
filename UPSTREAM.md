# Upstream sources

This file records where each skill in this repo came from: the upstream repo, the commit we copied, and the path in that repo. Use it to find what changed upstream since we copied, then port the fixes you want by hand. Kinds: **as-is** keeps the upstream text under our `sk-` prefix; **renamed** takes one upstream source under a new name; **merged** combines several sources into one skill, so upstream changes have to be applied by intent. A row with several upstream repos prefixes each path with its repo name (`repo:path`). `sk-ask` follows the shape of mattpocock's `ask-matt` with our own catalogue. Run `scripts/upstream-diff.sh <path-to-upstream-clone>` to list upstream commits touching each row's paths.

## Upstream repos

| Name | URL | Commit copied | Licence |
|---|---|---|---|
| mattpocock-skills | https://github.com/mattpocock/skills | `5beb35b040e3de97e54fa9e386d7e42d15c295c2` | MIT |
| superpowers | https://github.com/obra/superpowers | `b739a8af570e10a95898f2bdf6cec97467fa6c12` | MIT |
| agent-skills | https://github.com/addyosmani/agent-skills | `aeac41d4d005999432bb7312f7ff06383a91d59d` | MIT |
| humanizer | https://github.com/blader/humanizer | `8c307f367c91bd974002f10f2be2965d642c13df` | MIT |
| the-elements-of-style | https://github.com/obra/the-elements-of-style | `05fc4f0d2b97b7c042dd9949ad658568e4a1324e` | Public domain |
| pm-skills | https://github.com/phuryn/pm-skills | `07b34f64ee828df08953f505b7f747aef85ae7c6` | MIT |

## Skills

| Ours | Upstream repo | Upstream path(s) | Kind |
|---|---|---|---|
| sk-ask | mattpocock-skills | `skills/engineering/ask-matt` | renamed |
| sk-brainstorming | superpowers | `skills/brainstorming` | as-is |
| sk-build-skill | superpowers | `skills/writing-skills` | renamed |
| sk-decision-rounds | mattpocock-skills | `skills/productivity/grilling` | renamed |
| sk-discover-intent | agent-skills | `skills/interview-me` | renamed |
| sk-explain-plainly | mattpocock-skills | `skills/productivity/wait-what` | renamed |
| sk-handoff | mattpocock-skills | `skills/productivity/handoff` | as-is |
| sk-questionnaire | mattpocock-skills | `skills/productivity/to-questionnaire` | renamed |
| sk-research | mattpocock-skills | `skills/engineering/research` | as-is |
| sk-resume | pm-skills | `pm-toolkit/skills/review-resume` `pm-toolkit/commands/review-resume.md` `pm-toolkit/commands/tailor-resume.md` | merged |
| sk-stress-test | mattpocock-skills | `skills/productivity/grill-me` | renamed |
| sk-teach | mattpocock-skills | `skills/productivity/teach` | as-is |
| sk-writing | humanizer, the-elements-of-style, pm-skills | `humanizer:SKILL.md` `the-elements-of-style:skills/writing-clearly-and-concisely` `pm-skills:pm-toolkit/skills/grammar-check` `pm-skills:pm-toolkit/commands/proofread.md` | merged |
| sk-writing-for-agents | mattpocock-skills | `skills/productivity/writing-for-agents` | as-is |

## How to port an upstream change

1. Clone the upstream repo (or `git pull` an existing clone) and run `scripts/upstream-diff.sh <clone>` from this repo to see which rows have new commits.
2. In the clone, read the change: `git diff <sha>..main -- <path>`, with the commit and path from the tables above.
3. For an as-is or renamed row, apply the diff to our copy, keeping our names, cross-references and tool rewrites.
4. For a merged row, read the change and apply its intent by hand to the part of our skill that came from that source.
5. Once ported, update the commit in the repo table only if every row from that upstream is now current.
