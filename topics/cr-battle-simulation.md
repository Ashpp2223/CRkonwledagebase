---
id: cr-battle-simulation
title: "独立战斗模拟器"
type: topic
status: investigating
verification: author-documented
projects: [jason-simulator,hasty-cr,royalegym,crforge]
last_reviewed: null
---

# 独立战斗模拟器

**研究范围**：自主重写战斗规则的引擎及其确定性与性能验证。

## 相关实现（作者文档整理）

| 项目 | 路线 / 重点 |
| --- | --- |
| [Jason Clash Royale Simulator](../projects/jason-simulator.md) | 从零实现战斗逻辑，包含 A* 寻路、卡牌交互、局域网对战与 RL 环境 |
| [Hasty-CR](../projects/hasty-cr.md) | 自建整数确定性战斗引擎、机制测试、差分测量和 PPO 训练 |
| [RoyaleGym / RoyaleSim](../projects/royalegym.md) | RoyaleGym 提供 Gymnasium/PettingZoo 风格接口，RoyaleSim 提供 Rust 整数战斗引擎和 Python 调用。 |
| [crforge](../projects/crforge.md) | Java 确定性 Tick 模拟器，使用 ECS 风格实体与系统、JSON 驱动卡牌、LibGDX 调试界面和 ZMQ/Gymnasium 桥接。 |

## 复用判断

优先复用**公开可验证的机制描述、接口设计方法与测试思路**。实际代码复制需确认许可证、上游版权和版本适用性；不同项目的状态、时钟、坐标、卡牌 ID 不应假定兼容。

## 待核实

- 各项目固定提交、支持版本及运行证据。
- 同等测试条件下的行为差异和性能数据。
- 作者是否愿意共同维护专题。
