# 原生战斗控制：接入与验证手册

**范围**：帮助开发者选择既有控制接口、理解语义并计划可复现接入。下面只整理已定位的入口和实验设计，**不是中台提供的可安装 SDK**，也不是跨项目统一 ABI。

## 第一关：选择哪一层？

| 目标 | 优先阅读的入口 | 警告 |
| --- | --- | --- |
| 离线策略训练、合法动作掩码、双方观测 | FirstLight `BattleEnvV1` | ObservationV1 的 FAIR 观测 != 内部完整状态 |
| 直接按 Tick 推进原生引擎、读取探针状态 | FirstLight `NativeClashEnv` | 绑定当前进程/manager，游戏资源版本严格 |
| 简洁的 `reset(seed, match)` / `step(plays, ticks)` | Jason `Engine` | `Transition.executed` 有同 owner 同步动作识别限制 |
| 原生渲染的暂停、逐帧、历史节点与出牌 | Ashpp `BattleController` | 产品内部桥接，不承诺第三方稳定集成接口 |
| 导入 RoyaleAPI HTML 并观看重建 | ak1NaN Replay Studio | 隐藏状态缺失，不能声明完全复原 |

## 已审阅接口的签名对照

| 维度 | FirstLight | Jason Engine | Ashpp BattleController |
| --- | --- | --- | --- |
| 低层创建 | `NativeClashEnv(host, port, timeout)` | `Engine(host, port, timeout)` | `BattleController(runtime, engine_factory)` |
| 初始化 | `BattleEnvV1.reset(config, ...)` / `NativeClashEnv.create_match(...)` | `Engine.reset(seed=1, match=None)` | `reset(seed, deck0, deck1, forms0, ...)` |
| 推进 | `BattleEnvV1.step(actions, ...)` / `NativeClashEnv.step(ticks)` | `Engine.step(actions=(), ticks=5)` | `step(ticks=1, expected_tick=None)` |
| 观测 | `ObservationV1` 或原生 `observe*` | `State` | 结构化 `observation` 及其摘要 |
| 动作 | `ActionV1`，包含执行偏移及目标 | `Play(owner, slot, x, y)` | `play_card(owner, slot, x, y, expected_tick)` |
| 时间与返回 | 双方观测、奖励、终局等 / 原生命令回执 | `Transition(state, advanced, executed)` | 应用字典，拒绝无效基点并记录动作 |
| 快照 | `create_snapshot/restore/release_snapshot` | 未确认公开高级快照方法 | `snapshot_create/restore/release` |

以上是**代码签名层面**的静态核查结果：[FirstLight BattleEnv](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/battle_env.py#L2341-L2350) / [底层快照](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/cr_native_env.py#L2835-L2859) / [Jason Engine](https://github.com/Jason-XII/clash-royale-battle-engine/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/engine.py#L147-L161) / [Ashpp Controller](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L188-L209)。

## 必须执行的接入准备

1. 把目标游戏**客户端构建、资源版本、上游提交、原生探针 SHA/构建来源**登记为固定身份；不能只填“最新版”。
2. 先独立安装上游要求的运行环境，遵循各自 README。由使用者自行合法提供客户端文件；中台不下载或分发游戏专有文件。
3. 查询运行时 `status` / attestation（若上游提供），确认模式确实为 `headless` 或预期的 `native-render`；避免重复启动或占用已经使用的设备。
4. 固定双方牌组、等级、塔楼、Seed、游戏模式和初始牌序；不得仅固定 Seed 就断言两局严格相同。
5. 使用两个独立的最小实验：“只空转 Tick”和“提交一张合法卡牌”，记录提交前后的 Tick、`accepted`、回执和状态变化。
6. 用不合法坐标、不可支付圣水、非法目标、错误状态代际/预期 Tick 做拒绝测试；应返回可解释的错误或执行结果，不应该无声跳过。
7. 遇到连接或超时失败，**不要无条件重试写入动作**；优先重新观测并检查对局状态，防止重复执行。
8. 测量 30/180 秒原生 Tick 推进与观测耗时，记平台与窗口渲染模式；不能直接对比 README 的不同环境性能数字。

## 可复现检查表（由接入者填写）

| Case | 操作 | 观察和判定 |
| --- | --- | --- |
| B01 | 空对局初始化到第一可玩 Tick | 初始牌序/玩家阵营/塔数符合预期 |
| B02 | 连续推进 10/100 Tick | `advanced` 与时间顺序一致 |
| B03 | 单方合法出牌 | 回执、卡牌 ID、圣水扣减和实体生成能对应 |
| B04 | 双方动作竞争/同 Tick | 次序稳定；不同 API 的原子性差异已记录 |
| B05 | 非法部署与低圣水 | 拒绝原因明确，没有悄悄执行 |
| B06 | 断线/命令响应丢失 | 不盲重试副作用动作，能从状态确认结果 |
| B07 | 暂停与渲染模式切换 | 模式/速度回执一致，不能混同逻辑 Tick 与 UI FPS |
| B08 | 终局与重置 | 终局不再接受旧动作，旧代际句柄被拒绝 |
| B09 | 快照/重放 | 见 [专门验收表](../snapshot-recovery/integration.md) |
| B10 | 换构建/换资源版本 | 程序明确失配并中止，而非静默使用旧偏移 |

**只有实际执行并保存结果的 Case 才能填“通过”。本文未执行任何一项。**

## 中台验收记录格式（由实际测试者提交，不是 SDK 参数）

```yaml
project_id: jason-battle-engine
capability_id: battle-control
source_commit: null
game_build: null
asset_fingerprint: null
probe_sha256: null
platform: null
test_cases:
  B01: not-run
  B02: not-run
  B03: not-run
result: not-run
log_link: null
reviewer: null
```

[兼容对照](compatibility.md) · [源码证据](../../docs/source-audits/native-engine-2026-10-13.md) · [成熟度规则](../../docs/reuse-maturity.md)
