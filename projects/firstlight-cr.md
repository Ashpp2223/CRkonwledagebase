---
id: firstlight-cr
title: "FirstLight CR"
type: project
status: implemented
verification: author-documented
repository: https://github.com/Jaasssoooonnnnn/FirstLight_CR
topics: [cr-native-engine, cr-replay-state, cr-ai-environment]
maintainers: []
last_reviewed: "2026-11-10"
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

## 2026-11-10 上游提交复查

主分支在 2026-10-31 新增/修复了战斗部署布局与剩余运行时遥测的探针及测试（[固定提交](https://github.com/Jaasssoooonnnnn/FirstLight_CR/commit/d7d7deb3c28bb894511fa9b96d1529ba7610961d)），并调整 [BattleEnv 塔兵状态传递](https://github.com/Jaasssoooonnnnn/FirstLight_CR/commit/4c58aef6af2f4aa729a11a6eb139032a9ccf5076) 与 [丰富遥测适配](https://github.com/Jaasssoooonnnnn/FirstLight_CR/commit/270139f2df7744ef3ce991de39e6d596d79fc66f)。这是既有运行时的维护，不表示已经移植到 16.635。

[2026-10-31 README](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/4c82496ad5af49a3c7ea2392f26ff7bac33d9707/README.md) 另外介绍了单独 `yes-delay` 分支的 Everlight 模型，使用出牌后 **20 Tick（1 秒）** 生效的时序。该分支声明与主分支的现有安装/验证契约应分开记录，尚未对该分支做单独源码审计或客户端一致性测试。
