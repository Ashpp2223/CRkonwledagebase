---
id: cr-ai-environment
title: "AI 训练环境与决策"
type: topic
status: investigating
verification: author-documented
projects: [firstlight-cr, jason-battle-engine, jason-simulator, tencent-model-harness, hasty-cr, royalegym, royalesim, crforge, katacr]
last_reviewed: null
---

# AI 训练环境与决策

本页是**跨项目研究专题**；面向开发任务优先查看 [智能体环境与模型对接](../capabilities/agent-environment/README.md)、[对局状态观测](../capabilities/state-observation/README.md)。

## 相关项目与路线（依据公开文档）

| 项目 | 技术来源 |
| --- | --- |
| [FirstLight CR](../projects/firstlight-cr.md) | [作者仓库](https://github.com/Jaasssoooonnnnn/FirstLight_CR) |
| [Jason Clash Royale Battle Engine](../projects/jason-battle-engine.md) | [作者仓库](https://github.com/Jason-XII/clash-royale-battle-engine) |
| [Jason Clash Royale Simulator](../projects/jason-simulator.md) | [作者仓库](https://github.com/Jason-XII/clash-royale-simulator) |
| [Tencent Model Harness](../projects/tencent-model-harness.md) | [作者仓库](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness) |
| [Hasty-CR](../projects/hasty-cr.md) | [作者仓库](https://github.com/hastylmao/Hasty-CR) |
| [RoyaleGym](../projects/royalegym.md) | [作者仓库](https://github.com/RoyaleGym/RoyaleGym) |
| [RoyaleSim](../projects/royalesim.md) | [作者仓库](https://github.com/RoyaleGym/RoyaleSim) |
| [crforge](../projects/crforge.md) | [作者仓库](https://github.com/voonhous/crforge) |
| [KataCR](../projects/katacr.md) | [作者仓库](https://github.com/wty-yy/KataCR) |

## 研究边界与差异

模仿学习、PPO、视觉识别、实时模型部署是不同流水线环节。不能把模型训练成果等同于已经有可部署的统一接口。

## 需要补充的证据

- 固定游戏客户端、资源和源代码提交版本。
- 反例、差分对照测试、性能测量的条件。
- 作者审核与具体许可证影响（公开不代表可直接复制）。

[能力总入口](../capabilities/README.md) · [项目索引](../projects/README.md)
