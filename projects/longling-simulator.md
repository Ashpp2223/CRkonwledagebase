---
id: longling-simulator
title: "Longling CR Simulator × R2-Dreamer"
type: project
status: implemented
verification: author-documented
repository: https://github.com/longlingking/clash-royale-simulator
topics: [cr-battle-simulation, cr-ai-environment]
maintainers: []
last_reviewed: "2026-10-15"
license: unknown
---

# Longling CR Simulator × R2-Dreamer

**GitHub**：[longlingking/clash-royale-simulator](https://github.com/longlingking/clash-royale-simulator) · **固定源码提交**：`6086b9cac917cbdd479405091f90bca85b9bd66b`

## 定位与新增部分
此项目 Fork 自 [Jason-XII/clash-royale-simulator](https://github.com/Jason-XII/clash-royale-simulator)。GitHub Compare 2026-10-15 显示相对上游 `ahead 16 / behind 168`。增量主要为 **R2-Dreamer 模型式强化学习接入与自博弈**，不是独立开发的新战斗引擎。R2-Dreamer 本身源自 [NM512/r2dreamer](https://github.com/NM512/r2dreamer)。

## 技术实现与源码
- [`r2dreamer/envs/cr.py`](https://github.com/longlingking/clash-royale-simulator/blob/6086b9cac917cbdd479405091f90bca85b9bd66b/r2dreamer/envs/cr.py)：包装 `CREnv`。提供 `grid=(32,18,15)`、`hand=(5)`、`elixir=(1)` 与终局标志；动作空间为**三段共55维的multi-one-hot**（5 slot、32 y、18 x），分别 argmax 解码为 `(slot,y,x)`。
- [`r2dreamer/envs/cr_opponents.py`](https://github.com/longlingking/clash-royale-simulator/blob/6086b9cac917cbdd479405091f90bca85b9bd66b/r2dreamer/envs/cr_opponents.py)：`DreamerOpponent` 保存循环隐状态；`OpponentPool`、`SelfPlayController` 在固定策略、近期快照和基础 checkpoint 中抽样，并按胜率调整权重。
- [`tests/test_cr_selfplay.py`](https://github.com/longlingking/clash-royale-simulator/blob/6086b9cac917cbdd479405091f90bca85b9bd66b/tests/test_cr_selfplay.py)：包含快照排序、采样与工作进程测试定义；缺少训练 checkpoint 时部分测试标记为 skip。
- [`R2DREAMER_MIGRATION.md`](https://github.com/longlingking/clash-royale-simulator/blob/6086b9cac917cbdd479405091f90bca85b9bd66b/R2DREAMER_MIGRATION.md)：作者的迁移、安装、smoke 记录，不等于第三方复现。

## 复用边界
- [环境适配源码审查](../docs/source-audits/longling-r2dreamer-2026-10-15.md) 完成 **R2 静态核查**，未运行模型训练、smoke 或原生 Tick 差分。
- `cr.py` 在导入时使用 `os.chdir`，存在全局进程工作目录副作用；封装为服务前需移除或隔离。
- 自建战斗模拟的路径/卡牌行为与官方客户端并不保证同 Tick 保真。
- 根目录未核实统一机器可读许可证字段，登记 `unknown`；许可合作已由使用者与作者沟通，但项目元数据不据此伪造 SPDX。

[智能体环境能力](../capabilities/agent-environment/README.md) · [AI 训练专题](../topics/cr-ai-environment.md)
