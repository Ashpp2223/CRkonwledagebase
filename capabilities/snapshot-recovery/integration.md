# 状态快照：集成与验证清单（尚未实际执行）

此文仅列出**真实存在的具体接口及待执行实验**，并非声称当前各仓库已经支持多实例快照、序列化恢复或 MCTS 任意搜索。

## 接口现状

- [FirstLight NativeClashEnv](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/cr_native_env.py#L2835-L2860)：`create_snapshot()` → 句柄；`restore(handle)` → 原地恢复并观察；`release_snapshot(handle)` → 释放。当前 **app 进程 / headless manager generation** 有效。
- [Ashpp BattleController](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L240-L312)：`snapshot_create()`、`snapshot_restore(handle)`、`snapshot_release(handle)`；恢复时另执行 `replay-schedule-clear`，避免旧分支未执行指令残留。
- [Replay Studio](../../projects/replay-studio.md)：应用按 Tick 预演算与缓存，另按回放事件重建；不可据此推断存在通用原生 snapshot API。
- [Jason Engine](../../projects/jason-battle-engine.md)：本次核查的公开高级 `Engine` 封装仅确认 reset/step/schedule；**没有确认**它提供独立的 snapshot 公共方法。不要将其内部探针上游能力等同于可用客户端接口。

## 应用目标与合适机制

| 场景 | 适用思路 | 不能跳过的条件 |
| --- | --- | --- |
| 时间轴拖动 | 周期缓存/顺序重建 | 精确 Tick 和缓存失效规则 |
| 单进程交互式分支 | 进程内快照 + 独立动作后缀 | 调度队列与外部状态是否恢复 |
| 应用重启恢复 | 固定构建后基于 Seed 和日志重放 | 实际生成资源和牌组等完全一致 |
| MCTS 训练 | 低成本任意状态保存/恢复、多个独立实例 | 克隆时延、内存、并发安全、隐藏状态一致性 |

## 设备测试协议（请实际运行后提交日志）

1. 锁定每个实验的上游提交 SHA、APK/内容版本、探针 SHA、平台/ABI、牌组、形态、等级、Seed 与模拟 Tick。
2. 从 `tick = t` 保存句柄 H；继续运行后缀序列 S，保留每一步实体/手牌/圣水/塔血量摘要与终局信息。
3. 恢复 H，重复 S，逐 Tick 比较。**把“摘要字段”与“未测量的内部状态”分开报告。**
4. 创建两条相互矛盾的动作后缀，先跑 A，再恢复 H 跑 B，检查未执行动作、观察缓存、调度队列及模型隐状态是否污染 B。
5. 在 H 未释放、已释放、创建新 match、更换 manager generation、重启 app 之后分别恢复，确认拒绝与错误消息。
6. 测量 `create/restore/release` 的 P50/P95 时间、快照内存占用、成功率、峰值实体数；报告具体硬件与有无渲染。
7. 如果目标是**并行搜索**，重复实验，直到能够证明两个分支真正处于独立引擎实例；反复切换同一实例只能证明串行多分支。
8. 针对随机生成、复数单位、死亡衍生实体、技能生效与网络/渲染切换设计负向场景。

## 实验记录（示例字段，不是任何上游协议）

```yaml
capability_id: snapshot-recovery
project_id: firstlight-cr
source_commit: null
game_build: null
asset_fingerprint: null
probe_sha256: null
hardware: null
snapshot_tick: null
mode: in-process
tested_fields: []
test_status: not-run
branch_isolation: unknown
rng_equivalence: unknown
serialized_restoration: unknown
latency_p95_ms: null
evidence_log_url: null
```

所有未执行项目保留 `not-run` 和 `unknown`，不得填入猜测。参阅 [源码核查](../../docs/source-audits/native-engine-2026-10-13.md)。
