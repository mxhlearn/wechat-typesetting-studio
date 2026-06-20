# WeMD Visual Rhythm

Use this file when the article is targeting WeMD and should feel like a finished WeChat post after Markdown preview and copy.

The goal is not decorative styling. The goal is clean, breathable, publication-ready Markdown that survives WeMD themes and WeChat copy flow.

## Visual Priorities

Optimize for these outcomes in order:

1. the reader can understand the structure at a glance
2. the first screen feels light and readable
3. long sections break naturally before fatigue appears
4. screenshots, code blocks, diagrams, and notes do not interrupt the reading rhythm
5. the article still feels like content first, not a theme demo

## Opening Screen Rules

The first visible screen in WeMD preview should usually contain:

- one clear title
- one short summary line or lead quote
- one opening paragraph or one opening paragraph plus one short transition line

Avoid making the top of the article crowded.

Do not stack too many of these before the reader starts moving:

- long summary
- cover copy block
- multiple bold lines
- image marker
- list
- quote

If an image is useful near the top, place it after the opening rather than before the article has properly started.

For practical tutorials, the first screen should not hide the task behind brand storytelling. State the end state early.

## Section Rhythm

Each main section should feel like one screen-level idea.

Practical defaults:

- most sections should begin with a short framing sentence
- the core explanation should arrive within the first 2 paragraphs
- if a section exceeds 4 short paragraphs, look for a subhead, list, note, or cut
- if two neighboring paragraphs are doing the same job, merge or delete one

For tutorial articles:

- present action before commentary
- present verification before extra tips
- separate warnings from the main action path
- do not bury commands inside long prose

## Paragraph Texture

When targeting WeMD, paragraphs should usually feel lighter than a normal blog draft.

Use these defaults:

- 1 sentence paragraphs are acceptable when they create rhythm or emphasis
- 2 sentence paragraphs are often the best default
- 3 sentence paragraphs are fine when the idea is compact
- 4 sentence paragraphs are the upper edge for most instructional sections

Break earlier when:

- a sentence introduces a new action
- a sentence changes from explanation to example
- a sentence changes from action to warning
- a sentence introduces a result check

## Heading Style

Prefer headings that do real navigation work.

Good heading traits:

- direct
- concrete
- action-oriented when appropriate
- easy to scan on mobile

Avoid headings that are:

- too lyrical for a tutorial
- too abstract to predict the section
- near-duplicates of the title
- only decorative emotional phrases

For tutorials, good headings often start with an action or result. For commentary, good headings can state a judgment.

## WeMD Feature Discipline

WeMD supports modern Markdown-centered preview features, but the article should not depend on every advanced feature.

Use advanced features only when they serve the article:

- Tables: comparison data only.
- Code highlighting: tutorials and technical notes.
- Mermaid: diagrams only when simpler prose or bullets are worse.
- Math: only when the article genuinely needs formulas.
- Theme/CSS assumptions: keep content readable without custom styling.

If a feature may not survive the final WeChat copy flow, simplify it in the article. Use a sidecar fallback only when the user explicitly asks for one.

## List Rhythm

Lists should help scan speed, not inflate the article.

Use a list when:

- there are parallel options
- the reader needs a sequence
- the reader needs a compact checklist

Avoid back-to-back long lists unless the article is explicitly a checklist article.

If a list has more than 5 items, check whether:

- it should be split into 2 smaller lists
- some items should become prose
- a subhead should come before it

Avoid a list directly under every heading. Alternate prose, lists, screenshots, and verification lines when the article is long.

## Code And Screenshot Rhythm

Code blocks and screenshots should feel anchored, not dropped in randomly.

Before a code block:

- tell the reader where to run it
- tell the reader what the command is for

After a code block:

- tell the reader what successful output looks like when needed
- explain only the output signal the reader needs; do not paste fake output

Before a screenshot marker:

- make sure the surrounding text already explains why the screenshot matters

If a screenshot slot is essential, place it immediately after the step it proves.

## Emphasis Discipline

WeMD themes can make over-emphasis look noisy quickly.

Use emphasis sparingly:

- bold only key conclusions, warnings, or parameter names
- avoid bolding whole sentences unless the sentence is very short
- avoid repeated bold use in adjacent paragraphs

If everything is emphasized, nothing is emphasized.

## Closing Rhythm

The ending should feel lighter than the body, not heavier.

Good closing options:

- one concise recap
- one practical next step
- one calm CTA

Do not end with:

- a second full summary of the whole article
- a sales pitch that feels unrelated to the article
- a sudden emotional register change

## WeMD Visual QA

Before calling the article visually ready for WeMD, check:

- would the first screen feel clean on mobile
- do section breaks appear before fatigue
- are there any heavy text walls that need splitting
- do code blocks have enough framing
- are screenshot markers placed only where they help
- can the Markdown still read well without custom theme assumptions
- does the article still feel like content first, style second
- are long code blocks framed by purpose and verification
- are image notes close to the relevant action
- are accessibility cues present for important images, diagrams, and screenshots
- does the article remain understandable if optional images are missing
