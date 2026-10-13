---
name: synthesize-cr-knowledge
description: "Synthesize verified and source-backed Clash Royale knowledge across multiple projects into mechanisms, invariants, contrasts, decision criteria, and reusable technical explanations. Use when comparing implementations or explaining what knowledge transfers between engines, replay tools, AI pipelines, or client builds; not for collecting unrelated project descriptions."
---

# 跨项目知识综合：提取能迁移的技术规律

**目标**：将多份技术来源转化为**条件明确的机制解释和工程决策依据**，而不是拼接多篇 README。

## 操作流程

1. **限定比较问题**。例如“为什么原生快照不等于独立仿真状态克隆”，而非简单问“哪个项目最好”。
2. 从 [能力索引](../../../registry/capabilities.yaml)、[实现矩阵](../../../registry/implementations.yaml)、[专题](../../../topics/README.md) 和 [逆向发现](../../../registry/reverse-findings.yaml) 选取确实涉及同一个问题的来源。
3. 为每个实现建立**可比条件**：游戏版本/资源、原生或重写引擎、状态覆盖率、时基、坐标、持久化/进程边界、许可证和独立证据等级。缺少对照条件时禁止排名。
4. 提炼**共同语义、关键差异、不变量、反例和下游后果**；把“源文档明示”和“本中台从多源推导”标注清楚。
5. 对不一致情况给出更严格的分解：概念重名、实现层不同、版本漂移、作者声称冲突、数据集不同、未知。不要为了统一而隐藏冲突。
6. 产出有行动价值的建议：何种开发目标适合哪条路线，需满足什么条件，最小验收场景是什么；对做不到的能力直说。

## 可复用知识的最小结构

| 部分 | 要回答的技术问题 |
| --- | --- |
| 概念与边界 | 本文到底讨论哪个动作、对象、状态或约束？ |
| 共性与差异 | 哪些属性可以跨实现迁移？哪些依赖特定构建？ |
| 来源证据 | 各结论的代码/文档/测试来源是什么？ |
| 限制与反例 | 哪个假设有可能推翻结论？ |
| 工程应用 | 开发工具、模拟器或 AI 时应该如何选择？ |
| 下一步实验 | 怎样验证核心冲突或缺失的前提？ |

## 输出位置

- **机制/理论问题**：优先编辑 `topics/` 或 `research/`；有重要新归纳时可以在 `research/knowledge-notes/` 建立知识笔记。
- **用户需求与选型**：优先完善 `capabilities/<id>/README.md`，具体操作步骤放 `guides/`。
- **未获得上游共同认可的接口设计**：只能放 `contracts/`，明确 Draft。
- **项目资料**：不在综合文章里复制多份完整项目卡，使用指向 `projects/` 的链接。

**输出范例**：[快照、复制与动作重放的语义差异](../../../research/knowledge-notes/snapshot-semantics.md)。写入时按 [知识生命周期规范](../../../docs/knowledge-workflow.md) 保持来源与推导边界清晰，必要时由 [review-cr-evidence](../review-cr-evidence/SKILL.md) 审核具体事实。
