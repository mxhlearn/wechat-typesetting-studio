# Cover Prompt Recipes

Use this file only when the user asks for an actual raster cover or a generation-ready cover prompt.

First read [cover-brief.md](cover-brief.md), stabilize `visual-brief.md`, then choose one recipe below. Read [cover-qa.md](cover-qa.md) before delivery or retry. Keep the ratio `2.35:1` unless the user explicitly asks for another crop.

## Contents

- [Tutorial Cover](#tutorial-cover)
- [Commentary Cover](#commentary-cover)
- [Explainer Cover](#explainer-cover)
- [Text-Led Cover](#text-led-cover)
- [Retry Rules](#retry-rules)

## Tutorial Cover

Use when the article teaches a workflow or setup.

```text
Use case: stylized-concept
Asset type: WeChat public-account article cover
Ratio: 2.35:1
Article promise: <reader can complete the workflow>
Primary subject: one clean workflow path from setup to verified result
Scene/backdrop: abstract workstation or simple process scene, no fake UI
Style/medium: clean editorial 3D or flat editorial illustration
Style direction: Clean 3D editorial or editorial illustration
Type: conceptual
Palette family: macaron or cool
Rendering: flat-vector or hand-drawn
Text level: none
Mood level: balanced
Font: clean
Composition/framing: 2.35:1 wide cover, one clear focal path, crop-safe center, open margins
Color palette: restrained tech palette with one accent color
Text (verbatim): none
Constraints: no fake screenshots, no terminal text, no brand logos, no tiny UI
Avoid: cluttered desk scene, floating random icons, unreadable code, stock business people
```

## Commentary Cover

Use when the article gives a judgment or interpretation.

```text
Use case: stylized-concept
Asset type: WeChat public-account article cover
Ratio: 2.35:1
Article promise: <reader understands the real implication>
Primary subject: one symbolic object or scene that represents the tension
Scene/backdrop: minimal editorial scene with depth
Style/medium: refined editorial illustration
Style direction: Editorial illustration
Type: metaphor or typography
Palette family: elegant, mono, or duotone
Rendering: flat-vector or screen-print
Text level: none
Mood level: subtle
Font: clean or serif
Composition/framing: 2.35:1 wide cover, single focal subject, strong negative space
Lighting/mood: restrained, thoughtful, not dramatic
Text (verbatim): none
Constraints: no exaggerated emotion, no fake news style, no watermark
Avoid: chaotic collage, generic business handshake, alarmist visual language
```

## Explainer Cover

Use when the article explains a concept or distinction.

```text
Use case: infographic-diagram
Asset type: WeChat public-account article cover
Ratio: 2.35:1
Article promise: <reader understands one key distinction>
Primary subject: simple visual contrast between A and B
Style/medium: clean editorial diagram, few shapes, strong hierarchy
Style direction: Minimal diagram
Type: conceptual
Palette family: cool or macaron
Rendering: flat-vector or digital
Text level: none
Mood level: balanced
Font: clean
Composition/framing: 2.35:1 wide cover, two-part comparison, large readable elements
Color palette: neutral base plus two accent colors
Text (verbatim): none
Constraints: no dense labels, no more than 3 visual groups, no tiny text
Avoid: complicated flowcharts, decorative arrows, crowded icons
```

## Text-Led Cover

Use only when a short cover phrase is the main visual.

```text
Use case: ads-marketing
Asset type: WeChat public-account article cover
Ratio: 2.35:1
Primary subject: bold short Chinese cover phrase
Style/medium: clean editorial poster
Style direction: Text-led poster
Type: typography
Palette family: mono, elegant, or duotone
Rendering: flat-vector or screen-print
Text level: title-only
Mood level: balanced
Font: clean or display
Composition/framing: 2.35:1 wide cover, large centered text, generous margins, simple background
Text (verbatim): "<2-6 Chinese characters>"
Typography: bold modern Chinese typography, high contrast, exact text once
Constraints: no extra words, no subtitle, no watermark, no decorative clutter
Avoid: misspelled characters, warped type, multiple text copies, busy background
```

## Retry Rules

Retry once with one targeted change:

- too cluttered: reduce to one subject and remove secondary objects
- weak relevance: replace mood words with the article promise
- unreadable text: remove in-image text and keep copy as sidecar text
- fake UI: switch to concept cover or require real screenshot separately
- stock feel: specify editorial illustration and remove business stock tropes
- bad crop: add crop-safe center and wider negative space
