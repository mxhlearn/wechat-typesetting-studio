# WeMD Handoff Contract

Use this file when the final article must be directly formatted for WeMD and then copied to a WeChat public-account editor.

WeMD references: `https://wemd.app/docs/` and `https://github.com/tenngoxars/WeMD`. Treat WeMD as a Markdown-first WeChat formatting tool. Format the article before handoff; do not leave layout decisions as notes unless the asset is genuinely missing.

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

Do not create process logs, changelogs, quick references, or README files inside the skill output folder.

Default to no sidecars. Put publishable article content in `final-article.md` and images as separate assets.

## Final Shape

`final-article.md` should contain:

- one `#` title
- one short opening line after the title when useful
- 3 to 5 `##` sections for most articles
- `###` only when a section needs another layer
- a short closing section or CTA
- `## References` only when links must stay
- no file path that exposes the user's personal machine unless the user explicitly wants a local tutorial path shown

If links must remain, prefer:

- inline links for immediately useful resources
- `## References` for source lists, downloads, or nonessential background
- no bare long URL unless readability is less important than exact copying

Avoid:

- multiple H1 titles
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

## WeMD Component Examples

Use these patterns directly when they fit. Delete unused components before delivery.

Short emphasis:

```markdown
> 这一步的重点不是“安装成功”，而是确认它能在你的实际环境里跑起来。
```

GitHub-style callout:

```markdown
> [!TIP]
> 如果只是临时测试，先不要改全局配置；确认结果稳定后再固化到脚本里。
```

Warning callout:

```markdown
> [!WARNING]
> 不要把示例里的本地路径直接复制到生产环境，先替换成你自己的项目目录。
```

Command block:

````markdown
```powershell
wemd --version
```
````

Command explanation:

```markdown
这条命令只做版本确认。看到版本号后，再继续下一步。
```

Image asset:

```markdown
![WeMD 预览效果](section-01.png)
```

Missing screenshot note:

```markdown
[Image Note: place a real WeMD preview screenshot here after verifying the layout]
```

Compact comparison:

```markdown
| 场景 | 推荐写法 |
| --- | --- |
| 操作步骤 | 编号列表 |
| 并列观点 | 无序列表 |
| 参数对比 | 简表 |
```

Fallback for a wide table:

```markdown
- **操作步骤**：用编号列表，读者能按顺序执行。
- **并列观点**：用无序列表，读者能快速扫完。
- **参数对比**：只保留关键差异，超过 3 列就拆成小段。
```

Mermaid with plain-language fallback:

````markdown
```mermaid
flowchart LR
  A[输入草稿] --> B[整理结构]
  B --> C[WeMD 排版]
  C --> D[预览复制]
```

如果图表没有渲染，按这个顺序理解即可：先整理草稿，再套用 WeMD 排版，最后预览并复制到公众号编辑器。
````

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
- use AI images only for covers, concept diagrams, or section breaks
- never replace a required screenshot with a fake image

If image hosting, upload, or local asset handling matters, ask the user how they use WeMD. Do not invent an image-host workflow.

When the image is required for proof, use `Image Note`. When it is optional packaging, use `Cover Note` or keep it as an image asset.

## Sidecar Rules

Use sidecars only when the user explicitly asks for them:

- `visual-brief.md`: separate cover/image plan
- `review-notes.md`: standalone editorial audit report
- `style-profile.md`: reusable benchmark style constraints, without copied source text

Do not duplicate full article content across sidecars.

Default sidecar rule:

- no sidecar by default
- do not create `review-notes.md` for normal rewrite or polish tasks
- do not create `visual-brief.md` just because images are needed
- create `style-profile.md` only when the user asks for reusable style memory

When a sidecar is created, keep it short enough to be read before manual publishing.

Sidecar headers:

- `visual-brief.md`: `# Visual Brief`
- `review-notes.md`: `# Review Notes`
- `style-profile.md`: `# Style Profile`

Use one H1 per sidecar file.

Heading alternatives:

- do not create a separate title-options file by default
- keep exactly one H1 in `final-article.md`
- place optional `##` or `###` alternatives beside the relevant section only when useful
- keep alternatives in a short HTML comment block so WeMD preview remains clean

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
- sidecar-only material has not leaked into `final-article.md`
- no local absolute path leaks unless intentionally part of a tutorial
- output folder contains only the final article, requested sidecars, and image assets
