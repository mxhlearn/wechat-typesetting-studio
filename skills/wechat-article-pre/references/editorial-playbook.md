# Editorial Playbook

Use this file when the article needs a title, opening, structure, CTA, or review pass.

## Mission Lock

Reduce the article to one sentence:

`This article helps [reader] [finish / understand / decide / avoid] [specific outcome].`

If you cannot say that sentence cleanly, the scope is still too broad.

## Angle Selection

Pick one angle. Do not average three.

Use one of these:

- Task completion: finish one concrete workflow.
- Pitfall correction: show where readers get stuck.
- Decision lens: help the reader judge a tool or change.
- Method extraction: turn one case into a usable method.
- Experience reflection: pull a lesson from a real case.

Reject angles that rely on hype, false urgency, or a result the article cannot support.

## Title System

A good title does three things:

1. names the subject
2. implies a benefit
3. matches the body

### Title Families

**Direct utility**

- `Windows 下安装 X：从环境准备到最终验证`
- `把 X 跑起来：一条更稳的配置流程`
- `第一次使用 X，可以先完成这 4 步`

**Problem to result**

- `X 总是装不好，问题通常出在这几处`
- `写公众号总像 AI 稿，可以先改这 3 个地方`
- `用 X 做 Y 时，真正卡人的不是工具本身`

**Scope lock**

- `这篇只解决 3 件事：A、B、C`
- `不讲大而全，先把 X 跑通`
- `如果你只想完成 X，可以直接照这篇做`

**Insight correction**

- `很多人误解了 X：它真正改变的是 Y`
- `X 不是万能答案，但它适合解决这类问题`
- `别急着追新工具，先把这个判断标准弄清楚`

### Title Rules

- Choose one final H1 title unless the user explicitly asks to compare main titles.
- Avoid vague hype.
- Avoid clever wording that hides the topic.
- Avoid promise inflation.
- Do not use a title that promises a broader article than the body delivers.
- For tutorials, include the platform, task, or end state when it reduces ambiguity.
- For commentary, include the tension or judgment, not only the topic name.
- For list posts, include the selection principle, not only the item count.

### Title QA

Reject a title if:

- it could fit any article in the same category
- it hides the main subject
- it promises "complete" when the body has caveats
- it uses emotion to compensate for weak substance
- it sounds more like an ad than an article

## Subheading Options

Use subheading alternatives when section rhythm matters more than main-title choice.

Default behavior:

- keep one final `#` title
- do not create `title-options.md`
- if alternatives help, place them inside `final-article.md` near the relevant section
- use alternatives for `##` or `###`, not for the H1 title
- keep alternatives short and ready to choose manually

Format:

```markdown
## 安装前先确认这几件事

<!-- Subheading alternatives:
- 先把环境准备好
- 开始之前，先检查这几项
-->
```

Use comment blocks only when the user wants editable alternatives in the final file. Otherwise choose the best heading and omit alternatives.

## Opening System

The opening should answer three questions fast:

1. What does this article help me finish?
2. Why should I trust the path?
3. Why keep reading now?

### Opening Moves

**Direct task opening**

Start with the task and likely friction.

**Pain point opening**

Start with a concrete failure, not a broad emotion.

**Contrast opening**

Start with what people assume versus what matters.

**Small scene opening**

Start with a real moment, then connect it to the point.

### Opening Rules

- Avoid generic era or trend framing.
- Avoid `本文将从以下几个方面展开`.
- Avoid warm-up paragraphs that delay the point.
- Avoid repeated rhetorical questions.
- Do not start with a broad claim unless the next sentence proves it.
- Do not start with a quote unless the quote changes the reader's next action.
- If the source draft has a useful first-hand detail, use that detail before general background.

### Opening QA

After writing the opening, ask:

- Can the reader tell what they will get within 5 seconds?
- Is there one concrete friction, decision, or promise?
- Did the opening avoid explaining the whole outline?
- Would the second paragraph still be useful if the title were removed?

## Structure Patterns

Choose one structure before drafting.

If the user provides only a topic and no draft, choose the most conservative useful structure:

- operational topic: tutorial or checklist
- abstract concept: explainer
- product/tool change: news/update digest or commentary
- personal experience: case review
- people/company story: interview/profile

State assumptions briefly outside the publishable article only when they affect scope.

### Tutorial / Setup Guide

1. what this helps the reader finish
2. what to prepare
3. main steps
4. verification
5. fallback checks
6. next step

Rule: remove any paragraph that does not help the reader act, understand, verify, or avoid a mistake.

Protection rule: do not remove required installation paths, download sections, links, commands, screenshots, environment labels, warnings, or verification steps just because they interrupt prose flow.

### Commentary / Review

1. what changed
2. why it matters
3. what it means
4. what the reader should do

Rule: state a judgment. Do not hide behind neutral summaries.

### Explainer / Concept Note

1. define the idea
2. set the boundary
3. show an example
4. give a method

Rule: explain one distinction well. Do not turn the article into a glossary.

### Source Draft Rewrite

1. keep the real point
2. rebuild the spine
3. remove repetition
4. close on the reader outcome

Rule: preserve the user's meaning, not the user's sentence order.

### Checklist / List Post

1. define the scope
2. group the items
3. keep each item compact
4. end with a selection rule

