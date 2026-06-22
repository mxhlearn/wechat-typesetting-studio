#!/usr/bin/env python3
"""Check WeChat article outputs for publication-readiness issues.

The checker accepts either:

- a final article file
- an article output folder containing final-article.md

It uses only the Python standard library so it can run inside a skill folder.
"""

from __future__ import annotations

import argparse
import re
import struct
import sys
from pathlib import Path


ARTICLE_TYPES = {
    "auto",
    "tutorial",
    "setup",
    "commentary",
    "review",
    "explainer",
    "list",
    "case",
    "news",
    "interview",
}

ALLOWED_IMAGE_SUFFIXES = {
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".gif",
    ".svg",
}

ALLOWED_SIDECARS = {
    "review-notes.md",
    "style-profile.md",
    "visual-brief.md",
}

ERROR_PATTERNS = [
    (re.compile(r"\{\{[^}]+\}\}"), "template placeholder like {{...}}"),
    (re.compile(r"<!--\s*Component snippets", re.I), "raw component snippet library"),
    (re.compile(r"\bTODO\b", re.I), "TODO marker"),
    (
        re.compile(r"\b(Assumption|Plan|Draft|Review|Next action)\s*:", re.I),
        "internal planning label",
    ),
    (
        re.compile(r"\b(system prompt|prompt residue|editing note)\b", re.I),
        "prompt or editor residue",
    ),
]

WARNING_TERMS = [
    "不要着急",
    "别着急",
    "先别急",
    "别急",
    "不用着急",
    "不用担心",
    "放心",
    "接下来我们来看",
    "接下来我们详细了解",
    "本文将",
    "这篇文章主要讲",
    "下面从几个方面",
    "首先，我们先",
    "其次，我们再",
    "最后，我们总结",
    "常见问题",
    "值得一提的是",
    "总的来说",
    "可以说",
    "不可否认的是",
    "毋庸置疑",
]

FAQ_WARNING_TERMS = {
    "常见问题",
}

IMAGE_NOTE_RE = re.compile(r"\[(?:Image|Screenshot) Note:", re.I)
CHINESE_IMAGE_NOTE_RE = re.compile(r"\[(?:图片|截图)提示[:：]")
CHINESE_COVER_HEADING_RE = re.compile(r"^##\s+封面建议\s*$", re.M)
EN_COVER_HEADING_RE = re.compile(r"^##\s+Cover (?:Suggestion|Note|Brief)\s*$", re.I | re.M)
QUESTION_CUE_RE = re.compile(
    r"^#{1,3}\s+.*(?:哪一版|怎么|为什么|是不是|要不要|怎么办|如何).*?[？?]?\s*$"
)

LOCAL_PATH_RE = re.compile(
    r"(?<![\w/])(?:[A-Za-z]:\\(?:Users|Documents and Settings)\\[^\s)>\]，。；;]+|/Users/[^\s)>\]，。；;]+|/home/[^\s)>\]，。；;]+)"
)

MACHINE_INFO_RE = re.compile(
    r"\b(?:USERPROFILE|HOMEPATH|COMPUTERNAME|USERNAME|APPDATA|LOCALAPPDATA)\b",
    re.I,
)

SECRET_HINT_RE = re.compile(
    r"(?i)\b(?:api[_-]?key|access[_-]?token|secret|password|passwd|private[_-]?key|id_ed25519|BEGIN (?:OPENSSH|RSA|EC|DSA) PRIVATE KEY)\b"
)

HTML_RE = re.compile(r"<(div|span|section|article|style|script|iframe|table|br|p)\b", re.I)
IMAGE_RE = re.compile(r"!\[[^\]]*]\(([^)]+)\)")
BARE_URL_RE = re.compile(r"(?<!\]\()https?://[^\s)]+")
CODE_FENCE_RE = re.compile(r"^```(\S*)\s*$")

