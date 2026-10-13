---
name: research-cr-knowledge
description: "Investigate a Clash Royale technical question across GitHub source code, reverse-engineering notes, tests, issues, and experiments. Use to acquire new technical knowledge and extract verifiable claims with source provenance, game-build scope, uncertainties, and counterexamples before cataloging it. Do not use for routine project registration or PR approval."
---

# 技术知识研究：从原始资料到可核对的结论

**适用任务**：研究游戏机制、原生接口、内存结构、数据格式、模拟器差异，或者判断一项 GitHub 声明是否有技术根据。

## 输入和边界

先写出一个**可证伪的具体问题**，包括目标用途与需要的细度。例如“某构建的原生战斗状态是否可复制为独立搜索分支”，不是“全面研究模拟器”。

1. 查看已有 [研究入口](../../../research/README.md)、[专题](../../../topics/README.md)、[逆向发现索引](../../../registry/reverse-findings.yaml) 和 [实现矩阵](../../../registry/implementations.yaml)，避免重复研究。
2. 制定证据路线：原作者文档 → 具体源码入口 → 对应测试/问题报告 → 其他项目独立描述或反例；优先取**同一构建/同一语义**的资料，而非仅按 Star 排序。
3. 对每条来源记仓库/作者、固定 Git SHA、文件行区间、相关游戏 Build/ABI/资源版本、读取日期；无法固定时明确标为随时间变化的线索。
4. 将**事实、作者主张、自己的推导、假设和未知**分开记。确认一个函数存在不等于设备已运行，也不等于函数覆盖所有状态。
5. 主动查负证据：调用失败、未支持的卡牌、版本失效、与另一实现不一致、被废弃的测试数字、非独立的 Fork。
6. 如果没有合法实验环境，就只做源码静态研究，绝不捏造测试日志、通过率或兼容性。

## 知识提炼格式

对每一项可用结论记录：

- **研究问题 / 主张**：一句能单独核对的话，不写含混的“已完整实现”。
- **证据类型**：`author-documented`、`source-inspected`、`reproduced` 或 `unknown`。
- **证据锚点**：固定 SHA 的文件/行号、测试日志或论文具体章节。
- **适用边界**：游戏构建、资源、平台、ABI、Tick/坐标及观测权限；未知则标 Unknown。
- **反例与限制**：至少写明**一项未证明的泛化**；确有矛盾时保留双方来源。
- **复用价值**：它能帮助后续实现、适配还是设计验证？不把原理复用等同于源码可直接复制。
- **下一步验证**：可执行的最小实验及判定标准，而非“以后再研究”。

**输出**：优先更新已有 `research/` 或 `topics/`，只在形成跨源的新见解时创建知识笔记。允许给出“证据不足，暂不成立”的结论。若需要登记新的 Project/Capability/ReverseFinding，交由 [curate-cr-knowledge](../curate-cr-knowledge/SKILL.md) 完成；如果要求提升证据等级，交由 [review-cr-evidence](../review-cr-evidence/SKILL.md)。

## 退出检查

本轮具体回答了什么？每项关键事实有来源吗？哪些信息仅为作者报告？有没有因游戏构建/ABI/资源版本而不可比较？能否给下一位研究者留下可复验的反例或实验？

参阅 [知识生命周期规范](../../../docs/knowledge-workflow.md) 和 [知识笔记模板](../../../templates/knowledge-note.md)。
