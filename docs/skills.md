# 仓库级 Agent Skills

项目 Skill 放在 `.agents/skills/<name>/SKILL.md`，符合 [Agent Skills 文件格式](https://agentskills.io/specification)。AI 工具的具体自动发现能力可能有所不同；无论是否自动显示，都可以手动指示阅读相应文件。

| Skill | 什么时候使用 | 输入与成果 |
| --- | --- | --- |
| [curate-cr-knowledge](../.agents/skills/curate-cr-knowledge/SKILL.md) | 新项目、能力、研究专题、实现关系需要编目或更新 | 原始来源 → 结构化索引与读者入口 |
| [review-cr-evidence](../.agents/skills/review-cr-evidence/SKILL.md) | 校对逆向结论、验证源码、提升复用等级 | 固定版本证据 → 有边界的审核记录 |
| [review-cr-pr](../.agents/skills/review-cr-pr/SKILL.md) | 合并 PR 前审核索引、证据与文档质量 | 变更差异 → 审查结论、阻断项与修复意见 |

## 分工

- [AGENTS.md](../AGENTS.md)：仓库不变量和检索顺序。所有编辑任务默认生效。
- [维护者手册](maintainer-handbook.md)：面向人的维护流程、移交和故障排查。
- **Skill**：某类操作的可重复指令。按任务触发，不是每次都加载所有 Skill。
- [文档规范](editorial-standards.md)：术语、证据和写作风格的稳定规则。
- `scripts/validate.py` 与 `scripts/validate_skills.py`：机器校验。其通过不等于所有外部技术事实已验证。

## 在 Codex 等工具中使用

进入仓库后，可以显式指定 `$curate-cr-knowledge`、`$review-cr-evidence` 或 `$review-cr-pr`；如果工具没有显示仓库 Skill，也可以让 Agent 直接读取具体 `SKILL.md`。

增加 Skill 需要解决**新的、反复发生的维护任务**。优先扩充现有 Skill 的小型参考资料，避免为每个细分文档另建一个 Skill。名称与目录名一致，description 要写清触发时机。
