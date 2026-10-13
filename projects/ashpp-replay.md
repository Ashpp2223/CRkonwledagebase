---
id: ashpp-replay
title: "皇室战争复盘器"
type: project
status: implemented
verification: author-documented
repository: https://github.com/Ashpp2223/clashroyalereplay
topics: [cr-replay-state, cr-native-engine]
maintainers: []
last_reviewed: null
license: unknown
---

# 皇室战争复盘器

[上游仓库](https://github.com/Ashpp2223/clashroyalereplay) · [固定源码核查](../docs/source-audits/native-engine-2026-10-13.md)

Tauri + React 复盘器，带原生渲染、分支节点、原生进程内快照和重放恢复。源码在 [`BattleController`](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L43-L59) 中封装基本对局控制：`reset`、`step`、`play_card`；另有 [`snapshot_restore`](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L286-L312) 清理未来调度，防止分支污染。重放时检查动作顺序与预期摘要。[摘要构造](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L15-L35) 不等于完整原生 GameState 内容。

此程序的集成行为与客户端资源依赖于固定的构建与本地环境；**进程内快照句柄不跨进程**。尚未作为通用第三方 SDK 发布，许可证需单独确认，不能因为代码可见就默认具有复制许可。

[原生控制能力](../capabilities/battle-control/README.md) · [快照能力](../capabilities/snapshot-recovery/README.md) · [接入验收](../capabilities/snapshot-recovery/integration.md)
