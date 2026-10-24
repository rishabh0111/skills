# Writing patterns

The full catalogue for [`sk-writing`](SKILL.md). Two kinds of entry:

- **Tells** (§1 to §26): marks of machine-written prose. A language model makes the choice that fits the widest range of readers and subjects; a person chooses for one reader and one subject. Every tell is a form of that default choice. They are numbered strongest first: §1 to §5 justify an edit on one sighting, and a tell marked *weak alone* needs company from other tells in the same passage before you act. Word habits change with every model release; the structural tells persist, so they lead.
- **Rules** (§27 to §43, and the usage list): plain-writing rules. Apply every one to every sentence you write or edit.
- **Proofreading checks** (§44 to §53): grammar, logic, and flow errors the rules leave open. Apply them to every sentence too; a proofread reports them as fixes instead of rewriting.

Where a rule and a tell pull in different directions, the entry states which wins.

## When to leave a tell alone

Each tell is a default choice, and a person can make any one of them on purpose. Leave a watched phrase alone inside a quotation, a title, a proper name, or a passage that discusses the phrase rather than uses it. Salutations and sign-offs on a letter or comment predate chatbots. Text written before November 30, 2022 is not AI-written. People who judge by feel do little better than chance, and human writing keeps absorbing AI habits, so several tells together are the safeguard.

Keep the details that carry the writer's voice unless they hurt the meaning:

- A specific, unusual detail: a real address, an odd quote, "the lawyer who used to work upstairs from my dentist."
- Mixed feelings and unresolved tension: "I think this is mostly good, but it bothers me, and I can't fully explain why."
- Dated, era-bound references: slang, memes, and in-jokes that map to a specific year and subculture.
- A first-person choice the writer can explain.
- A genuine aside, parenthetical, or self-correction: "(I keep wanting to say 'almost' here, but it really was certain.)"

## A. Staging instead of stating

The strongest and most frequent tells in current model prose. Act on one sighting.

### 1. Not X but Y

**Watch for:** not X but Y; not just, not only, or not merely X, but Y; it's not X, it's Y; the reversed form X rather than Y; the same contrast split across sentences ("This does not mean X. It means Y."); a clipped negative tail ("..., no guessing"). The formula appears in every language; treat the equivalent construction the same way.
**Problem:** The negative half names something no one claimed, so the positive half sounds larger. It adds weight without adding a claim. State the point directly. Keep a contrast only when the negative half corrects a belief the reader actually holds, or when both halves carry information. This is the one test for every antithesis, including the deliberate kind in §29.
**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.
**After:**
> The heavy beat adds to the aggressive tone.
**Before (split across sentences):**
> This does not mean every choice is equal. It means there is no external system that confirms which choice is right.
**After:**
> No external system confirms which choice is right, although the choices still have different consequences.
**Before (clipped tail):**
> The options come from the selected item, no guessing.
**After:**
> The options come from the selected item without forcing the user to guess.

### 2. One-line closers and dramatic fragments

**Watch for:** a one-sentence paragraph that restates the paragraph before it; "That is the real win."; "That distinction matters."; "Read that again."; "Let that sink in."; the same closer after several sections; a sentence after an example, scene, or number that names what it showed ("This shows the importance of...", "The message was clear:", "It was a lesson in patience."); a row of fragments ("No aesthetic prior. No nostalgia."); one word in ALL CAPS or with periods between words (every. single. day.).
**Problem:** The line asks the reader to pause on a claim instead of adding to it. Cut a closer that repeats, including one that explains an example the reader just saw. Keep a short sentence or a single fragment when it carries a new fact or consequence the text has not shown; that is the only emphatic fragment §42 allows. Merge a row of fragments into a sentence with a specific claim. Emphasis comes from word order (§36), never from an added closer.
**Before:**
> Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.
**After:**
> AlphaEvolve changed the search because it did not favor symmetry or human-looking designs. That made some of the older assumptions less useful.
**Before (repeated closer):**
> Caching cuts repeat work.
>
> That is the real win.
>
> Retries hide brief outages.
>
> That is the real win.
**After:**
> Caching cuts repeat work.
>
> Retries hide brief outages.

### 3. Sayings that sound deep

**Watch for:** the real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter, X is the Y of Z, X becomes a trap, X is not a tool but a mirror, the language of, the currency of, the architecture of
**Problem:** An ordinary point is dressed as a hidden truth or an aphorism, and the dressing adds no detail. Replace the saying with the specific claim.
**Before:**
> The real question is whether teams can adapt. At its core, what really matters is organizational readiness.
**After:**
> The question is whether teams can adapt. That mostly depends on whether the organization is ready to change its habits.
**Before (aphorism):**
> Symmetry is the language of trust. Efficiency becomes a trap when teams forget the human layer.
**After:**
> Symmetric layouts often feel more predictable to users. Teams can over-optimize workflows and miss how people actually use them.

### 4. Staged run-up before the point

**Watch for:** Let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado, heads up, quick note, Honestly?, Look, Here's the thing, The thing is, Let's be honest, Real talk, and casual versions such as "one thing that bit me, so pay attention"; announcing that what follows is interesting.
**Problem:** The writer announces the point or stages a moment of candor instead of making the point. Remove the run-up, not just its tone. "Honestly" or "look" inside a casual sentence is ordinary; the tell is the standalone opener before a routine claim. Instead of saying a story is interesting, tell it.
**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.
**After:**
> Next.js caches data at multiple layers, including request memoization, the data cache, and the router cache.
**Before (staged candor):**
> Is it worth the price? Honestly? It depends on how often you'll use it.
**After:**
> Whether it's worth the price depends on how often you'll use it.

