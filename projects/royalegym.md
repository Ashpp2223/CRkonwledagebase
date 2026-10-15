---
id: royalegym
title: "RoyaleGym"
type: project
status: implemented
verification: author-documented
repository: https://github.com/RoyaleGym/RoyaleGym
topics: [cr-battle-simulation, cr-ai-environment]
maintainers: []
last_reviewed: null
license: MIT
---

# RoyaleGym

**原始仓库**：[RoyaleGym/RoyaleGym](https://github.com/RoyaleGym/RoyaleGym)。目前仅按作者文档编目，并未得到独立运行验证或作者加入确认。

## 公开实现的内容

Python 侧智能体接口，README 提供与底层 RoyaleSim 共同使用的对局与训练示例，面向 Gymnasium / PettingZoo 类工作流。

## 版本、运行与复用限制

必须核对 RoyaleSim 版本、依赖、卡牌覆盖和仿真规则精度。

## 相关能力

- [智能体环境与模型对接](../capabilities/agent-environment/README.md)：Gymnasium/PettingZoo 风格环境与评测（R1，author-documented）

## 相关研究专题

- [独立战斗模拟器](../topics/cr-battle-simulation.md)
- [AI 训练环境与决策](../topics/cr-ai-environment.md)

## 来源

- [上游 README](https://github.com/RoyaleGym/RoyaleSim)

**待核实**：精确上游提交、运行环境、独立复现测试以及上游作者审阅。

## 2026-10-15 补全模块化生态（独立 Project）

- [RoyaleSim](royalesim.md)：规则模拟器与客户端规则校准。
- [RoyaleLearn](royale-learn.md)：训练/模型存档。
- [RoyaleImitate](royale-imitate.md)：模仿/教师权重工件。
- [RoyaleViser](royale-viser.md)：保存轨迹及实时对局可视化。
- [RoyaleBot](royale-bot.md)：限定 Null's Android 客户端的模型部署。

这些模块分别建项目 ID，不将完整生态笼统归为 RoyaleGym 单一仓库的内建功能。
