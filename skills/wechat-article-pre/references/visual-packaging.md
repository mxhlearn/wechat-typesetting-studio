# Visual Packaging

Use this file when deciding whether the article needs visual support and where visuals belong.

For cover dimensions, style controls, cover copy, default cover suggestion, and prompt structure, read [cover-brief.md](cover-brief.md).

For cover inspection and retry decisions, read [cover-qa.md](cover-qa.md).

## Rule

Finish the article first. Then define visuals.

Do not make a cover or illustration carry work the article has not done.

## Visual Decision

Choose the lightest useful support:

- No visual: when the article is already clear and short.
- Image note: when the user needs a screenshot, diagram, or cover placeholder.
- Separate visual brief: only when the user explicitly asks for one.
- Generated cover: only when the user asks for a raster cover.

If visuals would slow delivery without improving reader action, skip optional illustrations and keep the article clean.

For tutorial, installation, setup, configuration, tool onboarding, and workflow articles, screenshot/image slots are useful by default. Add short `Image Note` lines near the relevant steps unless the user explicitly asks for text-only output.

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
- place screenshot notes immediately after the action or verification they support
- include at least one screenshot note for a UI-heavy tutorial, and usually 2 to 4 notes for a multi-step install/setup article
- use the note to name the missing proof, not to describe decoration

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

Default article handoff should still include a short cover suggestion near the end of `final-article.md`, even when no cover image is generated. Use the pattern in [cover-brief.md](cover-brief.md) and keep it concise enough to be publishable or easy to delete.

Keep article image notes short:

```markdown
[Image Note: place a real settings screenshot here]
[Cover Note: clean process cover, no fake UI]
```

If the article already includes a generated `cover-image.png`, replace this section with a one-line cover note or omit it when the user wants the article body only.

## QA

Before delivery, check:

- Does every visual slot serve a reader task?
- Is proof separated from concept art?
- Are screenshot notes short and placed near the relevant step?
- Is cover planning kept out of `final-article.md` unless requested?
- Does `final-article.md` include useful screenshot/image slots for tutorial steps?
- Does the ending include a concise cover suggestion when no generated cover asset or visual brief exists?
- Is `final-article.md` still clean WeMD Markdown?
- Are all generated-image prompts outside `final-article.md`?
- Are empty visual sections omitted from `visual-brief.md`?
- Do visual notes explain the purpose of the image, not just its appearance?
