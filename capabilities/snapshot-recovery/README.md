---
id: snapshot-recovery
title: "状态快照与恢复"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 状态快照与恢复

**开发需求**：历史局面重复运行、复盘分支、按 Tick 跳转或者 MCTS 策略搜索。

首先区分四种不同东西：**原生进程内快照**、**按 Tick 缓存状态**、**动作日志从起点重放**、**独立引擎实例的任意局面克隆**。现阶段不能证明它们等价。

## 公开实现对照

| 项目 | 明确证据 | 中台等级 | 尚未确认 |
| --- | --- | --- | --- |
| [FirstLight CR](../../projects/firstlight-cr.md) | `NativeClashEnv.create_snapshot/restore/release_snapshot` + 原生探针命令 | **R2/source-inspected**（只针对进程内快照接口的存在和限制） | 跨进程持久化、跨 manager generation 恢复、独立实例并行克隆、实际性能 |
| [Ashpp 复盘器](../../projects/ashpp-replay.md) | `BattleController.snapshot_create/restore` + 清空旧分支调度 + 动作日志回放 | **R2/source-inspected**（只针对控制流程） | 全 GameState 字节级等价、并行多实例、不同平台集成 |
| [Replay Studio](../../projects/replay-studio.md) | 按 Tick 预演算、应用级缓存和跳转 | R1/author-documented | 不等同于原生任意时刻快照 |

**第一项是本次重要更正**：FirstLight 在其原生控制层中确实具备快照接口；旧版知识库漏收了这一能力。具体证据：[Python API](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/cr_native_env.py#L2828-L2860) 与 [C++ 探针命令](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/probe/cr_replay_probe.cpp#L6804-L6868)。

Ashpp 的复盘控制器还明确处理了快照**之外**的调度队列，恢复后会清空旧分支未来动作：[源码](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L286-L312)。

## 关键区别

- **句柄有效期**：FirstLight 文档明确仅当前应用进程和 manager generation 有效；Ashpp 也不是序列化快照方案。
- **状态覆盖率**：即使原生快照保存内部 GameState，也不能未经测试就假设命令调度、外部缓存、模型记忆和 RNG 均被完整覆盖。
- **分支隔离**：进程内原地恢复是恢复一个实例，不等于可同时运行多条相互独立分支。
- **精确性**：Hash 相等最多证明已选摘要字段一致；证明全部状态等价需单独设计完整字段/差分验证。

## 准备开展的实验

请根据 [快照集成与验收清单](integration.md) 固定代码和游戏版本，测量恢复时间、内存、状态一致性、分支污染及重启边界。未执行真实实验不得将 R2 升为 R3。

[来源核查](../../docs/source-audits/native-engine-2026-10-13.md) · [返回能力目录](../README.md)
