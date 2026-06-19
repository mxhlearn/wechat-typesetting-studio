# WeMD Handoff Contract

Use this file when the final article must work cleanly in WeMD and then be copied to a WeChat public-account editor.

WeMD reference: `https://github.com/tenngoxars/WeMD`. Treat WeMD as a Markdown-first WeChat formatting tool. Do not assume publishing automation.

## Output Folder

Default to creating one article folder in the current session working directory.

Folder name:

- derive it from the final article title
- keep Chinese characters when useful
- remove Windows-invalid characters: `< > : " / \ | ? *`
- trim trailing spaces and dots
- if the title is missing, use a concise topic slug
- if the folder already exists, reuse it only when continuing the same article; otherwise append a short date or numeric suffix
- keep the folder near the active session/workspace directory unless the user gives an output path
- do not include the user's personal computer path in article content, README examples, or sidecar notes

Example:

```text
当前会话目录/
  让 Codex 桌面版更稳地跑起来/
    final-article.md
    visual-brief.md
    cover-image.png
```

Do not write article outputs to a generic `output/` directory unless the user explicitly asks for it.

If the user gives a specific output directory, use that directory and keep filenames stable.

## Final Shape

`final-article.md` should contain:

- one `#` title
- one short opening line after the title when useful
- 3 to 5 `##` sections for most articles
- `###` only when a section needs another layer
- a short closing section or CTA
- `## References` only when links must stay

Avoid:

- multiple H1 titles
- raw HTML for layout, color, or spacing unless the user explicitly asks for WeMD/CSS customization
- deeply nested headings
- table-heavy layouts unless comparison is essential
- editor notes
- TODOs
- prompt residue

## WeMD Import Rules

WeMD supports Markdown-centered writing and WeChat copy workflows. Prefer portable Markdown over editor-specific decoration.

Use:

- GitHub-flavored Markdown basics
- fenced code blocks with language tags
- simple tables only when the article truly needs comparison
- Mermaid notes only when the user asks for diagrams and confirms WeMD rendering is desired
- image placeholders that the user can replace with real assets
- short bracket notes for screenshots, covers, and diagrams

Do not:

- use raw HTML for layout, color, spacing, or cards by default
- assume WeMD-specific theme CSS will exist for every reader
- leave "Assumption", "Plan", "Draft", "Review", or "Next action" labels inside the publishable article
- include prompts, system notes, or editing rationale in the article body
- include multiple competing titles in the article body
- rely on complex nested lists to create visual hierarchy
- rely on hidden editor behavior that was not verified

## Image Notes

Use short bracket notes only:

```markdown
[Image Note: place a real terminal screenshot after verification]
[Cover Note: clean editorial cover, no fake UI screenshot]
```

For tutorials:

- use real screenshots for UI, settings, terminal output, and verification
- use AI images only for covers, concept diagrams, or section breaks
- never replace a required screenshot with a fake image

If image hosting, upload, or local asset handling matters, ask the user how they use WeMD. Do not invent an image-host workflow.

## Sidecar Rules

Use sidecars only when they reduce clutter:

- `title-options.md`: title choices only
- `visual-brief.md`: cover, image slots, prompts, asset names
- `review-notes.md`: editorial risks and fixes
- `style-profile.md`: reusable benchmark style constraints, without copied source text

Do not duplicate full article content across sidecars.

Default sidecar rule:

- no sidecar if the user asked for a single final article
- `title-options.md` only when title choices are useful or requested
- `visual-brief.md` only when cover or image planning matters
- `review-notes.md` only when risk, rationale, or editorial notes help
- `style-profile.md` only when benchmark learning or future reuse matters

## Final Check

Before delivery, verify:

- one H1 only
- headings no deeper than H3
- short paragraphs
- tagged code fences
- short image notes
- no raw HTML unless an explicit WeMD/CSS customization request was verified
- no publishing notes
- no internal commentary
- Markdown is ready for WeMD preview and copy flow
