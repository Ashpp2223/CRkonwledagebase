# 共享能力目录

这里是中台的**主入口**，按开发者意图而非作者和项目分类。一项能力可能有多个实现；同一项目也可能服务多个能力。能力存在只代表有相关研究或实现，**不等于提供可复制依赖的 SDK**。

| 能力 ID | 面向的问题 | 说明 |
| --- | --- | --- |
| `battle-control` | [原生战斗驱动](battle-control/README.md) | 如何在离线环境初始化、推进和控制原生战斗？ |
| `state-observation` | [对局状态观测](state-observation/README.md) | 如何从原生状态、内存或画面取得结构化观测？ |
| `snapshot-recovery` | [状态快照与恢复](snapshot-recovery/README.md) | 能否从任意历史局面继续执行，并保持状态一致？ |
| `replay-reconstruction` | [对局重建与分支回放](replay-reconstruction/README.md) | 如何把外部对局事件重建成可观看或可交互的战斗？ |
| `agent-environment` | [智能体环境与模型对接](agent-environment/README.md) | 如何将战斗与 AI 模型连接，用于训练、评测或本地推理？ |
| `asset-ingestion` | [资源与配置数据获取](asset-ingestion/README.md) | 如何定位、下载并解析指定版本的卡牌与地图相关资源？ |
| `rules-simulation` | [可修改的战斗规则模拟](rules-simulation/README.md) | 怎样在自己的模拟器中实现、验证与扩展战斗机制？ |

## 如何读一张能力卡

1. **边界**：它究竟解决什么，排除什么。
2. **最小接口/验收要求**：需求清单而非所有仓库的统一实现。
3. **实现矩阵**：每个项目一条能力关联，带证据和版本/运行限制。
4. **复用判断**：R0–R4、验证等级、集成状态和授权约束。
5. **延伸研究**：原项目及 [技术专题](../topics/README.md) 的来源。

所有项目—能力关联以 [registry/implementations.yaml](../registry/implementations.yaml) 为单一数据源。修改时应同步审阅能力卡与来源，并运行 `python scripts/validate.py`。
