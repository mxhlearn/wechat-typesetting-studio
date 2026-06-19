# Content Learning Loop

Use this file when the user gives feedback on article quality, style, structure, cover quality, or previous outputs.

## Rule

Treat feedback as reusable editing evidence.

Do not claim permanent memory. Learn inside the current task by extracting stable preferences, failure patterns, and stricter next-pass rules.

## Feedback Intake

When the user says something like "too watery", "not rigorous", "too narrow", "cover is messy", or "you optimized away my tutorial", convert it into editing rules:

- What failed?
- Where did it fail?
- What should be protected next time?
- What should be cut or reduced?
- What should be added to the review pass?

If feedback conflicts with an earlier rule, prefer the user's newer feedback unless it would create factual or publishing risk.

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
```

Do not put this note in `final-article.md`.

Put it in `review-notes.md` only when the user asks for review rationale or when the note would help future manual editing.

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
- Doocs: final Markdown must stay clean and paste-ready.

Update the ledger when the user gives new concrete feedback.

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
```

Keep it private unless the user asks for review notes.

If the user wants the style reused across later articles, write a compact `style-profile.md` sidecar. Do not store copied source text in it.

Treat that file as the portable memory. On future tasks, read it when the user provides it, then update it only from new feedback or new examples.

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

## Failure Modes

- Treating one feedback sample as the whole product scope.
- Overfitting the skill to a single article.
- Saying "learned" but only adding generic reminders.
- Making the article longer instead of sharper.
- Hiding uncertainty or inventing facts to sound more confident.
- Putting internal learning notes inside publishable Markdown.
- Copying a reference style so closely that the article loses the user's own point.
