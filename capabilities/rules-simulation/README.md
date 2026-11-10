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
| [RoyaleSim](../../projects/royalesim.md) | R1 · author-documented | Rust 固定 Tick 模拟；0.1.44 加入 16.635 的 `Giant_EV1` 表驱动规则 | 觉醒巨人时序来自表和内部测试，作者尚未用该卡的原生捕获校准 | [0.1.51](https://github.com/RoyaleGym/RoyaleSim/blob/d62501352d7995b352a167730c4a31e49f4ed570/CHANGELOG.md) |
| [crforge](../../projects/crforge.md) | R1 · author-documented | Java 21 / 50 ms Tick，支持 16.635.3 / 16.635.8 数据及觉醒巨人 | 作者回放对照不能扩展为全部规则等价 | [来源](https://github.com/voonhous/crforge/tree/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df) |

> 上表为**作者文档层级的能力关联**，未独立检查完整源码或运行测试；R0/R1 并不是可下载即用的组件。细节见 [成熟度规则](../../docs/reuse-maturity.md) 和 [机器登记](../../registry/implementations.yaml)。

## 选择与集成判断

- 强调可解释和规则修改时考虑独立模拟器。
- 需要对齐原游戏时，每个特殊卡牌行为都应通过可复现对照测试证明，而非套用整体准确率。

## 尚缺的中台资产

- 可复现的运行环境及固定提交、版本指纹。
- 统一测试场景下的功能验证、性能数据和错误案例。
- 作者审阅、许可证核对与明确的集成入口（若存在）。

[返回能力目录](../README.md) · [查看项目目录](../../projects/README.md)

## 扩展来源（2026-10-13）：已登记的高衍生实现

下面是本轮 GitHub 调查新增的候选。**能力评级以 [实现矩阵](../../registry/implementations.yaml) 为准；R2 仅对指定源码范围有效，均未完成第三方集成验收。**

| 项目 | 新的可复用切入点 |
| --- | --- |
| [ClashRoyaleEnv](../../projects/itzik-clashenv.md) | C++ 17 规则模拟与 PPO/搜索接口；R1 |
| [CRSim Agent](../../projects/crsim-agent-larkindaniel.md) | 固定八卡历史规则可重复实验；R1 |

[技术组合地图](../../landscape/composition-patterns.md) · [高价值项目调查](../../landscape/2026-10-13-landscape.md)

## 2026-11-10：16.635 觉醒巨人规则实现

[新版对照研究](../../research/knowledge-notes/cr-16635-evo-giant-parity-2026-11-10.md) 明确了两条自建模拟路线：crforge 的 `giant-evo-rage-v1/evo_giant_rage` 已有真实参考对照的 `diagnostic_match` 作者记录；RoyaleSim 将表中的狂暴触发、区域时钟、克隆语义写入专项场景测试，但承认尚无该卡的原生回放实测。本页的规则模拟能力保持 R1；crforge 的逐 Tick **校验接口**另在 [模拟器保真能力](../simulator-validation/README.md) 获得限定范围的 R2 静态审查。
