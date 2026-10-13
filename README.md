# CR Knowledge Base｜皇室战争开放技术中台

**从开发需求出发，查找现有技术、实现接口、验证证据与复用方法，并探索跨项目技术组合。**

> 2026-10-13 生态扩展调查：**24 个正式项目档案、12 项能力、64 条“项目×能力”关联、7 个跨项目研究专题**。大部分条目属于作者文档级证据（R0/R1），少量单项能力完成固定 Commit 静态源码审查（R2），**没有独立验证的 R3/R4 集成组件**。项目作者并未全部参与维护。

## 从需求开始

| 我需要的技术 | 中台入口 | 可能的衍生成果 |
| --- | --- | --- |
| 控制原生战斗、提交动作 | [原生战斗驱动](capabilities/battle-control/README.md) | 离线对局、原生研究、战斗测试 |
| 读取状态、手牌、单位 | [状态观测](capabilities/state-observation/README.md) | 事件解析、对局分析、感知融合 |
| 快速分叉或持久化恢复 | [状态快照与恢复](capabilities/snapshot-recovery/README.md) | 战术复盘、MCTS/搜索、AB 实验 |
| 候选动作前瞻与策略蒸馏 | [前瞻搜索](capabilities/lookahead-planning/README.md) | Teacher 搜索、策略改进、解释型 AI |
| 从真人对局重建 | [回放重建](capabilities/replay-reconstruction/README.md) | 时间轴分析、复盘编辑、数据生成 |
| 从录像/截图恢复游戏信息 | [视觉感知](capabilities/visual-perception/README.md) | 视觉教练、CV 分析、无内存观测研究 |
| 人类回放变成训练数据 | [回放到训练数据](capabilities/replay-to-learning/README.md) | 行为克隆、离线训练、模型对比 |
| 训练机器人或连接 RL 环境 | [智能体环境](capabilities/agent-environment/README.md) | PPO/IL 自博弈与评测 |
| 控制策略模型的设备执行流程 | [Agent 运行时](capabilities/agent-runtime/README.md) | 调度、延迟对齐、容错 |
| 开发自建战斗模拟器 | [规则模拟](capabilities/rules-simulation/README.md) | 快速仿真、修改规则、反事实实验 |
| 证明仿真到底准不准 | [模拟器保真验证](capabilities/simulator-validation/README.md) | 差分测试、卡牌行为校准 |
| 获取和解析游戏内容数据 | [资源与配置数据](capabilities/asset-ingestion/README.md) | 版本化卡牌表、地图研究和可溯源数值 |

## GitHub 全生态调查与选择依据

**[逆向工程知识中心](research/reverse-engineering/README.md)**：APK/Native、运行时内存、战斗对象布局、历史网络协议、资源格式、版本复验与 [13 条版本绑定的发现记录](registry/reverse-findings.yaml)。这是独立的证据型知识层，并非运行时组件。

- **[2026 年 GitHub 生态技术调查](landscape/2026-10-13-landscape.md)**：高价值项目与配套研究、优先级 A/B/C、排除理由及已知失效。
- **[可组合的技术链路](landscape/composition-patterns.md)**：原生→模拟→搜索、回放→训练、视觉→分析、资源→校准四条路线。
- **[衍生战斗力路线图](landscape/roadmap-derivative-power.md)**：接下来哪些底层验证和文档资产最能减少重复研究。

## 知识研究与复用

[知识生命周期与质量标准](docs/knowledge-workflow.md) · [知识笔记实例：四种状态恢复](research/knowledge-notes/snapshot-semantics.md) · [知识研究 / 综合 / 应用 Skills](docs/skills.md)

## 项目与证据

[能力目录](capabilities/README.md) · [项目来源档案](projects/README.md) · [研究专题](topics/README.md) · [源码审计](docs/source-audits/native-engine-2026-10-13.md) · [成熟度与授权](docs/reuse-maturity.md)

结构化登记：[能力](registry/capabilities.yaml) / [具体实现](registry/implementations.yaml) / [项目](registry/projects.yaml) / [专题](registry/topics.yaml) / [依赖/衍生关系](registry/relationships.yaml)。

## 如何参与

[维护者手册](docs/maintainer-handbook.md) · [项目 Skills](docs/skills.md) · [写作规范](docs/editorial-standards.md) · [贡献指南](CONTRIBUTING.md) · [AGENTS](AGENTS.md)

- 项目作者可以维护自己的来源文档，其他人可以提供有证据的功能补充与纠错。
- 提高某项能力的 R 等级需要固定版本和可核对的源码/实验记录；作者称“测试通过”不等于中台实测。
- 不镜像无授权 APK、原生库、模型权重、游戏贴图、泄露客户端或原始真人回放。
- 中台的 [接口草案](contracts/README.md) 均为 **Draft**，不暗示其他开发者已经采用统一 ABI。