### 5. Arguing with no one

**Watch for:** This isn't (mainly) about, I'm not saying, To be clear, Don't get me wrong, This is not to say, Some might say... but, A tempting approach would be, One might be tempted to, An obvious approach would be, You might think... but, It would be easy to just
**Problem:** The text answers an objection or rejects an option that appears nowhere else, usually a leftover from an earlier draft. Remove the defense; if it holds a real claim, state the claim. Keep an objection the text attributes or answers in full, and keep an option a reader would actually weigh. Several unrelated rejections in a row are a stronger sign than one.
**Before:**
> This isn't mainly about prompt length, and I'm not arguing that documentation doesn't matter. You could categorize the problem another way, but the issue is whether the agent can use the instruction when it acts.
**After:**
> The issue is whether the agent can use the instruction when it acts.
**Before (fake alternative):**
> Session tokens are rotated every 24 hours. A tempting approach would be to rotate them by restarting the auth service on a cron job, but that would drop every active session. Rotation happens in place, and clients refresh transparently.
**After:**
> Session tokens are rotated every 24 hours, in place, and clients refresh transparently.

## B. Rhythm by rule

Shapes and punctuation applied everywhere, whether or not the meaning asks for them. Parallel form (§33) is the legitimate version of these shapes: it follows the content, where these follow a rhythm.

### 6. Forced triads

**Problem:** Ideas arrive in threes to sound complete, whether the meaning has three parts or not. The tell can be one sentence ("innovation, inspiration, and insights"), three parallel examples, or three short facts followed by a lesson. Check that each item adds a distinct idea. Merge examples, develop the strongest one, or vary the structure when they do not. Keep three real items when the meaning needs three, and give them parallel form (§33).
**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.
**After:**
> The event includes talks and panels. There's also time for informal networking between sessions.
**Before (paragraph scale):**
> A career can look promising and fail. A relationship can feel important and end. A skill can take years and remain useless. These decisions rarely explain themselves.
**After:**
> A career can look promising and fail. So can a relationship that felt important and ended, or a skill that took years and remained useless. These decisions rarely explain themselves.

### 7. Repeated sentence openings

**Problem:** Several sentences in a row start with the same subject, often *she* or *he*, because repetition is handled by rule instead of by ear. Merge the sentences, change the subject, or begin with the action. A remaining sentence may still start with "She." Writers also repeat an opening on purpose when the sentences truly are parallel, as in "She came. She saw. She conquered."
**Before:**
> She noted the door. She noted the lock on it. She filed both away.
**After:**
> She noted the door and its lock, then filed both away.

### 8. Dashes as the universal connector

**Rule:** The final text contains no em dashes (—) or en dashes (–) unless the writer's sample uses them; then match the sample's rate. Replace each dash with a period, comma, colon, semicolon, or parentheses, or rewrite the sentence. This includes spaced dashes and double hyphens (` -- `) used as dashes. Leave dashes and hyphens inside code blocks, inline code, commands, paths, and URLs alone.
**Problem:** A dash lets the writer skip choosing how two clauses relate, so a model reaches for it everywhere. Many editors and journalists also use dashes, so one dash is *weak alone*; a text full of them is not.
**Before:**
> The new policy — announced without warning — affects thousands of workers. The changes -- long overdue according to critics -- will take effect immediately.
**After:**
> The new policy, announced without warning, affects thousands of workers. The changes, long overdue according to critics, will take effect immediately.

### 9. Stacked qualifiers

**Watch for:** to be fair, it's also possible, could potentially, might arguably, in some cases it may, this is an inference
**Problem:** Repeated editing adds one qualifier after another until every claim sounds uncertain, usually to repair an earlier overstatement rather than to report real doubt. Keep a qualifier only when the source supports it and the meaning needs it. Keep scope statements, legal and safety notices, and real corrections. Ordinary hedges such as *perhaps* or *tends to* are human habits and not tells. *Weak alone.* Make definite assertions where the source allows (§29).
**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.
**After:**
> The policy may affect outcomes.

### 10. Hyphenated pairs everywhere

**Watch for:** high-quality, well-known, well-documented, long-term, real-time, client-facing after the noun they describe
**Problem:** Compound modifiers keep their hyphen in every position. Keep the hyphen before a noun, as in `a high-quality report`, and drop it after the noun, as in `the report is high quality`. Words the dictionary always spells with a hyphen, such as third-party and cross-functional, keep it everywhere. *Weak alone.*
**Before:**
> The report is high-quality, the process is well-documented, and the plan is long-term.
**After:**
> The report is high quality, the process is well documented, and the plan is long term.

### 11. Passive voice and missing subjects

**Problem:** The text hides who acts or drops the subject. The active voice is more direct and shorter; use it by default. A passive with the actor dropped leaves the reader asking who did it. *Weak alone* as a tell, but the rule holds in all writing:

- Use the passive when the word that must be the subject is the one acted on: "The dramatists of the Restoration are little esteemed today" belongs in a paragraph about those dramatists; "Modern readers have little esteem for..." belongs in one about readers.
- Do not make one passive depend on another.
- Do not make a noun of the action the subject and leave the verb nothing to do.
- Replace limp openers such as *there is*, *there were*, and *could be heard* with a real verb.

**Before:**
> No configuration file needed. The results are preserved automatically.
**After:**
> You do not need a configuration file. The system preserves the results automatically.

