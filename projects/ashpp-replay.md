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

**原仓库**：[Ashpp2223/clashroyalereplay](https://github.com/Ashpp2223/clashroyalereplay)。**初次整理**：2026-10-13。仅依据公开作者文档，尚未得到原作者审核，也未独立测试。

## 公开描述的能力

Tauri + React 桌面复盘器，使用原生画面，支持节点分支、进程内状态快照、动作日志重放与状态摘要校验。

## 兼容与限制

进程内快照句柄不跨游戏进程保存；重启后需重新执行动作日志。

## 相关专题

- [回放、快照与状态恢复](../topics/cr-replay-state.md)
- [原生战斗引擎](../topics/cr-native-engine.md)

## 证据

- [仓库 README](https://github.com/Ashpp2223/clashroyalereplay)
- [补充来源](https://github.com/Ashpp2223/clashroyalereplay)

## 待复核

- 实际运行能力、对应提交 SHA、准确兼容版本、维护者确认和授权边界。
