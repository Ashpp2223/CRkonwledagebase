---
id: cr-battle-simulation
title: "独立战斗模拟器"
type: topic
status: investigating
verification: author-documented
projects: [jason-simulator, hasty-cr, royalegym, royalesim, crforge, itzik-clashenv, crsim-agent-larkindaniel]
last_reviewed: null
---

# 独立战斗模拟器

本页是**跨项目研究专题**；面向开发任务优先查看 [可修改的战斗规则模拟](../capabilities/rules-simulation/README.md)、[智能体环境与模型对接](../capabilities/agent-environment/README.md)。

## 相关项目与路线（依据公开文档）

| 项目 | 技术来源 |
| --- | --- |
| [Jason Clash Royale Simulator](../projects/jason-simulator.md) | [作者仓库](https://github.com/Jason-XII/clash-royale-simulator) |
| [Hasty-CR](../projects/hasty-cr.md) | [作者仓库](https://github.com/hastylmao/Hasty-CR) |
| [RoyaleGym](../projects/royalegym.md) | [作者仓库](https://github.com/RoyaleGym/RoyaleGym) |
| [RoyaleSim](../projects/royalesim.md) | [作者仓库](https://github.com/RoyaleGym/RoyaleSim) |
| [crforge](../projects/crforge.md) | [作者仓库](https://github.com/voonhous/crforge) |

## 研究边界与差异

各独立模拟器有不同语言、时基、卡牌覆盖率和验证方式；任何性能倍数都必须在统一硬件及统一对局负载下比较。

## 需要补充的证据

- 固定游戏客户端、资源和源代码提交版本。
- 反例、差分对照测试、性能测量的条件。
- 作者审核与具体许可证影响（公开不代表可直接复制）。

[能力总入口](../capabilities/README.md) · [项目索引](../projects/README.md)

## 新增技术来源（2026-10-13）

- [ClashRoyaleEnv](../projects/itzik-clashenv.md)：C++17确定性模拟器、独立深拷贝分支、搜索教师、PPO训练及浏览器可视化。
- [CRSim Agent](../projects/crsim-agent-larkindaniel.md)：冻结八卡的确定性模拟、信息公平性审计、PPO复现实验。
