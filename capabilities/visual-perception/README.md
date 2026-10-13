---
id: visual-perception
title: "屏幕感知与视觉状态融合"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 屏幕感知与视觉状态融合

**能力定义**：仅凭屏幕识别单位/卡牌/场地事件，并区分直接观测与引擎推断。

## 已有可衍生技术

| 来源 | 已有资产 | 复用等级 |
| --- | --- | --- |
| [clashai-vegetableleaf](../../projects/clashai-vegetableleaf.md) | 视觉与公开信息观测契约、状态融合 | R1（以作者资料为主） |
| [build-a-bot](../../projects/build-a-bot.md) | 截图检测器和结构化状态生成 | R1（以作者资料为主） |
| [detection-dataset](../../projects/detection-dataset.md) | 合成视觉标注样本 | R1（以作者资料为主） |
| [itzik-clashenv](../../projects/itzik-clashenv.md) | 视觉转游戏事件并驱动模拟器估计 | R1（以作者资料为主） |
| [katacr](../../projects/katacr.md) | YOLO/OCR 和视觉训练链 | R1（以作者资料为主） |
| [card-tracker](../../projects/card-tracker.md) | 早期视觉循环与卡牌识别研究 | R0（以作者资料为主） |

## 中台组合要求

- 显式记录上游仓库和固定版本，不能把不同引擎的动作/观测结构直接拼接。
- 训练、实机、模拟器三种环境的游戏版本、观察权限和延迟均需独立验证。
- 原作者报告的性能或成功率只作为研究线索，不是中台测试结果。
- 方案接入前须确认代码许可证、模型/数据授权和第三方游戏资源的使用权。
- 用最小可复现用例与反例检验后才能升级为 R3 集成能力。

[完整生态技术筛选](../../landscape/2026-10-13-landscape.md) · [能力目录](../README.md)
