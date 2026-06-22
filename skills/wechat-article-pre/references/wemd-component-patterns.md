# WeMD Component Patterns

Use this file when the article needs concrete WeMD-safe component examples. Use these patterns directly when they fit the article. Do not include all examples by default.

## Short Emphasis

```markdown
> 这一步的重点不是“安装成功”，而是确认它能在你的实际环境里跑起来。
```

## GitHub-Style Callouts

```markdown
> [!TIP]
> 如果只是临时测试，先不要改全局配置；确认结果稳定后再固化到脚本里。
```

```markdown
> [!WARNING]
> 不要把示例里的本地路径直接复制到生产环境，先替换成你自己的项目目录。
```

Use callouts only for actionable tips, warnings, caveats, or compact conclusions.

## Command Blocks

````markdown
```powershell
wemd --version
```
````

```markdown
这条命令只做版本确认。看到版本号后，再继续下一步。
```

## Images

Ready asset:

```markdown
![WeMD 预览效果](section-01.png)
```

Missing screenshot:

```markdown
[Image Note: place a real WeMD preview screenshot here after verifying the layout]
```

Keep image notes near the step, claim, or verification they support.

## Compact Comparison

```markdown
| 场景 | 推荐写法 |
| --- | --- |
| 操作步骤 | 编号列表 |
| 并列观点 | 无序列表 |
| 参数对比 | 简表 |
```

If the table becomes wide or dense, convert it to bullets:

```markdown
- **操作步骤**：用编号列表，读者能按顺序执行。
- **并列观点**：用无序列表，读者能快速扫完。
- **参数对比**：只保留关键差异，超过 3 列就拆成小段。
```

## Mermaid With Fallback

````markdown
```mermaid
flowchart LR
  A[输入草稿] --> B[整理结构]
  B --> C[WeMD 排版]
  C --> D[预览复制]
```

如果图表没有渲染，按这个顺序理解即可：先整理草稿，再套用 WeMD 排版，最后预览并复制到公众号编辑器。
````

Use Mermaid only when a diagram is clearer than prose, and keep a plain-language fallback for the key idea.
