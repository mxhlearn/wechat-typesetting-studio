# WeMD Handoff Contract

Use this file when the final article must be directly formatted for WeMD and then copied to a WeChat public-account editor.

WeMD references: `https://wemd.app/docs/` and `https://github.com/tenngoxars/WeMD`. Treat WeMD as a Markdown-first WeChat formatting tool. Format the article before handoff; do not leave layout decisions as notes unless the asset is genuinely missing.

## Contents

- [Output Folder](#output-folder)
- [File Naming](#file-naming)
- [Final Shape](#final-shape)
- [WeMD Layout Rules](#wemd-layout-rules)
- [Component Patterns](#component-patterns)
- [WeMD Import Rules](#wemd-import-rules)
- [Image Notes](#image-notes)
- [Sidecar Rules](#sidecar-rules)
- [Final Check](#final-check)

## Output Folder

Default to creating one article folder in the most relevant article workspace.

Destination priority:

1. user-provided output path
2. current project/workspace when it is clearly an article workspace, such as `officialaccounts`
3. current session working directory

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
  把草稿整理成可发布文章/
    final-article.md
    cover-image.png
    section-01.png
```

Do not write article outputs to a generic `output/` directory unless the user explicitly asks for it.

If the user gives a specific output directory, use that directory and keep filenames stable.

## File Naming

Use stable file names:

- `final-article.md`: publishable article only
- `cover-image.png`: generated cover image
- `section-01.png`, `section-02.png`: generated or prepared article images when useful

Do not create process logs, changelogs, quick references, README files, or audit reports inside the skill output folder unless the user explicitly asks for them.

Default to no sidecars. Put publishable article content in `final-article.md` and images as separate assets.

## Final Shape

`final-article.md` should contain:

- one `#` title
- one short opening line after the title when useful
- 3 to 5 `##` sections for most articles
- `###` only when a section needs another layer
- a short closing section or CTA
- `## 封面建议` near the end when no `cover-image.png` or separate `visual-brief.md` is requested
- `## References` only when links must stay
- no file path that exposes the user's personal machine unless the user explicitly wants a local tutorial path shown

The final article should look composed for its article job, not copied from a universal skeleton. Use images, tables, callouts, code blocks, lists, quotes, diagrams, and references as editorial choices.

If links must remain, prefer:

- inline links for immediately useful resources
- `## References` for source lists, downloads, or nonessential background
- no bare long URL unless readability is less important than exact copying

Avoid:

- multiple H1 titles
- template placeholders or raw component snippet libraries
- raw HTML for layout, color, or spacing unless the user explicitly asks for WeMD/CSS customization
- deeply nested headings
- table-heavy layouts unless comparison is essential
- editor notes
- TODOs
- prompt residue

## WeMD Layout Rules

Apply the layout before delivery:

- Use one `#` title only. Do not include title-option blocks unless the user asked for them.
- Use `##` for major sections and `###` for local steps or subpoints. Avoid deeper heading levels in normal articles.
- Keep paragraphs short: usually 1 to 3 sentences, one idea per paragraph.
- Use unordered lists for parallel points and numbered lists only for real sequences.
- Use blockquotes for concise emphasis, caveats, or quoted context; do not stack long quote blocks.
- Use bold for key terms or decisions only. Avoid bolding whole paragraphs.
- Use simple tables only for compact comparison. Convert wide or dense tables into bullets.
- Use fenced code blocks with language tags for commands, config, logs, or code.
- Use standard Markdown links with meaningful anchor text.
- Use standard Markdown images for ready assets. Use short bracket image notes only when the actual image is missing.
- Use GitHub-style alert/callout syntax only when it improves reading and WeMD preview supports it.
- Use Mermaid or math only when the user needs it and the article remains understandable without renderer-specific styling.
- Keep advanced CSS, custom themes, and HTML out of `final-article.md` unless the user explicitly requests a WeMD customization package.

For tutorials, order each section as: goal, action, verification, note. Do not separate a command from the reason or verification that makes it useful.

For commentary, keep the first screen tight: title, one clear opening claim, and the first `##` within a short scroll.

For component placement, use this order of thought:

- claim -> evidence image, table, quote, or source link
- step -> command, screenshot, verification, or warning
- comparison -> criteria, table, then interpretation
- concept -> diagram, example, then plain explanation
- resource -> grouped list, short note, and reference link

## Component Patterns

For concrete examples of callouts, command blocks, image notes, tables, and Mermaid fallbacks, read [wemd-component-patterns.md](wemd-component-patterns.md).

## WeMD Import Rules

WeMD supports Markdown-centered writing and WeChat copy workflows. Prefer portable Markdown over editor-specific decoration, but use supported syntax directly when it improves the article.

Use:

- GitHub-flavored Markdown basics
- GitHub-style callouts only for short tips, warnings, or conclusions
- fenced code blocks with language tags
- simple tables only when the article truly needs comparison
- Mermaid diagrams only when a diagram is clearer than prose and the user accepts renderer dependence
- math only when formulas are part of the article's substance
- image placeholders that the user can replace with real assets
- short bracket notes for screenshots, covers, and diagrams

Do not:

- use raw HTML for layout, color, spacing, or cards by default
- assume WeMD-specific theme CSS will exist for every reader
- leave "Assumption", "Plan", "Draft", "Review", or "Next action" labels inside the publishable article
- include prompts, system notes, or editing rationale in the article body
- include multiple competing H1 titles in the article body
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
- add screenshot notes by default for UI-heavy install/setup/configuration/tutorial drafts
- use AI images only for covers, concept diagrams, or section breaks
- never replace a required screenshot with a fake image

If image hosting, upload, or local asset handling matters, ask the user how they use WeMD. Do not invent an image-host workflow.

When the image is required for proof, use `Image Note`. When it is optional packaging, use `Cover Note` or keep it as an image asset.

Default tutorial screenshot note pattern:

```markdown
[Image Note: place a real screenshot of the settings page after completing this step]
```

Default cover suggestion pattern:

```markdown
## 封面建议

- **比例**：2.35:1
- **画面**：一个干净的流程感封面，主体围绕本文的关键工具和完成状态，不使用伪造截图。
- **文字**：建议后期添加 2-6 个字短标题。
```

## Sidecar Rules

Default to no sidecars. Create these only when explicitly requested:

- `visual-brief.md`: separate cover/image plan
- `review-notes.md`: standalone editorial audit report
- `style-profile.md`: reusable benchmark style constraints, without copied source text

When a sidecar is created, keep it short, give it one H1, and do not duplicate the article body.

Do not create title-option files by default. Keep exactly one H1 in `final-article.md`, and keep editable alternatives outside the normal publishable flow unless the user explicitly asks for them.

## Final Check

Before delivery, verify only the handoff-specific items here, then use [quality-gates.md](quality-gates.md) for broader editorial checks:

- one H1 only
- headings no deeper than H3
- short paragraphs
- no `{{...}}`, raw template snippets, TODOs, prompt residue, or internal planning labels
- layout style fits the article job
- components are placed where they help the reader act, compare, verify, or understand
- tagged code fences
- short image notes
- tutorial image notes are present when UI, terminal, setup, or verification proof matters
- a concise `## 封面建议` section is present when no cover asset or visual brief is requested
- no raw HTML unless an explicit WeMD/CSS customization request was verified
- Markdown is ready for WeMD preview and copy flow
- sidecar-only material has not leaked into `final-article.md`
- no local absolute path leaks unless intentionally part of a tutorial
- output folder contains only the final article, requested sidecars, and image assets
- `scripts/check_article_output.py` passes on the output folder without warnings unless the user explicitly accepted the warning
