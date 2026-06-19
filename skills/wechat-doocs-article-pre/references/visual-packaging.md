# Visual Packaging

Use this file when the article needs a cover, a small visual brief, or inline image slots.

## Contents

- [Rule](#rule)
- [Cover Decision](#cover-decision)
- [Canvas Ratio](#canvas-ratio)
- [Cover Workflow](#cover-workflow)
- [Cover Types](#cover-types)
- [Baoyu-Inspired Controls](#baoyu-inspired-controls)
- [Style Direction](#style-direction)
- [Cover Brief Template](#cover-brief-template)
- [Cover Rules](#cover-rules)
- [Cover Prompt Schema](#cover-prompt-schema)
- [Cover Copy](#cover-copy)
- [Inline Images](#inline-images)
- [Output](#output)
- [Cover QA](#cover-qa)
- [Failure Modes](#failure-modes)

## Rule

Finish the article first. Then define visuals.

Do not make the cover carry work the article has not done.

## Cover Decision

Choose the lightest useful output:

- Cover note only: use when the user only needs Doocs handoff.
- `visual-brief.md`: use when cover direction, prompt, or image slots matter.
- Actual raster cover: use only when the user asks to generate the cover image.

When generating an actual cover, use the structured prompt below and inspect the result. If image generation is handled by another skill/tool, borrow its discipline: labeled prompt, explicit constraints, output QA, then one targeted retry if needed.

## Canvas Ratio

Default cover ratio: `2.35:1`.

Use this ratio for cover briefs, generated cover prompts, and QA unless the user explicitly asks for another crop.

Practical sizes:

- `2256x960`
- `1504x640`
- `940x400`

Keep important content inside the central safe area. Do not place small text, faces, UI details, or key objects near the edges.

## Cover Workflow

Make the cover from the article promise, not from a random mood board.

Use this sequence:

1. identify the article promise
2. choose one visual metaphor or scene
3. choose one dominant mood
4. decide whether the cover needs text
5. decide the composition
6. name the asset
7. write the generation prompt only if an image will be generated
8. inspect the output against Cover QA
9. revise one constraint at a time

## Cover Types

Use the type that matches the article:

- Tutorial: real screenshot cover, clean process cover, or no-text concept cover. Do not fake product UI.
- Commentary: editorial concept, symbolic scene, or text-led poster.
- Explainer: simple concept diagram or one abstract visual metaphor.
- Case review: scene that reflects the real constraint, decision, or tradeoff.
- List post: compact, readable cover with one clear cue.
- News/update digest: factual editorial cover, not dramatic breaking-news art.
- Interview/profile: portrait, work scene, or object detail that reveals the subject.

Use image-generation use cases like this:

- `ads-marketing`: text-led public-account cover or campaign-like poster.
- `stylized-concept`: editorial metaphor, abstract scene, or concept cover.
- `photorealistic-natural`: real-world scene or desk/workflow cover.
- `infographic-diagram`: simple explainer diagram with few labels.
- `ui-mockup`: only for clearly fictional or illustrative UI; never for real verification screenshots.

## Baoyu-Inspired Controls

Borrow the multidimensional cover discipline from `JimLiu/baoyu-skills` (`https://github.com/JimLiu/baoyu-skills`), especially the `baoyu-cover-image` idea of separating type, palette, rendering, text, mood, and font.

Do not copy its workflow wholesale. This skill only needs a compact cover brief for WeChat/Doocs articles.

Use these dimensions:

| Dimension | Options | Default use |
| --- | --- | --- |
| Type | hero, conceptual, typography, metaphor, scene, minimal | choose one composition purpose |
| Palette | warm, elegant, cool, dark, earth, vivid, pastel, mono, retro, duotone, macaron | choose one color system |
| Rendering | flat-vector, hand-drawn, painterly, digital, chalk, screen-print | choose one rendering language |
| Text | none, title-only, title-subtitle | default to none for generated images |
| Mood | subtle, balanced, bold | default to balanced |
| Font | clean, handwritten, serif, display | use only when text is required |

Recommended mappings:

- Tutorial: conceptual or minimal + macaron/cool + flat-vector/hand-drawn + balanced + clean.
- Commentary: typography or metaphor + elegant/mono/duotone + screen-print/flat-vector + subtle.
- Explainer: conceptual + cool/macaron + flat-vector/digital + balanced.
- Case review: scene or metaphor + warm/elegant + hand-drawn/flat-vector + balanced.
- Update digest: minimal or hero + cool/mono + digital/flat-vector + subtle.

Avoid using `vivid`, `dark`, `hero`, `text-rich`, or `bold` unless the article truly needs a strong campaign-like cover.

## Style Direction

Choose one visual style direction before writing the prompt.

Preferred styles:

- Editorial illustration: best default for essays, commentary, explainers, and tool articles.
- Clean 3D editorial: good for tool workflows and abstract productivity topics.
- Minimal diagram: good for concept distinctions, method frameworks, and comparison posts.
- Photoreal editorial scene: good only when a real-world scene makes the article clearer.
- Text-led poster: use only when the cover phrase is short and central.

Avoid styles that usually look messy in WeChat covers:

- busy cyberpunk dashboards
- random floating icons
- collage of many unrelated objects
- generic business meeting scenes
- fake screenshots or fake product UI
- dense infographic posters
- glossy ad visuals without article relevance
- heavy gradients with no focal subject

Style borrowing rule:

- Borrow structure from good image-prompt references: use case, asset type, subject, scene, style, composition, palette, constraints, avoid list.
- Borrow only visual discipline from style libraries: named style direction, one composition, negative prompt, and QA.
- Do not import long prompt templates, model-specific syntax, or unrelated aesthetic tags.

## Cover Brief Template

Use this structure in `visual-brief.md`:

```markdown
## Cover

- Goal:
- Type:
- Core message:
- Visual metaphor:
- Mood:
- Text on cover:
- Text strategy:
- Style direction:
- Type:
- Palette family:
- Rendering:
- Text level:
- Mood level:
- Font:
- Composition:
- Color details:
- Ratio: 2.35:1
- Size:
- Asset name:
- Avoid:
```

## Cover Rules

- Keep the cover aligned with the article promise.
- Do not repeat the title word for word.
- Do not use generic business stock imagery.
- Do not use fake screenshots for real workflows.
- Default to no in-image Chinese text unless the user needs a text-led cover.
- Keep text short if the image already carries the topic.
- Use `2.35:1` as the default cover ratio.
- Use `cover-image.png` as the default asset name.
- Keep cover text under 12 Chinese characters when possible.
- Avoid small UI details that will not survive WeChat preview cropping.
- Use one focal subject, one visual metaphor, and one dominant mood.
- Limit visible elements. If more than 3 objects compete for attention, simplify.
- Leave clean negative space for crop safety and optional post-added text.
- Avoid tiny text, dense diagrams, collages, random icons, and decorative clutter.
- Avoid logos, watermarks, brand marks, fake app names, and unreadable pseudo-text.
- For tutorials, use real screenshots for proof and AI images only for cover/concept visuals.

## Cover Prompt Schema

Use short labeled lines. Do not write one long mood-board paragraph.

```text
Use case: <ads-marketing|stylized-concept|photorealistic-natural|infographic-diagram|ui-mockup>
Asset type: WeChat public-account article cover
Ratio: 2.35:1
Article promise: <what the article helps the reader finish, understand, decide, or avoid>
Audience: <reader group>
Primary subject: <single focal subject>
Scene/backdrop: <simple environment or abstract backdrop>
Visual metaphor: <one metaphor only, optional>
Style/medium: <editorial illustration / clean 3D / photorealistic / poster / diagram>
Style direction: <one style direction from this reference>
Type: <hero|conceptual|typography|metaphor|scene|minimal>
Palette family: <warm|elegant|cool|dark|earth|vivid|pastel|mono|retro|duotone|macaron>
Rendering: <flat-vector|hand-drawn|painterly|digital|chalk|screen-print>
Text level: <none|title-only|title-subtitle>
Mood level: <subtle|balanced|bold>
Font: <clean|handwritten|serif|display>
Composition/framing: <wide cover, one focal point, crop-safe center, generous negative space>
Lighting/mood: <restrained mood>
Color palette: <2-3 colors, high contrast, not one-note>
Text (verbatim): "<exact cover text or none>"
Typography: <only if text is required>
Constraints: <must-have constraints>
Avoid: <specific failure modes>
```

Text strategy:

- Prefer `Text (verbatim): none` for generated covers, then add Chinese text later in Doocs or a design tool.
- If text must be generated inside the image, keep it to 2 to 6 Chinese characters when possible.
- Quote the exact text and require it exactly once.
- Do not ask the model to render long Chinese subtitles.
- If text accuracy fails once, switch to no-text cover and keep the text in `visual-brief.md`.

For actual raster cover generation, read [cover-prompt-recipes.md](cover-prompt-recipes.md) after the cover brief is stable.

## Cover Copy

If the cover needs text, use one of these patterns:

- subject + outcome
- subject + friction
- subject + scope
- subject + decision lens

Keep it short. If the title already carries the promise, the cover text should narrow the angle, not restate it.

Good cover text:

- `先跑通`
- `少走弯路`
- `写得更像人`
- `从草稿到成稿`
- `只讲重点`
- `避开弯路`

Weak cover text:

- full article title
- generic slogan
- broad emotional phrase
- dense subtitle

## Inline Images

Use inline images only when they help the reader act or understand.

Good slots:

- after the opening tension
- before a dense framework
- before a likely confusion point
- after a visible verification step

For tutorials:

- use real screenshots for UI, settings, terminal output, and verification
- use AI images only for cover, concept, or section breaks
- separate `Screenshot Slots` from `AI Illustration Slots`

## Output

When visuals are needed, `visual-brief.md` should include:

- cover concept
- cover text options
- image type
- style
- style direction
- type
- palette family
- color details
- rendering
- text level
- mood level
- font
- composition
- slots
- prompt blocks
- asset names

If generating a cover directly, include one prompt block:

```markdown
### Prompt: cover-image.png

Use case:
Asset type:
Ratio: 2.35:1
Article promise:
Audience:
Primary subject:
Scene/backdrop:
Visual metaphor:
Style/medium:
Style direction:
Type:
Palette family:
Rendering:
Text level:
Mood level:
Font:
Composition/framing:
Lighting/mood:
Color palette:
Text (verbatim):
Typography:
Constraints:
Avoid:
```

## Cover QA

Before delivery or retry, check:

- Does the cover express the article promise without needing a paragraph of explanation?
- Is there one focal subject?
- Is the thumbnail still readable at small size?
- Is the center crop safe?
- Is the canvas ratio `2.35:1` unless the user requested otherwise?
- Are there fewer than 3 competing objects?
- Is any in-image text exact, short, and readable?
- Are there fake screenshots, fake UI states, fake logs, or invented brands?
- Does the image avoid stock-business cliches?
- Is there exactly one style direction?
- Does the prompt avoid long decorative adjectives?
- Is the file name stable, usually `cover-image.png`?

If the result fails, retry with one targeted change:

- too cluttered: reduce to one subject and remove secondary objects
- weak relevance: replace mood words with the article promise
- unreadable text: remove in-image text and keep copy as sidecar text
- fake UI: switch to concept cover or require real screenshot separately
- stock feel: specify editorial illustration, no business handshake, no generic office scene
- bad crop: add crop-safe center and wider negative space

## Failure Modes

- vague cover mood
- text that repeats the title
- generic stock art
- fake UI screenshots
- mixed visual styles in one article
- too many images for a short article
- long Chinese text rendered inside the generated image
- prompt that lists many metaphors instead of choosing one
- cover that looks attractive but does not match the article promise
