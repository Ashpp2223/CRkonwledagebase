# CR Knowledge Base｜皇室战争开源知识库

> 独立维护的社区项目知识索引：让开发者与 AI 能找到皇室战争相关工具、模拟器、回放研究与 AI 训练成果，并检查其来源、版本与复用边界。

本仓库 **只整理知识与引用，不整合其他作者代码**。每位作者继续维护自己的原仓库；这里维护项目目录、跨项目专题、证据和关系。与“黄神镇”无关，也不是 [clashroyalereplay](https://github.com/Ashpp2223/clashroyalereplay) 的软件开发仓库。

> 当前处于 **MVP 初始整理阶段**：项目条目以公开 README 等资料为依据，仅表示“文档声称”，不代表维护者已构建、运行或独立验证相关功能。项目尚未邀请/确认所有原作者作为维护者。

## 开始浏览

| 入口 | 用途 |
| --- | --- |
| [项目目录](projects/README.md) | 按项目定位其功能、来源、限制 |
| [技术专题](topics/README.md) | 按问题比较不同项目的实现 |
| [项目注册表](registry/projects.yaml) | 机器可读项目索引 |
| [专题注册表](registry/topics.yaml) | 机器可读技术分类 |
| [项目关系](registry/relationships.yaml) | 上游、衍生与引用关系（需要证据） |
| [AI 使用指南](docs/ai-retrieval-guide.md) | 如何避免版本与证据混淆 |
| [参与贡献](CONTRIBUTING.md) | 提交项目、研究、纠错 |
| [治理规则](GOVERNANCE.md) | 项目作者与知识库维护者的责任 |

## 第一批专题

- [原生战斗引擎](topics/cr-native-engine.md)
- [独立战斗模拟器](topics/cr-battle-simulation.md)
- [回放、快照与状态恢复](topics/cr-replay-state.md)
- [AI 训练环境与决策](topics/cr-ai-environment.md)
- [运行时游戏状态观测](topics/cr-runtime-observation.md)
- [资源与数据解析](topics/cr-assets-data.md)
- [战斗机制、寻路与数值](topics/cr-game-mechanics.md)

## 参与方式

发现新项目、发现事实错误或希望补充研究，均可提交 GitHub Issue / Pull Request。参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。所有重要事实请附源码或文档定位；不能验证时明确标记不确定性。

## 边界

- **已公开 ≠ 获得复制授权**：不镜像未获许可的代码、APK、`libg.so`、游戏素材、泄露资料或权重。
- **已实现 ≠ 经验证**：仓库 README 是作者陈述；独立验证需要可复现测试和记录。
- **同名接口 ≠ 版本兼容**：原生偏移、客户端版本、Tick 语义和坐标系必须逐项核对。
- **知识更新有时间性**：项目可能更新或失效，条目中的“尚未复核”不是“当前有效”。

项目索引最后初始化日期：2026-10-13。后续以各条目的独立证据和审核记录为准。
