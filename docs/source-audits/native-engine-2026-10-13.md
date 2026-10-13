# 源码核查：原生战斗控制与快照接口（2026-10-13）
 
**方法**：从四个项目当时的公开 Git 提交中阅读具体 Python / C++ 接口实现与初始化说明；未构建 APK、启动引擎、执行任何原生集成测试。以下 `source-inspected` 仅表示**所列接口的代码路径与约束经过静态检查**，不表示行为已在设备中复现。日期仅表示核查发生时间，未来上游更新后应重新比对。

| 项目 | 固定提交 | 范围 |
| --- | --- | --- |
| [FirstLight CR](../../projects/firstlight-cr.md) | `3ade158c52bf33de3ffcea600ce380946b7de0d8` | `battle_env.py`, `cr_native_env.py`, `contracts.py`, 原生探针与安装文档 |
| [Jason Battle Engine](../../projects/jason-battle-engine.md) | `2b3361954c189a8ea508f3f54cf94a56c2e045fc` | `engine.py`, README |
| [Ashpp 复盘器](../../projects/ashpp-replay.md) | `de46d7ea3831a64565140cdb9d4b947f9fe21916` | `bridge/controller.py`, README |
| [Replay Studio](../../projects/replay-studio.md) | `04d48bdcf2f54cf81dc809e56d9bc08691a167e2` | `app/engine.py`, README |

## 1. FirstLight：至少三层接口

