---
name: wechat-article-pre
description: Use when drafting, rewriting, polishing, packaging, or reviewing Chinese WeChat official account content into WeMD-ready Markdown. Covers rough drafts, notes, outlines, tutorials, commentary, reviews, list posts, explainers, case reviews, news/update digests, interviews/profiles, title/opening work, benchmark public-account style learning, feedback learning, cover briefs, cover prompt shaping, cover QA, visual notes, and final publication-readiness audits. Prioritize direct WeMD-adapted layout, precise Chinese writing, article-shape routing, low-AI voice, concise structure, factual restraint, GitHub-flavored Markdown compatibility, and light visual packaging.
---

# WeChat Article Pre

Use this skill to turn raw WeChat public-account content into finished WeMD-ready Markdown. Default output is one article file plus image assets.

## Defaults

Default to:

- Chinese-first output
- substance before packaging
- direct WeMD-adapted Markdown layout
- low-AI voice
- light visuals only when useful

If the brief is clear, draft or rewrite directly. Ask only for missing facts that would change the article.

Do not pad. Prefer a shorter finished article over a longer smooth draft.

## Scope

Use this skill for upstream WeChat content work:

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

If the request mixes shapes, choose one primary shape and one support shape. Example: a tutorial may use commentary in the opening, but the steps and verification still control the structure.

## Workflow

1. Lock the mission in one sentence.
2. Choose the article shape.
3. Identify protected facts, links, commands, quotes, images, and constraints.
4. If benchmark articles, sample accounts, or reusable style files exist, extract a style profile and borrow/avoid constraints before planning the article.
5. Choose the final title, opening move, section order, and any useful in-article subheading alternatives.
6. Draft or rewrite from the strongest point.
7. Cut generic lines and repeated ideas.
8. Check factual restraint and unsupported claims.
9. Apply WeMD layout rules before delivery.
10. Add in-article subheading alternatives and image notes only when useful.
11. Run final audit internally; do not write audit notes as an output file unless explicitly requested.

## Reference Routes

Read only what the task needs:

- Writing and structure: [references/editorial-playbook.md](references/editorial-playbook.md), [references/originality-and-voice.md](references/originality-and-voice.md), [references/layout-and-style.md](references/layout-and-style.md).
- WeMD formatting and output: [references/wemd-handoff-contract.md](references/wemd-handoff-contract.md), [references/wemd-capability-matrix.md](references/wemd-capability-matrix.md), [references/wemd-visual-rhythm.md](references/wemd-visual-rhythm.md).
- Feedback or benchmark style learning: [references/content-learning-loop.md](references/content-learning-loop.md), [references/wechat-style-learning.md](references/wechat-style-learning.md).
- Visuals and covers: [references/visual-packaging.md](references/visual-packaging.md), [references/cover-brief.md](references/cover-brief.md), [references/cover-qa.md](references/cover-qa.md), and [references/cover-prompt-recipes.md](references/cover-prompt-recipes.md) only for actual generation or prompt output.
- Spread/title packaging: [references/wechat-viral-patterns.md](references/wechat-viral-patterns.md).
- Final checks or skill regression checks: [references/quality-gates.md](references/quality-gates.md).

## Deliverable Contract

Default to a folder in the current session working directory, named after the article title.

Place publishable outputs inside that folder:

- `final-article.md`
- `cover-image.png` when a raster cover is generated
- other image files when generated or supplied for the article

`final-article.md` must:

- read like a finished article
- contain one `#` title
- use `##` for main sections
- use `###` only when needed
- avoid raw HTML unless the user explicitly asks for WeMD/CSS customization
- avoid TODOs, prompt residue, and editor notes
- keep image notes short and standalone
- use `## References` only when links must stay

Default to no sidecar files. The normal deliverable is one article file plus image assets.

The review pass is an internal quality gate. Do not materialize it as `review-notes.md` during normal drafting, rewriting, polishing, or packaging.

Create sidecars only when explicitly requested:

- `style-profile.md` for reusable style memory
- `visual-brief.md` for a separate visual plan
- `review-notes.md` for a standalone audit report

Do not create `title-options.md` by default. Use one final H1 title in `final-article.md`. When heading choices are useful, place concise alternatives beside the relevant `##` or `###` heading inside `final-article.md`.

When planning visuals internally, keep the plan out of `final-article.md` unless the user asks for `visual-brief.md`.

If the user asks for an actual raster cover, stabilize a compact visual plan first, then use the image-generation workflow and inspect the result before delivery.

## Article Rules

For tutorials, setup guides, workflow guides, or tool walkthroughs:

- preserve required steps, links, commands, screenshots, and verification
- prefer direct headings
- keep action, reason, and verification together
- label shell environments clearly
- use fenced code blocks with language tags
- mark real screenshot slots with standalone image notes
- do not fabricate screenshots, terminal output, or UI states
- keep heading depth at `###` or above

## Guardrails

Stay in article preparation. Keep facts accurate, avoid fake screenshots or invented UI states, do not copy benchmark-account wording, and do not promise platform results.

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
- Markdown is already formatted for WeMD preview/copy flow
- internal commentary is gone

When the user asks only for a review, return findings first, grouped by severity or publishing impact. Do not rewrite the full article unless asked.
