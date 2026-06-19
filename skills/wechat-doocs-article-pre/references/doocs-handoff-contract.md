# Doocs Handoff Contract

Use this file when the final article must import cleanly into Doocs.

## Output Folder

Default to creating one article folder in the current session working directory.

Folder name:

- derive it from the final article title
- keep Chinese characters when useful
- remove Windows-invalid characters: `< > : " / \ | ? *`
- trim trailing spaces and dots
- if the title is missing, use a concise topic slug
- if the folder already exists, reuse it only when continuing the same article; otherwise append a short date or numeric suffix

Example:

```text
当前会话目录/
  让 Codex 桌面版更稳地跑起来/
    final-article.md
    visual-brief.md
    cover-image.png
```

Do not write article outputs to a generic `output/` directory unless the user explicitly asks for it.

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
- decorative separators
- raw HTML
- deeply nested headings
- table-heavy layouts
- editor notes
- TODOs
- prompt residue

## Import Rules

- Keep the first screen light.
- Keep headings semantic.
- Keep screenshot and cover notes short.
- Keep command blocks fenced and labeled.
- Keep links readable in plain Markdown.
- Put image prompt detail in `visual-brief.md`, not in the article body.
- Keep cover notes out of the first paragraph.
- Keep title options out of `final-article.md` unless the user requested single-file packaging.

Do not:

- use HTML for spacing, color, or alignment
- stack quotes, bold lines, and lists before the article begins
- leave draft-note language in the final file
- leave "Assumption", "Plan", "Draft", "Review", or "Next action" labels inside the publishable article
- include prompts, system notes, or editing rationale in the article body
- include multiple competing titles in the article body

## Image Notes

Use short bracket notes only:

```markdown
[Image Note: place a real terminal screenshot after verification]
[Cover Note: clean editorial cover, no fake UI screenshot]
```

For tutorials:

- use real screenshots for real workflows
- use AI images for covers, concept diagrams, or section breaks
- never replace a required screenshot with a fake image

## Final Check

Before delivery, verify:

- one H1 only
- headings no deeper than H3
- short paragraphs
- tagged code fences
- short image notes
- no raw HTML
- no publishing notes
- no internal commentary
- direct paste into Doocs is possible

## Sidecar Rules

Use sidecars only when they reduce clutter:

- `title-options.md`: title choices only
- `visual-brief.md`: cover, image slots, prompts, asset names
- `review-notes.md`: editorial risks and fixes
- `style-profile.md`: reusable benchmark style constraints, without copied source text

Do not duplicate full article content across sidecars.
