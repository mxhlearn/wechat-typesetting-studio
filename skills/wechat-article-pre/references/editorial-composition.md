# Editorial Composition

Use this file when turning material into a finished WeChat public-account article, especially when the article needs human-like editorial arrangement instead of a fixed Markdown skeleton.

The goal is to compose the article like an editor: choose the article shape, decide the reading rhythm, place components where they help, and make the WeMD Markdown feel intentionally arranged.

## Contents

- [Core Rule](#core-rule)
- [Composition Pass](#composition-pass)
- [Editorial Decision Loop](#editorial-decision-loop)
- [Layout Styles](#layout-styles)
- [Component Decisions](#component-decisions)
- [Template Selection](#template-selection)
- [Section Flow](#section-flow)
- [Anti-Template Checks](#anti-template-checks)

## Core Rule

Do not treat components as decorations or as required blocks.

Use a component when it does one of these jobs:

- reduces reader confusion
- proves a step or claim
- compares options faster than prose
- warns against a likely mistake
- breaks a long reading stretch
- preserves a source link, download, or reference the reader may need

If a component does not change understanding, action, trust, or rhythm, remove it.

## Composition Pass

Before drafting, choose:

1. Reader state: first-time user, experienced user, decision maker, returning follower.
2. Article shape: tutorial, commentary, explainer, list, case review, news/update, interview/profile, or source rewrite.
3. Layout style: lean narrative, tutorial walkthrough, decision memo, visual explainer, checklist, case story, or resource guide.
4. Component plan: where images, tables, callouts, code blocks, lists, quotes, diagrams, and references belong.
5. First-screen rhythm: title, optional lead line, opening paragraph, and the first useful section.

Keep this plan private. Do not write "composition plan" into `final-article.md`.

## Editorial Decision Loop

Use this loop before drafting and again before final delivery:

1. Decide the article's job.
2. Choose the layout style that serves that job.
3. Pick only the components that improve action, comparison, proof, warning, or rhythm.
4. Place each component next to the sentence, step, or claim it supports.
5. Remove any component that exists only because a template offered it.

This is the core difference between formatting and editing: a real editor may use TIP blocks, tables, screenshots, references, diagrams, and quotes, but does not use all of them in every article.

## Layout Styles

### Lean Narrative

Use for commentary, reflection, opinion, and essays.

Typical rhythm:

- title
- direct opening judgment, scene, or tension
- 3 to 5 sections with prose-first paragraphs
- sparse lists
- maybe one quote or emphasis block if it sharpens the argument
- light closing judgment or next step

Use images only when they carry evidence, context, or atmosphere that prose cannot replace.

### Tutorial Walkthrough

Use for setup guides, workflows, tool tutorials, and operational posts.

Typical rhythm:

- title
- task-first opening
- prerequisites or environment section
- steps grouped by outcome
- code blocks or screenshots directly after the step they support
- verification lines after critical steps
- callouts for warnings or non-obvious choices
- troubleshooting or fallback only when useful

Do not move required commands, links, screenshots, or verification out of the article for the sake of a smoother narrative.

For serious tutorials, use a calm operational register:

- Prefer declarative headings over rhetorical questions.
- Use the heading to name the action or decision, not to simulate a conversation.
- Put verification immediately after the step that needs proof.
- Use `## 补充说明`, `## 版本选择`, `## 权限与环境检查`, or `## 排查建议` instead of `## 常见问题` unless FAQ is explicitly requested or the source is already Q&A.
- If a reader might panic, do not reassure them with "别急" or "不要着急"; give the check, risk, or next action.

### Decision Memo

Use for tool comparisons, reviews, recommendations, and buying/usage decisions.

Typical rhythm:

- title
- judgment or decision tension
- criteria before comparison
- compact table only when it makes differences clearer
- prose explanation after the table
- caveats and who should choose what

Tables are welcome here, but only if the rows and columns are tight enough for mobile reading.

### Visual Explainer

Use for concepts, frameworks, processes, and "how it works" topics.

Typical rhythm:

- title
- problem or confusion
- one diagram, image, or Mermaid block when it clarifies structure
- short sections that explain parts of the diagram
- plain-language fallback for diagrams

If a diagram is not necessary, use bullets or a short example instead.

### Checklist

Use when the article is genuinely a list, checklist, pitfall list, or resource selection.

Typical rhythm:

- title with scope
- short explanation of the selection principle
- grouped checklist items
- callouts only for high-risk items
- closing selection rule

Numbered headings are acceptable here because the article shape is truly list-based.

### Case Story

Use for experience posts, failure reviews, product usage stories, and personal notes.

Typical rhythm:

- title
- concrete scene or result
- what happened
- choice or turning point
- result
- lesson bounded to the case

Use screenshots, quotes, or tables only when they prove the case. Do not turn a case story into a generic lesson article.

### Resource Guide

Use when the article provides links, downloads, tools, reading lists, or source material.

Typical rhythm:

- title
- who the resource list is for
- grouping principle
- short notes per resource
- `## References` or resource section when links are part of the article value

References are not residue here; they are content.

## Component Decisions

### Lead Line

Use a short line after the title only when it adds a real judgment, promise, or reading frame.

Do not use a lead line just because the template has one. If the opening paragraph already carries the frame, skip the lead line.

### Lists

Use lists for:

- parallel choices
- steps
- checklists
- quick scans

Avoid list after list. If every section starts with bullets, the article will feel assembled rather than written.

### Callouts

Use callouts for:

- warnings that prevent mistakes
- tips that change the action
- conclusions worth isolating
- caveats that should not be buried

Do not use callouts for generic encouragement, repeated summaries, or decoration.

For WeMD-ready public-account drafts, a callout must survive this question: would the reader lose a warning, shortcut, or decision if this box became normal prose? If not, make it prose or cut it.

### Tables

Use tables for:

- compact comparison
- decision criteria
- parameters
- before/after differences

Avoid tables when:

- one column contains long paragraphs
- the table is wider than mobile reading can tolerate
- the same idea is clearer as bullets

For wide tables, split into grouped bullets or multiple small tables.

### Images And Screenshots

Use images for:

- cover image
- real UI or terminal proof
- step verification
- process diagrams
- conceptual section breaks
- visual examples that cannot be described cleanly

Place an image close to the sentence or step it supports.

For tutorials, use real screenshots for proof-heavy UI or terminal moments. Do not invent fake UI states or fake output.

When an expected screenshot is missing, keep a short image note where the screenshot belongs. Do not move all image notes to the end; placement is part of the reading path.

### Code Blocks

Use code blocks for commands, config, logs, code, and structured examples.

Before a code block, say where to run it and why. After it, say what success looks like when the reader needs confirmation.

### Quotes

Use quotes only when:

- supplied wording matters
- a user sentence reveals the problem
- a source quote changes interpretation
- a short emphasis block helps the reader pause

Do not open with a quote unless the quote is stronger than a direct opening.

### References

Use `## References` when links are part of the reader's next action, verification, download path, or source trail.

Do not create References just to park every URL. Keep inline links near the action when they are immediately useful.

Do not delete TIP, table, image, quote, code, diagram, or References material only because it looks like Markdown furniture. First decide whether it is content, proof, navigation, or residue.

## Template Selection

Choose a template by article job, not by habit:

| Article job | Preferred layout | Typical components |
| --- | --- | --- |
| Finish a task | Tutorial walkthrough | steps, code, screenshots, warnings, verification |
| Judge a tool | Decision memo | criteria, compact table, caveats |
| Explain a concept | Visual explainer | example, diagram, short callout |
| Share an experience | Case story | scene, result, bounded lesson |
| Curate resources | Resource guide | grouped lists, links, references |
| Argue a view | Lean narrative | sparse emphasis, one strong close |
| Prevent mistakes | Checklist | grouped pitfalls, warnings |

If the source draft already has a strong natural structure, preserve it and only improve rhythm.

## Section Flow

Each section needs one editorial job:

- orient
- prove
- explain
- compare
- instruct
- warn
- transition
- close

Adjacent sections should not do the same job. Merge or cut repeats.

Within a section, place components after the idea they support:

- claim -> evidence image/table/quote
- step -> command/screenshot/verification
- comparison -> table -> interpretation
- risk -> warning callout -> safer action
- concept -> diagram -> plain explanation

## Anti-Template Checks

Before final delivery, check:

- Does the article look intentionally composed, or like every component from a template was left in?
- Are images, tables, callouts, code blocks, and references placed because the content needs them?
- Could a reader predict the structure from the article job?
- Does the first screen feel written, not assembled?
- Did the article use at least one layout style consciously?
- Did WeMD formatting enhance the article instead of becoming the article?

Remove or move components that fail these checks.
