# Draft：Battle State v0（候选概念契约）

**状态：Draft / 尚无已确认的跨项目采纳者。** 本文定义数据语义检查清单，不定义任何上游项目实际导出格式。

## 必须区分的状态层

1. **Observation**：决策者在该时刻依法/技术条件下可看到的状态（可能不完整）。
2. **SimulationState**：引擎内部全部状态（可能包含不可公开或不可读取信息）。
3. **ReplayEvidence**：从网页/日志重建的事件与不确定条件。

三者不可随意互换；不能用训练期间的全量引擎字段冒充对战时可见输入。

## 建议字段（并非现成 API）

| 字段概念 | 语义约束 |
| --- | --- |
| `engine_build` | 可复现的游戏逻辑构建标识 |
| `asset_fingerprint` | 适用资源版本/指纹，未知可为 null |
| `tick` / `tick_duration_ms` | 时间离散序号及单位，不能只存 tick |
| `perspective` | 观测归属和敌我变换方式 |
| `coordinate_frame` | 网格/内部整数单位/屏幕像素坐标与朝向 |
| `entities` | 实体 ID 来源与存活周期；可能丢帧 |
| `players` | 双方可用手牌、圣水和塔状态及可见性 |
| `provenance` | 来源、采样方式、是否推断/可见、采样时间 |

## 适配前必测

- 坐标单位的转换及反向半场的对称性。
- 游戏 Tick 与观测采样 Tick 是否一致，以及迟到数据处理。
- 新一局是否清理旧局实体 ID 和缓存。
- 无法观测/不可信字段如何用 `null` 或显式状态表达，禁止默默填 0。

来源参考：[FirstLight 架构](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/main/docs/architecture.md)、[Jason Memory Reader](https://github.com/Jason-XII/cr-memory-reader)。
