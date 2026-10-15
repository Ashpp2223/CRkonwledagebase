---
id: agent-runtime
title: "智能体运行时与决策执行编排"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 智能体运行时与决策执行编排

**能力定义**：隔离观测、模型推理、输入调度、回执、设备生命周期和错误恢复。

## 已有可衍生技术

| 来源 | 已有资产 | 复用等级 |
| --- | --- | --- |
| [clashai-vegetableleaf](../../projects/clashai-vegetableleaf.md) | 观测—策略—输入与版本化部署检查 | R1（以作者资料为主） |
| [claude-royale](../../projects/claude-royale.md) | 指挥 Agent 与执行 Agent 并发，延迟补偿 | R1（以作者资料为主） |
| [build-a-bot](../../projects/build-a-bot.md) | 检测器、状态表示、动作决策的分层框架 | R1（以作者资料为主） |
| [tencent-model-harness](../../projects/tencent-model-harness.md) | 国服状态映射、模型推理、动作执行回执 | R1（以作者资料为主） |

## 中台组合要求

- 显式记录上游仓库和固定版本，不能把不同引擎的动作/观测结构直接拼接。
- 训练、实机、模拟器三种环境的游戏版本、观察权限和延迟均需独立验证。
- 原作者报告的性能或成功率只作为研究线索，不是中台测试结果。
- 方案接入前须确认代码许可证、模型/数据授权和第三方游戏资源的使用权。
- 用最小可复现用例与反例检验后才能升级为 R3 集成能力。

[完整生态技术筛选](../../landscape/2026-10-13-landscape.md) · [能力目录](../README.md)

## 2026-10-15 新增设备部署示例

- [RoyaleBot](../../projects/royale-bot.md)：将 RoyaleLearn 模型部署到**特定 Null's Royale 15.535.13 ARM64** 客户端，具备 PC 侧推理、dry-run 与可选可视化；客户端准备 `rb-build` 是单独发布的工具。此条为 R1/作者文档，不能自动扩展到正式服。
