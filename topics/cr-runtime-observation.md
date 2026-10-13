---
id: cr-runtime-observation
title: "运行时游戏状态观测"
type: topic
status: investigating
verification: author-documented
projects: [memory-reader, tencent-overlay, tencent-model-harness, katacr, clashai-vegetableleaf, build-a-bot, detection-dataset, claude-royale, card-tracker]
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

## 新增技术来源（2026-10-13）

- [ClashAI](../projects/clashai-vegetableleaf.md)：原生回放重驱、公开观测、模仿学习和强化学习部署流水线。
- [ClashRoyaleBuildABot](../projects/build-a-bot.md)：屏幕视觉检测器、结构化状态和动作策略分层。
- [CR Detection Dataset](../projects/detection-dataset.md)：历史图像切片及合成目标检测样本生成方法。
- [Claude Royale](../projects/claude-royale.md)：截图—LLM决策—输入的多智能体调度与UI生命周期经验。
- [AI Card Tracker](../projects/card-tracker.md)：早期CNN卡牌跟踪、循环和圣水估计。

逆向方法与版本证据另见 [逆向知识中心](../research/reverse-engineering/README.md) 和 [相关研究](../research/reverse-engineering/runtime-memory.md)。
