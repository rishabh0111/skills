---
name: sk-ask
description: Ask which general skill fits: thinking, writing, research, learning or skill building.
disable-model-invocation: true
---

# Ask

Answer with the skill to run next and why. Every skill, with its one-line purpose and whether it runs on its own, is in [catalog.md](catalog.md). Before you say what a skill does, read its `SKILL.md`.

## Thinking something through

- **A plan or decision to pressure-test:** `/sk-stress-test`. It asks every open question in rounds, each with a recommended answer.
- **An idea that is still fuzzy:** `/sk-brainstorming`. It finds out what is actually wanted, then writes the design.
- **A decision that needs someone else's input:** `/sk-questionnaire` writes them a questionnaire, aimed at what you don't know.
- `sk-decision-rounds` (the interview engine) and `sk-discover-intent` (finding the goal behind a vague ask) apply on their own.

## Finding out and writing it down

- **A question that needs primary sources:** `sk-research` applies on its own, or ask for it by name. It leaves a cited file.
- **Prose a person will read:** `sk-writing` applies on its own. It writes plainly and removes the tells of machine-written text.
- **An explanation that didn't land:** `/sk-explain-plainly`.

## Working across sessions and agents

- **Moving the work to a fresh agent, another folder or a colleague:** `/sk-handoff`.
- **Learning a subject over several sessions:** `/sk-teach`.

## Building skills

- **A new skill:** `/sk-build-skill` writes it and tests it against subagents.
- **Editing any skill or CLAUDE.md:** `sk-writing-for-agents` applies on its own.

## Elsewhere

- **Building or changing software:** `/sf-ask`, from software-factory.
- **Company work** (sales, support, finance, legal, HR, marketing and more): `/af-ask`, from agent-factory.

When one of these isn't installed, give its install line: `/plugin install sf-core --marketplace rishabh0111/software-factory`, or `/plugin install af-core --marketplace rishabh0111/agent-factory`.

## Reply

- **Run:** the skill, with what to say.
- **Why:** one line.