| Before | After |
| --- | --- |
| My first visit to Boston will always be remembered by me. | I shall always remember my first visit to Boston. |
| Gold was not allowed to be exported. | The export of gold was prohibited. |
| He has been proved to have been seen entering the building. | It has been proved that he was seen to enter the building. |
| A survey of this region was made in 1900. | This region was surveyed in 1900. |
| Confirmation of these reports cannot be obtained. | These reports cannot be confirmed. |
| There were a great number of dead leaves lying on the ground. | Dead leaves covered the ground. |
| The reason that he left college was that his health became impaired. | Failing health compelled him to leave college. |

## C. Inflation and borrowed authority

The fact underneath is usually sound. Keep it and remove the dressing.

### 12. Overused AI words

**Watch for:** Actually, additionally, align with, bolstered, crucial, deep dive, delve, enduring, enhance, garner, gate/gated/gating (figurative; keep technical uses), highlight (verb), interplay, intricate/intricacies, key (adjective), landscape (abstract noun), meticulous/meticulously, pivotal, quietly, robust (figurative; keep technical uses), showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant
**Problem:** Models use these words far more often than people do, especially in groups. The watch lists in §13 to §18 hold phrases that are tells because of how they are used; this list holds words that are tells wherever they appear. A formal word outside these lists is not a tell by itself; the usage list covers older overworked words.
**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.
**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.

### 13. Inflated significance

**Watch for:** stands as a testament, a pivotal or crucial moment, plays a key role, marking or shaping the, underscores its importance, reflects a broader, enduring or lasting legacy, setting the stage for, evolving landscape, indelible mark; Despite these challenges... continues to thrive, Challenges and Legacy, Future Outlook, Awards and recognition; the future looks bright, exciting times ahead, a step in the right direction
**Problem:** An ordinary detail is said to mark a change, prove a legacy, or promise a future. The move appears at three scales: a phrase, a stock "challenges and outlook" section, and a send-off paragraph. Keep the fact and drop the significance. End on the last concrete fact; if the source states real plans, use those.
**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.
**After:**
> The Statistical Institute of Catalonia was established in 1989, part of a wider decentralization of administrative functions in Spain.
**Before (stock section):**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.
**After:**
> Korattur has recurring traffic congestion and water shortages.
**Before (send-off):**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence.
**After:**
> (Cut the paragraph. End on the last concrete fact.)

### 14. Vague connection or association

**Watch for:** associated with, in association with, connected to, in connection with, linked to, tied to, along these lines
**Problem:** The text says two things are connected without saying how. "He was associated with the leadership of ExampleCorp" hides whether he was the CEO, a board member, or a consultant. Name the relationship the source gives. If the source does not say, keep the vague wording rather than inventing a role.
**Before:**
> He is associated with the Rajhans Orchestra, which he founded and conducts. The concerts were organised in connection with the celebrations of Pakistan's 50th anniversary.
**After:**
> He founded and conducts the Rajhans Orchestra. The concerts were part of the celebrations of Pakistan's 50th anniversary.

### 15. Shallow -ing riders

**Watch for:** highlighting, underscoring, emphasizing, ensuring, reflecting, symbolizing, contributing to, cultivating, fostering, encompassing, showcasing
**Problem:** An -ing phrase is bolted onto a simple fact to make it sound deeper. Attaching it to a named source ("Roger Ebert highlighted the lasting influence") does not make it true. Keep the fact; keep the rider only when the source supports what it claims.
**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.
**After:**
> The temple is painted blue, green, and gold, colors meant to evoke Texas bluebonnets and the Gulf of Mexico.

### 16. Sales language

**Watch for:** rich (figurative), profound, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, featuring, diverse array, breathtaking, must-visit, stunning
**Problem:** The text reads like an advertisement, especially for places, culture, products, or organizations. State what the thing is.
**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.
**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia.

### 17. Borrowed authority

**Watch for:** experts argue, observers have cited, industry reports, some critics, several publications; cited, featured, or profiled in [a list of outlets], trade publications, independent coverage; active social media presence, over N followers
**Problem:** A name or an unnamed authority stands in for what was said. Unnamed experts prop up a claim; a list of prestige outlets props up a person. When the source text names the real source and what it said, use that. Otherwise cut the unsupported claim or the list. A missing citation alone is not a tell; most writing is unsourced.
**Before (unnamed authority):**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.
**After:**
> Researchers and conservationists study the Haolai River for its unusual characteristics.
**Before (prestige list):**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.
**After:**
> Her views have been cited in The New York Times and the BBC.

### 18. Avoiding is, are, and has

**Watch for:** serves as, stands as, functions as, operates as, marks, represents [a]; boasts, features, offers, maintains, possesses [a]; refers to
**Problem:** Simple verbs are replaced with longer phrases. Use *is*, *are*, and *has*.
**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.
**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

## D. Formatting by rule

Templates and visual editors also produce clean formatting. The tell is decoration on every item.

### 19. Bold as decoration

**Problem:** Words are bolded without a reason, and vertical lists give every item a bold label and a colon. Remove the bold. Turn a labeled list into prose when the labels carry no information of their own.
**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.
**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.
**Before (labeled list):**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.
**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

### 20. Decorative headings

**Problem:** Headings capitalize every main word, and headings or list items carry emojis or arrows (→) as decoration. A horizontal rule sits between every section, or the document opens with a top-level heading that repeats its own title. A heading written for effect ("The decision, on one screen") should name what the section holds ("How the six options compare"). Use sentence case, remove the decoration and the rules, and let the title stand once.
**Before:**
> ## Strategic Negotiations And Global Partnerships
**After:**
> ## Strategic negotiations and global partnerships
**Before (emojis):**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
**After:**
> The product launches in Q3. User research showed a preference for simplicity.

### 21. Curly quotation marks

