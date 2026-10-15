---
id: battle-visualization
title: "战斗轨迹可视化与逐帧检查"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: "2026-10-15"
---

# 战斗轨迹可视化与逐帧检查

**需求**：对已有模拟器状态帧与已保存的战斗轨迹进行播放/暂停、单步、实体数据检查，不负责重新推演原生规则。

与 [对局重建与分支回放](../replay-reconstruction/README.md) 的**状态重建、分支运行**语义不同：轨迹浏览 ≠ 在指定 Tick 恢复可运行引擎。

## 已登记来源

| 项目 | 输入/输出 | 证据 |
| --- | --- | --- |
| [RoyaleViser](../../projects/royale-viser.md) | RoyaleGym 运行时或保存的 `.msgpack` 战斗轨迹 → 可交互查看器 | R1 · author-documented，未集成。 [固定 README](https://github.com/RoyaleGym/RoyaleViser/blob/8aada19cdf95f3e18b6bf7f3a33c521fc6b01a26/README.md) |

## 接入前的准入验证

1. 分清状态帧、增量事件、动作日志；固定对象 ID、坐标、Tick/采样间隔与 JSON/msgpack schema。
2. 验证暂停/单步/seek/末帧、实体死亡/生成/演化等边界，并保留同一场原始轨迹反例。
3. 对接 [Ashpp 的原生复盘器](../../projects/ashpp-replay.md) 前先做 schema 变换与可复现时间轴对齐，**不要把 `.msgpack` 文件误当 libg 快照**。

[返回能力目录](../README.md)
