---
name: wechat-article-pre
description: Use when drafting, rewriting, polishing, packaging, or reviewing Chinese WeChat official account content into WeMD-ready Markdown. Covers rough drafts, notes, outlines, tutorials, commentary, reviews, list posts, explainers, case reviews, news/update digests, interviews/profiles, title/opening work, benchmark public-account style learning, feedback learning, adaptive editorial composition, cover briefs, cover prompt shaping, cover QA, visual notes, and final publication-readiness audits. Prioritize direct WeMD-adapted layout, precise Chinese writing, article-shape routing, human-like component placement, low-AI voice, concise structure, factual restraint, GitHub-flavored Markdown compatibility, and light visual packaging.
---

# WeChat Article Pre

Use this skill to turn raw WeChat public-account material into finished WeMD-ready Markdown. Default delivery is one article-title folder containing `final-article.md` plus useful image assets.

## Operating Defaults

- Write Chinese-first, publishable prose.
- Preserve protected facts, links, commands, quotes, images, and constraints.
- Choose the article shape, layout rhythm, and components from the article's job instead of forcing a fixed template.
- Use screenshots, tables, callouts, code blocks, quotes, diagrams, and references when they clarify, prove, compare, warn, verify, or improve reading rhythm.
- Keep the voice concise, specific, and edited; avoid formulaic openings, repeated reassurance, and FAQ-style serious tutorials unless the source or user asks for that shape.
- Apply WeMD-ready Markdown before delivery.
- Default output is one article folder with `final-article.md` plus image assets. Do not create sidecars unless explicitly requested.
- Tutorial/setup/tool walkthrough drafts include concrete screenshot/image slots by default.
- Final drafts include a concise cover suggestion unless the user explicitly opts out or a cover asset/visual brief replaces it.
- Keep personal local paths, account details, keys, and machine-specific information out of publishable output unless the user explicitly says the detail is meant to be public.

If the brief is clear, draft or rewrite directly. Ask only for missing facts that would change the article.

Do not pad. Prefer a shorter finished article over a longer smooth draft.

## Shape Routing

Choose the narrowest shape that fits the request:

- Tutorial or setup guide: action, reason, verification.
- Commentary or review: tension, interpretation, implication.
- Explainer or concept note: definition, boundary, method.
- Source draft rewrite: preserve the point, repair the structure.
- Checklist or list post: compact scope, easy scan, clear grouping.
- Case review or reflection: facts, decision, result, lesson.
- News or update digest: fact, context, impact, caveat.
- Interview or profile: scene, person, judgment, takeaway.
- Audit or polish: title, opening, structure, voice, WeMD readiness.

If the request mixes shapes, choose one primary shape and one support shape. Example: a tutorial may use commentary in the opening, but the steps and verification still control the structure.

If the shape is unclear, infer it from the source and mention the assumption outside the article only when it affects scope. When feedback exists, convert it into concrete editing constraints before revising.

## Workflow

1. Lock the mission, reader, article shape, and protected facts.
2. Load only the references needed for the task.
3. If benchmark articles, sample accounts, or reusable style files exist, extract transferable constraints before planning.
4. Choose the final title, opening move, section order, component plan, image slots, and cover handling.
5. Draft or rewrite from the strongest point, then cut generic lines and repeated ideas.
6. Apply the WeMD handoff contract and quality gates.
7. When `final-article.md` is created or edited, run `scripts/check_article_output.py` on the article folder before delivery.
8. Keep review/audit notes internal unless the user explicitly asks for a standalone report.

## Reference Routes

Read only what the task needs:

- Writing and structure: [references/editorial-playbook.md](references/editorial-playbook.md), [references/editorial-composition.md](references/editorial-composition.md), [references/originality-and-voice.md](references/originality-and-voice.md), [references/layout-and-style.md](references/layout-and-style.md).
- WeMD formatting and output: [references/wemd-handoff-contract.md](references/wemd-handoff-contract.md), [references/wemd-capability-matrix.md](references/wemd-capability-matrix.md), [references/wemd-visual-rhythm.md](references/wemd-visual-rhythm.md), and [references/wemd-component-patterns.md](references/wemd-component-patterns.md) only when concrete syntax examples are needed.
- Feedback or benchmark style learning: [references/content-learning-loop.md](references/content-learning-loop.md), [references/wechat-style-learning.md](references/wechat-style-learning.md).
- Visuals and covers: [references/visual-packaging.md](references/visual-packaging.md), [references/cover-brief.md](references/cover-brief.md), [references/cover-qa.md](references/cover-qa.md), and [references/cover-prompt-recipes.md](references/cover-prompt-recipes.md) only for actual generation or prompt output.
- Spread/title packaging: [references/wechat-viral-patterns.md](references/wechat-viral-patterns.md).
- Final checks or skill regression checks: [references/quality-gates.md](references/quality-gates.md).

## Deliverable Contract

Follow [references/wemd-handoff-contract.md](references/wemd-handoff-contract.md) for file placement, naming, WeMD-safe Markdown, image notes, sidecars, and final shape.

Normal output is `final-article.md` plus generated or supplied image assets. If the user asks for an actual raster cover, stabilize a compact visual plan, use the cover references, and inspect the result before delivery.

## Article Rules

Open from a concrete task, friction, scene, fact, or judgment. Do not default to "three things", "several points", "first/second/finally", or other meta-outline openings unless the article is explicitly a list or checklist.

Compose the article like a finished public-account post. Choose the layout style and component placement from the article's job; do not force every article into the same skeleton.

For tutorials, setup guides, workflow guides, or tool walkthroughs, preserve required steps, links, commands, screenshots, verification, and environment labels. Use direct headings, pair each action with its reason or verification, reserve screenshot slots near the step they support, and avoid FAQ-style self-questioning unless the user requests it or the source is truly Q&A.

Use one final `#` title. Do not generate main-title option files by default. Do not list heading alternatives outside the publishable flow unless the user explicitly asks for editable alternatives.

## Guardrails

Stay in article preparation. Keep facts accurate, avoid fake screenshots or invented UI states, do not copy benchmark-account wording, do not promise platform results, and do not remove useful TIPs, tables, images, references, or callouts merely to make the article plain.

## Final Audit

Before delivery, verify the essentials, then use [references/quality-gates.md](references/quality-gates.md) when the task is substantial or a file is written:

- title matches the promise
- shape matches content
- voice sounds specific, concise, and edited
- layout style and components match the article job
- tutorial image slots and cover suggestion are present when useful
- Markdown is formatted for WeMD preview/copy flow
- no personal local path, account detail, secret, or machine-specific note leaked into publishable content
- `scripts/check_article_output.py` passes without warnings unless the user explicitly accepts the warning
- internal commentary is gone

When the user asks only for a review, return findings first, grouped by severity or publishing impact. Do not rewrite the full article unless asked.