**Problem:** Curly quotes (“...”) appear where the writer or target format uses straight quotes ("..."). Most editors auto-curl, so this is *weak alone*.
**Before:**
> He said “the project is on track” but others disagreed.
**After:**
> He said "the project is on track" but others disagreed.

## E. Leftovers from the chat and the draft

Remove these outright. Nothing here needs rewriting.

### 22. Chatbot residue

**Watch for:** I hope this helps, Of course!, Certainly!, Great question!, You're absolutely right, Would you like..., Want me to...?, Should I continue?, let me know, here is a..., thanking you in advance
**Problem:** A chatbot's greeting, praise, offer, or closing remains in text that should stand on its own. It is the most certain tell in this list and the easiest to miss when it wraps real content. Remove the wrapper and keep the content.
**Before:**
> Great question! Here is an overview of the French Revolution. It began in 1789 when a financial crisis and food shortages led to widespread unrest. I hope this helps! Let me know if you'd like me to expand on any section.
**After:**
> The French Revolution began in 1789 when a financial crisis and food shortages led to widespread unrest.

### 23. Knowledge-limit disclaimers and guesses

**Watch for:** as of [date], up to my last training update, while specific details are limited, based on available information, not publicly available, not widely documented or disclosed, in the provided or available sources, maintains a low profile, keeps personal details private, likely [grew up, studied, began], it is believed that
**Problem:** The text mentions where the model's knowledge ends, or admits it found no source and then fills the gap with a plausible guess. State what the source does not show, or remove the sentence.
**Before (cutoff disclaimer):**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.
**After:**
> The company's founding date is not documented in the available sources. (Or cut the sentence.)
**Before (guess):**
> Information about her early life is not publicly available, suggesting she maintains a low profile. She likely grew up in a middle-class household, which shaped her later interest in education reform.
**After:**
> Her early life is not documented in the available sources. (Or omit the section.)

### 24. A heading repeated in the first sentence

**Problem:** A heading is followed by a one-line paragraph that restates it before the real content begins. Remove the repeated sentence.
**Before:**
> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.
**After:**
> ## Performance
>
> When users hit a slow page, they leave.

### 25. Writing about the document instead of its subject

**Watch for:** what the text replaced ("was added to replace"); how it was assembled or sourced ("generated from", "compiled from", "anything unconfirmed is flagged rather than guessed"); a legend, layout, or order the reader can already see ("the table below compares", "this section is organized by owner").
**Problem:** The text describes itself instead of its subject. Mention a previous version only in change logs, release notes, migration guides, and other documents about change. Keep a source credit the reader can follow; cut the account of how you worked. Keep a caveat that changes what the reader should do. State a convention only when the reader cannot infer it, and state it once. A single description of the page is *weak alone*.
**Before:**
> This function was added to replace the previous approach of iterating through all items, which caused O(n²) performance.
**After:**
> This function uses a hash map for O(1) lookups, avoiding the O(n²) cost of naive iteration.
**Before (method narration):**
> The figures below are drawn from each vendor's published pricing; anything we could not confirm is flagged rather than guessed.
**After:**
> Prices are each vendor's published rate. Two vendors publish nothing; call them.

## F. Writing for the wrong reader

A model writes for a reader who shares no context, because that fits the widest range of cases. A reply in a thread has a reader who already knows the background. Act on this tell when you can see the surrounding conversation, or when the text plainly is a reply. If you cannot tell, ask or leave the text alone.

### 26. Re-explaining what the reader knows

**Watch for:** a short reply that restates the problem, walks through the diagnosis, and lays out the evidence before it reaches the decision; a query, command, or set of numbers included to prove a plan will work; background the other person wrote or already agreed to; the answer itself sitting in the last line.
**Problem:** In a reply the reader already has the context, so rebuilding it adds nothing and buries the point. Each sentence can read fine on its own, so this survives sentence-level cleanup. Lead with the decision and keep only the reasoning that would change whether the reader agrees: usually one fact they lack and any link they need to act. The diagnosis and the proof that a plan will work belong in the ticket or document that follows; a reviewer raising a topic is not a request for the full write-up.
**Before:**
> Yeah, you're right, this works around the issue rather than fixing it. The real fix is in `MergeService`: when we move a child under a new parent, it should update `pipeline_id` along with `parent_id`. We can backfill the bad rows from the audit log with `Change.where(field: "pipeline_id", source: "merge")`. I checked QA: 123 past merges, only 6 rows wrong now, so the cleanup is small.
>
> Since `MergeService` is shared and not specific to this account, I'd rather open a separate ticket than widen this PR. The fallback here is fine to keep until then.
**After:**
> Agreed, this is a workaround. Fixing it properly in `MergeService` would widen this ticket well past its scope: it is shared code, so it means checking the merge flow for every account, plus a backfill for the rows that are already wrong.
>
> I'd rather keep this PR account specific and open a separate ticket for the `MergeService` fix and the backfill. Let me know if that works.

## G. Composition

Rules for paragraphs and sentences. They apply to all prose, machine-written or not.

### 27. One paragraph per topic

**Rule:** Give each topic its own paragraph; the break tells the reader a new step has begun. A brief subject (a short description, a summary, one incident, one idea) fits in one paragraph; check afterwards whether splitting would help. A single sentence is not a paragraph, except a transition between parts of an argument, or in guides and reference works that treat many topics briefly. In dialogue, each change of speaker starts a new paragraph.

### 28. Topic sentence first

**Rule:** Begin a paragraph with its topic sentence, develop it in the sentences that follow (restate, define, illustrate, prove, or trace consequences), and end on the strongest fact or an important consequence. Never end on a digression or a minor detail. The last sentence carries new weight, not a restatement of the first (§2). Show the paragraph's link to what came before with a word or phrase (*again*, *therefore*, *for the same reason*); if the transition needs more than one sentence, give it its own paragraph. In narrative, an opening that sums up the details to come ("The campaign opened with a series of reverses.") becomes a mannerism if overused; short paragraphs of fast action may have no topic sentence at all.

