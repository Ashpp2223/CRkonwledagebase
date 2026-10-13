---
id: asset-ingestion
title: "资源与配置数据获取"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 资源与配置数据获取

**需要解决的问题**：如何定位、下载并解析指定版本的卡牌与地图相关资源？

**能力边界**：资源下载、解压、版本归档与数据规范化是独立环节。

## 采用前必须回答

- 保留资源清单与原始版本标识（例如 fingerprint/masterhash）。
- 明确压缩格式、失败重试和校验策略。
- 区分逻辑 CSV、贴图、动画与可用的元数据。
- 不分发没有授权的游戏素材和原始客户端。

## 已公开的相关实现

| 来源项目 | 复用成熟度 / 证据 | 公开描述 | 限制 | 原始来源 |
| --- | --- | --- | --- | --- |
| [SC Downloader GUI](../../projects/sc-downloader.md) | R1 · author-documented | 多线程资源下载、解压与版本文件缓存 | 皇室战争 Latest Patch 握手暂不可用 | [来源](https://github.com/Darknighture/sc-downloader-gui) |

> 上表为**作者文档层级的能力关联**，未独立检查完整源码或运行测试；R0/R1 并不是可下载即用的组件。细节见 [成熟度规则](../../docs/reuse-maturity.md) 和 [机器登记](../../registry/implementations.yaml)。

## 选择与集成判断

- 先复用资源发现和解析流程，再自行生成可共享的元数据与文档。
- 游戏更新可能影响地址、格式和登录握手，须将失效情况写清。

## 尚缺的中台资产

- 可复现的运行环境及固定提交、版本指纹。
- 统一测试场景下的功能验证、性能数据和错误案例。
- 作者审阅、许可证核对与明确的集成入口（若存在）。

[返回能力目录](../README.md) · [查看项目目录](../../projects/README.md)

## 扩展来源（2026-10-13）：已登记的高衍生实现

下面是本轮 GitHub 调查新增的候选。**能力评级以 [实现矩阵](../../registry/implementations.yaml) 为准；R2 仅对指定源码范围有效，均未完成第三方集成验收。**

| 项目 | 新的可复用切入点 |
| --- | --- |
| [sc_extract](../../projects/sc-extract.md) | Rust Sprite/SC/CSV CLI 和 crate；R1 |
| [Supercell CSV Decoder](../../projects/supercell-csv-decoder.md) | Python 旧格式解码与实验性编码；R1 |
| [RoyaleAPI Static Data](../../projects/royaleapi-static-data.md) | 第三方静态 JSON/常量；R1 |

[技术组合地图](../../landscape/composition-patterns.md) · [高价值项目调查](../../landscape/2026-10-13-landscape.md)
