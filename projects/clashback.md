---
id: clashback
title: "Clashback"
type: project
status: implemented
verification: author-documented
repository: https://github.com/ak1NaN/Clashback
topics: [cr-native-engine, cr-replay-state]
maintainers: []
last_reviewed: "2026-11-10"
license: unknown
---

# Clashback：16.635.x 新版原生战斗引擎接口与本地回放

**上游**：[ak1NaN/Clashback](https://github.com/ak1NaN/Clashback) · **固定核查**：[`45c1f26b942ae1d706f2004791e73013e4330099`](https://github.com/ak1NaN/Clashback/tree/45c1f26b942ae1d706f2004791e73013e4330099)（2026-11-04 最后提交；2026-11-10 检索）· **性质**：直接运行版本锁定的原始 x86_64 `libg.so`，与重新实现游戏规则的 Java/Rust 模拟器区分。

## 固定构建与运行环境

- 原生库构建 `160635001`，固定 SHA-256：`c4721bd90f46fd1709e9dc498e286462ad88cf817ec645c5749f0aa445fd6539`。校对入口：[`vendor/crx/bindings/160635001.json`](https://github.com/ak1NaN/Clashback/blob/45c1f26b942ae1d706f2004791e73013e4330099/vendor/crx/bindings/160635001.json)。该文件包含约 90 个原生函数绑定及 156 个字段定义，源于从 `160402020` 迁移并带指令签名检查。
- 仓库 README 记载同步数据版本为 `16.635.8`；`160635001` 是原生构建标识，`16.635.8` 是可热更新资源版本，不能混为同一个号。[项目说明](https://github.com/ak1NaN/Clashback/blob/45c1f26b942ae1d706f2004791e73013e4330099/README.md)。
- 作者当前提供 Apple 芯片 Mac、macOS ≥14.4、Rosetta 2 与 x86_64 Python 的离线回放使用路径，游戏原生引擎在 Rosetta 下运行、渲染由 macOS 窗口和 ANGLE 完成。不是已经验证的 Windows 或独立 Linux SDK。
- 同构建热更新仅更换资源；如更换客户端构建，需要匹配 x86_64 APKM、重新适配引擎及观战资产，绑定文件的地址不能跨 build 直接复用。

## 已有原生接口（源码静态定位）

[`vendor/crx/env.py`](https://github.com/ak1NaN/Clashback/blob/45c1f26b942ae1d706f2004791e73013e4330099/vendor/crx/env.py) 包含 `CrxEnv`：

| 方法 | 可核查行为 |
| --- | --- |
| `create_match(config)` | 按配置启动原生战斗，返回初始观察；同一进程的再次建局走 `_restart`，源码注释及作者报告提醒不同系统的重启稳定性限制 |
| `step(ticks)` | 通过原生 `gate3.step` 推进战斗 Tick |
| `observe()` | 读取玩家、手牌/循环、实体与结束结果 |
| `queue_hand_action_at` / `queue_card_at` | 根据执行 Tick 调度手牌或卡牌 ID、落点 |
| `queue_ability_action_at` | 校验技能对象存活/就绪后写入原生命令队列 |
| `run_lean` | 按采样间隔读取较小的战场帧 |

[`neo_replay/native_snapshots.py`](https://github.com/ak1NaN/Clashback/blob/45c1f26b942ae1d706f2004791e73013e4330099/neo_replay/native_snapshots.py) 实现 `NativeSnapshotStream.save/load`，通过战斗快照 encode/load、原版回放 restore 和状态缓存支撑逐 Tick 快进/回退；仅显式支持 `160402020` 和 `160635001`。快照还原要求同一有效战斗和拥有线程；磁盘缓存与当前引擎 SHA、对局文件摘要绑定，**尚无跨独立进程任意分叉的验证**。

## 面向回放的实现

`neo_replay/native_worker.py` 根据 RoyaleAPI HTML 重建双方卡牌、落点及技能事件，通过 `CrxEnv` 模拟全场，导出命令与终局日志。由于 HTML 缺失随机种子、起手牌等隐含信息，采用候选种子/共同时间基准推断。作者明确将终局塔血和出牌对齐与逐帧状态一致区分；`diagnostic_match` 级别的原版 Tick 对照需另外收集真实轨迹。

## 觉醒巨人的当前证据边界

游戏数据版本 `16.635.8` 包含 `Giant_EV1` 相关内容，项目支持该版本的原生建局与资源，但**当前公开档案没有单独证明觉醒巨人出牌、半血狂暴和区域变化完整通过原生测试**。必须准备匹配的形态/卡组输入，分别确认部署、状态、狂暴作用与快照恢复；不能用“数据已更新”替代专项验证。

## 复用与风险

- 可研究新版原生引擎的创建、推进、命令提交、状态观测和快照；目前这些是回放程序内部 Python 接口，未声明稳定的第三方 SDK 或跨平台兼容性。
- **证据范围**：本次仅读取固定提交 README、绑定配置、`CrxEnv` 及原生快照源码；未在 Mac 下载实际游戏二进制、执行验证或复核作者测试数据。对外部运行成功的表述沿用作者报告。
- **授权**：未在仓库根目录及 `vendor/crx` 发现明确 LICENSE；暂记 `unknown`，不推定允许复制、再分发原生游戏文件或兼容库。上游不等于游戏发行方授权。

[原生战斗能力](../capabilities/battle-control/README.md) · [快照能力](../capabilities/snapshot-recovery/README.md) · [回放重建](../capabilities/replay-reconstruction/README.md) · [11 月新版证据对照](../research/knowledge-notes/cr-16635-evo-giant-parity-2026-11-10.md)
