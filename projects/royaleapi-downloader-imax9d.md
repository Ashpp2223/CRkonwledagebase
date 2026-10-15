---
id: royaleapi-downloader-imax9d
title: "RoyaleAPI Downloader"
type: project
status: implemented
verification: author-documented
repository: https://github.com/IMAX9D/royaleapi-downloader
topics: [cr-replay-state]
maintainers: []
last_reviewed: 2026-10-15
license: unknown
---

# RoyaleAPI Downloader

**上游**：[IMAX9D/royaleapi-downloader](https://github.com/IMAX9D/royaleapi-downloader) · [查阅提交 ed80af8eedec](https://github.com/IMAX9D/royaleapi-downloader/tree/ed80af8eedecbd48e7a49babfee309f41b595e9d)

## 有证据的技术资产

对局事件与相关元数据的批量采集：SQLite 持久化队列、跨玩家去重、固定赛季、增量回填和离线校验。

**衍生价值**：可作为真人回放→原生重建→训练/保真验证链路的数据入口；源文件约定与批次来源可追踪。

## 适用边界

来源网站回放时效、授权和反自动化策略会影响可靠性；客户端构建、首发手牌及随机种子并不必然齐全；未知整体许可证。

**验证状态**：根据固定提交中的仓库文档及公开代码入口编目；中台没有运行其游戏环境、二进制或完整回归测试。

[2026-10-15 来源网络调查](../landscape/2026-10-15-source-network.md) · [项目目录](README.md)
