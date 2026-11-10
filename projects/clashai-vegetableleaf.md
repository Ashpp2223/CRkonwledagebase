---
id: clashai-vegetableleaf
title: "ClashAI"
type: project
status: implemented
verification: author-documented
repository: https://github.com/vegetableleaf/ClashAI
topics: [cr-ai-environment, cr-runtime-observation, cr-replay-state]
maintainers: []
last_reviewed: "2026-11-10"
license: unknown
---

# ClashAI

**来源**：[vegetableleaf/ClashAI](https://github.com/vegetableleaf/ClashAI)，参考提交 [f1aed2cd034a](https://github.com/vegetableleaf/ClashAI/tree/f1aed2cd034a87f1af4df996cc16d4922d9a8b6f)。目前以作者公开资料编目；尚未完成第三方设备/性能测试，原作者也未确认加入中台。

## 核心可衍生资产

原生回放重驱、公开观测、模仿学习和强化学习部署流水线。

## 能力入口

- [replay-to-learning](../capabilities/replay-to-learning/README.md)
- [visual-perception](../capabilities/visual-perception/README.md)
- [agent-runtime](../capabilities/agent-runtime/README.md)
- [agent-environment](../capabilities/agent-environment/README.md)

## 研究网络

- [AI 训练环境与决策](../topics/cr-ai-environment.md)
- [运行时游戏状态观测](../topics/cr-runtime-observation.md)
- [回放、快照与状态恢复](../topics/cr-replay-state.md)

## 限制

请将作者声称的性能、准确率、游戏版本支持与独立复现区分开来。代码开源许可证不自动涵盖游戏素材/模型/回放权属。项目入目录不等于当前即可集成；按 [复用成熟度](../docs/reuse-maturity.md) 处理。

## 16.402.12 ORACLE：独立战斗宿主迁移研究（2026-10-15 核查）

在上游固定 [218554aee8b7](https://github.com/vegetableleaf/ClashAI/tree/218554aee8b7be9b3ad5298349853d6fe747c90f) 中，`scratchpad/gauntlet/L74/oracle` 已公开 160402012 原生生命周期的静态研究材料。v3 列出 GameMain、DataTables、地图资源、Replay Loader 和 Battle Tick 的高置信候选；[v7 门禁](https://github.com/vegetableleaf/ClashAI/blob/218554aee8b7be9b3ad5298349853d6fe747c90f/scratchpad/gauntlet/L74/oracle/linux/qualify/jnihost_ro/v7/GATES.md) 仍未完成 Android 运行验证（G5），不能称已有新版独立 reset/step 引擎。旧版数据采集依赖 `cr-native-sandbox` 15.535.29，不得与新版 ORACLE 混为一谈。

[详细版本对照与记谱器接入条件](../research/reverse-engineering/client-build-migration-2026-10.md)

## 2026-11-10 上游跟踪：公开训练管线与结果边界

[2026-11-06 固定提交](https://github.com/vegetableleaf/ClashAI/commit/21e28ae2b101a70e7f3a1218d149d343b860b49d) 重组了公开目录，并新增 [README](https://github.com/vegetableleaf/ClashAI/blob/21e28ae2b101a70e7f3a1218d149d343b860b49d/README.md) / [RESULTS](https://github.com/vegetableleaf/ClashAI/blob/21e28ae2b101a70e7f3a1218d149d343b860b49d/RESULTS.md)。**当前公开的仿真训练/评估使用外部 RoyaleSim 包**；部分历史模型来自其他未包含在该仓库中的引擎。此前 16.402 ORACLE 路线属于旧提交的静态迁移材料，不能从其存在推断当前主线已可启动 16.635 原生引擎。

当前 README 指明只将玩家公开可见的观测输入策略模型，对手手牌、下一张牌及真实圣水不直接提供；对手圣水从公开事件估计。训练运行依赖使用者自行准备的初始 checkpoint 与回放池；仓库不包含权重/数据集，也**未在干净安装环境验证部署说明**。

作者 [RESULTS](https://github.com/vegetableleaf/ClashAI/blob/21e28ae2b101a70e7f3a1218d149d343b860b49d/RESULTS.md) 报告 CLXV 与 CLXVI 在各 150 局 Ranked 样本上分别为 52/150 与 64/150（34.7% 和 42.7%），两者差异为 +8.0 个百分点、95% 区间 [-3.0, +19.0]。样本证据不足以确认新模型优于旧模型；这些数字为作者统计，**不是中台独立复测**。
