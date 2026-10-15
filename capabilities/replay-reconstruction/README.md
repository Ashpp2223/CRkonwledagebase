---
id: replay-reconstruction
title: "对局重建与分支回放"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 对局重建与分支回放

**需要解决的问题**：如何把外部对局事件重建成可观看或可交互的战斗？

**能力边界**：事件相容重建与精确原局复现必须明确区分。

## 采用前必须回答

- 识别事件时间、卡牌 ID、等级、形态、落点和阵营。
- 声明原始种子与隐藏初手是否可获取。
- 支持无效事件/不支持卡牌的诊断。
- 展示回放、分叉和状态核对的验收方法。

## 已公开的相关实现

| 来源项目 | 复用成熟度 / 证据 | 公开描述 | 限制 | 原始来源 |
| --- | --- | --- | --- | --- |
| [Clash Royale Replay Studio](../../projects/replay-studio.md) | R1 · author-documented | RoyaleAPI HTML 事件导入与原生画面重建 | 缺少种子/秘密初手；不保证完全一致 | [来源](https://github.com/ak1NaN/ClashRoyale-replay-studio) |
| [FirstLight CR](../../projects/firstlight-cr.md) | R1 · author-documented | Parquet 对局回放的原生重建和模仿学习数据生成 | 对局复现成功比例为作者报告，不代表所有回放准确 | [来源](https://github.com/Jaasssoooonnnnn/FirstLight_CR) |
| [皇室战争复盘器](../../projects/ashpp-replay.md) | R1 · author-documented | 动作历史、分支节点、从日志恢复局面 | 是交互式复盘/假设分支，不等同于导入真人对局 | [来源](https://github.com/Ashpp2223/clashroyalereplay) |
| [Jason Clash Royale Battle Engine](../../projects/jason-battle-engine.md) | R1 · author-documented | 重建回放与原生状态缓存研究 | 依赖 FirstLight 与具体游戏版本 | [来源](https://github.com/Jason-XII/clash-royale-battle-engine) |

> 上表为**作者文档层级的能力关联**，未独立检查完整源码或运行测试；R0/R1 并不是可下载即用的组件。细节见 [成熟度规则](../../docs/reuse-maturity.md) 和 [机器登记](../../registry/implementations.yaml)。

## 选择与集成判断

- RoyaleAPI HTML 只包含部分对局信息，不应保证还原所有隐藏状态。
- 复盘器的自由分叉属于新实验路径，与原回放记录应分别标记。

## 尚缺的中台资产

- 可复现的运行环境及固定提交、版本指纹。
- 统一测试场景下的功能验证、性能数据和错误案例。
- 作者审阅、许可证核对与明确的集成入口（若存在）。

[返回能力目录](../README.md) · [查看项目目录](../../projects/README.md)

## 扩展来源（2026-10-13）：已登记的高衍生实现

下面是本轮 GitHub 调查新增的候选。**能力评级以 [实现矩阵](../../registry/implementations.yaml) 为准；R2 仅对指定源码范围有效，均未完成第三方集成验收。**

| 项目 | 新的可复用切入点 |
| --- | --- |
| [ClashAI](../../projects/clashai-vegetableleaf.md) | 真人回放在原生环境重驱，用于训练数据加工；R1 |

[技术组合地图](../../landscape/composition-patterns.md) · [高价值项目调查](../../landscape/2026-10-13-landscape.md)

## 2026-10-15 发现：数据来源与原生重驱应分层

- [RoyaleAPI Downloader](../../projects/royaleapi-downloader.md) 做上游对局抓取、去重与标准化，**不是**原生战斗执行器。
- [CR Native Sandbox](../../projects/cr-native-sandbox.md) 执行固定构建原生回放重驱；即使所有已知动作被接受，也不证明隐藏初手和种子恢复准确。
- [ClashAI 的实验记录](../../projects/clashai-vegetableleaf.md) 提供作者对原生重驱可复现性和拒绝动作的测量路径；由作者测量，不等于中台重测。

[开发者网络调查](../../landscape/2026-10-15-developer-network.md)
