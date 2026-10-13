---
id: royalesim
title: "RoyaleSim"
type: project
status: implemented
verification: author-documented
repository: https://github.com/RoyaleGym/RoyaleSim
topics: [cr-battle-simulation, cr-ai-environment, cr-game-mechanics]
maintainers: []
last_reviewed: null
license: MIT
---

# RoyaleSim

**原始仓库**：[RoyaleGym/RoyaleSim](https://github.com/RoyaleGym/RoyaleSim)。目前仅按作者文档编目，并未得到独立运行验证或作者加入确认。

## 公开实现的内容

Rust 独立战斗引擎；README 描述整数 Tick 仿真及 Python 调用（Battle/reset/step）。

## 版本、运行与复用限制

自研规则不能未经逐项验证就称为官方原生引擎等价实现；底层源码 MIT 不等于第三方游戏素材获许可。

## 相关能力

- [智能体环境与模型对接](../capabilities/agent-environment/README.md)：Rust 底层战斗引擎与 Python API（R1，author-documented）
- [可修改的战斗规则模拟](../capabilities/rules-simulation/README.md)：Rust 固定 tick 战斗引擎（R1，author-documented）

## 相关研究专题

- [战斗机制、寻路与数值](../topics/cr-game-mechanics.md)

- [独立战斗模拟器](../topics/cr-battle-simulation.md)
- [AI 训练环境与决策](../topics/cr-ai-environment.md)

## 来源

- [上游 README](https://github.com/RoyaleGym/RoyaleSim)

**待核实**：精确上游提交、运行环境、独立复现测试以及上游作者审阅。
