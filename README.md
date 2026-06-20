# Maxh-skills

> 个人 Codex Skills 仓库，面向真实写作和内容生产流程。

保持入口轻、规则清楚、产物干净。

## Skill Categories

```text
skills/
  wechat-article-pre/
```

每个 skill 只在 `SKILL.md` 保留核心流程，详细方法放在 `references/`。

### Content Skills

面向写作、内容整理、公众号排版和发布前准备。

| Skill | 用途 |
| --- | --- |
| [`wechat-article-pre`](skills/wechat-article-pre/SKILL.md) | 把公众号草稿、笔记、教程、评论、解释、清单、案例、访谈和选题整理成适合 [WeMD](https://wemd.app/docs/) 的最终稿 |

### Visual Skills

面向封面、配图、信息图、卡片和视觉包装。后续新增相关 skill 时放在这里。

### Utility Skills

面向同步、检查、转换、批处理等辅助工作流。后续新增相关 skill 时放在这里。

## wechat-article-pre

把微信公众号草稿、笔记、教程、评论、解释、清单、案例、访谈和选题整理成适合 [WeMD](https://wemd.app/docs/) 的 Markdown。

核心能力：

- 公众号文章起稿、改写、审稿
- 教程、观点、复盘、解释、清单、资讯、访谈等形态路由
- 保留教程里的必要步骤、链接、命令、截图提示和验证点
- 学习示例公众号的语言节奏和排版规律，但不复制表达
- 明确要求时才输出 `style-profile.md`，便于后续文章沿用风格约束
- 根据用户反馈更新写作约束和审稿标准
- 按 WeMD 官方文档支持的 Markdown、图片、代码、表格、提示块和图表规则直接排版
- 规划或生成封面与配图，封面默认比例 `2.35:1`

## Examples

```text
使用 $wechat-article-pre，把这篇草稿改成适合导入 WeMD 的公众号文章。

使用 $wechat-article-pre，参考这 3 篇公众号文章的语言节奏和排版风格，为我的选题生成原创文章。

使用 $wechat-article-pre，把这篇教程改成最终稿，保留操作步骤，去掉水话，并生成一个 2.35:1 封面。

使用 $wechat-article-pre，围绕这个选题直接起草一篇公众号解释文，读者是第一次接触这个概念的人。
```

## Output

产物放在当前会话工作目录下，以最终文章标题命名文件夹：

```text
文章标题/
  final-article.md
  cover-image.png      # 生成封面时
  section-01.png       # 生成或提供配图时
```

## Cover

- 默认比例：`2.35:1`
- 推荐尺寸：`2256x960`、`1504x640`、`940x400`
- 借鉴 [`baoyu-skills`](https://github.com/JimLiu/baoyu-skills) 的封面维度：类型、色板、渲染、文字层级、情绪、字体
