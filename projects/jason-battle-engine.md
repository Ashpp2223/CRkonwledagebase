---
id: jason-battle-engine
title: "Daybreak CR (historical Clash Royale Battle Engine)"
type: project
status: implemented
verification: author-documented
repository: https://github.com/Jason-XII/daybreak-cr
topics: [cr-native-engine, cr-ai-environment, cr-replay-state]
maintainers: []
last_reviewed: null
license: unknown
---

# Jason Clash Royale Battle Engine

[上游仓库](https://github.com/Jason-XII/daybreak-cr) · [源码核查](../docs/source-audits/native-engine-2026-10-13.md)

## 已定位的代码入口

- [`Engine.reset`](https://github.com/Jason-XII/daybreak-cr/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/engine.py#L202-L221) 固定原生 headless 对局及初始 Tick 暖机；
- [`Engine.step`](https://github.com/Jason-XII/daybreak-cr/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/engine.py#L222-L239) 以 `Play(owner, slot, x, y)` 提交动作，返回 `Transition`；
- [`RenderedEngine`](https://github.com/Jason-XII/daybreak-cr/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/engine.py#L289-L320) 控制原生渲染模式。

公开 README 将 ARM64 Android 原生探针、训练缓存和 Linux x86_64 的 `clapha-engine` PPO 训练区分为不同阶段，具体版本/平台请按各模块核对。

## 复用约束

中台仅对**接口代码存在及签名**做了静态核查；客户端源码没有已确认的整体标准许可证，不能默认复制。没有完成统一安装、版本兼容或性能验证。同 owner 同步动作的回执匹配有限制；遇到写入通信异常不能盲重试。

[原生控制能力](../capabilities/battle-control/README.md) · [兼容性对照](../capabilities/battle-control/compatibility.md)

## 仓库重命名与技术阶段（2026-11-13 核查）

原 `Jason-XII/clash-royale-battle-engine` 已重命名为 `Jason-XII/daybreak-cr`，GitHub repository ID 同为 `1366867946`。历史提交 `2b3361954c189a8ea508f3f54cf94a56c2e045fc` 和 `70a08af6807fa4d59a11c7d52bf6272a96afe30c` 仍可在新仓库查询。上文历史 `engine.py` 入口属于旧提交，不代表当前 main 仍有同路径。

当前 main 的核心是 `cr/engine.py`（blob `2fd09083a59241137e49048ec507c8e4abbe384b`），依赖仓库外 `clapha-engine` 的 `CrxEnv`；其 `State`、`Play`、`Transition`、`Engine` 提供训练/回放驱动接口。`cr/live_budget.py`（blob `e5de3dd79cbdef3b77f7e452f8685d4165fa6a82`）处理动作在途、圣水预留与回执滞后；`tests/test_engine.py`（blob `64b8f126d3e6e3d7dd3adf0351ba1ce38433784c`）有不依赖原生引擎的动作接受/拒绝测试。未执行测试；当前代码与历史接口的兼容性未确认。

原独立登记 `jason-daybreak` 已并入此项目 ID；保留旧研究文档作历史链接，不再重复计算项目。
