# 任务指南：建立皇室战争智能体

## 技术路线

| 路线 | 参考项目 | 优先验证 |
| --- | --- | --- |
| 原生引擎离线训练 | [FirstLight](../projects/firstlight-cr.md)、[Jason Battle Engine](../projects/jason-battle-engine.md) | 固定游戏版本、`reset/step` 及训练数据泄漏 |
| 自建规则模拟器训练 | [RoyaleGym](../projects/royalegym.md)、[Jason Simulator](../projects/jason-simulator.md)、[Hasty-CR](../projects/hasty-cr.md)、[crforge](../projects/crforge.md) | 真实机制偏差、卡牌覆盖、相同 Seed 的结果 |
| 视频视觉感知 | [KataCR](../projects/katacr.md) | 分辨率、遮挡、推理延迟与误检 |
| 客户端本地推理部署 | [Tencent Harness](../projects/tencent-model-harness.md) | 游戏版本偏移、模型张量格式、命令回执及服务条款 |

## 决策前必须明确

- 观测是否只包含代理在推理时可获得的信息。
- 动作表示是卡牌槽位、卡牌 ID、网格坐标、像素坐标或内部整数单位。
- 奖励定义是否与最终目标一致；如何防止利用模拟器漏洞刷分。
- 如何划分训练牌组、测试牌组、不同对手池及留出 Seed。
- 推理在原生客户端与离线引擎之间如何适配输入、时序和合法动作。

## 最小验收

先跑空动作/随机合法动作验证环境生命周期，再在留出牌组与 Seed 上做重复对局；报告胜率时附样本数量和置信范围。仿真对局胜率不等于真实客户端表现。切勿未经授权在正式服进行自动化行为。

参阅 [智能体能力](../capabilities/agent-environment/README.md) 与 [候选动作契约](../contracts/battle-action-v0-draft.md)。
