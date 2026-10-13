---
id: snapshot-recovery
title: "状态快照与恢复"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 状态快照与恢复

**需要解决的问题**：能否从任意历史局面继续执行，并保持状态一致？

**能力边界**：快照恢复、逐 tick 缓存、从开局重放是不同能力。

## 采用前必须回答

- 定义状态覆盖范围：实体、随机数、动作队列、手牌、计时器。
- 明确快照是否只在当前进程有效。
- 记录恢复速度、内存开销与是否支持独立分叉。
- 用相同动作序列校验恢复后的状态摘要。

## 已公开的相关实现

| 来源项目 | 复用成熟度 / 证据 | 公开描述 | 限制 | 原始来源 |
| --- | --- | --- | --- | --- |
| [皇室战争复盘器](../../projects/ashpp-replay.md) | R1 · author-documented | 原生进程内快照与动作日志重放 | 快照句柄不跨进程，重启需重放 | [来源](https://github.com/Ashpp2223/clashroyalereplay) |
| [Clash Royale Replay Studio](../../projects/replay-studio.md) | R1 · author-documented | 按 tick 预演算和缓存支持时间跳转 | 不能直接等同于可分叉的任意状态原生快照 | [来源](https://github.com/ak1NaN/ClashRoyale-replay-studio) |

> 上表为**作者文档层级的能力关联**，未独立检查完整源码或运行测试；R0/R1 并不是可下载即用的组件。细节见 [成熟度规则](../../docs/reuse-maturity.md) 和 [机器登记](../../registry/implementations.yaml)。

## 选择与集成判断

- 只需回放拖动时，缓存或动作重放可能足够。
- 要做 MCTS / 并行树搜索，必须单独验证任意节点克隆、实例隔离、恢复开销。

## 尚缺的中台资产

- 可复现的运行环境及固定提交、版本指纹。
- 统一测试场景下的功能验证、性能数据和错误案例。
- 作者审阅、许可证核对与明确的集成入口（若存在）。

[返回能力目录](../README.md) · [查看项目目录](../../projects/README.md)
