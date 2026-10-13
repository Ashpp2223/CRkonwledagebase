---
id: crsim-agent-larkindaniel
title: "CRSim Agent"
type: project
status: implemented
verification: author-documented
repository: https://github.com/larkindaniel/clash-royale-agent
topics: [cr-battle-simulation, cr-ai-environment, cr-game-mechanics]
maintainers: []
last_reviewed: null
license: MIT
---

# CRSim Agent

**来源**：[larkindaniel/clash-royale-agent](https://github.com/larkindaniel/clash-royale-agent)，参考提交 [c283c698ad74](https://github.com/larkindaniel/clash-royale-agent/tree/c283c698ad74fcc1304b612b11c2f399160d1055)。目前以作者公开资料编目；尚未完成第三方设备/性能测试，原作者也未确认加入中台。

## 核心可衍生资产

冻结八卡的确定性模拟、信息公平性审计、PPO复现实验。

## 能力入口

- [simulator-validation](../capabilities/simulator-validation/README.md)
- [rules-simulation](../capabilities/rules-simulation/README.md)
- [agent-environment](../capabilities/agent-environment/README.md)

## 研究网络

- [独立战斗模拟器](../topics/cr-battle-simulation.md)
- [AI 训练环境与决策](../topics/cr-ai-environment.md)
- [战斗机制、寻路与数值](../topics/cr-game-mechanics.md)

## 限制

请将作者声称的性能、准确率、游戏版本支持与独立复现区分开来。代码开源许可证不自动涵盖游戏素材/模型/回放权属。项目入目录不等于当前即可集成；按 [复用成熟度](../docs/reuse-maturity.md) 处理。
