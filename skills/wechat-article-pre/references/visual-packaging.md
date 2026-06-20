# Visual Packaging

Use this file when deciding whether the article needs visual support and where visuals belong.

For cover dimensions, style controls, cover copy, and prompt structure, read [cover-brief.md](cover-brief.md).

For cover inspection and retry decisions, read [cover-qa.md](cover-qa.md).

## Rule

Finish the article first. Then define visuals.

Do not make a cover or illustration carry work the article has not done.

## Visual Decision

Choose the lightest useful support:

- No visual: when the article is already clear and short.
- Image note: when the user needs a screenshot, diagram, or cover placeholder.
- `visual-brief.md`: only when the user explicitly asks for a separate visual plan.
- Generated cover: only when the user asks for a raster cover.

If visuals would slow delivery without improving reader action, skip them and keep the article clean.

## Inline Images

Use inline images only when they help the reader act or understand.

Good slots:

- after the opening tension
- before a dense framework
- before a likely confusion point
- after a visible verification step

For tutorials:

- use real screenshots for UI, settings, terminal output, and verification
- use AI images only for cover, concept diagrams, or section breaks
- separate `Screenshot Slots` from `AI Illustration Slots`
- never replace a required proof screenshot with a generated image

## Article Shape Mapping

- Tutorial: screenshots for proof, cover for concept or process.
- Commentary: one metaphorical cover or one supporting illustration.
- Explainer: simple diagram only when prose is worse.
- Case review: one scene, object, or decision diagram.
- List post: visuals only if they improve scanning.
- News/update digest: factual cover, no alarmist imagery.
- Interview/profile: portrait, workspace, object detail, or no visual.

For any shape, do not mix proof visuals and mood visuals in the same slot.

## Output

When the user explicitly asks for `visual-brief.md`, include only useful parts:

- cover concept
- cover copy options
- image type and style
- prompt block when generation is requested
- screenshot slots
- diagram slots
- asset names
- source requirements for real screenshots when needed

Recommended structure:

```markdown
# Visual Brief

## Cover

## Screenshot Slots

## Diagram Slots

## Prompt Blocks

## Asset Names
```

Omit empty sections.

Do not put long prompts in `final-article.md`. If no `visual-brief.md` is requested, keep prompts internal and deliver only generated image assets.

Keep article image notes short:

```markdown
[Image Note: place a real settings screenshot here]
[Cover Note: clean process cover, no fake UI]
```

## QA

Before delivery, check:

- Does every visual slot serve a reader task?
- Is proof separated from concept art?
- Are screenshot notes short and placed near the relevant step?
- Is cover planning kept out of `final-article.md` unless requested?
- Is `final-article.md` still clean WeMD Markdown?
- Are all generated-image prompts outside `final-article.md`?
- Are empty visual sections omitted from `visual-brief.md`?
- Do visual notes explain the purpose of the image, not just its appearance?