### 29. Positive form

**Rule:** Make definite assertions. Use *not* to deny or to contrast, never to evade. Say what is, not only what is not; turn a negative into a positive word where one exists. Other negative words (*never*, *no*) are usually strong. A deliberate antithesis ("Not charity, but simple justice.") stands only when its negative half corrects a belief the reader holds (§1).

| Before | After |
| --- | --- |
| He was not very often on time. | He usually came late. |
| He did not think that studying Latin was much use. | He thought the study of Latin useless. |
| not honest | dishonest |
| not important | trifling |
| did not remember | forgot |
| did not pay any attention to | ignored |
| did not have much confidence in | distrusted |

### 30. Definite, specific, concrete language

**Rule:** Prefer the specific to the general, the definite to the vague, the concrete to the abstract. Give the significant details, sharply enough that the reader can picture them; not every detail. In exposition and argument, follow each general principle with an instance of it. An abstract word makes the reader pick an image; a specific one hands it over.

| Before | After |
| --- | --- |
| A period of unfavorable weather set in. | It rained every day for a week. |
| He showed satisfaction as he took possession of his well-earned reward. | He grinned as he pocketed the coin. |
| In proportion as the manners, customs, and amusements of a nation are cruel and barbarous, the regulations of their penal code will be severe. | In proportion as men delight in battles, bull-fights, and combats of gladiators, will they punish by hanging, burning, and the rack. |

### 31. Omit needless words

**Rule:** Make every word tell. This does not mean short sentences or no detail: it means no word, and no sentence, that does no work. Revise *the fact that* out of every sentence. Cut a *who is* or *which was* that adds nothing. Combine a single complex idea told step by step across several sentences into one.

| Before | After |
| --- | --- |
| the question as to whether | whether |
| there is no doubt but that | no doubt |
| used for fuel purposes | used for fuel |
| he is a man who | he |
| in a hasty manner | hastily |
| this is a subject which | this subject |
| His story is a strange one. | His story is strange. |
| owing to the fact that | since |
| in spite of the fact that | although |
| call your attention to the fact that | remind you |
| the fact that he had not succeeded | his failure |
| His brother, who is a member of the same firm | His brother, a member of the same firm |
| Macbeth was very ambitious. This led him to wish to become king of Scotland. The witches told him that this wish of his would come true. The king of Scotland at this time was Duncan. Encouraged by his wife, Macbeth murdered Duncan. He was thus enabled to succeed Duncan as king. | Encouraged by his wife, Macbeth achieved his ambition and realized the prediction of the witches by murdering Duncan and becoming king of Scotland in his place. |

### 32. A run of loose sentences

**Watch for:** a paragraph of two-clause sentences, each joined by *and*, *but*, *so*, *who*, *which*, *when*, *where*, or *while*.
**Rule:** One such sentence is fine; a series is monotonous. Recast enough of them, as simple sentences, sentences joined by a semicolon, or periodic sentences, to match the real relations of the thought.
**Before:**
> The third concert of the series was given last evening, and a large audience was in attendance. Mr. Appleton was the soloist, and the orchestra furnished the instrumental music. The former showed himself to be an artist of the first rank, while the latter proved itself fully deserving of its high reputation.
**After:**
> A large audience heard the third concert of the series last evening. Mr. Appleton, the soloist, proved an artist of the first rank, and the orchestra lived up to its reputation.

### 33. Parallel form for parallel content

**Rule:** Give ideas of the same kind and function the same grammatical form, so the reader sees the likeness. This is the one rule for repeated shapes: use parallel form when the content truly is parallel, and never impose a triad, a repeated opening, or a closer to make content look parallel (§6, §7, §2). Varying the form of truly parallel items for variety's sake reads as indecision.

- An article or preposition that covers a series goes before the first term only, or before every term.
- Correlatives (*both, and*; *not, but*; *not only, but also*; *either, or*; *first, second*) take the same construction after each half.
- Many parallel items: group them and apply the form within each group, or use a table.

| Before | After |
| --- | --- |
| Formerly, science was taught by the textbook method, while now the laboratory method is employed. | Formerly, science was taught by the textbook method; now it is taught by the laboratory method. |
| The French, the Italians, Spanish, and Portuguese | The French, the Italians, the Spanish, and the Portuguese |
| In spring, summer, or in winter | In spring, summer, or winter |
| It was both a long ceremony and very tedious. | The ceremony was both long and tedious. |
| A time not for words, but action. | A time not for words, but for action. |
| Either you must grant his request or incur his ill will. | You must either grant his request or incur his ill will. |
| My objections are, first, the injustice of the measure; second, that it is unconstitutional. | My objections are, first, that the measure is unjust; second, that it is unconstitutional. |

### 34. Keep related words together

**Rule:** Word position shows relationship, so keep related words together and unrelated ones apart.

- Do not separate subject and main verb with a phrase that can move to the front. (A relative clause, an appositive, or deliberate suspense in a periodic sentence may interrupt.)
- Put a relative pronoun right after its antecedent; after a group of words, at the end of the group unless that is ambiguous. An appositive may sit between them.
- Put a modifier next to the word it modifies, and order several modifiers so none suggests a wrong relation.