Rule: if an item needs more than 3 short paragraphs, it is probably a section, not a list item.

A list post must have a selection principle. Do not create a loose pile of tips.

### Case Review / Reflection

1. state the case
2. explain the decision
3. show the result
4. extract the lesson

Rule: cut diary detail unless it changes the lesson.

Separate "what happened" from "what it means". Do not make the lesson sound broader than the case supports.

### News / Update Digest

1. state what happened
2. explain what changed
3. show who is affected
4. give the caveat or next signal

Rule: separate fact, interpretation, and speculation. Do not turn uncertainty into certainty.

For recent or changeable facts, verify dates and current source material before drafting. If verification is not available, mark the point as unverified outside the publishable article.

### Interview / Profile

1. open with one scene or judgment
2. introduce the person or subject
3. show the key choices
4. extract the useful insight

Rule: do not flatter the subject. Use details that reveal a decision, constraint, or tradeoff.

Do not invent quotes, private motivations, or biographical detail. If a quote is supplied, preserve meaning and do not smooth away the speaker's actual point.

## Factual Discipline

- Do not invent data, timelines, quotes, product behavior, screenshots, or reader feedback.
- Mark uncertain points as uncertain, or remove them.
- Keep claims proportional to the supplied material.
- Separate observation from judgment.
- Use examples to clarify, not to fake authority.
- If a missing fact would change the conclusion, ask or leave a short note outside the publishable article.
- For links, versions, prices, schedules, laws, policies, or product features, treat freshness as a risk and verify when possible.
- Do not cite a source you did not read.
- If the article uses external sources, keep source names and links precise.

## Source Triage

Before rewriting from a source draft, sort source material into:

- Must keep: facts, steps, links, commands, caveats, quotes, screenshots, examples, user viewpoint.
- Can reshape: order, headings, transitions, paragraph rhythm, examples that are redundant.
- Can cut: repeated explanation, generic preface, unsupported promise, filler summary.
- Must verify or flag: dates, versions, prices, product behavior, legal/medical/financial claims.

Do not cut a "must keep" item to make the prose smoother.

## Hard Editing Rules

- One section, one job.
- One paragraph, one movement.
- One sentence, one claim.
- One claim, one basis.
- Cut throat-clearing.
- Cut explanations of what the article is about to explain.
- Cut generic reassurance.
- Cut repeated transitions.
- Keep claims proportional to evidence.
- Prefer concrete nouns and verbs.
- Prefer deletion over ornamental rewriting.

## Density Check

Before final delivery, scan every paragraph:

- Does it add a fact, judgment, step, example, or consequence?
- If not, cut it.
- Can two adjacent paragraphs become one?
- If yes, merge them.
- Is the sentence true but obvious?
- If yes, cut it or make it specific.
- Does the sentence exist only to sound complete?
- If yes, delete it.

## Tutorial Structure

For tutorials, keep action, reason, and verification together.

Use concise verification lines:

- `验证：输出版本号即表示安装完成。`
- `验证：页面能正常打开，说明本地服务已经启动。`
- `验证：WeMD 预览中只出现一个一级标题。`

Do not narrate obvious steps.

Before rewriting a tutorial, build a preservation checklist:

```text
Preserve:
- required tools:
- required links:
- required commands:
- required screenshots:
- required verification:
- required caveats:
```

After rewriting, check every preserved item appears in the final article or in an explicit sidecar note when the user requested sidecars.

## CTA

Use the smallest CTA that matches the article:

- try the workflow
- save the checklist
- comment with a specific case
- read the next article only if needed

Do not end with generic encouragement.

## Review Rubric

Check these before final delivery:

- Title: specific, restrained, true
- Opening: fast, clear, useful
- Structure: one job per section
- Voice: specific, edited, not generic
- Editor-ready Markdown: one H1, shallow headings, short paragraphs
- Evidence: current, sourced, or clearly qualified
- Scope: no promise beyond the body

## Review Mode

Use review mode when the user asks to audit, check, diagnose, or improve an existing article without asking for a full rewrite.

Return findings first. Group them by publishing impact:

- Blocking: factual error, missing required step, broken link, unsafe command, fake screenshot, multiple H1 titles, prompt residue.
- Major: weak title promise, slow opening, broken structure, unsupported claim, tutorial step without verification, WeMD-incompatible layout.
- Minor: filler, repeated transition, awkward heading, over-bolding, paragraph wall, weak CTA.

For each finding, include:

- where it appears
- why it hurts the article
- the smallest useful fix

Use this compact finding shape:

```text
[Severity] Location
Issue:
Impact:
Fix:
```

Then add a short "rewrite priority" list in the chat response. Do not produce a full rewrite unless the user asks.

When the user asks for both review and rewrite, keep review rationale out of `final-article.md`. Create `review-notes.md` only when the user explicitly asks for a standalone audit file.

If review findings depend on facts outside the draft, label them as verification risks rather than definitive errors.

## Common Fixes

- If the title is vague, add the task or outcome.
- If the opening is slow, cut background.
- If the body is long, merge repeated sections.
- If the voice sounds AI-like, replace abstractions with facts and choices.
- If the markdown feels noisy, cut bold, quotes, and nested lists.
- If the article feels broad, cut one audience or one promise.
- If the article feels thin, add a concrete example, step, or consequence before adding adjectives.
