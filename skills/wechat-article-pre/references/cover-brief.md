# Cover Brief

Use this file when the article needs a cover direction, an internal visual plan, or a generation-ready cover prompt.

The cover must clarify the article promise. It should not decorate a weak article.

## Contents

- [Decision](#decision)
- [Canvas](#canvas)
- [Brief Workflow](#brief-workflow)
- [Cover Types](#cover-types)
- [Style Controls](#style-controls)
- [Layout Density](#layout-density)
- [Brief Template](#brief-template)
- [Prompt Schema](#prompt-schema)
- [Cover Copy](#cover-copy)
- [Rules](#rules)

## Decision

Choose the lightest useful output:

- Internal cover plan: default for cover direction, prompt, or image slots.
- `visual-brief.md`: only when the user explicitly asks for a separate visual plan.
- `cover-image.png`: only when the user asks for an actual raster cover.
- `## 封面建议` in `final-article.md`: default lightweight handoff when no raster cover or separate visual brief is requested.

If generating a cover, stabilize a compact internal visual plan first. Then read [cover-prompt-recipes.md](cover-prompt-recipes.md).

When not generating a cover, include a concise cover suggestion in `final-article.md`:

- ratio
- one visual subject or metaphor
- style direction
- text strategy
- one avoid rule

Do not include long prompts, detailed mood boards, or generation parameters in the article body.

## Canvas

Default ratio: `2.35:1`.

Recommended sizes:

- `1880 x 800`
- `1645 x 700`
- `1410 x 600`

Use one of these sizes when generating or preparing a raster cover unless the user gives another size. After generation, run the output-folder check so `cover-image.png` dimensions are validated.

- `2256x960`
- `1504x640`
- `940x400`

Keep the focal subject, face, title text, and key visual relation inside the central safe area. Do not place small text or important UI near the edges.

## Brief Workflow

Build the cover from the article promise:

1. Identify the reader outcome.
2. Choose one visual metaphor or scene.
3. Choose one dominant mood.
4. Decide whether in-image text is needed.
5. Choose composition and crop safety.
6. Name the asset.
7. Write a short prompt only when an image will be generated.

If the article has no stable promise yet, return to the article before designing the cover.

## Cover Types

Choose one type:

- Tutorial: clean process cover, real screenshot cover, or no-text concept cover. Never fake product UI.
- Commentary: editorial metaphor, symbolic scene, or restrained typography.
- Explainer: simple concept diagram or one visual contrast.
- Case review: scene that reflects the real constraint, decision, or tradeoff.
- List post: compact cover with one clear cue.
- News/update digest: factual editorial cover, not breaking-news drama.
- Interview/profile: portrait, work scene, or object detail that reveals the subject.

## Style Controls

Borrow the multidimensional discipline from `JimLiu/baoyu-skills`: select dimensions explicitly instead of stacking vague adjectives.

Use these dimensions:

| Dimension | Options | Default |
| --- | --- | --- |
| Type | hero, conceptual, typography, metaphor, scene, minimal | conceptual |
| Palette | warm, elegant, cool, dark, earth, vivid, pastel, mono, retro, duotone, macaron | cool or macaron |
| Rendering | flat-vector, hand-drawn, painterly, digital, chalk, screen-print | flat-vector |
| Text | none, title-only, title-subtitle | none |
| Mood | subtle, balanced, bold | balanced |
| Font | clean, handwritten, serif, display | clean |

Recommended mappings:

- Tutorial: conceptual or minimal, cool or macaron, flat-vector or digital, balanced, clean.
- Commentary: metaphor or typography, elegant or duotone, screen-print or flat-vector, subtle.
- Explainer: conceptual, cool or macaron, flat-vector or digital, balanced.
- Case review: scene or metaphor, warm or elegant, hand-drawn or flat-vector, balanced.
- Update digest: minimal, cool or mono, digital or flat-vector, subtle.

Avoid `vivid`, `dark`, `hero`, `title-subtitle`, and `bold` unless the article truly needs a strong poster.

Do not combine more than one rendering language. Choose flat-vector, clean 3D, hand-drawn, or screen-print; do not ask for all of them.

## Layout Density

Add one density choice:

- sparse: 1 focal subject, best for covers and commentary.
- balanced: 2 to 3 visual elements, best default for tutorials and explainers.
- dense: only for checklist or knowledge-card articles; avoid for cover thumbnails.
- comparison: two-side visual contrast.
- flow: 3 to 5 step path, useful for setup tutorials.

If the cover has more than 3 competing objects, simplify before prompting.

For tool tutorials, prefer `flow` only when each step can be represented without labels. Otherwise use `balanced`.

## Brief Template

Use this as an internal planning checklist. Write it to `visual-brief.md` only when the user explicitly asks for a separate visual plan:

```markdown
## Cover

- Goal:
- Article promise:
- Reader:
- Cover type:
- Visual metaphor:
- Primary subject:
- Composition:
- Density:
- Style direction:
- Type:
- Palette:
- Rendering:
- Text level:
- Mood:
- Font:
- Text on cover:
- Text strategy:
- Screenshot/proof requirement:
- Post-edit text plan:
- Ratio: 2.35:1
- Size:
- Asset name:
- Avoid:
```

## Prompt Schema

Use short labeled lines. Do not write one long mood-board paragraph.

```text
Use case:
Asset type: WeChat public-account article cover
Ratio: 2.35:1
Article promise:
Audience:
Primary subject:
Scene/backdrop:
Visual metaphor:
Style/medium:
Style direction:
Type:
Palette:
Rendering:
Text level:
Mood:
Font:
Layout density:
Composition/framing:
Lighting/mood:
Color palette:
Text (verbatim):
Typography:
Constraints:
Avoid:
```

## Cover Copy

Prefer no in-image Chinese text for generated covers. Add text later in WeMD or a design tool when text accuracy matters.

If text is required:

- keep it under 12 Chinese characters
- prefer 2 to 6 Chinese characters
- quote the exact text once
- use title-only, not title plus long subtitle
- switch to no-text cover if text accuracy fails once

Good cover copy patterns:

- subject + outcome
- subject + friction
- subject + scope
- subject + decision lens

Weak cover copy:

- full article title
- generic slogan
- dense subtitle
- broad emotional phrase

If title text will be added after generation, keep a post-edit text plan internally unless the user explicitly asks for `visual-brief.md`: exact text, placement, contrast, and maximum length.

## Rules

- Align the cover with the article promise.
- Use one focal subject, one metaphor, one mood.
- Default to `2.35:1`.
- Use `cover-image.png` as the default generated asset name.
- Prefer `1880 x 800`, `1645 x 700`, or `1410 x 600` for raster covers.
- If no cover image is generated, include a short `## 封面建议` section in `final-article.md` unless the user explicitly says not to.
- Avoid fake screenshots, fake UI states, fake logs, invented brands, logos, and watermarks.
- Avoid random floating icons, generic business stock imagery, dense diagrams, and mixed visual styles.
- For tutorials, use real screenshots for proof and AI images only for covers or conceptual visuals.
- Do not use exact product logos unless the user provides permission or asks for brand-faithful assets.
- Leave enough quiet space for WeChat cropping and optional post-added text.