| Before | After |
| --- | --- |
| Cast iron, when treated in a Bessemer converter, is changed into steel. | By treatment in a Bessemer converter, cast iron is changed into steel. |
| He wrote three articles about his adventures in Spain, which were published in Harper's Magazine. | He published in Harper's Magazine three articles about his adventures in Spain. |
| This is a portrait of Benjamin Harrison, grandson of William Henry Harrison, who became President in 1889. | This is a portrait of Benjamin Harrison, grandson of William Henry Harrison. He became President in 1889. |
| All the members were not present. | Not all the members were present. |
| He only found two mistakes. | He found only two mistakes. |

### 35. One tense in summaries

**Rule:** Summarize a play in the present tense; a story or novel preferably in the present, though the past is allowed. Whichever you choose, hold it: earlier action takes the perfect (with present) or past perfect (with past), and a past tense in indirect speech stays past ("The Friar confesses that it was he who married them."). When summarizing someone else's argument, say once that it is a summary, then drop the repeated "he said", "the author adds". In criticism, write a discussion backed by evidence, not a summary with comments, and aim at general conclusions rather than taking works one by one in order.

### 36. Emphatic words at the end

**Rule:** Put the word or phrase you want most prominent at the end of the sentence: usually the new element. The beginning is the other strong position, for any element except the subject; a subject gains emphasis by position only when moved to the predicate's place ("Through the middle of the valley flowed a winding stream."). The same holds for sentences in a paragraph and paragraphs in a piece: reorder so the new point comes last. Emphasis comes from that order, never from an added closer or fragment (§2).

| Before | After |
| --- | --- |
| Humanity has hardly advanced in fortitude since that time, though it has advanced in many other ways. | Humanity, since that time, has advanced in many other ways, but it has hardly advanced in fortitude. |
| This steel is principally used for making razors, because of its hardness. | Because of its hardness, this steel is principally used in making razors. |

## H. Punctuation and grammar

### 37. Possessive singular

**Rule:** Add *'s* whatever the final consonant: *Charles's friend*, *Burns's poems*. Exceptions: ancient names in *-es* and *-is*, *Jesus'*, and *for conscience' sake*; even these read better as *the laws of Moses*. The possessive pronouns *hers*, *its*, *theirs*, *yours*, *oneself* take no apostrophe.

### 38. Serial comma

**Rule:** In a series of three or more with one conjunction, put a comma after each term but the last: *red, white, and blue*. Company names drop the last comma: *Brown, Shipley & Co.*

### 39. Parenthetic expressions between commas

**Rule:** Enclose a parenthetic expression in a pair of commas, never one; omit both only when the interruption is slight. If a conjunction precedes it, the first comma goes before the conjunction ("He saw us coming, and unaware that we had learned of his treachery, greeted us with a smile."). Always set off: the year in a date (*April 6, 1917.*) and the date after a weekday; *etc.* and *jr.*; and non-restrictive clauses, which add a statement without identifying the noun ("The audience, which had at first been indifferent, became more and more interested."). A restrictive clause, which identifies the noun, takes no commas ("The candidate who best meets these requirements will obtain the place."). Introductory or trailing phrases and dependent clauses are set off the same way.

### 40. Comma before a conjunction joining clauses

**Rule:** Put a comma before *and*, *but*, *as* (meaning *because*), *for*, *or*, *nor*, and *while* (meaning *and at the same time*) when they introduce a second independent clause. When the second clause opens with an adverb, use a semicolon (§41). In formal writing, *so* as a connective reads as colloquial: drop it and open with *as* or *since* ("As I had never been there before, I had difficulty finding my way."). If a dependent clause sits between the conjunction and the second clause, no comma follows the conjunction. With one shared subject, keep the comma before *but* and drop it before *and* when the link is close ("He has had several years' experience and is thoroughly competent."). Where the relation is cause or result, a subordinate clause often states it better than *and*.

### 41. No comma splice

**Rule:** Join two independent clauses without a conjunction by a semicolon, or make them two sentences. The semicolon shows their close relation most briefly. An adverb such as *accordingly*, *besides*, *then*, *therefore*, or *thus* still needs the semicolon. Exceptions: very short clauses alike in form ("Man proposes, God disposes."), and the colloquial "I hardly knew him, he was so changed" in dialogue or a familiar letter.

### 42. Do not break sentences in two

**Rule:** Do not use a period where a comma belongs.
**Before:**
> He was an interesting talker. A man who had traveled all over the world and lived in half a dozen countries.
**After:**
> He was an interesting talker, a man who had traveled all over the world and lived in half a dozen countries.

An emphatic fragment ("Again and again he called out. No reply.") stands only on the terms of §2.

### 43. An opening phrase must fit the subject

**Rule:** A participial phrase, prepositional phrase, appositive, or adjective at the start of a sentence refers to the grammatical subject. Recast when it does not.

| Before | After |
| --- | --- |
| On arriving in Chicago, his friends met him at the station. | When he arrived in Chicago, his friends met him at the station. |
| A soldier of proved valor, they entrusted him with the defence of the city. | A soldier of proved valor, he was entrusted with the defence of the city. |
| Young and inexperienced, the task seemed easy to me. | Young and inexperienced, I thought the task easy. |
| Wondering irresolutely what to do next, the clock struck twelve. | While I wondered what to do next, the clock struck twelve. |

## I. Usage list

Words and expressions commonly misused, alphabetical. Some are plain errors; others are fine in their place but crowd into places where they say nothing. When you catch one, recast the sentence around what you mean rather than swapping one word for another.

