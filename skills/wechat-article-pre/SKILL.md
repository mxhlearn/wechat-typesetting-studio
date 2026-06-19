---
name: wechat-article-pre
description: Use when drafting, rewriting, polishing, packaging, or reviewing Chinese WeChat official account content into editor-ready Markdown, with WeMD as the default handoff target. Covers rough drafts, notes, outlines, tutorials, commentary, reviews, list posts, explainers, case reviews, news/update digests, interviews/profiles, title/opening work, benchmark public-account language/layout learning, content feedback learning, cover briefs, cover prompt shaping, cover-generation QA, visual notes, and final publication-readiness audits. Prioritize precise Chinese writing, article-shape routing, low-AI voice, concise structure, factual restraint, WeMD handoff cleanliness, GitHub-flavored Markdown compatibility, and light visual packaging; avoid publishing automation, browser upload flows, HTML-first export, fake screenshots, or multi-session orchestration.
---

# WeChat Article Pre

Use this skill to turn raw WeChat public-account content into clean, publishable Markdown. Default to WeMD as the current editor target.

## Defaults

Default to:

- Chinese-first output
- one-session delivery
- substance before packaging
- WeMD-friendly Markdown
- low-AI voice
- light visuals only when useful
- no publishing automation

If the brief is clear, draft or rewrite directly. Ask only for missing facts that would change the article.

Do not pad. Prefer a shorter finished article over a longer smooth draft.

## Scope

Use this skill for the full upstream WeChat content workflow:

- tutorial
- commentary
- review
- explainer
- list post
- case review
- news/update digest
- interview/profile
- draft rewrite
- title/opening repair
- benchmark account style learning
- cover brief
- feedback-driven revision
- audit and polish

If the shape is unclear, infer it from the source and state the assumption before writing.

When feedback exists, convert it into concrete editing constraints before revising.

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

## Workflow

1. Lock the mission in one sentence.
2. Choose the article shape.
3. If benchmark articles, sample accounts, or reusable style files exist, extract a style profile and borrow/avoid constraints before planning the article.
4. Choose the promise, title direction, opening move, and section order.
5. Draft or rewrite from the strongest point.
6. Cut generic lines and repeated ideas.
7. Check factual restraint and unsupported claims.
8. Tighten Markdown for WeMD.
9. Add title options, cover brief, or image notes only when useful.
10. Run final audit.

For title, opening, structure, CTA, and review rules, read [references/editorial-playbook.md](references/editorial-playbook.md).

For voice, anti-AI cleanup, and rewrite discipline, read [references/originality-and-voice.md](references/originality-and-voice.md).

For layout, paragraph length, and tutorial rhythm, read [references/layout-and-style.md](references/layout-and-style.md).

For WeMD handoff rules, Markdown compatibility, copy-to-WeChat constraints, image notes, and output folder rules, read [references/wemd-handoff-contract.md](references/wemd-handoff-contract.md).

For WeMD-specific features such as GFM tables, Mermaid, math, image hosting, custom themes, CSS, or copy behavior, read [references/wemd-capability-matrix.md](references/wemd-capability-matrix.md).

For WeMD visual rhythm, first-screen density, mobile scanability, theme-aware Markdown, or public-account reading experience, read [references/wemd-visual-rhythm.md](references/wemd-visual-rhythm.md).

For user feedback, repeated quality issues, or self-improving revision behavior, read [references/content-learning-loop.md](references/content-learning-loop.md).

For sample public-account articles, benchmark account language, layout style learning, or "write like this but for my topic" requests, read [references/wechat-style-learning.md](references/wechat-style-learning.md).

For deciding whether visuals are needed and where they belong in the article, read [references/visual-packaging.md](references/visual-packaging.md).

For cover planning, cover dimensions, visual style controls, cover copy, and generation-ready brief structure, read [references/cover-brief.md](references/cover-brief.md).

For cover inspection, crop safety, clutter control, text accuracy, and retry decisions, read [references/cover-qa.md](references/cover-qa.md).

For actual raster cover generation prompt recipes, read [references/cover-prompt-recipes.md](references/cover-prompt-recipes.md) after the visual brief is stable.

For current WeChat title and first-screen packaging patterns, read [references/wechat-viral-patterns.md](references/wechat-viral-patterns.md) when the user asks for stronger spread, shareability, or public-account packaging.

## Deliverable Contract

Default to a folder in the current session working directory, named after the article title.

Place publishable outputs inside that folder:

- `final-article.md`
- `visual-brief.md` when useful
- `title-options.md` when useful
- `review-notes.md` when useful
- `style-profile.md` when the user explicitly asks to learn from benchmark articles/accounts or reuse style later
- `cover-image.png` when a raster cover is generated

The final article file must:

- read like a finished article
- contain one `#` title
- use `##` for main sections
- use `###` only when needed
- avoid raw HTML unless the user explicitly asks for WeMD/CSS customization
- avoid TODOs, prompt residue, and editor notes
- keep image notes short and standalone
- use `## References` only when links must stay

Add sidecar files only when they help:

- `title-options.md`
- `visual-brief.md`
- `review-notes.md`
- `style-profile.md`

If the user asks for a single file, keep all publishable content in `final-article.md`.

`visual-brief.md` is for planning visuals. Do not put long image prompts in `final-article.md`.

If the user asks for an actual raster cover, stabilize the `visual-brief.md` first, then use the image-generation workflow and inspect the result before delivery.

## Tutorial Rules

When the article is a tutorial, setup guide, workflow guide, or tool walkthrough:

- preserve required steps, links, commands, screenshots, and verification
- prefer direct headings
- keep action, reason, and verification together
- label shell environments clearly
- use fenced code blocks with language tags
- mark real screenshot slots with standalone image notes
- do not fabricate screenshots, terminal output, or UI states
- keep heading depth at `###` or above

## Boundaries

Do not turn this skill into a downstream publishing tool.

Do not provide:

- WeChat API publishing
- browser-assisted publishing
- automated draft upload
- HTML-first export pipelines
- multi-agent publishing orchestration
- large publish packages
- broad image-generation decision trees

## Final Audit

Before delivery, verify:

- title matches the promise
- opening earns the next scroll
- each section has one job
- repeated ideas are cut
- voice sounds specific and edited
- shape matches content
- tutorial steps are executable
- user feedback has been applied without overfitting
- Markdown is ready for WeMD preview/copy flow
- internal commentary is gone

When the user asks only for a review, return findings first, grouped by severity or publishing impact. Do not rewrite the full article unless asked.
