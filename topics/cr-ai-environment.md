---
id: cr-ai-environment
title: "AI 训练环境与决策"
type: topic
status: investigating
verification: author-documented
projects: [firstlight-cr,jason-battle-engine,jason-simulator,tencent-tools,hasty-cr,royalegym,crforge,katacr]
last_reviewed: null
---

# AI 训练环境与决策

**研究范围**：观测空间、动作空间、模型服务、模仿学习、PPO 和评估。

## 相关实现（作者文档整理）

| 项目 | 路线 / 重点 |
| --- | --- |
| [FirstLight CR](../projects/firstlight-cr.md) | 原生战斗环境、结构化状态与动作、Parquet 回放重建、模仿学习与 PPO 自博弈 |
| [Jason Clash Royale Battle Engine](../projects/jason-battle-engine.md) | 以 Python API 封装原生战斗引擎、对局数据与训练流水线 |
| [Jason Clash Royale Simulator](../projects/jason-simulator.md) | 从零实现战斗逻辑，包含 A* 寻路、卡牌交互、局域网对战与 RL 环境 |
| [Tencent Overlay 与 Model Harness](../projects/tencent-tools.md) | Tencent Model Harness 将腾讯客户端读取状态转换为 FirstLight V4 输入，输出动作与回执 |
| [Hasty-CR](../projects/hasty-cr.md) | 自建整数确定性战斗引擎、机制测试、差分测量和 PPO 训练 |
| [RoyaleGym / RoyaleSim](../projects/royalegym.md) | RoyaleGym 提供 Gymnasium/PettingZoo 风格接口，RoyaleSim 提供 Rust 整数战斗引擎和 Python 调用。 |
| [crforge](../projects/crforge.md) | Java 确定性 Tick 模拟器，使用 ECS 风格实体与系统、JSON 驱动卡牌、LibGDX 调试界面和 ZMQ/Gymnasium 桥接。 |
| [KataCR](../projects/katacr.md) | 非嵌入式视觉 AI，使用图像识别、分类和离线强化学习策略。 |

## 复用判断

优先复用**公开可验证的机制描述、接口设计方法与测试思路**。实际代码复制需确认许可证、上游版权和版本适用性；不同项目的状态、时钟、坐标、卡牌 ID 不应假定兼容。

## 待核实

- 各项目固定提交、支持版本及运行证据。
- 同等测试条件下的行为差异和性能数据。
- 作者是否愿意共同维护专题。
