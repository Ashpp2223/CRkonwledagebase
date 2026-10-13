---
id: jason-battle-engine
title: "Jason Clash Royale Battle Engine"
type: project
status: implemented
verification: author-documented
repository: https://github.com/Jason-XII/clash-royale-battle-engine
topics: [cr-native-engine, cr-ai-environment, cr-replay-state]
maintainers: []
last_reviewed: null
license: unknown
---

# Jason Clash Royale Battle Engine

[上游仓库](https://github.com/Jason-XII/clash-royale-battle-engine) · [源码核查](../docs/source-audits/native-engine-2026-10-13.md)

## 已定位的代码入口

- [`Engine.reset`](https://github.com/Jason-XII/clash-royale-battle-engine/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/engine.py#L202-L221) 固定原生 headless 对局及初始 Tick 暖机；
- [`Engine.step`](https://github.com/Jason-XII/clash-royale-battle-engine/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/engine.py#L222-L239) 以 `Play(owner, slot, x, y)` 提交动作，返回 `Transition`；
- [`RenderedEngine`](https://github.com/Jason-XII/clash-royale-battle-engine/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/engine.py#L289-L320) 控制原生渲染模式。

公开 README 将 ARM64 Android 原生探针、训练缓存和 Linux x86_64 的 `clapha-engine` PPO 训练区分为不同阶段，具体版本/平台请按各模块核对。

## 复用约束

中台仅对**接口代码存在及签名**做了静态核查；客户端源码没有已确认的整体标准许可证，不能默认复制。没有完成统一安装、版本兼容或性能验证。同 owner 同步动作的回执匹配有限制；遇到写入通信异常不能盲重试。

[原生控制能力](../capabilities/battle-control/README.md) · [兼容性对照](../capabilities/battle-control/compatibility.md)
