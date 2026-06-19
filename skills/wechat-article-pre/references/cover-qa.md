# Cover QA

Use this file to inspect cover briefs, generated prompts, or raster cover images before delivery.

## Checks

Before delivery, verify:

- Does the cover express the article promise without a paragraph of explanation?
- Is there one focal subject?
- Is the thumbnail readable at small size?
- Is the center crop safe?
- Is the canvas ratio `2.35:1` unless the user asked otherwise?
- Are there fewer than 3 competing objects?
- Is any in-image text exact, short, and readable?
- Are there fake screenshots, fake UI states, fake logs, or invented brands?
- Does the image avoid stock-business cliches?
- Is there exactly one style direction?
- Does the prompt avoid long decorative adjective chains?
- Is the file name stable, usually `cover-image.png`?

## Crop Safety

For `2.35:1` covers:

- keep the main subject near the center third
- avoid tiny labels and UI details near both horizontal edges
- leave negative space for optional title placement
- make the cover still legible if WeChat crops slightly

## Text QA

Generated text is fragile.

Pass only when:

- the exact text appears once
- the text is short
- there are no extra pseudo-characters
- the text is not warped or hidden by the subject

If text fails once, remove in-image text and keep the copy in `visual-brief.md`.

## Failure Modes

- vague cover mood
- cover repeats the full title
- generic stock art
- fake UI screenshots
- mixed visual styles
- too many icons
- long Chinese text inside the image
- prompt lists many metaphors instead of choosing one
- cover looks attractive but does not match the article promise

## Retry Ladder

Retry once with one targeted change:

- Too cluttered: reduce to one subject and remove secondary objects.
- Weak relevance: replace mood words with the article promise.
- Unreadable text: remove in-image text.
- Fake UI: switch to concept cover or require a real screenshot separately.
- Stock feel: specify editorial illustration and remove business tropes.
- Bad crop: add crop-safe center and wider negative space.

If the second result still fails, deliver the best brief and state the remaining visual risk outside the publishable article.