- **All right.** Two words. Fine as "Agreed" or "Go ahead"; otherwise avoid.
- **As good or better than.** Rearrange: "as good as his, or better."
- **As to whether.** *Whether* is enough (§31).
- **Bid.** Takes the infinitive without *to*; past tense *bade*.
- **But.** Unneeded after *doubt* and *help*: "I have no doubt that", "He could not help seeing that". Overused, it makes the loose sentences of §32. Avoid one *but* answering another; rearrange.
- **Can.** Means *is able*; not a substitute for *may*.
- **Case.** Usually unnecessary: "Many of the rooms were poorly ventilated", not "In many cases, the rooms...".
- **Certainly.** Not an all-purpose intensifier.
- **Character, nature.** Often redundant: "hostile acts", not "acts of a hostile character". *Nature* is also vague in "poems about nature" unless specifics follow.
- **Claim (verb).** Means *lay claim to*; not a substitute for *declare*, *maintain*, or *charge*. "He claimed to be the heir."
- **Clever.** Overused; keep it for ingenuity in small matters.
- **Compare to, compare with.** *Compare to* points out likeness between things of different kinds (life to a pilgrimage); *compare with* points out differences between things of the same kind (Congress with Parliament).
- **Consider.** No *as* when it means *believe to be*: "I consider him competent."
- **Data.** Plural: "These data were tabulated."
- **Dependable.** Use *reliable* or *trustworthy*.
- **Different than.** Use *different from*, *other than*, or *unlike*.
- **Divided into.** Not for *composed of*: plays are divided into acts; poems are composed of stanzas.
- **Don't.** Means *do not*; *does not* is *doesn't*.
- **Due to.** Attaches to a noun ("losses due to preventable fires"), not an adverbial phrase: "He lost, because of carelessness", not "due to carelessness".
- **Effect, affect.** *Effect* as a noun is a result, as a verb is *to bring about*; *affect* means *to influence*. "A charming effect" in writing about the arts is vague; say what it was.
- **Etc.** Only where *and so forth* would leave nothing important in doubt; never after *such as* or *for example*.
- **Fact.** Only for what can be verified, not for judgments.
- **Factor, feature.** Hackneyed; say the thing directly. "He won the match by being better trained", not "His superior training was the great factor". *Feature* as a verb is the sales language of §16.
- **Fix.** In writing, means *fasten*, not *arrange*, *prepare*, or *mend*.
- **Folk.** Collective; singular form only.
- **Get.** Write *have*, not *have got*.
- **He is a man who.** Redundant: "He is very ambitious." (§31)
- **However.** Meaning *nevertheless*, not first in its clause: "At last, however, we reached camp." First in the sentence, it means *in whatever way*: "However you advise him, he will do as he thinks best."
- **Interesting.** Make it so instead of announcing it (§4).
- **Kind of, sort of.** Not for *rather* or *something like*; keep the literal sense: "a kind of fossil resin."
- **Less, fewer.** *Less* for quantity, *fewer* for number: "fewer men". A round number treated as an amount takes *less*: "less than a hundred".
- **Like, as.** *Like* before nouns and pronouns; *as* before phrases and clauses: "He thought as I did."
- **Line, along these lines.** Overworked; say what you mean: "He is studying French literature."
- **Literally.** Not for exaggeration: "a flood of abuse", not "a literal flood".
- **Lose out, try out, win out, sign up.** Weaker than the plain verb. Keep the idioms whose meaning differs from the plain verb (*find out*, *run out*, *make up*).
- **Most.** Not for *almost*: "almost everybody".
- **Near by.** Prefer *near* or *near at hand*; as an adjective, *neighboring*.
- **Oftentimes, ofttimes.** Write *often*.
- **One hundred and one.** Keep the *and*.
- **One of the most.** Threadbare as an opening for an essay or paragraph. The relative clause after it takes a plural verb: "one of the ablest men that have attacked this problem."
- **Participle for verbal noun.** Use the possessive before a gerund: "Do you mind my asking?", "the prospect of the Senate's accepting". Where the possessive is awkward, recast: "If it should become necessary to reconsider the whole matter."
- **People, public.** *The people* is political; *the public* is an audience or a market.
- **Phase.** A stage of change ("the phases of the moon"), not an *aspect* or *topic*.
- **Possess.** Not for *have* or *own* (§18).
- **Prove.** Past participle *proved*.
- **Respective, respectively.** Usually omit: "listed under the names of their authors." Keep it for formal proofs.
- **Shall, will; should, would.** In formal writing, plain future takes *shall* in the first person and *will* in the second and third; *I will* expresses determination or consent. A first-person conditional takes *should* ("I should not have succeeded without his help"), as does *shall* reported after a past verb. For habitual past action, the plain past is shorter and stronger: "Once a year he visited the old mansion."
- **So.** Not as an intensifier ("so good"). As a connective, see §40.
- **Split infinitive.** Put the adverb outside: "to inquire diligently".
- **State.** Means *express fully*, not *say*.
- **Student body.** Write *students*.
- **System.** Often needless: "dormitories", not "the dormitory system".
- **Thanking you in advance.** Write "Will you please", and thank the person afterwards.
- **They.** A distributive antecedent (*each*, *everybody*, *anyone*, *someone*) takes a singular pronoun. Singular *they* is that pronoun; do not default to *he*.
- **Very.** Sparingly; where emphasis is needed, use a word strong in itself.
- **Viewpoint.** Write *point of view*, and not for *view* or *opinion*.
- **While.** Literally *during the time that*. Not a substitute for *and* or *but* (use a semicolon), and for *although* only where no ambiguity results.
- **Whom.** *Who* when it is the subject of the next verb: "His brother, who he said would send the money."
- **Worth while.** Only of actions ("Is it worth while to telegraph?"), never before a noun: "His books are not worth reading."

## J. Proofreading checks

