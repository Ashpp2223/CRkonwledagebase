# v1 项目索引迁移记录

2026-10-13 起，以能力目录为主入口，`topics/` 保留作为研究专题。

- `projects/tencent-tools.md` 曾组合两个仓库，现拆为 `tencent-overlay` 和 `tencent-model-harness`；旧页保留指引。
- `projects/royalegym.md` 现专指 RoyaleGym Python 仓库；`royalesim.md` 独立记录 Rust 引擎。
- `registry/projects.yaml` 的项目 ID 是 GitHub 仓库身份；`registry/implementations.yaml` 的能力 ID 与项目 ID 是显式关联。
- 旧主题链接依然有效；AI 检索入口改为 `registry/capabilities.yaml`。
- 原作者仓库不受本次迁移影响。

[架构决策 ADR-0001](adr/0001-capability-center.md)
