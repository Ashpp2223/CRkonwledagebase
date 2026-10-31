---
id: simulator-validation
title: "模拟器保真校准与反例验证"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 模拟器保真校准与反例验证

**能力定义**：比较自建模拟与原生对局的时序、寻路、碰撞、卡牌行为和偏差。

## 已有可衍生技术

| 来源 | 已有资产 | 复用等级 |
| --- | --- | --- |
| [royalesim](../../projects/royalesim.md) | 真实对局差分、单位时序和误差校准；指定接口有固定源码审查 | R2（仅指定接口，详见下文） |
| [hasty-cr](../../projects/hasty-cr.md) | 大量机制回归及已知失败案例 | R1（以作者资料为主） |
| [crsim-agent-larkindaniel](../../projects/crsim-agent-larkindaniel.md) | 信息泄露测试、模拟偏差、PPO 可复现实验 | R1（以作者资料为主） |
| [itzik-clashenv](../../projects/itzik-clashenv.md) | 快照隔离、随机一致性、卡牌行为测试 | R1（以作者资料为主） |
| [jason-simulator](../../projects/jason-simulator.md) | 寻路、攻击和卡牌规则验证参照 | R1（以作者资料为主） |

## 中台组合要求

- 显式记录上游仓库和固定版本，不能把不同引擎的动作/观测结构直接拼接。
- 训练、实机、模拟器三种环境的游戏版本、观察权限和延迟均需独立验证。
- 原作者报告的性能或成功率只作为研究线索，不是中台测试结果。
- 方案接入前须确认代码许可证、模型/数据授权和第三方游戏资源的使用权。
- 用最小可复现用例与反例检验后才能升级为 R3 集成能力。

[完整生态技术筛选](../../landscape/2026-10-13-landscape.md) · [能力目录](../README.md)

## 2026-10-15：RoyaleSim 源码核查升级

[跨版本校准接口](../../docs/source-audits/royalesim-client-parity-2026-10-15.md) 已按 `R2 / source-inspected` 登记到 `simulator-validation--royalesim`。可核查 `client_arms`、`replay_parity`、建筑部署末 Tick 的分支回归**代码和测试定义**；上游实际录制数据、误差数字及所有版本精度均未在本中台独立复现。

采用 [版本差异方法笔记](../../research/knowledge-notes/cr-model-selfplay-client-parity-2026-10-15.md) 构造固定客户端、卡表与动作时序的差分基准。

## 2026-10-31：版本校准适用域补充

[RoyaleSim 0.1.42 变更记录](../../projects/royalesim.md#2026-10-31-复查0142-的客户端版本差异) 将 16.402 系列的充能命中时机、隐身和冲刺状态与旧版 15.535.29 行为显式分开；0.1.40 还引入 **2026-10-19 卡表的可选覆写**。建立差分样本时，除动作、Tick 和 seed 外，至少同时保存所用**客户端构建、卡表摘要、引擎固定提交和校准分支**。这些是作者发布内容的新核查，不自动扩展 2026-10-15 静态源码审查的覆盖面。
