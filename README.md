# CR Knowledge Base｜皇室战争开放技术中台

**从开发需求出发，查找现有技术、实现接口、验证证据与复用方法，并探索跨项目技术组合。**

> 截至 2026-11-12（目录与关联复核）：**58 个正式项目档案、13 项能力、90 条“项目×能力”关联、7 个跨项目研究专题**。大部分条目属于作者文档级证据（R0/R1），少量单项能力完成固定 Commit 静态源码审查（R2），**没有独立验证的 R3/R4 集成组件**。项目作者并未全部参与维护。

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

**[逆向工程知识中心](research/reverse-engineering/README.md)**：APK/Native、运行时内存、战斗对象布局、历史网络协议、资源格式、版本复验与 [21 条版本绑定的发现记录](registry/reverse-findings.yaml)。这是独立的证据型知识层，并非运行时组件。

- **[2026-10-15 开发者网络与新仓库调查](landscape/2026-10-15-developer-network.md)**：从开发者公开仓库及已确认的 Fork/协作关系发现原生宿主、私有 Clapha、数据与训练线索；不可访问的 Star/Follow 图谱明确标注。
- **[新版 16.402.12 原生生命周期研究](research/reverse-engineering/client-upgrade-160402.md)**：区分静态定位、源码编译与真正的新版离线原生执行。
- **[2026 年 GitHub 生态技术调查](landscape/2026-10-13-landscape.md)**：高价值项目与配套研究、优先级 A/B/C、排除理由及已知失效。
- **[可组合的技术链路](landscape/composition-patterns.md)**：原生→模拟→搜索、回放→训练、视觉→分析、资源→校准四条路线。
- **[2026-10-15 研究者项目/Fork 网络](landscape/2026-10-15-source-network.md)**：新增 Linux 原生宿主、可玩离线壳、回放采集和旧版 Fork 差异；[新版战斗迁移进度](research/reverse-engineering/client-build-migration-2026-10.md)。
- **[2026-10-15 社交图复查与 RoyaleGym 模块补充](landscape/2026-10-15-social-graph-followup.md)**：核查四位开发者账号的可访问边界，新增 RoyaleBot、RoyaleViser、RoyaleLearn、RoyaleImitate 候选研究；核对 FirstLight 派生 Fork 的增量。
- **[衍生战斗力路线图](landscape/roadmap-derivative-power.md)**：接下来哪些底层验证和文档资产最能减少重复研究。

## 知识研究与复用

[知识生命周期与质量标准](docs/knowledge-workflow.md) · [原生引擎宿主架构的可迁移知识](research/knowledge-notes/native-runtime-hosting.md) · [知识笔记实例：四种状态恢复](research/knowledge-notes/snapshot-semantics.md) · [知识研究 / 综合 / 应用 Skills](docs/skills.md)

## 项目与证据

[能力目录](capabilities/README.md) · [项目来源档案](projects/README.md) · [研究专题](topics/README.md) · [源码审计](docs/source-audits/native-engine-2026-10-13.md) · [成熟度与授权](docs/reuse-maturity.md)

结构化登记：[能力](registry/capabilities.yaml) / [具体实现](registry/implementations.yaml) / [项目](registry/projects.yaml) / [专题](registry/topics.yaml) / [依赖/衍生关系](registry/relationships.yaml)。

## 如何参与

[维护者手册](docs/maintainer-handbook.md) · [项目 Skills](docs/skills.md) · [写作规范](docs/editorial-standards.md) · [贡献指南](CONTRIBUTING.md) · [AGENTS](AGENTS.md)

- 项目作者可以维护自己的来源文档，其他人可以提供有证据的功能补充与纠错。
- 提高某项能力的 R 等级需要固定版本和可核对的源码/实验记录；作者称“测试通过”不等于中台实测。
- 不镜像无授权 APK、原生库、模型权重、游戏贴图、泄露客户端或原始真人回放。
- 中台的 [接口草案](contracts/README.md) 均为 **Draft**，不暗示其他开发者已经采用统一 ABI。

## 2026-10-15：CR 模拟器与 AI 技术知识扩展

- [5 个新来源和项目说明](projects/README.md)：Longling R2-Dreamer、RoyaleLearn、RoyaleImitate、RoyaleViser、RoyaleBot。
- [跨客户端规则保真与模型自博弈专题](research/knowledge-notes/cr-model-selfplay-client-parity-2026-10-15.md)：将可信源码入口、可用范围和测试反例结合。
- [战斗轨迹可视化](capabilities/battle-visualization/README.md)：与原生恢复/事件重建分开分类。
- [Longling 源码审查](docs/source-audits/longling-r2dreamer-2026-10-15.md) · [RoyaleSim 源码审查](docs/source-audits/royalesim-client-parity-2026-10-15.md)。

## 2026-10-31：重点上游版本复查

- [皇室战争复盘器](projects/ashpp-replay.md)：10 月 18 日提交新增**国服 38.4.5 / 0.4.1** 接入，与原引擎分开选择；记录版本身份、卡牌/形态目录和快照/日志恢复的验收边界。
- [RoyaleSim](projects/royalesim.md)：10 月 23 日发布 **0.1.42**；继续采用带来源的客户端差异参数，明确 16.402 系列与旧版 15.535.29 的规则和卡表边界。
- [RoyaleLearn](projects/royale-learn.md)：10 月 27 日发布 **0.5.20**；扩展观测编码的舍入/裁剪诊断与 float16 存储配置。
- [RoyaleGym](projects/royalegym.md)：复查文档入口，校正来源链接。各上游的发布事实均为来源核对，**不等于本知识库新增独立运行验证**；实现成熟度仍以 [机器登记](registry/implementations.yaml) 与对应的固定源码审计为准。

