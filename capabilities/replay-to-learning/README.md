---
id: replay-to-learning
title: "回放到训练样本流水线"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 回放到训练样本流水线

**能力定义**：将真人回放转为原生重建、观测-动作数据集、模仿学习和评测输入。

## 已有可衍生技术

| 来源 | 已有资产 | 复用等级 |
| --- | --- | --- |
| [clashai-vegetableleaf](../../projects/clashai-vegetableleaf.md) | 真人回放经原生重建、IL、PPO 和验收门禁 | R1（以作者资料为主） |
| [firstlight-cr](../../projects/firstlight-cr.md) | 回放重建、结构化观测、IL 与 PPO | R1（以作者资料为主） |
| [jason-battle-engine](../../projects/jason-battle-engine.md) | 原生回放缓存与训练/评测流程 | R1（以作者资料为主） |
| [royalegym](../../projects/royalegym.md) | 行为克隆与 Gymnasium 训练流程 | R1（以作者资料为主） |
| [detection-dataset](../../projects/detection-dataset.md) | 合成视觉数据集生成方法 | R1（以作者资料为主） |

## 中台组合要求

- 显式记录上游仓库和固定版本，不能把不同引擎的动作/观测结构直接拼接。
- 训练、实机、模拟器三种环境的游戏版本、观察权限和延迟均需独立验证。
- 原作者报告的性能或成功率只作为研究线索，不是中台测试结果。
- 方案接入前须确认代码许可证、模型/数据授权和第三方游戏资源的使用权。
- 用最小可复现用例与反例检验后才能升级为 R3 集成能力。

[完整生态技术筛选](../../landscape/2026-10-13-landscape.md) · [能力目录](../README.md)
