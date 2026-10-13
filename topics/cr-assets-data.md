---
id: cr-assets-data
title: "资源与数据解析"
type: topic
status: investigating
verification: author-documented
projects: [sc-downloader, sc-extract, supercell-csv-decoder, royaleapi-static-data]
last_reviewed: null
---

# 资源与数据解析

本页是**跨项目研究专题**；面向开发任务优先查看 [资源与配置数据获取](../capabilities/asset-ingestion/README.md)。

## 相关项目与路线（依据公开文档）

| 项目 | 技术来源 |
| --- | --- |
| [SC Downloader GUI](../projects/sc-downloader.md) | [作者仓库](https://github.com/Darknighture/sc-downloader-gui) |

## 研究边界与差异

抓取原始游戏文件与共享可再分发的技术知识不同；资源版本及第三方素材许可必须独立核对。

## 需要补充的证据

- 固定游戏客户端、资源和源代码提交版本。
- 反例、差分对照测试、性能测量的条件。
- 作者审核与具体许可证影响（公开不代表可直接复制）。

[能力总入口](../capabilities/README.md) · [项目索引](../projects/README.md)

## 新增技术来源（2026-10-13）

- [sc_extract](../projects/sc-extract.md)：Rust SC图像、精灵与CSV格式处理CLI和crate。
- [Supercell Resource Decoder](../projects/supercell-csv-decoder.md)：Supercell旧式二进制CSV解码和实验性编码。
- [RoyaleAPI Static Data](../projects/royaleapi-static-data.md)：第三方卡牌JSON及显示元数据历史参考。
