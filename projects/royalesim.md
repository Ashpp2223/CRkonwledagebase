---
id: royalesim
title: "RoyaleSim"
type: project
status: implemented
verification: author-documented
repository: https://github.com/RoyaleGym/RoyaleSim
topics: [cr-battle-simulation, cr-ai-environment, cr-game-mechanics]
maintainers: []
last_reviewed: "2026-10-31"
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

**待核实**：独立运行环境、复现实验、完整跨构建差分结果及上游作者审阅。指定接口的固定源码审查见下文。

## 2026-10-15 追加：真实轨迹差分与客户端规则分支

源码定位了 [`client_arms.rs`](https://github.com/RoyaleGym/RoyaleSim/blob/39e7d48253877858a064a4df140f01f4c4866d6c/crates/royalesim/src/client_arms.rs)、[`replay_parity.rs`](https://github.com/RoyaleGym/RoyaleSim/blob/39e7d48253877858a064a4df140f01f4c4866d6c/crates/royalesim/examples/replay_parity.rs) 与 [`building_deploy_last_tick.rs`](https://github.com/RoyaleGym/RoyaleSim/blob/39e7d48253877858a064a4df140f01f4c4866d6c/crates/royalesim/tests/building_deploy_last_tick.rs)。其中 `15.535.29` 的客户端规则覆写与 `16.402` 默认 ledger 分别管理，按 Tick 对齐数据后对比最早分叉，并通过机制选择分支构造反例。

`simulator-validation--royalesim` **单项 R2 静态核查**，见 [详细审查](../docs/source-audits/royalesim-client-parity-2026-10-15.md)。这不证明整个 RoyaleSim 已达到原生保真或任何第三方已运行验证。

## 2026-10-31 复查：0.1.42 的客户端版本差异

[固定提交 `b21765e`](https://github.com/RoyaleGym/RoyaleSim/tree/b21765e58c5b09c30cf0eca5db897ac3c51b569f) 的 [CHANGELOG](https://github.com/RoyaleGym/RoyaleSim/blob/b21765e58c5b09c30cf0eca5db897ac3c51b569f/CHANGELOG.md) 记载 2026-10-22 版本 `0.1.42`（PyPI 于 10 月 23 日发布），主要延伸了 16.402 客户端的机制差分，而不是宣布完全保真：

- **0.1.42**：`charge.CHARGED_HIT_TIMING` 将充能完毕所在 Tick 与**已经经过一次满充能步进**的攻击区分；作者以王子/黑暗王子真实轨迹解释新版客户端行为。
- **0.1.41**：`targeting.INVISIBILITY`（皇家幽灵重隐/攻击显形时机）和 `knockback.DASH_IMMUNE_PUSH`（冲刺免伤状态下的击退）。
- **0.1.40**：新增 2026-10-19 平衡更新对应的可选卡表 `client160402017_20261019`；**默认卡表不变**。通过 `calibration_overrides` 指定，`Battle.card_table_fnv1a64()` 可记录实际使用的卡表摘要。

上游说明：旧版 `client_arms("15.535.29")` 与 `replay_parity` 继续选择旧行为；上述发布中 `SNAPSHOT_FORMAT` 仍为 `20`。使用不同客户端或平衡内容进行差分时，应同时固定**引擎提交、客户端 build、卡表及校准分支**，避免把版本差异误归因于物理规律错误。

这是一份上游变更说明核对，不是本中台对新提交的 R2 源码审计或任何 R3 集成测试。既有 `simulator-validation--royalesim` 的 **R2** 仍仅适用于 [2026-10-15 固定源码审查](../docs/source-audits/royalesim-client-parity-2026-10-15.md) 指明的接口。
