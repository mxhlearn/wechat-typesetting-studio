# WeChat Style Learning

Use this file when the user provides or asks for example WeChat public-account articles, benchmark accounts, screenshots, Markdown samples, or style references and wants a new original article for their own topic.

The goal is not imitation. The goal is to extract transferable writing and layout discipline, then produce original WeMD-ready Markdown.

## Contents

- [Source Intake](#source-intake)
- [Sample Collection](#sample-collection)
- [Learning Boundary](#learning-boundary)
- [Style Profile](#style-profile)
- [Language Extraction](#language-extraction)
- [Layout Extraction](#layout-extraction)
- [Pattern Matrix](#pattern-matrix)
- [Drafting Workflow](#drafting-workflow)
- [Borrow / Avoid List](#borrow--avoid-list)
- [WeMD Combination](#wemd-combination)
- [Reuse Across Articles](#reuse-across-articles)
- [Similarity QA](#similarity-qa)
- [Output](#output)
- [Failure Modes](#failure-modes)

## Source Intake

Accept these inputs:

- public article links the agent can browse
- pasted article text
- screenshots of article layout
- exported Markdown or HTML
- the user's previous successful posts
- a named benchmark account plus a request to search for public examples

If public pages cannot be accessed, ask for pasted text or screenshots.

Use 2 to 5 samples when possible. One sample is enough for a light pass, but do not overfit it.

Do not require the user to provide a whole account archive.

When using screenshots, learn layout rhythm only. Do not infer exact wording from unreadable text.

## Sample Collection

When the user gives only an account name or says to find examples:

1. Search for public, accessible articles from that account or close public mirrors.
2. Prefer 2 to 5 articles that match the user's target article shape.
3. Prefer recent samples when the account style may have changed.
4. Ignore pages that require login, app-only access, or unverifiable reposts.
5. If no reliable public sample is available, ask the user to paste article text, upload screenshots, or provide exported Markdown.

Do not invent account style from memory.

When samples differ from each other, extract the stable pattern and note the variance. Do not average incompatible styles into vague advice.

## Learning Boundary

Learn from:

- title promise
- opening move
- reader positioning
- paragraph density
- sentence length
- section rhythm
- evidence threshold
- transition style
- emphasis habits
- list and quote usage
- image placement
- closing and CTA restraint
- WeMD-compatible Markdown shape

Do not copy:

- distinctive phrases
- private slogans
- repeated jokes
- memorable metaphors
- exact sentence cadence
- unique section names
- source-specific examples
- full section order unless it is a generic article shape
- any text the user did not authorize for reuse

If the source account is a living creator or active brand, keep more distance. Borrow the method, not the voice identity.

When learning from a benchmark account and the user's own writing at the same time, extract two profiles:

- User voice: preferred terms, stance, recurring concerns, boundaries.
- Benchmark discipline: pacing, packaging, layout, evidence habits.

Apply user voice first and benchmark discipline second.

## Style Profile

Before drafting, create a compact private profile:

```text
Benchmark style profile:
- Source count:
- Reader:
- Topic promise:
- Title pattern:
- Opening move:
- Paragraph rhythm:
- Sentence rhythm:
- Section rhythm:
- Evidence density:
- Layout habits:
- Image habits:
- CTA style:
- Evidence habits:
- Risk distance:
- Words to avoid copying:
- Reusable constraints:
```

Keep the profile out of `final-article.md`.

Write `style-profile.md` only when:

- the user explicitly asks to learn from sample accounts or benchmark articles
- the user asks to reuse the style later

For one-off style learning, apply the learned constraints to `final-article.md` without creating a separate profile file.

When writing `style-profile.md`, include only the rules a future agent can apply without seeing the original samples.

## Language Extraction

Extract language style by answering:

- Is the voice tutorial-like, analytical, conversational, sharp, restrained, or reflective?
- Does the account prefer direct claims or slow build-up?
- Does it use short blunt sentences, medium explanatory paragraphs, or long narrative blocks?
- Does it lead with task, pain point, contrast, scene, result, or judgment?
- How much personal stance appears in each section?
- How often does it qualify claims?
- What words or sentence patterns appear often enough to be style signals?
- Which phrases are too distinctive to reuse?

Convert the answers into constraints, not prose decoration.

Good constraints:

- `Open with the task and one real friction point.`
- `Use short paragraphs; keep most paragraphs under 80 Chinese characters.`
- `Use explicit verification lines in tutorial sections.`
- `State one editorial judgment per main section.`
- `Avoid slogan-like transitions and broad encouragement.`

Weak constraints:

- `Write warmly.`
- `Make it viral.`
- `Use the same tone as the sample.`
- `Be more like this account.`

Prefer measurable constraints when possible:

- paragraph length range
- frequency of examples
- whether headings are nouns, actions, or judgments
- how often the author states a viewpoint
- how much background appears before the first usable point
- how warnings and caveats are placed

## Layout Extraction

Extract layout style separately from language:

- heading depth and heading length
- first-screen density
- average paragraphs per section
- list frequency
- numbered steps versus bullets
- quote block frequency
- bold usage
- image slot placement
- screenshot versus illustration use
- code block framing
- closing shape

Then translate it to WeMD-safe Markdown:

- one `#` title
- `##` for main sections
- `###` only when needed
- short paragraphs
- fenced code blocks with language tags
- short standalone image notes
- no raw HTML unless the user explicitly asks for WeMD/CSS customization
- no decorative separators
- no prompt residue

If a benchmark account relies on heavy HTML styling, custom cards, color blocks, or complex image-text layout, approximate the reading rhythm in Markdown instead of recreating the decoration.

## Pattern Matrix

Build this matrix when the user provides multiple examples or asks for style learning across later articles:

| Layer | Extract | Convert to constraint |
| --- | --- | --- |
| Title | promise, subject, tension, length | 3 to 5 title patterns that fit the new topic |
| Opening | task, pain, contrast, scene, judgment | one opening move and one thing to avoid |
| Paragraph | average length, sentence rhythm | target paragraph density and cut threshold |
| Section | heading style, section count, section job | section order that serves the current topic |
| Evidence | examples, screenshots, numbers, quotes | evidence threshold and unsupported-claim rule |
| Emphasis | bold, quotes, lists, separators | WeMD-safe emphasis limits |
| Visuals | screenshot timing, cover style, diagrams | visual slots and cover brief constraints |
| CTA | comment prompt, next article, no CTA | smallest useful closing move |
| Reader fit | assumed knowledge and explanation depth | detail level for this article |
| Freshness | dates, versions, current claims | verify, qualify, or remove unstable points |

Then write a compact transfer note:

```text
Transfer note:
- Use:
- Adapt:
- Do not copy:
- WeMD conversion:
```

Use this note to draft. Do not keep re-reading source phrasing while writing.

## Drafting Workflow

Use this workflow:

1. Identify the user's own article mission.
2. Study the examples and build the style profile.
3. Build the pattern matrix when there are 2 or more samples.
4. Write a "borrow / avoid" list before drafting.
5. Choose the article shape from `SKILL.md`.
6. Draft from the user's topic, facts, and judgment.
7. Apply benchmark rhythm only where it serves the topic.
8. Clean for WeMD Markdown.
9. Run originality and overfit checks.
10. Save outputs to the article-title folder.

The user's substance wins over the benchmark style.

If the benchmark style conflicts with accuracy, clarity, or WeMD cleanliness, keep accuracy, clarity, and WeMD cleanliness.

Do not let style learning remove operational content. For tutorials, protect steps, commands, screenshots, verification, and caveats before applying style rhythm.

## Borrow / Avoid List

Create this before drafting:

```text
Borrow:
- 
- 
- 

Avoid:
- 
- 
- 
```

Examples:

- Borrow: fast task-first opening.
- Borrow: headings that state a decision, not a topic label.
- Borrow: screenshots only after the step is explained.
- Avoid: same metaphor as the sample.
- Avoid: same title syntax in every option.
- Avoid: long lead quote before the article has started.

If the borrow list contains more than 5 items, choose the 3 most important. Too many style constraints usually make the article stiff.

## WeMD Combination

When combining benchmark learning with WeMD:

- keep mobile reading lighter than the source if the source is dense
- turn decorative subheadings into semantic headings
- turn long quote-led openings into one concise lead
- turn image-heavy rhythm into explicit image slots
- turn repeated bold lines into fewer, stronger emphasis points
- keep cover and image prompt detail internal unless the user explicitly asks for `visual-brief.md`

WeMD is the default handoff format. The benchmark account is only a style reference.

## Reuse Across Articles

Do not claim persistent memory.

When the user wants the learned style to carry into future articles, save the reusable constraints in `style-profile.md`. On later tasks, treat a provided `style-profile.md` as an input source and update it only when the user gives new samples or feedback.

The profile should contain patterns, constraints, and anti-patterns. It should not contain copied source paragraphs.

When updating a profile, append only durable constraints. Do not add one-off article facts or temporary campaign needs.

## Similarity QA

Before delivery, check:

- Would a reader recognize the source account from phrasing alone?
- Are any phrases, metaphors, or section names too close?
- Does the article preserve the user's topic and facts?
- Does each section have a new job?
- Does the structure serve this article, not the sample?
- Is the Markdown clean enough for WeMD preview and copy flow?
- Are repeated sentence openings from the source avoided?
- Are the user's own terms and viewpoint still visible?

If the answer suggests overfitting, rebuild the affected section from:

- the user's point
- the article mission
- the extracted constraints

Do not rewrite by swapping synonyms.

## Output

Default article folder:

```text
文章标题/
  final-article.md
  cover-image.png         # only when generated or supplied
  section-01.png          # only when generated or supplied
```

`style-profile.md` should be compact. It is a reusable working brief, not a public article.

If benchmark style suggests stronger section rhythm, put optional `##` or `###` subheading alternatives directly in `final-article.md`; do not create a separate title-options file.

Do not store copied source text inside `style-profile.md`.

Do not store raw URLs to private or login-only articles unless the user explicitly wants them preserved.

## Failure Modes

- Treating one benchmark article as a complete account style.
- Copying signature phrases while claiming to learn structure.
- Making the article sound like a different person with no user viewpoint.
- Recreating HTML-heavy layout inside Markdown.
- Forgetting WeMD constraints after studying the source.
- Producing a style profile but not applying it.
- Applying benchmark rhythm so strongly that tutorial steps or facts disappear.
- Producing a pattern matrix but ignoring it during the draft.
- Learning public-account decoration while ignoring the user's topic promise.
