---
id: cr-native-engine
title: "原生战斗引擎"
type: topic
status: investigating
verification: author-documented
projects: [firstlight-cr, jason-battle-engine, replay-studio, ashpp-replay]
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
