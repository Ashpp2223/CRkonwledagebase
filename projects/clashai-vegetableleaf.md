---
id: clashai-vegetableleaf
title: "ClashAI"
type: project
status: implemented
verification: author-documented
repository: https://github.com/vegetableleaf/ClashAI
topics: [cr-ai-environment, cr-runtime-observation, cr-replay-state]
maintainers: []
last_reviewed: null
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