## 2026-11-10：16.635 新版规则、觉醒巨人与回放对照

- **[新版战斗引擎与觉醒巨人研究](research/knowledge-notes/cr-16635-evo-giant-parity-2026-11-10.md)**：核对 16.635.1 客户端与 16.635.8 数据版本，区分官方原生引擎、crforge 参考回放逐 Tick 比对，以及 RoyaleSim 数据表/专项测试。
- **[crforge 项目档案](projects/crforge.md)**：11 月 5 日实现 `Giant_EV1`，上游提交报告真实参考场景 `diagnostic_match`；[差分接口 R2 静态审计](docs/source-audits/crforge-16635-parity-2026-11-10.md) 仅覆盖指定源码和测试入口。
- **[RoyaleSim 项目档案](projects/royalesim.md)**：更新至 0.1.51；觉醒巨人的区域/时钟测试来自 16.635 游戏表，作者说明该形态尚未被实际捕获轨迹校准。两项目此前均已入库；这一轮仅对它们的能力登记增加 1 条验证关联。另行发现的新版原生宿主 Clashback 见下节。

## 2026-11-10 重要补充：新版原生引擎接口已经存在

[Clashback](projects/clashback.md)（ak1NaN）已公开 x86_64 `libg.so` 构建 `160635001`、游戏数据 `16.635.8` 对应的原生绑定，并在 macOS / Rosetta 下提供 `CrxEnv.create_match/step/observe/queue_card_at` 与 Tick 快照保存/恢复。它直接调用原生引擎，区别于重建战斗规则的 [crforge](projects/crforge.md)、[RoyaleSim](projects/royalesim.md)；觉醒巨人的专项原生校验尚无固定公开证据；其资源清单还需确认觉醒形态定义是否实际加载。补入 1 个 Project 和 3 条实现关联（战斗驱动、快照恢复两项 R2 静态核查；回放重建 R1），授权状态 unknown，未独立运行验证。[研究笔记](research/knowledge-notes/cr-16635-evo-giant-parity-2026-11-10.md) 已相应纠错。

## 2026-11-12：RoyaleFish 离线强化学习项目

- [RoyaleFish](projects/royalefish.md)：补入原生战斗引擎并行自博弈、V4 recurrent actor-critic、PPO 训练与公开模型基线；原生引擎和 V4 框架需自行提供。
- 新增 1 个 Project 和 1 条 `agent-environment` 实现关联；已按固定提交 [e94f9d6](https://github.com/fabiospalla9-tech/RoyaleFish/tree/e94f9d6b3c17c5e308272d01d6fdfe0e312201e9) 对训练流水线完成 [R2 静态源码审查](docs/source-audits/royalefish-2026-11-12.md)。性能、胜率、引擎运行与分支快照均未独立验证。

## 2026-11-12：跨名称关联扩展

新增 [6 个独立项目来源](projects/README.md)：Clash Royale Research、CrownZero、Clash Royale Post-Game Analyzer、Elixir MCP、Elixir MCP Collector、Clash Royale Dataset Browser。检索包括非直观仓库名与项目依赖链；均为 R1 作者文档级证据，未增加能力实现关联或宣称独立运行验证。

## 2026-11-12：第二轮发现

新增 [4 个独立项目](projects/README.md)：CR Native Sandbox、SC Fingerprint Downloader Rust、Supercell Asset Decompressor、RoyaleAPI Replay Dataset；Jason-XII 模拟器已在库中，未重复登记。全部保持 R1 作者文档证据。

## 2026-11-12：作者级仓库复核

对 Jason-XII（24 个公开仓库）和 IMAX9D（7 个公开仓库）逐一筛选，并与现有注册表核对。新增 [Daybreak CR](projects/jason-daybreak.md)；IMAX9D 的 Linux Bionic、RoyaleAPI Downloader、R0 Elite 已在库中，不重复建档。今后扩展搜索应优先沿已收录作者的全部仓库和项目依赖链核对。

## 2026-11-12：作者仓库全量名称筛查

从注册表得到 30 个不同 GitHub 所有者，枚举各账号公开仓库并对重点候选读取 README，新增 [9 项](projects/README.md)。发现 IMAX9D/cr-native-sandbox 在 registry/projects.yaml 中有两条登记：已移除重复的 `imax-native-sandbox` 注册条目，保留原 `native-sandbox-imax9d` 正式档案；目前为 58 条登记、58 个不同仓库。

### 研究修订：FirstLight Zero 回放一致性边界

新增 [FirstLight Zero 训练与回放合同审查](docs/source-audits/firstlight-zero-2026-11-12.md)。其回放导出/重驱检查覆盖动作及终局字段，不可据此推断逐 Tick 完整状态一致或支持任意帧快照恢复。另核对 RoyaleAPI/cr-api-docs 为 2020 年停用的历史 API 文档归档。
