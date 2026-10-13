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
| [royalesim](../../projects/royalesim.md) | 真实对局差分、单位时序和误差校准日志 | R1（以作者资料为主） |
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
