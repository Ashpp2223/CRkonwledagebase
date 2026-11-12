# 2026-11-12 GitHub 增量发现：原生规则证据与公开 API 历史

本轮以 [项目注册表](../registry/projects.yaml) 为去重基准，检索 GitHub 上的 battle simulator、native engine、RL、replay、API analytics 等关键词；核对候选 README，重点读取 aboufama 的 `STATE.md`。仅为**候选调查**，没有运行测试或固定提交源码审计；不直接新增 Project / Implementation ID。

## A：优先正式建档

### aboufama/clash-royale-research

- 上游：https://github.com/aboufama/clash-royale-research
- 文档：[README](https://github.com/aboufama/clash-royale-research/blob/main/README.md) / [STATE](https://github.com/aboufama/clash-royale-research/blob/main/STATE.md) / [FIDELITY](https://github.com/aboufama/clash-royale-research/blob/main/docs/FIDELITY.md)
- **差异化**：针对 Android `160402020` 的原生行为研究与 TypeScript 20 Hz 重建模拟器；`STATE.md` 报告 70 张可玩卡、126 个核心测试、400 Tick 原生轨迹的 539/539 位置与 HP 对照，以及 SC2 动画/音频还原、浏览器交互沙盒。原生 Unicorn 路线因性能与任意动作/重置限制暂停，转向机制逐项移植及差分核验。
- **边界**：README 开头仍写“Private repository”，但 `STATE.md` 称后改公开；两份文档的进度口径不同，必须以固定提交源码和测试核实。包含原版游戏素材/二进制的说明，不得镜像或将其视为可再分发资源。作者报告的对照范围不能外推至完整原版保真。
- **建议关联**：`rules-simulation`、`simulator-validation`、`asset-ingestion`、`battle-visualization`；优先核查 `sim/core`、`tests`、`docs/FIDELITY.md`、`research/evidence` 的真实证据。

## B：公开 API 历史数据体系

### jthingelstad/elixir-mcp

- 上游：https://github.com/jthingelstad/elixir-mcp
- [README](https://github.com/jthingelstad/elixir-mcp/blob/main/README.md)
- **差异化**：持续采集官方公开 API 的玩家/部落数据并保留历史；提供 MCP、JSON API 和网页。README 给出 `packages/contracts`、`packages/ledger`、`services/collector` 等源码入口。与战斗内部 Tick 状态和原生复盘是不同数据层。
- **建议**：先作为数据服务/外部分析研究线索；若要正式建档，需评估知识库现有 13 项能力是否涵盖“公开 API 历史采集”，避免强行归入回放重建。

### jthingelstad/elixir-mcp-collector

- 上游：https://github.com/jthingelstad/elixir-mcp-collector
- [README](https://github.com/jthingelstad/elixir-mcp-collector/blob/main/README.md)
- **差异化**：Go 标准库实现的自托管采集 Worker；租约分配、固定 IP API key、HTTPS 提交、全局节流和版本签名验收。与 Elixir MCP 是同一技术链的不同仓库，若建档应分别登记来源并关联依赖。
- **边界**：依赖第三方服务和官方 API 配额/条款；没有原生战斗引擎或逐帧回放能力。

## 已去重或暂不收录

| 候选 | 处理 |
| --- | --- |
| [cole-zoom/clash-royale-env](https://github.com/cole-zoom/clash-royale-env) | README 大量内容与已入库 [itzik123/ClashRoyaleAi](../projects/itzik-clashenv.md) 重合，且 CI badge 指向 itzik 仓库；需确认 Fork/独立增量，暂不重复建档 |
| [oghyhk/crforge](https://github.com/oghyhk/crforge) | README 的 CI 指向已收录 [voonhous/crforge](../projects/crforge.md)；暂按可能同源 Fork 处理 |
| [MSU-AI/clash-royale-gym](https://github.com/MSU-AI/clash-royale-gym) | 已在 [2026-10-13 调查](2026-10-13-landscape.md) 评为 C：README 初版 mock API |
| [OwenCochell/clash-royale-rl](https://github.com/OwenCochell/clash-royale-rl) | README 与 MSU-AI gym 内容高度相同，尚无明确独立增量 |
| [RoyaleAPI/cr-api](https://github.com/RoyaleAPI/cr-api) | 已在旧调查作为历史 API 项目排除；当前 README 主要为支持工单入口 |
| [Argon-18AR/GoblinBattleSimulator](https://github.com/Argon-18AR/GoblinBattleSimulator) | 仓库为空，无可核查实现 |
| [jthingelstad/elixir-bot](https://github.com/jthingelstad/elixir-bot) | README 明确 2026-09-26 退役，后续由 elixir-mcp 系列替代；保留架构史线索即可 |

## 下一步验收

1. 固定 aboufama 仓库 commit，核对 `sim/core`、`tests`、原生轨迹文件及其重现脚本，逐项划分实证与作者描述；检查仓库中的第三方资源分发风险。
2. 审查 Elixir MCP 的数据合同、采集去重、历史版本和公开 API 数据边界，决定是否新增“公开 API 历史数据”能力；避免与内部战斗状态混淆。
3. 扩展检索尚未覆盖的回放数据集、对局解析和版本化资产项目；本轮不是 GitHub 穷尽扫描。

**登记原则**：候选不等于正式项目；README 不能单独证明运行成熟度。
