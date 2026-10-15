---
id: cr-game-mechanics
title: "战斗机制、寻路与数值"
type: topic
status: investigating
verification: author-documented
projects: [jason-simulator, hasty-cr, crforge, royalesim, itzik-clashenv, crsim-agent-larkindaniel]
last_reviewed: null
---

# 战斗机制、寻路与数值

本页是**跨项目研究专题**；面向开发任务优先查看 [可修改的战斗规则模拟](../capabilities/rules-simulation/README.md)。

## 相关项目与路线（依据公开文档）

| 项目 | 技术来源 |
| --- | --- |
| [Jason Clash Royale Simulator](../projects/jason-simulator.md) | [作者仓库](https://github.com/Jason-XII/clash-royale-simulator) |
| [Hasty-CR](../projects/hasty-cr.md) | [作者仓库](https://github.com/hastylmao/Hasty-CR) |
| [crforge](../projects/crforge.md) | [作者仓库](https://github.com/voonhous/crforge) |
| [RoyaleSim](../projects/royalesim.md) | [作者仓库](https://github.com/RoyaleGym/RoyaleSim) |

## 研究边界与差异

研究寻路、索敌、攻击和状态效果时应优先提交可复现反例；实现 100+ 卡牌数据定义不等于规则逐项准确。

## 需要补充的证据

- 固定游戏客户端、资源和源代码提交版本。
- 反例、差分对照测试、性能测量的条件。
- 作者审核与具体许可证影响（公开不代表可直接复制）。

[能力总入口](../capabilities/README.md) · [项目索引](../projects/README.md)

## 新增技术来源（2026-10-13）

- [ClashRoyaleEnv](../projects/itzik-clashenv.md)：C++17确定性模拟器、独立深拷贝分支、搜索教师、PPO训练及浏览器可视化。
- [CRSim Agent](../projects/crsim-agent-larkindaniel.md)：冻结八卡的确定性模拟、信息公平性审计、PPO复现实验。

## 2026-10-15：从单项规则反例校准机制

[RoyaleSim 静态核查](../docs/source-audits/royalesim-client-parity-2026-10-15.md) 以 `combat.BUILDING_DEPLOY_LAST_TICK` 为具体例子，说明 Tesla 和普通建筑的部署末帧行为不能用一条笼统规则概括。通过固定客户端构建和 `calibration_overrides`，可以保存不同客户端规则而不污染原本的仿真基线。
