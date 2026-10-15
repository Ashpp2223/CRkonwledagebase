---
id: royaleapi-downloader
title: "RoyaleAPI Downloader"
type: project
status: implemented
verification: author-documented
repository: https://github.com/IMAX9D/royaleapi-downloader
topics: [cr-replay-state, cr-ai-environment]
maintainers: []
last_reviewed: "2026-10-15"
license: unknown
---

# RoyaleAPI Downloader

**上游：**[https://github.com/IMAX9D/royaleapi-downloader](https://github.com/IMAX9D/royaleapi-downloader)；**证据：**[固定版本](https://github.com/IMAX9D/royaleapi-downloader/tree/ed80af8eedecbd48e7a49babfee309f41b595e9d)。

## 已知技术成果

RoyaleAPI 对局列表与事件批量采集：SQLite 持久队列、去重、断点续传、赛季采样、页面/回放解析及离线校验；输出结构化数据。

## 适用边界

作者未提供完整许可证；网站访问条件、历史事件缺失与数据使用条款需逐项确认。采集回放不意味着可以完全复原隐藏初手/随机种子。

## 对中台的可复用价值

- 从 [项目—能力矩阵](../registry/implementations.yaml) 找到这项技术可支撑的具体任务，不由项目整体评分代替单项证据。
- 优先复用**接口语义、版本指纹、验证与实验方法**；需要运行时再核对依赖、资源和授权。
- 目前仅为公开源码/文档证据；中台没有进行第三方集成测试。

[技术网络与开发者追踪](../landscape/2026-10-15-developer-network.md)
