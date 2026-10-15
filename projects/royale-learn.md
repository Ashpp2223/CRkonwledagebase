---
id: royale-learn
title: "RoyaleLearn"
type: project
status: implemented
verification: author-documented
repository: https://github.com/RoyaleGym/RoyaleLearn
topics: [cr-ai-environment]
maintainers: []
last_reviewed: "2026-10-15"
license: MIT
---

# RoyaleLearn

**GitHub**：[RoyaleGym/RoyaleLearn](https://github.com/RoyaleGym/RoyaleLearn) · **固定源码提交**：`bd497751321127a8e4934a18f18ab9ef927c5cc9`

## 具体能力
[固定 README](https://github.com/RoyaleGym/RoyaleLearn/blob/bd497751321127a8e4934a18f18ab9ef927c5cc9/README.md) 提供 RoyaleGym 环境训练器，包含 `Learner(build_env)`、自定义奖励、`learn(total_steps=...)`、策略保存与接续训练。职责是策略优化/训练工件管理，**不是新的战斗规则引擎**。

模型、环境配置、观察空间和动作词表需要一致。未复现学习曲线或真实客户端胜率。R1 / author-documented / unverified。

[智能体环境能力](../capabilities/agent-environment/README.md)
