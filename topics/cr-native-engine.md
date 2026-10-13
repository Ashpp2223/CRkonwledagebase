---
id: cr-native-engine
title: "原生战斗引擎"
type: topic
status: investigating
verification: author-documented
projects: [firstlight-cr,jason-battle-engine,replay-studio,ashpp-replay]
last_reviewed: null
---

# 原生战斗引擎

**研究范围**：原版游戏原生逻辑驱动的离线对局、探针与 Python 环境。

## 相关实现（作者文档整理）

| 项目 | 路线 / 重点 |
| --- | --- |
| [FirstLight CR](../projects/firstlight-cr.md) | 原生战斗环境、结构化状态与动作、Parquet 回放重建、模仿学习与 PPO 自博弈 |
| [Jason Clash Royale Battle Engine](../projects/jason-battle-engine.md) | 以 Python API 封装原生战斗引擎、对局数据与训练流水线 |
| [Clash Royale Replay Studio](../projects/replay-studio.md) | 解析 RoyaleAPI 独立对局 HTML，在本地原生引擎中预演算、缓存并以 0.25×–16× 倍速回放。 |
| [皇室战争复盘器](../projects/ashpp-replay.md) | Tauri + React 桌面复盘器，使用原生画面，支持节点分支、进程内状态快照、动作日志重放与状态摘要校验。 |

## 复用判断

优先复用**公开可验证的机制描述、接口设计方法与测试思路**。实际代码复制需确认许可证、上游版权和版本适用性；不同项目的状态、时钟、坐标、卡牌 ID 不应假定兼容。

## 待核实

- 各项目固定提交、支持版本及运行证据。
- 同等测试条件下的行为差异和性能数据。
- 作者是否愿意共同维护专题。
