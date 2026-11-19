---
name: sk-book-notes
description: Turns a book into one clearly explained notes file in the book's own terms, with review prompts that make it last in memory. Use whenever the user mentions a book by title or author, shares a book's text, chapters or highlights, or asks for notes, a summary or the key ideas of a book.
---

# Book notes

The notes present the book: its whole, its parts, its terms, its claims and its reasons, each stated as directly as the book states it and explained clearly enough that someone who has not read the book understands it. Every line is **grounded** in the book. Nothing in the notes is about the book; everything in them is the book.

If the book came up in passing inside another task, finish that task and offer the notes in one line. Start on the notes when the book is the subject or the user asks for them.

## 1. Fix the book and the source

Pin the exact title, author and year. If the title could be two books, ask which.

Then settle the **source**, which decides what the notes may contain:

- **Text provided** (a file, pasted chapters, highlights): read all of it before writing anything. A long file is read in ranges until every page is covered. The notes cover what was provided; if it is a part of the book, the header says which part.
- **No text**: write from what you know of the book. If you cannot state the book's unity, its major parts and its main claims with confidence, say what you can state and ask for the text or highlights. Gaps stay gaps.

Quote only from text you have in front of you. Give chapter or page locations only when you are certain of them.

Done when: title, author, year and source are fixed.

## 2. Read for understanding

Work through these in order. Each one is the base for the next.

1. **Kind**: practical (it tells the reader what to do) or theoretical (it tells what is the case), and the subject.
2. **Unity**: the whole book in two to four sentences. Test it: every major part of the book fits under it.
3. **Parts**: the book's major divisions and the job each does for the whole. These follow the book's argument, which is often coarser than its chapters.
4. **Questions**: the questions the book sets out to answer.
5. **Terms**: the words the argument turns on, each pinned to the meaning the book gives it. Ordinary words used in a special sense count most.
6. **Claims**: the book's central propositions, each with the reasons and evidence the book gives for it, and the book's own example of it. For a practical book, also the prescriptions: what the book tells the reader to do, in the book's order.
7. **Answers**: how the book answers each question from item 4, including the questions the book itself says remain open.

Then test understanding in plain words: explain each claim simply, using no technical word beyond the book's defined terms. A claim that resists plain explanation marks a gap in understanding; go back to the text or your knowledge of it and close the gap before writing.

Done when: every item above is answered, every part has its claims, every claim has its reasons, and every term the claims use is defined.

## 3. Write the file

One Markdown file per book. Use the folder the user has named for notes; otherwise `~/book-notes/<Title> (<Author>).md`. If the file already exists, update it in place. Where no file tools exist, give the same content inline.

### A linear read

The file reads top to bottom, once, like the book told clearly and briefly in its own voice. Four rules make it linear:

- **The book's order.** The parts come in the book's order, and the ideas within a part in the order the book builds them, so each idea rests only on what came before it.
- **Define once, at first use.** Each term is set in bold, with its meaning in plain words, the first time the notes need it. After that it is used without being defined again.
- **Say each thing once.** Each explanation, list, set of rules and sequence of steps appears in one place, where the book explains it. A later idea that depends on it names it in words ("the four questions") and moves on.
- **Connect in prose.** Where the book ties an idea to an earlier one, say so in the idea's opening words: "The second stage builds on this structure." The headings are the outline, so the reader always knows where they are.

The shape:

```markdown
# <Title>
<Author>, <year> · <kind and subject> · Source: <full text | chapters or highlights provided: which | written from knowledge of the book>

<The unity: two to four sentences.>

## <First part of the book>
<The question this part answers, in a sentence or two.>

### <An idea, titled as a claim in a short sentence>
<The claim explained in plain words; the book's reasons, step by step; the book's own example; at most one short exact quote, with its location when known.>

### <The next idea>

## <Next part of the book>
<The question this part answers, and how it follows from the part before.>

## Review
<See step 4.>
```

Each idea is **atomic**: one claim, the whole claim. Merge closely related claims so the file holds at most 25 ideas; most books need 8 to 20.

### The form

Give each piece of the book the form that carries it best, inside the idea it belongs to:

- **Prose** for claims and their reasons, examples and conditions: everything that needs "because".
- **A diagram** (Mermaid, drawn top to bottom) for structure: a sequence, a hierarchy or branching, a cycle, levels, cause and effect.
- **A table** for a comparison: several things described by the same attributes.
- **A numbered list** for steps or rules the book gives in order, each with its explanation.

Two rules govern diagrams and tables. **Draw only what the book states**: its own divisions, orders and relations, never a link or grouping the book does not make. **Replace, never repeat**: a diagram or table takes the place of the prose that would describe the same structure, the prose around it keeps only what the picture cannot carry, and a term the picture defines is defined there.

The notes are read on phones and e-ink screens, so pictures stay small and plain: black and white, at most about seven boxes and three side by side, labels of a few words broken over short lines, tables of at most three columns with short cells.

### The voice

- **The book speaks.** State each claim as the book makes it, in the present tense: "Attention is the scarce resource." Attribute only to separate the book's position from a view it reports or rejects: "The book rejects the view that talent is fixed."
- **The book's terms.** Keep the book's vocabulary, exactly as the book uses it.
- **Clearly explained.** Short sentences, common words, one idea per sentence, enough that a reader new to the book follows each idea.

What a reader needs is the book itself, so these stay out of the notes:

- evaluation of any kind: praise, criticism, agreement, verdicts on how well an argument works;
- interpretation that goes past what the text says;
- outside material: the author's life, the book's reception, later research, other books;
- advice to the reader beyond what the book itself prescribes;
- retelling in page order, chapter by chapter;
- framing talk about the notes themselves, hedges and filler.

Done when: every claim from step 2 is in an idea, every structure the book states is in the form that carries it best, every term is defined at its first use and nowhere else, and every explanation appears once.

## 4. Write the review prompts

The last section of the file, **Review**, is built for **retrieval**: recalling an idea from memory, at spaced intervals, is what makes it last. It is the one place that repeats on purpose, because it tests the reader on everything above. Group the prompts under the part names, in order, with two to four prompts per idea, plus prompts for the unity and for each bold term.

Format: one prompt per line, `question :: answer`, which imports into common flashcard tools as one deck per book.

A good prompt:

- asks for one thing, with one short correct answer;
- makes the answer recalled from memory, never readable from the question's wording;
- asks why and how as often as what: why the book holds a claim, how two claims connect, which idea the book's example shows;
- breaks a list into one prompt per item, each giving the item's place or cue;
- uses the book's terms exactly as the notes do;
- asks for a fact or a reason, so the answer is never a bare yes or no.

Open the section with these lines:

```markdown
Before reading the notes, recall from memory: the book in brief, its parts, its terms. Then answer each prompt before revealing the answer.
Review again after 1 day, 3 days, 1 week, 2 weeks, 1 month, then every few months. Rewrite a prompt missed twice; retire one answered easily three times in a row.
```

Done when: every idea and every bold term has prompts, and every answer can be checked against the file.

## 5. Check and hand over

Read the whole file once, top to bottom, against these questions, fixing as you go:

- Is every line grounded in the book?
- Does it read straight through, with nothing used before it is explained?
- Outside the Review, is each thing said once, with no diagram or table repeating its prose?
- Does every diagram and table show only what the book states?
- Is every quote from text you have, and every location certain?

Then pass the file to the sk-reading-pdf skill, which makes one PDF of it for reading on any device.

Reply with the file path, the PDF path and the book in brief. The notes speak for themselves.
