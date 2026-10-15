---
id: cr-collector-arron
title: "Arron CR Collector"
type: project
status: implemented
verification: author-documented
repository: https://github.com/arronwang01/cr-collector
topics: [cr-replay-state]
maintainers: []
last_reviewed: 2026-10-15
license: unknown
---

# Arron CR Collector

**上游**：[arronwang01/cr-collector](https://github.com/arronwang01/cr-collector) · [查阅提交 e70ceafcfd64](https://github.com/arronwang01/cr-collector/tree/e70ceafcfd64d78d332dae16ccfc05071da3a803)

## 有证据的技术资产

面向 RoyaleAPI 公开对局信息的志愿者采集客户端与协调服务，含分布式采集、进度恢复和透明的运行范围说明。

**衍生价值**：可研究轻量级采集协调、公开数据来源和重试/去重；并不直接提供原生对局引擎。

## 适用边界

需网站会话/采集参与者，站点政策可能限制自动化；未知整体许可证；不能保证采集到足够还原 RNG/牌序的事件。

**验证状态**：根据固定提交中的仓库文档及公开代码入口编目；中台没有运行其游戏环境、二进制或完整回归测试。

[2026-10-15 来源网络调查](../landscape/2026-10-15-source-network.md) · [项目目录](README.md)
