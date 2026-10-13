---
id: cr-assets-data
title: "资源与数据解析"
type: topic
status: investigating
verification: author-documented
projects: [sc-downloader]
last_reviewed: null
---

# 资源与数据解析

**研究范围**：版本指纹、卡牌配置、CSV、地图与 SC 资源处理。

## 相关实现（作者文档整理）

| 项目 | 路线 / 重点 |
| --- | --- |
| [SC Downloader GUI](../projects/sc-downloader.md) | 图形化下载 Supercell 资源，支持 Masterhash/Fingerprint、按类型下载、断点补齐、可选压缩格式解码。 |

## 复用判断

优先复用**公开可验证的机制描述、接口设计方法与测试思路**。实际代码复制需确认许可证、上游版权和版本适用性；不同项目的状态、时钟、坐标、卡牌 ID 不应假定兼容。

## 待核实

- 各项目固定提交、支持版本及运行证据。
- 同等测试条件下的行为差异和性能数据。
- 作者是否愿意共同维护专题。