TUTORIAL_HINTS = [
    "安装",
    "配置",
    "步骤",
    "验证",
    "命令",
    "终端",
    "CLI",
    "教程",
    "环境",
    "下载",
    "运行",
    "一键安装",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def count_h1(markdown: str) -> int:
    return sum(1 for line in markdown.splitlines() if re.match(r"^#(?!#)\s+\S", line))


def issue_lines(markdown: str, pattern: re.Pattern[str]) -> list[int]:
    return [i for i, line in enumerate(markdown.splitlines(), 1) if pattern.search(line)]


def cjk_len(text: str) -> int:
    return sum(1 for ch in text if "\u4e00" <= ch <= "\u9fff")


def is_tutorial_like(markdown: str, article_type: str) -> bool:
    if article_type in {"tutorial", "setup"}:
        return True
    if article_type != "auto":
        return False
    score = sum(1 for hint in TUTORIAL_HINTS if hint in markdown)
    return score >= 3


def resolve_target(target: Path) -> tuple[Path, Path | None]:
    if target.is_dir():
        return target / "final-article.md", target
    return target, target.parent if target.name == "final-article.md" else None


def image_size(path: Path) -> tuple[int, int] | None:
    try:
        with path.open("rb") as f:
            header = f.read(16)
            if header.startswith(b"\x89PNG\r\n\x1a\n"):
                f.seek(16)
                width, height = struct.unpack(">II", f.read(8))
                return width, height
            if header.startswith(b"\xff\xd8"):
                f.seek(2)
                while True:
                    marker_start = f.read(1)
                    if not marker_start:
                        return None
                    if marker_start != b"\xff":
                        continue
                    marker = f.read(1)
                    while marker == b"\xff":
                        marker = f.read(1)
                    if marker in {b"\xc0", b"\xc1", b"\xc2", b"\xc3"}:
                        f.read(3)
                        height, width = struct.unpack(">HH", f.read(4))
                        return width, height
                    size_bytes = f.read(2)
                    if len(size_bytes) != 2:
                        return None
                    segment_size = struct.unpack(">H", size_bytes)[0]
                    f.seek(segment_size - 2, 1)
            if header[:4] == b"RIFF" and header[8:12] == b"WEBP":
                data = path.read_bytes()
                if data[12:16] == b"VP8X" and len(data) >= 30:
                    width = 1 + int.from_bytes(data[24:27], "little")
                    height = 1 + int.from_bytes(data[27:30], "little")
                    return width, height
    except OSError:
        return None
    return None


def check_output_folder(
    folder: Path,
    article_path: Path,
    errors: list[str],
    warnings: list[str],
    allow_sidecars: bool,
) -> None:
    if not article_path.exists():
        errors.append(f"folder is missing final-article.md: {folder}")
        return

    for item in folder.iterdir():
        if item.is_dir():
            errors.append(f"unexpected directory in article output folder: {item.name}")
            continue
        if item.name == "final-article.md":
            continue
        if item.suffix.lower() in ALLOWED_IMAGE_SUFFIXES:
            continue
        if item.name in ALLOWED_SIDECARS:
            if allow_sidecars:
                continue
            errors.append(f"unrequested sidecar file in output folder: {item.name}")
            continue
        errors.append(f"unexpected file in article output folder: {item.name}")

    cover = folder / "cover-image.png"
    if cover.exists():
        size = image_size(cover)
        if not size:
            warnings.append("cover-image.png exists but image dimensions could not be read")
        else:
            width, height = size
            ratio = width / height if height else 0
            if abs(ratio - 2.35) > 0.04:
                errors.append(
                    f"cover-image.png ratio should be about 2.35:1, found {width}:{height} ({ratio:.2f}:1)"
                )


def check_markdown_structure(
    markdown: str,
    article_path: Path,
    folder: Path | None,
    article_type: str,
    errors: list[str],
    warnings: list[str],
    allow_raw_html: bool,
    allow_faq: bool,
    allow_missing_cover: bool,
    allow_bare_urls: bool,
) -> None:
    h1_count = count_h1(markdown)
    if h1_count != 1:
        errors.append(f"expected exactly one H1 title, found {h1_count}")

    for pattern, label in ERROR_PATTERNS:
        lines = issue_lines(markdown, pattern)
        if lines:
            errors.append(f"found {label} on line(s): {', '.join(map(str, lines[:8]))}")

    html_lines = issue_lines(markdown, HTML_RE)
    if html_lines and not allow_raw_html:
        warnings.append(
            "raw HTML found; keep final article Markdown-only unless WeMD/CSS customization was requested: "
            + ", ".join(map(str, html_lines[:8]))
        )

    heading_depth_lines = [
        i
        for i, line in enumerate(markdown.splitlines(), 1)
        if re.match(r"^#{4,}\s+\S", line)
    ]
    if heading_depth_lines:
        errors.append(
            "heading depth deeper than H3 on line(s): "
            + ", ".join(map(str, heading_depth_lines[:8]))
        )

    for term in WARNING_TERMS:
        if allow_faq and term in FAQ_WARNING_TERMS:
            continue
        occurrences = markdown.count(term)
        if occurrences:
            warnings.append(f"found '{term}' {occurrences} time(s)")

    tutorial_like = is_tutorial_like(markdown, article_type)
    question_count = markdown.count("？")
    if tutorial_like and question_count >= 3 and not allow_faq:
        warnings.append(
            f"found {question_count} Chinese question marks in a tutorial-like article; use declarative wording"
        )

    question_heading_lines = issue_lines(markdown, QUESTION_CUE_RE)
    if tutorial_like and question_heading_lines and not allow_faq:
        warnings.append(
            "question-cue heading(s) need direct declarative wording on line(s): "
            + ", ".join(map(str, question_heading_lines[:8]))
        )

    has_image_note = bool(IMAGE_NOTE_RE.search(markdown) or CHINESE_IMAGE_NOTE_RE.search(markdown))
    has_cover_section = bool(
        CHINESE_COVER_HEADING_RE.search(markdown)
        or EN_COVER_HEADING_RE.search(markdown)
        or "[Cover Note:" in markdown
    )
    has_cover_asset = bool(folder and (folder / "cover-image.png").exists())
    has_visual_brief = bool(folder and (folder / "visual-brief.md").exists())

    if tutorial_like and not has_image_note:
        warnings.append(
            "tutorial-like article has no Image Note screenshot slots; reserve proof images near key steps"
        )

    if not has_cover_section and not has_cover_asset and not has_visual_brief and not allow_missing_cover:
        warnings.append(
            "missing cover suggestion; add a concise ## 封面建议 section or provide cover-image.png/visual-brief.md"
        )

    local_path_lines = issue_lines(markdown, LOCAL_PATH_RE)
    if local_path_lines:
        warnings.append(
            "possible personal local path on line(s): "
            + ", ".join(map(str, local_path_lines[:8]))
        )

    machine_info_lines = issue_lines(markdown, MACHINE_INFO_RE)
    if machine_info_lines:
        warnings.append(
            "possible machine-specific environment detail on line(s): "
            + ", ".join(map(str, machine_info_lines[:8]))
        )

    secret_hint_lines = issue_lines(markdown, SECRET_HINT_RE)
    if secret_hint_lines:
        warnings.append(
            "possible secret, token, password, or private-key wording on line(s): "
            + ", ".join(map(str, secret_hint_lines[:8]))
        )

    bare_urls = issue_lines(markdown, BARE_URL_RE)
    if bare_urls and not allow_bare_urls:
        warnings.append(
            "bare URL(s) found; prefer meaningful Markdown links or References: "
            + ", ".join(map(str, bare_urls[:8]))
        )

    in_fence = False
    untagged_fences: list[int] = []
    for i, line in enumerate(markdown.splitlines(), 1):
        match = CODE_FENCE_RE.match(line)
        if not match:
            continue
        if not in_fence:
            in_fence = True
            if not match.group(1):
                untagged_fences.append(i)
        else:
            in_fence = False
    if untagged_fences:
        warnings.append(
            "untagged code fence(s) on line(s): "
            + ", ".join(map(str, untagged_fences[:8]))
        )

    for i, paragraph in enumerate(re.split(r"\n\s*\n", markdown), 1):
        text = " ".join(line.strip() for line in paragraph.splitlines())
        if text.startswith("#") or text.startswith("```") or text.startswith("|"):
            continue
        if cjk_len(text) > 180:
            warnings.append(f"long paragraph around block {i}; split for mobile reading")
            break

    image_targets = [target.strip() for target in IMAGE_RE.findall(markdown)]
    for target in image_targets:
        if target.startswith(("http://", "https://")):
            continue
        if target.startswith(("C:\\", "D:\\", "/", "file:")):
            errors.append(f"image uses local absolute path: {target}")
            continue
        if folder:
            clean_target = target.split()[0].strip("<>")
            if not (folder / clean_target).exists():
                warnings.append(f"referenced image asset is missing: {target}")

    if "## References" in markdown and markdown.count("## References") > 1:
        errors.append("multiple ## References sections found")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan final-article.md or an article folder for WeMD/public-account output problems."
    )
    parser.add_argument("target", type=Path, help="Path to final-article.md or its output folder")
    parser.add_argument(
        "--article-type",
        choices=sorted(ARTICLE_TYPES),
        default="auto",
        help="Article shape; controls tutorial-specific checks. Default: auto.",
    )
    parser.add_argument(
        "--allow-warnings",
        action="store_true",
        help="Return success when only warnings are present. Final delivery should usually omit this.",
    )
    parser.add_argument(
        "--allow-sidecars",
        action="store_true",
        help="Allow explicitly requested sidecar files in an output folder.",
    )
    parser.add_argument(
        "--allow-raw-html",
        action="store_true",
        help="Allow raw HTML warnings when the user explicitly requested WeMD/CSS customization.",
    )
    parser.add_argument(
        "--allow-faq",
        action="store_true",
        help="Allow FAQ-style question headings and repeated question marks in tutorial-like articles.",
    )
    parser.add_argument(
        "--allow-missing-cover",
        action="store_true",
        help="Allow final articles without a cover suggestion or cover asset.",
    )
    parser.add_argument(
        "--allow-bare-urls",
        action="store_true",
        help="Allow bare URLs when exact copyability matters more than link polish.",
    )
    args = parser.parse_args()

    article_path, folder = resolve_target(args.target)
    if not article_path.exists():
        print(f"ERROR: final article does not exist: {article_path}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []

    if folder and args.target.is_dir():
        check_output_folder(folder, article_path, errors, warnings, args.allow_sidecars)

    markdown = read_text(article_path)
    check_markdown_structure(
        markdown=markdown,
        article_path=article_path,
        folder=folder,
        article_type=args.article_type,
        errors=errors,
        warnings=warnings,
        allow_raw_html=args.allow_raw_html,
        allow_faq=args.allow_faq,
        allow_missing_cover=args.allow_missing_cover,
        allow_bare_urls=args.allow_bare_urls,
    )

    if errors:
        print("Article output check failed:")
        for item in errors:
            print(f"- ERROR: {item}")
        for item in warnings:
            print(f"- WARNING: {item}")
        return 1

    if warnings:
        print("Article output check failed with warnings:")
        for item in warnings:
            print(f"- WARNING: {item}")
        return 0 if args.allow_warnings else 1

    print("Article output check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
