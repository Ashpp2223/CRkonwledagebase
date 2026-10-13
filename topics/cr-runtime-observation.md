---
id: cr-runtime-observation
title: "运行时游戏状态观测"
type: topic
status: investigating
verification: author-documented
projects: [memory-reader, tencent-overlay, tencent-model-harness, katacr]
last_reviewed: null
---

# 运行时游戏状态观测

本页是**跨项目研究专题**；面向开发任务优先查看 [对局状态观测](../capabilities/state-observation/README.md)。

## 相关项目与路线（依据公开文档）

| 项目 | 技术来源 |
| --- | --- |
| [CR Memory Reader](../projects/memory-reader.md) | [作者仓库](https://github.com/Jason-XII/cr-memory-reader) |
| [Tencent Overlay](../projects/tencent-overlay.md) | [作者仓库](https://github.com/ak1NaN/ClashRoyale-tencent-overlay) |
| [Tencent Model Harness](../projects/tencent-model-harness.md) | [作者仓库](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness) |
| [KataCR](../projects/katacr.md) | [作者仓库](https://github.com/wty-yy/KataCR) |

## 研究边界与差异

内存/Frida 读取与画面视觉识别依赖完全不同。腾讯 38.4.2 的旧覆盖层偏移已经按其 README 标为失效。

## 需要补充的证据

- 固定游戏客户端、资源和源代码提交版本。
- 反例、差分对照测试、性能测量的条件。
- 作者审核与具体许可证影响（公开不代表可直接复制）。

[能力总入口](../capabilities/README.md) · [项目索引](../projects/README.md)
