---
id: cr-replay-state
title: "回放、快照与状态恢复"
type: topic
status: investigating
verification: author-documented
projects: [firstlight-cr, jason-battle-engine, replay-studio, ashpp-replay, clashai-vegetableleaf, fl-royale, royaleapi-downloader-imax9d, cr-collector-arron, royale-viser]
last_reviewed: null
---

# 回放、快照与状态恢复

本页是**跨项目研究专题**；面向开发任务优先查看 [状态快照与恢复](../capabilities/snapshot-recovery/README.md)、[对局重建与分支回放](../capabilities/replay-reconstruction/README.md)。

## 相关项目与路线（依据公开文档）

| 项目 | 技术来源 |
| --- | --- |
| [FirstLight CR](../projects/firstlight-cr.md) | [作者仓库](https://github.com/Jaasssoooonnnnn/FirstLight_CR) |
| [Jason Clash Royale Battle Engine](../projects/jason-battle-engine.md) | [作者仓库](https://github.com/Jason-XII/clash-royale-battle-engine) |
| [Clash Royale Replay Studio](../projects/replay-studio.md) | [作者仓库](https://github.com/ak1NaN/ClashRoyale-replay-studio) |
| [皇室战争复盘器](../projects/ashpp-replay.md) | [作者仓库](https://github.com/Ashpp2223/clashroyalereplay) |

## 研究边界与差异

区分事件重建、实时录制、逐 tick 缓存、进程内快照、动作日志重放；这些方案的状态精度和成本不能直接排序。

## 需要补充的证据

- 固定游戏客户端、资源和源代码提交版本。
- 反例、差分对照测试、性能测量的条件。
- 作者审核与具体许可证影响（公开不代表可直接复制）。

[能力总入口](../capabilities/README.md) · [项目索引](../projects/README.md)

## 新增技术来源（2026-10-13）

- [ClashAI](../projects/clashai-vegetableleaf.md)：原生回放重驱、公开观测、模仿学习和强化学习部署流水线。

## 新增研究来源（2026-10-15）

- [FL Royale](../projects/fl-royale.md)：基于 FirstLight 的 Android 离线可玩客户端，提供原生战斗画面、大厅、卡组、对战 AI 及本地流程。
- [RoyaleAPI Downloader](../projects/royaleapi-downloader-imax9d.md)：对局事件与相关元数据的批量采集：SQLite 持久化队列、跨玩家去重、固定赛季、增量回填和离线校验。
- [Arron CR Collector](../projects/cr-collector-arron.md)：面向 RoyaleAPI 公开对局信息的志愿者采集客户端与协调服务，含分布式采集、进度恢复和透明的运行范围说明。

## 2026-10-15：轨迹浏览与原生快照的区别

[RoyaleViser](../projects/royale-viser.md) 可以单步观看 RoyaleGym 运行时/保存的模拟战斗，属于 [战斗轨迹可视化](../capabilities/battle-visualization/README.md)。其 `.msgpack` 并非原生 `libg` 的可恢复战斗状态，不能直接支持任意 Tick 分叉或原生撤回。
