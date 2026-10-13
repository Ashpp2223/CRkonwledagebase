---
id: cr-runtime-observation
title: "运行时游戏状态观测"
type: topic
status: investigating
verification: author-documented
projects: [memory-reader,tencent-tools,katacr]
last_reviewed: null
---

# 运行时游戏状态观测

**研究范围**：客户端内部数据和图像识别两条信息输入路线。

## 相关实现（作者文档整理）

| 项目 | 路线 / 重点 |
| --- | --- |
| [CR Memory Reader](../projects/memory-reader.md) | 通过原生内存/探针研究读取圣水、手牌、皇家塔血量及场上实体 |
| [Tencent Overlay 与 Model Harness](../projects/tencent-tools.md) | Tencent Model Harness 将腾讯客户端读取状态转换为 FirstLight V4 输入，输出动作与回执 |
| [KataCR](../projects/katacr.md) | 非嵌入式视觉 AI，使用图像识别、分类和离线强化学习策略。 |

## 复用判断

优先复用**公开可验证的机制描述、接口设计方法与测试思路**。实际代码复制需确认许可证、上游版权和版本适用性；不同项目的状态、时钟、坐标、卡牌 ID 不应假定兼容。

## 待核实

- 各项目固定提交、支持版本及运行证据。
- 同等测试条件下的行为差异和性能数据。
- 作者是否愿意共同维护专题。
