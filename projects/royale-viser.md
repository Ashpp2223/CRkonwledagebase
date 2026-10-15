---
id: royale-viser
title: "RoyaleViser"
type: project
status: implemented
verification: author-documented
repository: https://github.com/RoyaleGym/RoyaleViser
topics: [cr-replay-state]
maintainers: []
last_reviewed: "2026-10-15"
license: MIT
---

# RoyaleViser

**GitHub**：[RoyaleGym/RoyaleViser](https://github.com/RoyaleGym/RoyaleViser) · **固定源码提交**：`8aada19cdf95f3e18b6bf7f3a33c521fc6b01a26`

## 具体能力
[固定 README](https://github.com/RoyaleGym/RoyaleViser/blob/8aada19cdf95f3e18b6bf7f3a33c521fc6b01a26/README.md) 描述观看 RoyaleGym **实时模拟战斗**或保存的 `.msgpack` 轨迹；支持暂停、逐步浏览和实体检查。

这属于**模拟轨迹可视化**，不是直接加载 Supercell 原生 libg 状态、生成官方录像或恢复某时刻的可运行原生快照。

## 可移植知识
抽取 trace 帧/实体展示、调试交互及轨迹消费接口的方法；没有核对其消息 schema 与用户本地复盘器的动作日志之间的兼容性。R1 / author-documented / unverified。

[战斗轨迹可视化](../capabilities/battle-visualization/README.md)
