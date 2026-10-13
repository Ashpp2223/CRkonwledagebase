---
name: review-cr-pr
description: "Review pull requests, contributions, and maintenance changes in the Clash Royale knowledge base for registry consistency, evidence quality, broken links, licensing, version drift, and unnecessary documentation noise. Use before merging a PR or auditing a proposed change."
---

# 技术知识库 PR 审查

目标是让未来维护者能安全合并变更，而不是仅根据 Markdown 是否好看做判断。

## 顺序

1. 阅读 [维护者手册](../../../docs/maintainer-handbook.md) 的 PR 流程以及本次 Git Diff；先确定改动对象和影响范围。
2. 校验 Schema：Project/Topic 双向链接、Capability—Implementation 端点、唯一 ID、ReverseFinding 来源与构建状态；新能力是否真的不能归入旧能力。
3. 校验**证据**：事实性陈述是否含准确来源、固定版本和局限；R2+ 是否有专门的审查和日志；历史记录是否误称当前可用。
4. 校验**人类可发现性**：新增项目是否能从项目表查询；新增实现是否出现在能力页；新增逆向发现是否有研究入口。谨防文档与注册表互相矛盾。
5. 校验**信息密度**：删除与技术任务无关的身份解释、重复免责声明、无证据排名、空泛宣传；保留真正影响判断的版本/安全/版权边界。
6. 检查许可证、来源归属、个人隐私、二进制资源、模型与回放内容。不要因为项目是公开仓库就直接转载所有内容。
7. 执行 `python scripts/validate.py` 和 `python scripts/validate_skills.py`，并检查 GitHub CI 实际结果。不可仅写“应该通过”。
8. 给出判定：**通过 / 修改后通过 / 阻止合并**。阻止项必须指出文件、具体事实或不变量及可操作的修复办法。

## 审核输出建议

| 问题 | 位置 | 影响 | 修复要求 |
| --- | --- | --- | --- |
| 证据等级与实际材料不符 | 文件/行 | 误导集成选型 | 降级或补充复现证据 |
| 机器索引与人类入口不一致 | 两个路径 | AI 检索不完整 | 双向修正 |
| 推断被写成确定值 | 源码或逆向记录 | 版本迁移风险 | 明确 unknown/estimated |

没有发现问题时也要说明实际检查的范围、执行的校验及其状态。