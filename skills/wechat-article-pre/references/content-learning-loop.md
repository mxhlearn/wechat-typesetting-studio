# Content Learning Loop

Use this file when the user gives feedback on article quality, style, structure, cover quality, or previous outputs.

## Rule

Treat feedback as reusable editing evidence.

Do not claim permanent memory. Learn inside the current task by extracting stable preferences, failure patterns, and stricter next-pass rules.

Portable learning lives in files the user explicitly asks to keep, usually `style-profile.md`.

## Feedback Intake

When the user says something like "too watery", "not rigorous", "too narrow", "cover is messy", or "you optimized away my tutorial", convert it into editing rules:

- What failed?
- Where did it fail?
- What should be protected next time?
- What should be cut or reduced?
- What should be added to the review pass?

If feedback conflicts with an earlier rule, prefer the user's newer feedback unless it would create factual or publishing risk.

If the feedback is emotional but not specific, infer one likely rule and verify it against the artifact before changing the skill or profile.

## Style Sources

When the user provides benchmark articles, previous successful posts, brand notes, GitHub-style writing references, or sample public-account articles, learn from patterns, not wording.

For public-account language and layout learning, also read [wechat-style-learning.md](wechat-style-learning.md).

Extract:

- promise type
- opening move
- paragraph density
- section rhythm
- evidence threshold
- transition style
- CTA restraint
- terminology and formatting habits

Do not copy:

- distinctive metaphors
- sentence cadence
- named examples not supplied by the user
- full section order unless it serves the current article

Borrow useful public-writing discipline:

- Chinese copywriting guides: spacing, punctuation, and typography consistency.
- Technical writing guides: concrete headings, user task first, no ornamental explanation.
- Prompt-engineering guides: turn feedback into explicit constraints, then test against failure modes.

## Learning Note

Before revising, create a short private learning note:

```text
Feedback learned:
- Protect:
- Avoid:
- Raise:
- Next pass must check:
- Applies to:
- Do not overfit:
```

Do not put this note in `final-article.md`.

Do not create `review-notes.md` unless the user explicitly asks for a standalone audit file.

## Article Adaptation

Apply feedback at three levels:

- Strategy: adjust article shape, reader promise, scope, and evidence threshold.
- Structure: change section order, merge repeated sections, restore missing steps, or add verification.
- Sentence: cut filler, qualify claims, remove generic transitions, and replace vague phrases with concrete facts.

Do not simply rewrite the same structure with smoother wording.

## Preference Ledger

Within the task, maintain a compact preference ledger:

- Voice: concise, rigorous, low-fluff.
- Structure: protect operational steps and verification in tutorials.
- Scope: keep the skill broad for all WeChat articles, not one source folder.
- Cover: use structured briefs, one focal subject, and default 2.35:1.
- Output: create an article-title folder in the current session directory.
- WeMD: final Markdown must stay clean, preview-friendly, and copy-ready.
- Evidence: protect source facts and mark freshness risks.
- Reader: tune detail level to novice, experienced, decision maker, or follower.

Update the ledger when the user gives new concrete feedback.

When the user provides an existing `style-profile.md`, merge it with the current brief:

1. Keep explicit user instructions from the current task first.
2. Keep durable preferences from the profile second.
3. Add new feedback only if it is concrete.
4. Drop stale rules that conflict with the current article shape.
5. Do not preserve rules that caused the previous failure.

Write the merged rules into a short private note before drafting.

## Style Profile Template

When style learning matters, build this compact profile before rewriting:

```text
Style profile:
- Reader:
- Promise:
- Opening:
- Density:
- Evidence:
- Section rhythm:
- Words to prefer:
- Words to avoid:
- Formatting habits:
- Non-negotiables:
- Reader level:
- Evidence threshold:
- Feedback history:
- Last updated from:
```

Keep it private unless the user asks for review notes.

If the user wants the style reused across later articles, write a compact `style-profile.md` sidecar. Do not store copied source text in it.

Treat that file as the portable memory. On future tasks, read it when the user provides it, then update it only from new feedback or new examples.

Keep `style-profile.md` actionable:

- write constraints, not praise
- keep each bullet short
- include "protect" and "avoid" rules
- record article shapes the profile applies to
- avoid storing source paragraphs, private snippets, or full benchmark excerpts

Recommended `style-profile.md` sections:

```markdown
# Style Profile

## Applies To

## Voice

## Structure

## Evidence

## Formatting

## Protect

## Avoid

## Update Notes
```

Keep update notes brief: date/source type and what changed, not a changelog.

## Feedback To Rule Conversion

Use this conversion table:

| Feedback | Rule to add |
| --- | --- |
| 太水 | cut paragraphs without fact, judgment, step, example, consequence, or contrast |
| 不严谨 | qualify claims, mark uncertainty, and remove unsupported promises |
| 太窄 | check whether the rule overfits one article before adding it to the skill/profile |
| 教程被优化掉 | protect required steps, links, screenshots, commands, and verification lines |
| 封面杂乱 | enforce one focal subject, one metaphor, one style direction, `2.35:1` |
| 太像 AI | replace generic transitions with concrete task, choice, or evidence |
| 排版不适合公众号 | shorten paragraphs, reduce nesting, and check first-screen density |
| 标题没吸引力 | make the subject, promise, and boundary visible without exaggeration |
| 开头没抓住人 | start with task, friction, contrast, or judgment within 2 paragraphs |
| 太散 | lock one mission sentence and remove sections that do not serve it |
| 风格不像我 | preserve the user's viewpoint, preferred terms, and judgment rhythm |
| 太像别人 | rebuild from the user's facts and constraints; do not synonym-swap |
| 信息不准 | add freshness checks and separate fact from interpretation |
| 太基础 | reduce definitions and focus on caveats, differences, or decisions |
| 看不懂 | add one definition, one example, or one verification line near the confusion |

## Self-Review Loop

Before final delivery after feedback, run this loop:

1. Restate the learned constraint in one sentence.
2. Identify the affected files or article sections.
3. Revise the smallest useful surface.
4. Check the old failure mode is gone.
5. Check the revision did not overfit to one sample.

For article outputs, add one extra pass:

- Does this revision generalize to the user's future article types?
- Did it preserve original facts, tutorial steps, and real constraints?
- Did it reduce filler without making the article stiff?
- Did it update the portable profile only when the new rule should survive future tasks?

If the same feedback appears twice, promote it from one-off note to reusable style/profile constraint.

## Failure Modes

- Treating one feedback sample as the whole product scope.
- Overfitting the skill to a single article.
- Saying "learned" but only adding generic reminders.
- Making the article longer instead of sharper.
- Hiding uncertainty or inventing facts to sound more confident.
- Putting internal learning notes inside publishable Markdown.
- Copying a reference style so closely that the article loses the user's own point.
- Treating `style-profile.md` as permanent truth instead of a user-editable working brief.
- Updating many references for a one-off preference that belongs only in the chat response.
