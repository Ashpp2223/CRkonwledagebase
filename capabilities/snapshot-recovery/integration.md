# 状态快照能力：集成与验收清单（草案）

本文件不是已存在的跨仓库 API，也不承诺某个上游项目满足下述全部条件。

## 明确你的需求

| 需求 | 可考虑的技术 | 必须澄清 |
| --- | --- | --- |
| 倍速播放或时间轴跳转 | 周期性状态缓存、顺序重放 | 缓存上限、Seek 精度、缓存无效条件 |
| 交互式复盘分支 | 进程内快照 + 动作日志 | 分支如何隔离、节点 ID 与 Tick 的关系 |
| 进程重启后恢复 | 输入日志确定性重放 + 摘要校验 | 游戏版本/资源/Seed 一致性 |
| MCTS 多分支搜索 | 任意局面独立恢复或克隆 | 每次克隆耗时、并发安全、状态完整性 |

## 最小验证实验

1. 固定游戏构建、资源指纹、双方牌组、初始状态和随机种子（如果引擎暴露）。
2. 在 `tick = t` 保存状态；推进一段相同的出牌序列至 `t+n`，记录实体/手牌/圣水/塔血量/随机状态（如果可观测）的摘要。
3. 恢复 `t`，再次执行相同输入；比较逐 Tick 摘要差异，明确不可观测字段。
4. 从同一状态创建两个不同动作后缀，确认分支间不互相污染。
5. 在不同 Tick、长局面、高实体数量下分别测量快照内存、存取时间和恢复失败率。
6. 重启引擎重复验证，并**明确标注**进程内句柄不能跨进程持久化的情况。

## 记录格式（人工实验记录，而非客户端接口）

```yaml
engine_build: null
asset_fingerprint: null
scenario_id: null
snapshot_tick: null
recovery_mode: unknown # in-process-handle | serialized | replay-from-start
state_equivalence: unknown # tested | partial | failed | unknown
seed_known: false
metrics_source: null
report_link: null
```

相关实例：[皇室战争复盘器](../../projects/ashpp-replay.md)、[Replay Studio](../../projects/replay-studio.md)。
