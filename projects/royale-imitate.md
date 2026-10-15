---
id: royale-imitate
title: "RoyaleImitate"
type: project
status: implemented
verification: author-documented
repository: https://github.com/RoyaleGym/RoyaleImitate
topics: [cr-ai-environment]
maintainers: []
last_reviewed: "2026-10-15"
license: MIT
---

# RoyaleImitate

**GitHub**：[RoyaleGym/RoyaleImitate](https://github.com/RoyaleGym/RoyaleImitate) · **固定源码提交**：`357cd55bf77f5c5d591de523ae9336cae3ab8f9c`

## 具体能力
[固定 README](https://github.com/RoyaleGym/RoyaleImitate/blob/357cd55bf77f5c5d591de523ae9336cae3ab8f9c/README.md)：教师权重 `save_actor` 与摘要、`warm_start` 初始化及可选模仿约束；与 RoyaleLearn 协作。可研究模型工件身份、教师—学生训练与回放样本的衔接，但**权重初始化不等于真人回放重建/完整模仿学习已复现**。

要求教师/学生模型架构和 observation/action 契约相容。R1 / author-documented / unverified。

[回放到训练能力](../capabilities/replay-to-learning/README.md)
