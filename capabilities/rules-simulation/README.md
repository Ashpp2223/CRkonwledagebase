---
id: rules-simulation
title: "可修改的战斗规则模拟"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 可修改的战斗规则模拟

**需要解决的问题**：怎样在自己的模拟器中实现、验证与扩展战斗机制？

**能力边界**：可配置自建模拟器不等于官方原生行为的逐 tick 等价。

## 采用前必须回答

- 确定 Tick、定点精度和随机种子控制。
- 逐项验证索敌、寻路、碰撞、攻击、死亡与卡牌生命周期。
- 明确已经覆盖的卡牌、形态及未实现机制。
- 提供对照实验、反例和性能测量条件。

## 已公开的相关实现

| 来源项目 | 复用成熟度 / 证据 | 公开描述 | 限制 | 原始来源 |
| --- | --- | --- | --- | --- |
| [Jason Clash Royale Simulator](../../projects/jason-simulator.md) | R1 · author-documented | 自主战斗实现、寻路与卡牌行为 | README 称实现 47 卡，非官方原生逻辑 | [来源](https://github.com/Jason-XII/clash-royale-simulator) |
| [Hasty-CR](../../projects/hasty-cr.md) | R1 · author-documented | 整数确定性机制实现、机制探针与大量测试 | 仍须验证与目标原生版本的逐项一致性 | [来源](https://github.com/hastylmao/Hasty-CR) |
| [RoyaleSim](../../projects/royalesim.md) | R1 · author-documented | Rust 固定 tick 战斗引擎 | 卡牌覆盖、准确性需基准评估 | [来源](https://github.com/RoyaleGym/RoyaleSim) |
| [crforge](../../projects/crforge.md) | R1 · author-documented | Java ECS、数据驱动卡牌和状态效果 | 实现广度不代表无偏差 | [来源](https://github.com/voonhous/crforge) |

> 上表为**作者文档层级的能力关联**，未独立检查完整源码或运行测试；R0/R1 并不是可下载即用的组件。细节见 [成熟度规则](../../docs/reuse-maturity.md) 和 [机器登记](../../registry/implementations.yaml)。

## 选择与集成判断

- 强调可解释和规则修改时考虑独立模拟器。
- 需要对齐原游戏时，每个特殊卡牌行为都应通过可复现对照测试证明，而非套用整体准确率。

## 尚缺的中台资产

- 可复现的运行环境及固定提交、版本指纹。
- 统一测试场景下的功能验证、性能数据和错误案例。
- 作者审阅、许可证核对与明确的集成入口（若存在）。

[返回能力目录](../README.md) · [查看项目目录](../../projects/README.md)
