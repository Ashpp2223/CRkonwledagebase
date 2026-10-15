---
id: cr-native-engine
title: "原生战斗引擎"
type: topic
status: investigating
verification: author-documented
projects: [firstlight-cr, jason-battle-engine, replay-studio, ashpp-replay, native-sandbox-imax9d, native-bionic-imax9d, fl-royale, clapha-engine]
last_reviewed: null
---

# 原生战斗引擎

本页是**跨项目研究专题**；面向开发任务优先查看 [原生战斗驱动](../capabilities/battle-control/README.md)、[状态快照与恢复](../capabilities/snapshot-recovery/README.md)、[对局重建与分支回放](../capabilities/replay-reconstruction/README.md)。

## 相关项目与路线（依据公开文档）

| 项目 | 技术来源 |
| --- | --- |
| [FirstLight CR](../projects/firstlight-cr.md) | [作者仓库](https://github.com/Jaasssoooonnnnn/FirstLight_CR) |
| [Jason Clash Royale Battle Engine](../projects/jason-battle-engine.md) | [作者仓库](https://github.com/Jason-XII/clash-royale-battle-engine) |
| [Clash Royale Replay Studio](../projects/replay-studio.md) | [作者仓库](https://github.com/ak1NaN/ClashRoyale-replay-studio) |
| [皇室战争复盘器](../projects/ashpp-replay.md) | [作者仓库](https://github.com/Ashpp2223/clashroyalereplay) |

## 研究边界与差异

原生引擎封装与完整训练环境在耦合层级上不同。不能从“原生引擎可启动”推断公开了可跨进程持久化的状态克隆。

## 需要补充的证据

- 固定游戏客户端、资源和源代码提交版本。
- 反例、差分对照测试、性能测量的条件。
- 作者审核与具体许可证影响（公开不代表可直接复制）。

[能力总入口](../capabilities/README.md) · [项目索引](../projects/README.md)

逆向方法与版本证据另见 [逆向知识中心](../research/reverse-engineering/README.md) 和 [相关研究](../research/reverse-engineering/native-layouts.md)。

## 新增研究来源（2026-10-15）

- [CR Native Sandbox](../projects/native-sandbox-imax9d.md)：原版 Android x86_64 `libg.so` 离线无画面战斗宿主；通过 JniHost/AssetManager/JNI 初始化，提供 reset、step、双方动作、原生观测与 JSON-line Worker。
- [CR Native Linux Bionic](../projects/native-bionic-imax9d.md)：在 Linux x86_64 宿主中部署 Android API 31 Bionic linker/ART 和 Binderless JniHost，直接驱动版本固定的原版游戏 Worker，不启动 AVD/KVM。
- [FL Royale](../projects/fl-royale.md)：基于 FirstLight 的 Android 离线可玩客户端，提供原生战斗画面、大厅、卡组、对战 AI 及本地流程。

- [Clapha Engine（仅公开适配器）](../projects/clapha-engine.md)：Jason 的 `clapha.py` 提供 Linux x86_64 原生环境调用，底层 loader 私有、无法独立核查。
