---
id: firstlight-cr
title: "FirstLight CR"
type: project
status: implemented
verification: author-documented
repository: https://github.com/Jaasssoooonnnnn/FirstLight_CR
topics: [cr-native-engine, cr-replay-state, cr-ai-environment]
maintainers: []
last_reviewed: null
license: Apache-2.0
---

# FirstLight CR

[上游仓库](https://github.com/Jaasssoooonnnnn/FirstLight_CR) · [固定源码核查](../docs/source-audits/native-engine-2026-10-13.md)

## 功能分层

- 底层：`NativeClashEnv` 本地控制与原生探针；包含观察、Tick 逐步推进、原生渲染、进程内快照命令。
- 环境：`BattleEnvV1` 的双边 FAIR 观测、动作掩码和回合奖励。
- AI：模仿学习、PPO 训练、模型服务及回放数据管线（训练指标仍为作者声明）。

[低层接口](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/cr_native_env.py#L2739-L2860) · [环境接口](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/battle_env.py#L362-L381) · [私有 Python 契约](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/contracts.py#L1614-L1633)。

## 环境与限制

[安装说明](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/docs/getting_started.md#L13-L23) 固定 Windows / Android 12 MuMu ARM64、Null's Royale APK 15.535.13 及内容 15.535.86 的安装目标。用户须自行具备合法客户端资源。**进程内快照句柄随进程与 manager generation 失效**，没有证明任意状态多实例克隆。当前没有中台设备实测。

[原生控制能力](../capabilities/battle-control/README.md) · [快照恢复能力](../capabilities/snapshot-recovery/README.md) · [AI 训练专题](../topics/cr-ai-environment.md)

本项目涉及的逆向研究方法与跨版本限制已整理至 [逆向工程知识中心](../research/reverse-engineering/README.md)。
