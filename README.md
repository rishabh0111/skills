# skills

Small, sharp skills for thinking, writing and research, for Claude Code and any agent that reads `SKILL.md` folders.

```
/plugin install skills-core --marketplace rishabh0111/skills
```

Needs Claude Code 2.1.275 or later. Every skill starts with `sk-`, so none clash with built-in commands or other plugins.

<!-- skills:start -->
## Not sure which?

| Skill | Say this | You get |
|---|---|---|
| `/sk-ask` | "which skill helps me plan a talk?" | The skill to run next, and why |

## Think

| Skill | Say this | You get |
|---|---|---|
| `/sk-stress-test` | "stress-test my plan to move billing to Stripe" | Every open decision in rounds, each with a recommended answer |
| `/sk-brainstorming` | "I want to build something for my running club" | Questions until the real want is clear, then a written design |
| `sk-discover-intent` | applies on its own when a request is vague | The goal behind the ask, before any work starts |
| `sk-decision-rounds` | applies on its own when decisions are open | The engine behind stress-test: one round of numbered questions at a time |
| `/sk-questionnaire` | "turn this decision into questions for the finance team" | A questionnaire someone else can fill in |

## Write and research

| Skill | Say this | You get |
|---|---|---|
| `sk-research` | "find out what the EU AI Act requires for chatbots" | A cited answer from primary sources, saved to a file |
| `sk-writing` | "proofread this cover letter", or on its own when you write or edit prose | Plain, clear text without machine-sounding tells, or a list of grammar, logic and flow fixes |
| `/sk-explain-plainly` | "wait, explain that again" | The last answer in plain words |
| `/sk-resume` | "tailor my résumé to this job posting" | A scored review with the top fixes, or a tailored résumé with a gap analysis |

## Work with agents

| Skill | Say this | You get |
|---|---|---|
| `/sk-handoff` | "hand this off, the next session will write the tests" | A handoff document a fresh agent can pick up |
| `/sk-teach` | "teach me Kubernetes over the next few weeks" | A teaching workspace with lessons and practice across sessions |
| `sk-writing-for-agents` | applies on its own when you edit a skill or CLAUDE.md | Rules for writing documents an agent reads well |
| `/sk-build-skill` | "make a skill for our release checklist" | A new skill, tested against subagents before you rely on it |
<!-- skills:end -->

## Part of a set

- [software-factory](https://rishabh0111.github.io/software-factory/): from idea to shipped change. Installs these skills with itself.
- [agent-factory](https://rishabh0111.github.io/agent-factory/): specialists for sales, support, finance, legal, HR and more.

## Licence

Each skill's licence file sits beside its content.