Errors a proofread catches that the rules above leave open. Each is a plain error in anyone's writing, so one sighting is enough. A proofread sorts every finding into three kinds: **grammar** (§34, §37 to §49, and the usage list), **logic** (§52, §53, and the support test in [`SKILL.md`](SKILL.md)), and **flow** (§1 to §5, §7, §11, §28, §31, §32, §50, §51). Separate *wrong* from *different*: an intentional short sentence for impact, correct informal language such as contractions in casual text, a rhetorical device such as deliberate repetition, and the writer's own voice all stand unless they hurt the meaning or the text's objective.

### 44. Spelling and typos

**Rule:** Correct misspellings ("buisness"), doubled or dropped words, and missing apostrophes in contractions ("Lets get started" for "Let's"). Keep the spelling convention the text already uses (US or UK) and make it consistent.

### 45. Agreement

**Rule:** A verb agrees with its subject, not with the nearest noun ("The list of changes is ready"). A collective noun (*team*, *company*, *committee*) takes a singular verb in US English and may take a plural in UK English; pick the text's convention and hold it. A pronoun agrees in number with its antecedent (see *They* in the usage list).

### 46. Tense drift

**Rule:** Within a passage, keep the tense the time frame calls for. Shift only when the time of the action shifts ("We launched last month, and users now report fewer errors" is a real shift; "We launched last month and are seeing results. Users reported satisfaction" drifts). §35 covers summaries.

### 47. Ambiguous pronouns

**Rule:** A pronoun points to one clear antecedent. When two nouns could own it ("The manager told the designer that she should revise the mockups"; "We met the vendor about their API. It was complicated."), name the noun or recast: "The manager told the designer to revise the mockups."

### 48. Run-on sentences

**Rule:** Two independent clauses fused with no punctuation, or a chain of clauses the reader cannot hold, become separate sentences or take a semicolon or conjunction. A comma alone between them is the splice of §41.

### 49. Articles

**Rule:** Supply a missing *a*, *an*, or *the*, and cut one that is wrong ("the" before a general plural: "The users want speed" when users in general are meant). *An* goes before a vowel sound: *an hour*, *a user*.

### 50. Choppy runs

**Watch for:** a row of short sentences of the same shape, each one step: "We launched the product. We got feedback. We iterated. We improved the feature."
**Rule:** The reverse of §32. Combine the steps that form one idea: "After launch, we used early feedback to improve the feature." Keep a short sentence that carries its own weight (§2).

### 51. Register drift

**Rule:** Hold one register for the audience and the objective. A formal proposal that suddenly says "this is gonna blow your mind", or a chatty note that turns stiff, reads as two writers. Name the dominant register and bring the outliers to it.

### 52. Contradictions

**Rule:** Two statements in the text that cannot both be true ("We prioritise user privacy" beside "We share user data with 50 third parties") get flagged with both locations. The writer reconciles them; the fix names the detail that would make both true, or asks which one stands.

### 53. Leaps in reasoning

**Watch for:** a cause asserted from sequence alone ("We launched in Q3, so adoption rose"); a claim proved by itself ("the best product because customers prefer it"); a claim offered without the evidence the reader would need ("our product is the best on the market"); a conclusion that does not follow from the points before it.
**Rule:** Flag the gap and say what would close it: the evidence, the missing step, or a narrower claim. Supply a figure only when the source or the user gives it; otherwise the fix asks for it. Vague claims ("saves time and money") are §30.

## Full example

A whole piece with tells at every scale, and its rewrite.

**Before:**
> I recently spent five unforgettable days in Lisbon last October, and let me tell you — this city completely stole my heart. From the moment I checked into my charming hotel perched high in the historic Alfama district, I knew I was somewhere truly special.
>
> Yes, the famous hills are challenging — with countless stairs between my hotel and everything else, my legs certainly felt it! — but every climb rewards you with breathtaking, panoramic views that make it all worthwhile.
>
> No trip would be complete without riding the iconic Tram 28, a roughly forty-minute journey shared with plenty of fellow travelers eager to capture the magic. And the food? Simply divine. While the pastéis de nata at Pastéis de Belém are a beloved national treasure, my absolute favorite came from a hidden gem in Graça, still warm from the oven.
>
> But what truly makes Lisbon special isn't just the sights — it's the feeling. Wander just a block or two above the main squares and you'll discover a quieter, more authentic side of the city, inviting you to slow down and savor every moment.
>
> Of course, the must-see São Jorge Castle offers stunning views over the rooftops below. The queues can be long, but the experience is absolutely worth it for any history buff or curious traveler.
>
> Would I go back? Absolutely — next time in spring, and with better shoes! Lisbon isn't just a place to visit; it's a place to fall in love with, again and again. ✨

**After:**
> I spent five days in Lisbon last October. My hotel was up in Alfama, with a lot of stairs between it and everything else, and my legs felt every one of them. The views from the top were worth the climb.
>
> Everyone tells you to ride Tram 28, so I did. The trip took about forty minutes, and most of the car was other tourists taking pictures out the windows. The custard tarts at Pastéis de Belém are the famous ones, but my favorite came from a place in Graça, still warm from the oven.
>
> The part of Lisbon I liked best starts a block or two above the main squares, where the streets go quiet and nobody is in a hurry. São Jorge Castle has good views over the rooftops and a long queue to get them.
>
> I'd go back, in spring next time, and with better shoes.

## Sources

The tells come from Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup, and from reviews of AI-generated text. The composition, punctuation, and usage rules adapt a public-domain style handbook from 1918. See `LICENSE-ai-tells` for the licence of the adapted tell catalogue, and `LICENSE-grammar` for the proofreading checks in §44 to §53 and the proofread steps in `SKILL.md`.
