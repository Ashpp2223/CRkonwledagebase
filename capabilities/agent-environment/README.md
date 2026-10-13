---
id: agent-environment
title: "智能体环境与模型对接"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 智能体环境与模型对接

**需要解决的问题**：如何将战斗与 AI 模型连接，用于训练、评测或本地推理？

**能力边界**：训练环境、策略服务和真实客户端部署三者并不自动兼容。

## 采用前必须回答

- 定义 observation / action / reward / terminated 的语义。
- 统一合法动作掩码及卡牌位置坐标说明。
- 避免将训练时可见的隐藏信息泄漏给对战策略。
- 记录实验版本、种子、对手池和回归基准。

## 已公开的相关实现

| 来源项目 | 复用成熟度 / 证据 | 公开描述 | 限制 | 原始来源 |
| --- | --- | --- | --- | --- |
| [FirstLight CR](../../projects/firstlight-cr.md) | R1 · author-documented | 原生环境、模仿学习、PPO、自博弈、策略服务 | 模型与环境使用特定 Observation/Action 契约 | [来源](https://github.com/Jaasssoooonnnnn/FirstLight_CR) |
| [Jason Clash Royale Battle Engine](../../projects/jason-battle-engine.md) | R1 · author-documented | 离线对局与模仿/PPO 训练流水线 | 依赖原生游戏数据及外部模拟环境 | [来源](https://github.com/Jason-XII/clash-royale-battle-engine) |
| [Jason Clash Royale Simulator](../../projects/jason-simulator.md) | R1 · author-documented | 独立模拟器和强化学习环境 | 卡牌覆盖不完整 | [来源](https://github.com/Jason-XII/clash-royale-simulator) |
| [Hasty-CR](../../projects/hasty-cr.md) | R1 · author-documented | 可确定性运行的模拟器及策略训练 | 独立模拟准确性必须按机制验证 | [来源](https://github.com/hastylmao/Hasty-CR) |
| [RoyaleGym](../../projects/royalegym.md) | R1 · author-documented | Gymnasium/PettingZoo 风格环境与评测 | 需与 RoyaleSim 版本配套 | [来源](https://github.com/RoyaleGym/RoyaleGym) |
| [RoyaleSim](../../projects/royalesim.md) | R1 · author-documented | Rust 底层战斗引擎与 Python API | 只是引擎，不等于完整训练工具链 | [来源](https://github.com/RoyaleGym/RoyaleSim) |
| [crforge](../../projects/crforge.md) | R1 · author-documented | Java 模拟器经 ZMQ/Gymnasium 接口训练 | 需要 Java 运行时和桥接进程 | [来源](https://github.com/voonhous/crforge) |
| [KataCR](../../projects/katacr.md) | R1 · author-documented | 视觉观测下的策略训练和执行 | 验证环境为历史版本，运行前需重新评估 | [来源](https://github.com/wty-yy/KataCR) |
| [Tencent Model Harness](../../projects/tencent-model-harness.md) | R1 · author-documented | FirstLight V4 模型在腾讯客户端的推理部署 | 这是推理适配而不是新的训练环境 | [来源](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness) |

> 上表为**作者文档层级的能力关联**，未独立检查完整源码或运行测试；R0/R1 并不是可下载即用的组件。细节见 [成熟度规则](../../docs/reuse-maturity.md) 和 [机器登记](../../registry/implementations.yaml)。

## 选择与集成判断

- 原生环境优先保真；独立模拟器利于加速和修改；视觉/设备部署则必须处理延迟与误差。
- 策略模型输入格式不同，需要专用适配器；不存在现成的社区统一模型 ABI。

## 尚缺的中台资产

- 可复现的运行环境及固定提交、版本指纹。
- 统一测试场景下的功能验证、性能数据和错误案例。
- 作者审阅、许可证核对与明确的集成入口（若存在）。

[返回能力目录](../README.md) · [查看项目目录](../../projects/README.md)

## 扩展来源（2026-10-13）：已登记的高衍生实现

下面是本轮 GitHub 调查新增的候选。**能力评级以 [实现矩阵](../../registry/implementations.yaml) 为准；R2 仅对指定源码范围有效，均未完成第三方集成验收。**

| 项目 | 新的可复用切入点 |
| --- | --- |
| [ClashRoyaleEnv](../../projects/itzik-clashenv.md) | Python/Gymnasium PPO 环境；R1 |
| [ClashAI](../../projects/clashai-vegetableleaf.md) | 回放 IL→RL 与公平观测；R1 |
| [CRSim Agent](../../projects/crsim-agent-larkindaniel.md) | PPO checkpoint 重现与信息边界审计；R1 |

[技术组合地图](../../landscape/composition-patterns.md) · [高价值项目调查](../../landscape/2026-10-13-landscape.md)
