# 任务指南：建立复盘工具

## 先做四项选择

| 决策 | 推荐检查的能力 | 关键问题 |
| --- | --- | --- |
| 自主规则还是原生引擎 | [原生战斗驱动](../capabilities/battle-control/README.md) / [规则模拟](../capabilities/rules-simulation/README.md) | 版本保真程度与运行依赖 |
| 读取真人对局还是自主编排 | [对局重建](../capabilities/replay-reconstruction/README.md) | 出牌事件是否完整？隐藏状态是否缺失？ |
| 拖动时间轴还是自由分支 | [快照恢复](../capabilities/snapshot-recovery/README.md) | 是否能按成本要求恢复独立节点？ |
| 本地实时可视化或离线测试 | [状态观测](../capabilities/state-observation/README.md) | 可用画面、状态字段与数据时间戳 |

## 最小实验

1. 锁定原生/独立引擎版本、资源指纹、牌组、Seed（如果知道）。
2. 在单局固定动作序列中验证实体、圣水、塔血量及终局。
3. 在多个节点重放相同动作，记录逻辑摘要与时间轴偏差。
4. 创建两个分支，验证各自修改不会回写另一分支。
5. 断开和重启进程，确认哪些状态只能通过完整动作日志恢复。
6. 使用包含不支持卡牌、缺失形态和异常动作的负向用例，验证明确失败而非静默回放。

## 可参考的现有路线

- [Replay Studio](../projects/replay-studio.md)：导入 HTML，预演算后播放；缺少原始隐藏状态时为相容重建。
- [Ashpp 复盘器](../projects/ashpp-replay.md)：原生复盘、节点分叉、进程内状态快照与动作日志恢复。
- [FirstLight](../projects/firstlight-cr.md)：原生对局环境与回放数据重建。

不把任何一个项目内建接口称为跨项目稳定 API。更细的 [快照验收表](../capabilities/snapshot-recovery/integration.md)。
