---
id: royale-learn
title: "RoyaleLearn"
type: project
status: implemented
verification: author-documented
repository: https://github.com/RoyaleGym/RoyaleLearn
topics: [cr-ai-environment]
maintainers: []
last_reviewed: "2026-10-31"
license: MIT
---

# RoyaleLearn

**GitHub**：[RoyaleGym/RoyaleLearn](https://github.com/RoyaleGym/RoyaleLearn) · **固定源码提交**：`bd497751321127a8e4934a18f18ab9ef927c5cc9`

## 具体能力
[固定 README](https://github.com/RoyaleGym/RoyaleLearn/blob/bd497751321127a8e4934a18f18ab9ef927c5cc9/README.md) 提供 RoyaleGym 环境训练器，包含 `Learner(build_env)`、自定义奖励、`learn(total_steps=...)`、策略保存与接续训练。职责是策略优化/训练工件管理，**不是新的战斗规则引擎**。

模型、环境配置、观察空间和动作词表需要一致。未复现学习曲线或真实客户端胜率。R1 / author-documented / unverified。

[智能体环境能力](../capabilities/agent-environment/README.md)

## 2026-10-31 复查：训练观测编码与策略契约

[2026-10-27 固定提交](https://github.com/RoyaleGym/RoyaleLearn/tree/be967e58e49dd9ea4d45173fef1e3473b525aacb) 的 [CHANGELOG](https://github.com/RoyaleGym/RoyaleLearn/blob/be967e58e49dd9ea4d45173fef1e3473b525aacb/CHANGELOG.md) 记录：

- **0.5.20**：对无法无损写入 `uint8` 观测平面的非整数值记录 `health/obs_codec_rounded` 并报警；`health/obs_codec_clipped` 汇总进程 Worker 中实际编码的裁剪次数，不再只看父进程。新增 `rollout.codec_float16_planes` 和 `rollout.codec_unseen_float16`，用于明确指定要用 `float16` 存储的平面。
- **0.5.19**：`ppo.policy_transform` 可通过 `plugin:<module>:<function>` 改写策略 logits，并纳入策略概率、训练路径及算法身份校验；另修复共享主干的 float32 policy head 语义与已存环境重建检查。
- **0.5.18**：`rollout.mask_only_scripted` 允许脚本对手只生成动作掩码、跳过其不需要的后续观察，但依赖作者指定的 RoyaleGym 兼容版本。

**工程价值**：跨版本续训/策略复现除了记录权重，还应保存环境配置、观察编码表及其摘要、策略变换插件与训练算法身份。浮点特征在打包为整型平面时可能因舍入或裁剪造成输入信息变化，编码健康指标应和训练结果一同检查。

以上均为作者发布记录，尚未由中台实测编码、训练性能或恢复一致性；保持 `R1 / author-documented / unverified`。
