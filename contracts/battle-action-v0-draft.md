# Draft：Battle Action v0（候选概念契约）

**状态：Draft / 尚无已确认采纳者。** 本文不是 FirstLight 或任何其他项目真实可调用的动作 API。

## 需要表达的要素

| 要素 | 必须显式定义 |
| --- | --- |
| `owner` | 阵营方向及它与观测 perspective 的映射 |
| `issued_tick` / `effective_tick` | 决策时间与游戏实际生效时间的区别 |
| `kind` | wait / deploy / ability 等动作类型 |
| `hand_slot` / `card_id` | 提交时的手牌位及随回合变化的卡 ID |
| `position` / `coordinate_frame` | 落点单位、合法部署区域和朝向 |
| `status` | accepted / rejected / deferred / unknown |
| `reason` | 失败原因，如圣水不足或非法格 |

## 验收重点

- 连续两个动作是否能在同一 Tick 接受，或存在部署队列。
- 圣水检查、合法动作掩码与能力冷却由谁负责。
- 引擎接收命令与命令真正生效之间是否有延迟。
- 分支重放时同一 Tick 多动作的确定顺序。

相关参考：[FirstLight Policy Service](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/main/docs/policy_service.md)。
