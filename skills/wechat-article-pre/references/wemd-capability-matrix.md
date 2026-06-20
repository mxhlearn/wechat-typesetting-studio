# WeMD Capability Matrix

Use this file when a task depends on WeMD-specific Markdown features, copy behavior, image handling, or theme behavior.

Source references: `https://wemd.app/docs/` and `https://github.com/tenngoxars/WeMD`.

## Known From WeMD Project Positioning

WeMD is a Markdown-first WeChat public-account formatting tool. Public project materials describe support for:

- Markdown writing and preview
- basic Markdown syntax
- extended Markdown syntax
- one-click copy to WeChat public-account editor
- GitHub-flavored Markdown
- GitHub-style alert/callout blocks
- tables
- code highlighting
- math formulas
- Mermaid diagrams
- theme and CSS customization
- image hosting options
- local-first or local editing orientation
- dark-mode preview
- sliding image groups
- search and batch replacement

Treat this as feature awareness, not a guarantee that every feature is appropriate for every article.

## Capability Tiers

Use this tiering before writing the final article:

| Tier | Features | Default handling |
| --- | --- | --- |
| Safe core | headings, paragraphs, lists, blockquotes, links, standard images, fenced code | use directly |
| Safe when simple | tables, code highlighting, short GitHub-style callouts, basic emphasis | use only when they improve clarity |
| Confirm first | Mermaid, math, custom CSS, theme-specific blocks, sliding image groups, image hosting | ask or verify when final copy behavior matters |
| Avoid in article body | raw HTML cards, complex nested lists, wide tables, local-only image paths | simplify for publishable Markdown |

WeMD can support advanced features, but the public-account article should remain readable if a theme, CSS block, image host, or diagram renderer changes.

## Feature Decision

Before using a WeMD feature, ask:

1. Does it help the reader understand or act?
2. Will it survive copy to the WeChat editor?
3. Is there a plain Markdown fallback?
4. Would a mobile reader still scan it easily?

If any answer is uncertain, use the fallback.

## Default Compatibility Profile

For publishable article Markdown, default to:

- one `#` title
- `##` and limited `###`
- short paragraphs
- standard fenced code blocks
- short callouts for tips, warnings, or conclusions when useful
- simple tables only when needed
- standard image syntax or short image notes
- plain blockquotes
- no raw HTML for layout unless the user explicitly asks for WeMD/CSS customization
- no theme-dependent meaning
- no dependence on local editor state

## Ask Or Verify Before Using

Ask the user or verify in WeMD before relying on:

- Mermaid rendering in the final copy destination
- math formula rendering in the final copy destination
- custom CSS or theme-specific blocks
- image-host upload behavior
- sliding image group syntax or behavior
- local image path behavior
- HTML snippets
- complex nested lists
- wide tables on mobile
- desktop-only paths or image assets
- WeChat copy behavior for advanced components

## WeMD-Safe Fallbacks

- Mermaid: provide a short text summary below the diagram.
- Math: add a plain-language explanation near the formula.
- Wide table: convert to bullets or split into smaller comparison blocks.
- Image hosting uncertainty: use stable asset names and keep only short publishable image notes in `final-article.md` when the image is part of the article.
- Theme uncertainty: keep Markdown semantic and readable without color or card styling.
- CSS customization: keep the publishable article readable without the custom CSS, and place CSS/theme notes outside `final-article.md` unless the user asks for an integrated WeMD package.
- Sliding image group uncertainty: list images as separate standard Markdown image slots in `final-article.md`, or keep them as separate assets if placement is not yet decided.

## Mobile Risk

Avoid these in publishable Markdown unless the user explicitly accepts the tradeoff:

- wide comparison tables
- multi-column concepts expressed as tables
- long formula blocks
- diagrams with tiny labels
- long code blocks without explanation
