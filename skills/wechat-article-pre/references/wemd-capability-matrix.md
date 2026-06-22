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
| Supported, use deliberately | Mermaid, math formulas, sliding image groups | use when the component is better than prose, with a text fallback for the key idea |
| Confirm workflow first | custom CSS, theme-specific blocks, image hosting, local image behavior | ask or verify when the user's final copy flow matters |
| Avoid in article body | raw HTML cards, complex nested lists, wide tables, local-only image paths | simplify for publishable Markdown |

WeMD can support advanced features, but the public-account article should remain readable if a theme, CSS block, image host, or diagram renderer changes.

## Verification Rule

If final delivery uses a feature from "Supported, use deliberately", keep the key idea readable without the renderer. WeMD supports Mermaid, math formulas, and sliding image groups, but the article should not depend on them as the only explanation.

If final delivery depends on "Confirm workflow first", either verify the behavior in the user's WeMD flow or keep the workflow note outside `final-article.md`.

Do not rely on unverified editor behavior for the only explanation of a key idea. A Mermaid diagram, formula, image-host link, custom CSS block, or sliding image group must have a readable fallback or a user-confirmed workflow.

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

WeMD supports Mermaid, math formulas, and sliding image groups. Do not ask just to use them; ask only when the final WeChat copy behavior, theme behavior, image hosting, or local asset workflow matters.

Ask the user or verify before relying on:

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
- Sliding image group: provide clear image order or separate standard image slots when the group is not essential.
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
