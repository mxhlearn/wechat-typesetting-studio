# Quality Gates

Use this file for final delivery checks or regression checks after changing the skill.

Keep the check focused on output quality: one finished article, useful image assets, clean WeMD formatting, and no process residue.

## Load Gate

Read only the references needed for the task:

- Rewrite draft: `editorial-playbook.md`, `originality-and-voice.md`, `layout-and-style.md`, `wemd-handoff-contract.md`.
- Tutorial: add tutorial guidance in `editorial-playbook.md` and `wemd-visual-rhythm.md`.
- Style learning: `wechat-style-learning.md`, `content-learning-loop.md`, then writing/layout references.
- Cover or visual assets: `visual-packaging.md`, `cover-brief.md`, `cover-qa.md`; read `cover-prompt-recipes.md` only for actual generation or prompt output.
- WeMD advanced feature: `wemd-capability-matrix.md`.
- Spread/title packaging: `wechat-viral-patterns.md`.

Avoid loading every reference by default.

## Delivery Gate

Before delivery, verify:

- `final-article.md` reads like a publishable article, not a plan.
- The article has exactly one `#` title.
- Main sections use `##`; local subsections use `###` only when useful.
- Paragraphs are short enough for mobile reading.
- Lists, tables, callouts, code blocks, images, Mermaid, and math are used only when they clarify the article.
- Tutorial steps preserve required links, commands, screenshots, verification, and environment labels.
- Claims are restrained and unsupported facts are removed or marked as uncertain.
- Benchmark style is transformed into constraints, not copied phrasing.
- The output folder is named after the article title unless the user gave a path.
- The output folder contains only `final-article.md`, requested sidecars, and image assets.
- No generic `output/` folder is used unless requested.
- No personal local path appears unless intentionally part of the article.
- No README, changelog, quick reference, process log, prompt residue, or editor note appears in the article output.

## Sidecar Gate

Default output is one article plus image assets.

Create these only when the user explicitly asks:

- `style-profile.md`
- `visual-brief.md`
- `review-notes.md`

Do not create `title-options.md` by default. Put useful `##` or `###` heading alternatives directly near the relevant section in `final-article.md`.

## Visual Gate

For covers:

- Ratio is `2.35:1` unless the user asks otherwise.
- One focal subject, one metaphor, one rendering style.
- No fake screenshots, fake terminal output, invented UI states, watermarks, or random icon piles.
- Generated cover text is omitted unless short text is essential and can be verified.
- A failed text render switches to no-text cover plus post-edit text guidance.

For article images:

- Real screenshots are required for proof-heavy tutorial steps.
- AI images are acceptable for covers, concept diagrams, or section breaks.
- Image notes are short and publishable when the actual image is missing.

## Forward-Test Prompts

Use these after major revisions:

```text
Use $wechat-article-pre to rewrite a Windows tool setup draft for WeMD. Preserve links, commands, screenshots, and verification. Output final-article.md only.
```

```text
Use $wechat-article-pre to learn from three public-account samples and draft an original explainer for a different topic. Save style-profile.md only because I explicitly asked for reusable style memory.
```

```text
Use $wechat-article-pre to turn a rough commentary outline into a WeMD-ready article with a 2.35:1 cover image.
```

Expected pass signals:

- final output is article-first, not notes-first
- no unrequested sidecars
- no separate main-title option file
- WeMD formatting is applied before delivery
- tutorial facts and steps survive polishing
- cover guidance stays visually coherent

## Revision Check

After changing this skill, confirm:

- `SKILL.md` stayed concise.
- Detailed rules live in references.
- New references are linked from `SKILL.md`.
- `agents/openai.yaml` still matches current behavior.
- `quick_validate.py` passes.
- Workspace and installed skill are synced when permissions allow.