**低层控制层**：[`NativeClashEnv`](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/cr_native_env.py#L2479-L2496)，通过本地控制通道提交命令，默认端口在 [配置常量](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/cr_native_env.py#L33-L43) 中。[`step(ticks)`, `observe`, `observe_atomic`](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/cr_native_env.py#L2739-L2785) 可以按 Tick 推进及取得原生状态。原生渲染控制属于另一模式，[`advance_native_render`](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/cr_native_env.py#L2744-L2758) 有显式回执校验。

**对局/策略层**：[`BattleEnvV1`](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/battle_env.py#L362-L408) 提供双方观测和奖励语义，使用类似 PettingZoo Parallel 的模式但**不依赖 PettingZoo**。[`reset`](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/battle_env.py#L645-L674) 返回观测与信息，[`step`](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/battle_env.py#L2341-L2365) 返回双方观测、奖励、终止/截断和信息。它当前只接受 `FAIR` 观测层，不要误以为策略可读取所有原生隐藏状态。

**类型契约层**：[`ActionV1`](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/contracts.py#L1614-L1633) 包含 `owner`, `kind`, `hand_slot`, `target_grid`, `execute_offset_ticks` 等；[`ObservationV1`](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/contracts.py#L2663-L2685) 包含 `tick`, `owner`, `players`, `entities`, `action_mask`, `terminal` 等。这些都是 **FirstLight 私有的版本化 Python 契约**，不是本中台发布的公共协议。

**原生进程内快照：确有源码实现**。[`create_snapshot`, `restore`, `release_snapshot`](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/cr_native_env.py#L2828-L2860) 存在；注释明确句柄仅在当前 app 进程和无渲染 manager generation 内有效，重新配置对局会失效。[`cr_replay_probe.cpp` 中的命令分支](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/probe/cr_replay_probe.cpp#L6804-L6868) 存在并检查恢复句柄。**不能据此推出进程重启后可恢复、可序列化或支持并行 MCTS 克隆。**

**环境锁定**：[`getting_started.md`](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/docs/getting_started.md#L13-L23) 对 Windows 安装路线写明 Android 12 MuMu、ARM64、Null's Royale APK 15.535.13 和更新资源 15.535.86。这是**该文档的已知安装目标**，不应推广为所有仓库通用标准。

## 2. Jason Battle Engine：紧凑客户端 + 原生探针

[`Engine.connect`](https://github.com/Jason-XII/clash-royale-battle-engine/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/engine.py#L147-L169) 使用本地 TCP `127.0.0.1:26789` 并发送 `session-v1` 握手；[`Engine.reset`](https://github.com/Jason-XII/clash-royale-battle-engine/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/engine.py#L202-L221) 要求 `headless` 模式，构造对局、预推进 90 Tick；[`Engine.step`](https://github.com/Jason-XII/clash-royale-battle-engine/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/engine.py#L222-L239) 以 `minimal-transition` 提交一组 `Play(owner, slot, x, y)`，返回 `Transition(state, advanced, executed)`。

尤其应注意源码备注：同一个 owner 在一次 step 中提交两个动作，`executed` 的匹配无法区分；传输失败后清空内部状态，**不能盲目重发副作用命令**。它并不是 FirstLight 的 `BattleEnvV1.step()` 等价 API。

[`RenderedEngine`](https://github.com/Jason-XII/clash-royale-battle-engine/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/engine.py#L289-L321) 单独提供原生渲染控制路线；[README](https://github.com/Jason-XII/clash-royale-battle-engine/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/README.md#L7-L17) 声明 IL 数据重建在 ARM64 Android 原生探针，PPO 阶段另用 Linux x86_64 的 `clapha-engine`。**同一个仓库的不同阶段使用不同引擎环境**，不应将其性能、兼容性混为一谈。

该仓库公开元数据未确认整体标准开源许可证；引用源代码位置不意味着可以复制实现。

## 3. Ashpp 复盘器：在引擎之上的产品控制层

[`BattleController.reset`](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L126-L155) 将 seed、卡组、形态、等级、塔楼种类等作为对局配置；[`step`](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L188-L202) 具备 `expected_tick` 并校验实际推进量；[`play_card`](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L204-L239) 显式检查落点和手牌槽位。

[`snapshot_create`](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L240-L248) 请求进程内快照；[`snapshot_restore`](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L286-L312) 恢复后**清空原生回放调度队列**，防止不同复盘分支之间遗留未执行动作污染结果。这是需要在公共快照验收方案中单独检查的状态边界。

[`replay`](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L314-L385) 支持从快照续放或者从 seed 完整重放，按 Tick + sequence 排序，对可用动作类型做校验，并提供预期摘要不符时拒绝结果的机制。这里的摘要仅覆盖该应用选定的观测事实，**不是完整 GameState 字节级证明**。[`observation` 摘要构造](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L15-L35) 可供确定字段范围。

## 4. Replay Studio：时间轴/重建应用而非公共引擎 SDK

[`app/engine.py` 的 `reset`](https://github.com/ak1NaN/ClashRoyale-replay-studio/blob/04d48bdcf2f54cf81dc809e56d9bc08691a167e2/app/engine.py#L63-L77) 与 [原生渲染 reset](https://github.com/ak1NaN/ClashRoyale-replay-studio/blob/04d48bdcf2f54cf81dc809e56d9bc08691a167e2/app/engine.py#L79-L120) 使用事件重建的管理流程；[`set_speed`](https://github.com/ak1NaN/ClashRoyale-replay-studio/blob/04d48bdcf2f54cf81dc809e56d9bc08691a167e2/app/engine.py#L123-L126) 支持 0.25、0.5、1、2、4、8、16 倍，**和 FirstLight 原生渲染速度限制不同**。对于精确复现，需另读 README 关于缺失 seed/初手的边界。

## 5. 结论与未验证问题

- **确有不同的已写出接口**，但没有经过验证的跨项目统一 ABI。
- FirstLight 的进程内 snapshot 已被静态确认；此前“只有其他复盘器具备该能力”的列表不完整，已更正能力矩阵。
- “R2 / source-inspected”仅针对本文明确审阅的窄范围接口，不宣称已构建原生探针，也不承诺适配性。
- 尚需测试状态快照是否覆盖待执行队列、随机数、隐含时序，是否允许克隆为多个独立引擎实例，以及在不同游戏构建下的行为。
- 当前源码审查未核验上游所有转引依赖、原始游戏文件权利及维护者长期支持情况。

下一步执行参考 [控制能力验收](../../capabilities/battle-control/integration.md) 与 [快照能力验收](../../capabilities/snapshot-recovery/integration.md)。
