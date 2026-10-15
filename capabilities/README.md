# 可复用能力目录（主入口）

这里按**开发者意图**分类，而非按作者或项目分类。一项能力能从多个仓库取得技术来源，具体的项目×能力复用等级、来源与限制在 [实现矩阵](../registry/implementations.yaml) 中维护。

| 类别 | 能力 | 解决的问题 |
| --- | --- | --- |
| 原生底座 | [原生战斗驱动](battle-control/README.md) | 原生战斗初始化、Tick 和出牌 |
| 原生底座 | [状态观测](state-observation/README.md) | 内部状态、实体与合法动作 |
| 状态研究 | [快照与恢复](snapshot-recovery/README.md) | 进程快照、回放、序列化及分叉 |
| 搜索 | [前瞻规划](lookahead-planning/README.md) | 多候选模拟、评估与策略蒸馏 |
| 回放 | [轨迹可视化](battle-visualization/README.md) | 已有模拟器轨迹的播放、单步与实体检查 |
| 回放 | [对局重建](replay-reconstruction/README.md) | 外部事件与对局复现 |
| 感知 | [视觉状态](visual-perception/README.md) | 屏幕识别与状态融合 |
| 训练数据 | [回放→训练样本](replay-to-learning/README.md) | 真人样本重建、IL/RL 数据版本化 |
| AI 环境 | [智能体环境](agent-environment/README.md) | 对局 API、观测、动作、训练 |
| Agent 执行 | [运行时编排](agent-runtime/README.md) | 截图、策略、动作执行与确认 |
| 独立模拟 | [规则模拟](rules-simulation/README.md) | 自研引擎、卡牌机制 |
| 验证 | [仿真保真](simulator-validation/README.md) | 真实对局与模拟差分、反例库 |
| 数据 | [资源解析](asset-ingestion/README.md) | 数据格式、资源版本、解码 |

## 复用分级不是推荐榜

- R0：线索/历史实验；R1：知识可参考；R2：指定代码接口已静态审查；R3：指定运行环境的独立集成测试；R4：有维护承诺与回归机制。
- 项目“A/B/C”仅是**编辑收录优先级**（见 [生态调查](../landscape/2026-10-13-landscape.md)），不能与 R0–R4 混用。
- 一项引擎可能在状态快照上是 R2，在训练接口或画面渲染上仍只是 R1。
- 新增关联时请更新 [实现矩阵](../registry/implementations.yaml)，而不是只在本文插入项目名称。

[源码审查实例](../docs/source-audits/itzik-clashenv-2026-10-13.md) · [组合技术路线](../landscape/composition-patterns.md) · [贡献指南](../CONTRIBUTING.md)
