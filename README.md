# CR Knowledge Base｜皇室战争开放技术中台

**从开发需求出发，找到已有能力、实现来源、接入约束与验证证据。** 这是一个由社区共同维护的**技术文档中台**，不是代码镜像、官方游戏文档、统一 SDK 或单纯的 GitHub 项目榜单。

> **MVP / 资料整理阶段**：当前实现登记主要来自作者公开 README，未逐项构建测试，也未获得全部原作者审核。可读到 ≠ 已验证 ≠ 可集成。所有成熟度仅是当前证据所支持的最低承诺。

## 我要做什么？

| 开发需求 | 能力入口 | 相关指南 |
| --- | --- | --- |
| 控制原生对局的开始、推进与出牌 | [原生战斗驱动](capabilities/battle-control/README.md) | [开发复盘工具](guides/build-replay-tool.md) |
| 获取双方手牌、圣水、实体状态 | [对局状态观测](capabilities/state-observation/README.md) | [观测和接口约束](contracts/battle-state-v0-draft.md) |
| 从历史节点恢复、探索分支 | [状态快照与恢复](capabilities/snapshot-recovery/README.md) | [开发复盘工具](guides/build-replay-tool.md) |
| 从第三方战报重建战斗 | [对局重建与分支回放](capabilities/replay-reconstruction/README.md) | [开发复盘工具](guides/build-replay-tool.md) |
| 接入 AI 进行训练或评测 | [智能体环境与模型对接](capabilities/agent-environment/README.md) | [开发游戏智能体](guides/build-agent.md) |
| 下载或解析卡牌资源 | [资源与配置数据获取](capabilities/asset-ingestion/README.md) | [资源方案](topics/cr-assets-data.md) |
| 实现可修改的战斗模拟器 | [可修改的战斗规则模拟](capabilities/rules-simulation/README.md) | [机制研究](topics/cr-game-mechanics.md) |

## 中台的不同信息层级

- [能力目录](capabilities/README.md) — 解决什么问题、有哪些实现、依赖与限制、复用成熟度。
- [项目档案](projects/README.md) — 谁维护源码、项目提供什么、上游与许可证。
- [研究专题](topics/README.md) — 不同实现的机制、差异、证据和未解决问题。
- [候选接口协议](contracts/README.md) — **均为 Draft**，不能当作现有项目的 API。
- [任务指南](guides/README.md) — 按具体开发任务组合能力和测试。
- [源码审计实例](docs/source-audits/native-engine-2026-10-13.md) — 已核查 FirstLight 快照、Jason Engine 接口、复盘器分支隔离；设备级复现仍缺。\n- [机器索引](registry/capabilities.yaml) — 配合 [实现矩阵](registry/implementations.yaml)、[项目表](registry/projects.yaml)、[专题表](registry/topics.yaml) 与 [关系表](registry/relationships.yaml)。

### 如何判断能否复用

先查看 [复用成熟度和证据等级](docs/reuse-maturity.md)：R0 研究线索、R1 可参考知识、R2 有源码核查证据、R3 满足指定条件的集成、R4 有维护承诺。**每项能力的实现单独评级；技术成熟度、实测证据、版权/许可证和版本兼容是不同维度。** 目前只有部分接口获得了**限定范围的静态源码核查（R2）**，整个仓库仍未完成原生集成测试，因此不宣称 R3/R4。

## 一起维护

- [贡献指南](CONTRIBUTING.md) · [协作治理](GOVERNANCE.md) · [架构与数据模型](docs/architecture.md) · [AI 检索说明](docs/ai-retrieval-guide.md) · [AGENTS.md](AGENTS.md)
- GitHub Issue 用于报错、补充研究与申请登记项目；PR 用于添加或修订可追溯的文档。

**边界**：不分发无授权的 APK、`libg.so`、原始素材、泄露源码或模型权重。仓库中的候选协议由本社区拟议，不能暗示它们是 Supercell 或第三方项目已有的正式接口。
