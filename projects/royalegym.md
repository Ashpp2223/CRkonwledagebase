---
id: royalegym
title: "RoyaleGym"
type: project
status: implemented
verification: author-documented
repository: https://github.com/RoyaleGym/RoyaleGym
topics: [cr-battle-simulation, cr-ai-environment]
maintainers: []
last_reviewed: "2026-11-10"
license: MIT
---

# RoyaleGym

**原始仓库**：[RoyaleGym/RoyaleGym](https://github.com/RoyaleGym/RoyaleGym)。目前仅按作者文档编目，并未得到独立运行验证或作者加入确认。

## 公开实现的内容

Python 侧智能体接口，README 提供与底层 RoyaleSim 共同使用的对局与训练示例，面向 Gymnasium / PettingZoo 类工作流。

## 版本、运行与复用限制

必须核对 RoyaleSim 版本、依赖、卡牌覆盖和仿真规则精度。

## 相关能力

- [智能体环境与模型对接](../capabilities/agent-environment/README.md)：Gymnasium/PettingZoo 风格环境与评测（R1，author-documented）

## 相关研究专题

- [独立战斗模拟器](../topics/cr-battle-simulation.md)
- [AI 训练环境与决策](../topics/cr-ai-environment.md)

## 来源

- [上游 README](https://github.com/RoyaleGym/RoyaleGym)

**待核实**：精确上游提交、运行环境、独立复现测试以及上游作者审阅。

## 2026-10-15 补全模块化生态（独立 Project）

- [RoyaleSim](royalesim.md)：规则模拟器与客户端规则校准。
- [RoyaleLearn](royale-learn.md)：训练/模型存档。
- [RoyaleImitate](royale-imitate.md)：模仿/教师权重工件。
- [RoyaleViser](royale-viser.md)：保存轨迹及实时对局可视化。
- [RoyaleBot](royale-bot.md)：限定 Null's Android 客户端的模型部署。

这些模块分别建项目 ID，不将完整生态笼统归为 RoyaleGym 单一仓库的内建功能。

## 2026-10-31 文档入口核查

[固定 FAQ](https://github.com/RoyaleGym/RoyaleGym/blob/ef0eb176f735e438fb4fcc13a3f190e8ffdebb91/docs/site/pages/faq.md) 为训练、环境配置和模型部署提供了上游说明。FAQ 将纯本地模拟训练与连接 Null's Royale 的独立 RoyaleBot 流程分开；后者不意味着 RoyaleGym 会直接控制官方游戏客户端。复用前应分清模拟器、训练器、可视化和设备部署各自负责的接口和版本。

本次只核查文档入口及说明范围，不增加单项实现的复用等级。

## 2026-11-10 复查：Null's 16.635 训练配置

[2026-11-06 固定提交](https://github.com/RoyaleGym/RoyaleGym/commit/75075e5d1211b34cad6092a483e4f49111b74196) 更新了 [Null's Royale 训练说明](https://github.com/RoyaleGym/RoyaleGym/blob/75075e5d1211b34cad6092a483e4f49111b74196/docs/site/pages/clash-royale/nulls-royale.md)：新版推荐以 `calibration_overrides` 选择 `cards.CARD_TABLE=client160635007_20261103`（客户端内容 `16.635.8`）；同时标明此配置**尚未与该服实际录制战斗校准**。既有 `15.535` 评分只属于旧环境。设备部署须另用 [RoyaleBot](royale-bot.md) 的 `rb-build 0.1.2`，支持 Null's 16.635.1/15.535.13。这里只登记文档级来源，不提高实现成熟度。

## 2026-11-13 官方站点与快速上手入口补充

- [官方文档首页](https://royalegym.github.io/RoyaleGym/)：统一的安装、Quick Start、FAQ 和架构入口。
- [安装指南](https://royalegym.github.io/RoyaleGym/install/)；[Quick Start](https://royalegym.github.io/RoyaleGym/quickstart/)；[架构说明](https://royalegym.github.io/RoyaleGym/repos/royalegym/architecture/)；[Cloning a Bot](https://royalegym.github.io/RoyaleGym/clash-royale/cloning-a-bot/)。
- 上游 README 当前给出 `pip install "royalegym[all]"`、`make_env()` / `play_battle()` 及 `royaleviser` 查看 `.msgpack` 对局的示例；声明 Gymnasium + PettingZoo API、Rust 确定性模拟器、50ms Tick（20 Tick/s）与 2305 个动作。以上均为上游文档声明，未在本知识库独立运行验证。
- 区分 `RoyaleGym`（环境与入口）、`RoyaleSim`（自建规则模拟）、`RoyaleLearn`（训练）、`RoyaleImitate`（模仿）、`RoyaleViser`（可视化）、`RoyaleBot`（设备部署）；不得将独立模拟结果视为官方原生战斗引擎逐 Tick 一致性证明。

**核对依据**：[上游 README](https://github.com/RoyaleGym/RoyaleGym/blob/main/README.md)；本次仅补充官方入口与文档级接口事实，维持 R1 / author-documented，不增加项目 ID 或实现关联。
