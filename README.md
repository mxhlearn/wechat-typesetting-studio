# Maxh-skills

用于收纳个人可复用的 Codex Skills。仓库结构参考大型 skill 集合的组织方式：把不同能力放进 `skills/`，每个 skill 保持独立、可验证、可安装。

## 风险提示

本仓库中的 skill 由 AI 辅助生成和维护，可能存在遗漏、误判或不适用于当前场景的规则。使用前请自行辨别、测试和修改。

涉及事实、链接、产品版本、法律、医疗、金融、安全、账号发布、平台规则等内容时，请以官方来源和实际测试结果为准。本仓库不承诺生成内容一定准确、合规、可发布，也不承诺任何平台审核或传播效果。

## Skills

| 分类 | Skill | 用途 |
| --- | --- | --- |
| 内容处理 | [`wechat-article-pre`](skills/wechat-article-pre/SKILL.md) | 将中文公众号草稿、笔记、教程、选题整理成适合导入 [WeMD](https://wemd.app/docs/) 的 Markdown 成稿 |

## wechat-article-pre

`wechat-article-pre` 面向微信公众号发文前处理，适合起草、改写、润色、审稿和排版粗稿。它会根据文章目标选择教程、评论、解释、清单、案例、资讯、访谈等结构，并直接输出 WeMD 友好的 Markdown。

核心能力：

- 生成一个可发布的 `final-article.md`
- 保留事实、链接、命令、步骤、截图位置、表格、引用和 References
- 根据内容编排标题、段落、提示块、代码块、图片、图表和封面建议
- 学习公开样文的节奏和排版习惯，但不复制原句
- 降低 AI 味，让语言更精炼、严谨、平铺直叙
- 默认不生成审稿记录、视觉方案、风格档案等过程文件

示例提示词：

```text
使用 $wechat-article-pre，帮我把下面这篇内容整理成适合微信公众号发布的 WeMD Markdown 成稿。

要求：
- 直接生成 final-article.md
- 输出到文章标题命名的文件夹
- 保留事实、链接、命令、步骤、截图位置、表格、引用和 References
- 根据文章内容选择合适结构和排版，不套固定模板
- 语言精炼、严谨、平铺直叙，减少 AI 味
- 教程类文章少用疑问句和自问自答小标题
```

## 输出约定

默认输出为文章标题命名的文件夹：

```text
文章标题/
  final-article.md
  cover-image.png
  section-01.png
```

图片文件只在生成、提供或确实需要占位时出现。过程类 sidecar 文件只在明确要求时生成。

## 验证

Skill 修改后运行：

```bash
python path/to/quick_validate.py skills/wechat-article-pre
python skills/wechat-article-pre/scripts/check_article_output.py path/to/article-folder --article-type tutorial
```

仓库不应提交本机绝对路径、账号信息、密钥、缓存文件或临时输出。

## 结构

```text
skills/
  wechat-article-pre/
    SKILL.md
    agents/
    assets/
    references/
    scripts/
scripts/
```
