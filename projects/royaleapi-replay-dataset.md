---
id: royaleapi-replay-dataset
title: "RoyaleAPI Replay Dataset"
type: project
status: research
verification: author-documented
repository: https://github.com/Aminiwow/royaleapi-replay-dataset
topics: [cr-replay-state, cr-ai-environment]
maintainers: []
last_reviewed: null
license: unknown
---

# RoyaleAPI Replay Dataset

- 上游：https://github.com/Aminiwow/royaleapi-replay-dataset
- 证据等级：R1 / author-documented（仅核查 README，未运行）
- 来源：https://github.com/Aminiwow/royaleapi-replay-dataset/blob/HEAD/README.md
- 许可：待核查；第三方游戏文件和素材不可因仓库公开而推定可再分发

## 技术价值与边界

匿名化皇室战争回放导出数据，README 指向 Releases；数据字段、样本来源、匿名化与授权尚未核实，暂作为数据线索。

## 后续验证

固定上游 commit；核查实现入口、依赖版本、许可证与测试；原生战斗相关项目需核对 Tick、状态恢复、输入与快照的一致性。当前不登记 R2/R3 能力实现。
