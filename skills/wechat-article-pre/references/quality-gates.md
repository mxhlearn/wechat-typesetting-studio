# Quality Gates

Use this file for final delivery checks or regression checks after changing the skill.

Keep the check focused on output quality: one finished article, useful image assets, clean WeMD formatting, and no process residue.

## Load Gate

Read only the references needed for the task:

- Rewrite draft: `editorial-playbook.md`, `editorial-composition.md`, `originality-and-voice.md`, `layout-and-style.md`, `wemd-handoff-contract.md`.
- Tutorial: add tutorial guidance in `editorial-playbook.md` and `wemd-visual-rhythm.md`.
- Style learning: `wechat-style-learning.md`, `content-learning-loop.md`, then writing/layout references.
- Cover or visual assets: `visual-packaging.md`, `cover-brief.md`, `cover-qa.md`; read `cover-prompt-recipes.md` only for actual generation or prompt output.
- WeMD advanced feature: `wemd-capability-matrix.md`.
- Spread/title packaging: `wechat-viral-patterns.md`.

Avoid loading every reference by default.

## Delivery Gate

Before delivery, verify:

- `final-article.md` reads like a publishable article, not a plan.
- The opening starts from a task, friction, scene, fact, or judgment, not from `三件事`, `几点`, `几个方面`, `首先/其次/最后`, or a table-of-contents announcement.
- The layout style matches the article job instead of following one fixed skeleton.
- Paragraphs are short enough for mobile reading.
- Reassurance phrases such as `不要着急`, `别急`, `不用担心`, and `放心` do not repeat; replace them with concrete checks, risks, or actions.
- Serious tutorials do not default to FAQ-style self-questioning; use declarative notes unless FAQ is requested or source-driven.
- Serious tutorials do not overuse rhetorical questions; if there are many Chinese question marks, convert most of them into action headings or notes.
- Serious tutorial headings do not rely on question-cue words such as `哪一版`, `怎么`, `为什么`, `是不是`, `要不要`, or `怎么办`; rewrite them as direct actions, choices, or checks.
- Lists, tables, callouts, code blocks, images, Mermaid, math, quotes, and references are placed where they clarify, prove, compare, warn, verify, or improve reading rhythm.
- Useful components are not removed merely to keep the article plain.
- Tutorial steps preserve required links, commands, screenshots, verification, and environment labels.
- Claims are restrained and unsupported facts are removed or marked as uncertain.
- Benchmark style is transformed into constraints, not copied phrasing.
- No personal local path appears unless intentionally part of the article.
- No README, changelog, quick reference, process log, prompt residue, or editor note appears in the article output.
- The handoff contract passes: one H1, clean WeMD Markdown, useful image notes, cover suggestion when needed, no unrequested sidecars, and no local path leaks.

When a publishable file exists on disk, run:

```bash
python scripts/check_article_output.py path/to/article-folder --article-type tutorial
```

Use the nearest matching `--article-type` when known. For final delivery, warnings are blockers by default.

Prefer targeted allowances over `--allow-warnings`:

- `--allow-faq`: when the user explicitly requested FAQ/Q&A structure.
- `--allow-raw-html`: when the user explicitly requested WeMD/CSS customization.
- `--allow-missing-cover`: when the user requested text-only delivery or no cover guidance.
- `--allow-bare-urls`: when exact visible URLs are more important than link polish.

Use `--allow-warnings` only when the user explicitly accepts every remaining warning.

The checker must pass on the article folder, not only the Markdown file, whenever the output folder exists. This verifies the normal contract: one `final-article.md`, generated/supplied images, and no unrequested sidecars.

## Sidecar Gate

Use [wemd-handoff-contract.md](wemd-handoff-contract.md) as the source of truth: default to no sidecars, create them only on explicit request, and keep heading/title alternatives out of the publishable flow unless requested.

## Visual Gate

For covers:

- Ratio is `2.35:1` unless the user asks otherwise.
- Generated cover assets must be checked by `scripts/check_article_output.py` through the output-folder check when the cover file exists.
- One focal subject, one metaphor, one rendering style.
- No fake screenshots, fake terminal output, invented UI states, watermarks, or random icon piles.
- Generated cover text is omitted unless short text is essential and can be verified.
- A failed text render switches to no-text cover plus post-edit text guidance.

For article images:

- Real screenshots are required for proof-heavy tutorial steps.
- AI images are acceptable for covers, concept diagrams, or section breaks.
- Image notes are short and publishable when the actual image is missing.
- Tutorial image notes must identify the proof to capture, not generic decoration.

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
- component placement feels edited, not template-leftover

## Revision Check

After changing this skill, confirm:

- `SKILL.md` stayed concise.
- Detailed rules live in references.
- New references are linked from `SKILL.md`.
- `agents/openai.yaml` still matches current behavior.
- `scripts/check_article_output.py` passes on representative clean, failing, and targeted-allowance examples when the script changes.
- `quick_validate.py` passes.
- Workspace and installed skill are synced when permissions allow.
