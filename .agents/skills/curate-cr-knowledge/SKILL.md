---
name: curate-cr-knowledge
description: "Maintain this Clash Royale knowledge base when adding or updating projects, capabilities, implementation records, research topics, guides, or indexes. Use for cataloging GitHub projects and organizing reusable technical knowledge; not for independently verifying a source or reviewing an entire pull request."
---

# 收录与更新技术知识

此 Skill 负责**记录结构正确且可发现的知识**，证据提升另用 [review-cr-evidence](../review-cr-evidence/SKILL.md)。

## 开始前

1. 阅读 [项目规范](../../../AGENTS.md)、[维护者手册](../../../docs/maintainer-handbook.md) 和 [文档写作规范](../../../docs/editorial-standards.md)。
2. 先查 `registry/` 是否已有同义项目、能力或研究记录。不要因为换了名称就创造新 ID。
3. 明确本次主要实体：Project（来源仓库）、Capability（开发需求）、Implementation（某项目提供的具体能力）、Topic（跨项目机制）、ReverseFinding（版本绑定发现）、Guide（实践流程）。

## 按实体更新

- **Project**：一个上游 GitHub 仓库一个稳定 ID；新增 `projects/<id>.md` 和 `registry/projects.yaml`，核对仓库与许可证。若属于 Topic，则同步登记 `registry/topics.yaml` 和 Topic front matter 双向关系。
- **Capability**：面向用户意图，不面向作者；新增 `capabilities/<id>/README.md` 和 `registry/capabilities.yaml`，说明输入/输出语义、限制、验收条件和下游用途。仅在出现与已有能力不同的需求边界时新增。
- **Implementation**：在 `registry/implementations.yaml` 添加唯一 `<capability>--<project>`，记录 `claim`、`limits`、`evidence`、`reuse_level`、`verification`、`integration`；将重要新增候选同步写入相应能力卡，避免机器索引与人类入口断裂。
- **Topic**：以问题/原理比较技术路线；保持 `projects` 的双向索引一致，不将作者 README 大段复制到 Topic 中。
- **ReverseFinding**：复用 [逆向发现模板](../../../templates/reverse-finding.md)，更新 `registry/reverse-findings.yaml`，显式限定 `source_sha`、`game_build`、`applicability`。历史结果不能写成当代版本支持。
- **Guide**：只描述任务路线和验证条件；未经实测的命令不得写成已验收的集成教程。

## 完成条件

1. 主入口能让读者从需求找到能力，再找到项目与证据。
2. 不修改原项目身份、不合并无关仓库，不复制第三方受限资源。
3. 不重复维护可由机器索引派生的项目—能力事实；相应摘要只用于解释选择和局限。
4. 运行 `python scripts/validate.py` 与 `python scripts/validate_skills.py`；如无法执行，明确记录未验证项目和阻碍。
5. 在 PR 中说明受影响的稳定 ID、实际来源、风险和验证记录。

需要升级 R2/R3/R4、审查逆向结论时使用 [review-cr-evidence](../review-cr-evidence/SKILL.md)。