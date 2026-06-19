# Maxh-skills

> Personal Codex skills collection. 当前收纳公众号内容预处理 Skill，后续可继续扩展其他 Skill。

## Skills

```text
skills/
  wechat-doocs-article-pre/
```

## wechat-doocs-article-pre

把微信公众号草稿、笔记、教程、评论、解释、清单、案例、访谈和选题整理成 Doocs-ready Markdown。

核心能力：

- 公众号文章起稿、改写、审稿
- 教程、观点、复盘、解释、清单、资讯、访谈等形态路由
- 学习示例公众号的语言节奏和排版规律，但不复制表达
- 输出可复用 `style-profile.md`，便于后续文章沿用风格约束
- 根据用户反馈更新写作约束和审稿标准
- 输出适合导入 Doocs 的干净 Markdown
- 生成封面 brief，默认比例 `2.35:1`

## Examples

```text
使用 $wechat-doocs-article-pre，把这篇草稿改成适合导入 Doocs 的公众号文章。

使用 $wechat-doocs-article-pre，参考这 3 篇公众号文章的语言节奏和排版风格，为我的选题生成原创文章。

使用 $wechat-doocs-article-pre，审一下这篇教程，保留操作步骤，去掉水话，并补一个 2.35:1 封面 brief。
```

## Output

产物放在当前会话工作目录下，以最终文章标题命名文件夹：

```text
文章标题/
  final-article.md
  style-profile.md
  visual-brief.md
  title-options.md
  review-notes.md
  cover-image.png
```

只在必要时创建 sidecar 文件。

## Cover

- 默认比例：`2.35:1`
- 推荐尺寸：`2256x960`、`1504x640`、`940x400`
- 借鉴 [`baoyu-skills`](https://github.com/JimLiu/baoyu-skills) 的封面维度：类型、色板、渲染、文字层级、情绪、字体
- 一个视觉中心、一个隐喻、一套画风参数
- 默认不把长中文放进生成图
- 避免假截图、商务图库感、随机图标堆叠和混合画风

## Validate

```powershell
python <codex-home>\skills\.system\skill-creator\scripts\quick_validate.py skills\wechat-doocs-article-pre
```
