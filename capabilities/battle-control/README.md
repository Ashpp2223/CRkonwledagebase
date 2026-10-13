---
id: battle-control
title: "原生战斗驱动"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 原生战斗驱动

> **技术中台能力**：在可控的离线环境中使用原生战斗逻辑初始化对局、推进时间、提交动作和读取状态。不同项目的控制接口不是统一 SDK。

## 适用问题

- 我能否在本地控制一场不依赖实时服务器玩家操作的原生对局？
- 我需要逐 Tick 推进、双边出牌、原生渲染或 AI 训练，应该选什么层级？
- 对方已经做好的哪些功能能够参考，哪些**有条件才能集成**？

## 现有实现及静态核查

| 项目 | 有证据的入口 | 复用判断 | 来源 |
| --- | --- | --- | --- |
| [FirstLight CR](../../projects/firstlight-cr.md) | `BattleEnvV1.reset/step`、`NativeClashEnv` 控制通道、原生快照 | R1；存在源码接口，但特定环境与完整接入未验证 | [实现](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/battle_env.py#L362-L381) |
| [Jason Battle Engine](../../projects/jason-battle-engine.md) | `Engine.reset/step`、`RenderedEngine`，支持 `minimal-transition` | **R2/source-inspected（仅限客户端控制层代码）**；集成未验证，缺整体许可证确认 | [控制实现](https://github.com/Jason-XII/clash-royale-battle-engine/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/engine.py#L147-L239) |
| [Ashpp 复盘器](../../projects/ashpp-replay.md) | `BattleController.reset/step/play_card`，额外验证预期 Tick | R1；产品内部桥接，**不是**第三方公共 API | [实现](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L126-L239) |
| [Replay Studio](../../projects/replay-studio.md) | `app/engine.py` 的原生画面控制，导入对局后重建 | R1；面向回放产品，非现成组件包 | [实现](https://github.com/ak1NaN/ClashRoyale-replay-studio/blob/04d48bdcf2f54cf81dc809e56d9bc08691a167e2/app/engine.py#L63-L126) |

> 细粒度评级以 [实现登记](../../registry/implementations.yaml) 为准。**R2 只确认已静态阅读控制入口及其限定条件**，不代表真实运行测试、跨项目 ABI 稳定或允许复制源码。

## 理解三种不同的接口层

**原生传输**：NativeClashEnv 的原生命令和 Jason 的 TCP 协议，需要匹配的 APK/原生库、探针和本地设备。语义接近但**请求格式、回执和状态对象都可能不同**。

**战斗环境**：FirstLight 的 `BattleEnvV1` 把原生状态包装成 FAIR 双边 Observation/Action，并定义奖励、终局和 ActionMask；它不是底层 `NativeClashEnv.step(ticks)` 的别名。

**复盘产品控制**：Ashpp 的 `BattleController` 在引擎上添加用户操作基点校验、状态摘要、分支恢复和持久化路径，不能当作已有标准化第三方 SDK。

更完整的 [接口签名与接入步骤](integration.md)、[环境/版本对照](compatibility.md) 和 [固定提交源码核查](../../docs/source-audits/native-engine-2026-10-13.md)。

## 选型与前置问题

1. **原生准确性**：目标游戏构建和资源指纹是否一致？有没有明确的重建/测试基准？
2. **运行成本**：需要 Android ARM64、原生探针还是另一套 Linux in-process 引擎？能否承受启动/通信延迟？
3. **动作语义**：出牌是当前 Tick 还是下一 Tick 执行？相同 owner 一次提交多个动作是否能区分回执？
4. **观测范围**：是 FAIR 策略观测还是引擎内部状态？隐藏数据能否合法用于训练/评测？
5. **错误行为**：写入超时后是否可能已执行？能否读取动作日志/代际后决定重试？
6. **许可**：即使接口可用，上游源码、专有游戏素材、模型和客户端文件也需要各自的授权判断。

## 未完成的中台资产

- 不同游戏版本的原生环境实测和行为差分报告。
- 各项目可被第三方引用的、声明版本支持的稳定接口。
- 基准对局数据、卡牌覆盖报告及公开维护者审核。
- 可复用的自动化端到端验收测试；目前只有**测试说明**，未有实测结果。

[返回能力目录](../README.md) · [查看快照能力](../snapshot-recovery/README.md)
