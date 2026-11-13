# 全库源码普查总账（2026-11-12 启动）

范围：原注册表 58 条，2026-11-13 去重后 57 个独立 GitHub 项目；本表按**项目**而非作者计数。此表的“源码已读”只表示此前存在可追溯的部分文件检查，不代表全项目审计完成。

## 统一检查标准

1. 固定上游 commit、许可证、仓库类型（独立/Fork/镜像/资源/文档/归档）。
2. 枚举目录与核心入口；至少核查关键实现、接口/数据模型、依赖和测试，记录具体文件、blob 或 commit。
3. 将 README 的宣称逐条映射到源码实现；追踪未实现、条件成立、已知缺陷、版本和外部依赖。
4. 对原生引擎与回放特别核查 Tick、RNG、状态序列化、快照恢复、动作排序、坐标系、版本一致性。
5. 标注审查层级：P0=仅入库；P1=部分源码文件检查；P2=核心实现+测试/依赖审查；P3=独立运行/回归验证。P1/P2/P3 必须链接证据；不可自动升级。
6. 沿作者、Fork、子模块、外部数据、引用与上游继续扩展。项目记录与验证结论分开维护。

## 当前登记项目与审查状态

| ID | 上游 | 源码检查状态 | 备注 |
|---|---|---|---|
| firstlight-cr | [repo](https://github.com/Jaasssoooonnnnn/FirstLight_CR) | P1（部分源码） | [2026-11-13 审查](firstlight-cr-source-2026-11-13.md)；未运行测试 |
| jason-battle-engine | [repo](https://github.com/Jason-XII/daybreak-cr) | P1（部分源码） | [2026-11-13 审查](jason-daybreak-source-2026-11-13.md)；旧名 clash-royale-battle-engine |
| jason-simulator | [repo](https://github.com/Jason-XII/clash-royale-simulator) | P1（部分源码） | [2026-11-13 审查](jason-simulator-source-2026-11-13.md)；未运行测试 |
| replay-studio | [repo](https://github.com/ak1NaN/ClashRoyale-replay-studio) | P1（部分源码） | [2026-11-13 审查](replay-studio-source-2026-11-13.md)；未运行测试 |
| ashpp-replay | [repo](https://github.com/Ashpp2223/clashroyalereplay) | P1（部分源码） | [2026-11-13 审查](ashpp-replay-source-2026-11-13.md)；未运行测试 |
| memory-reader | [repo](https://github.com/Jason-XII/cr-memory-reader) | P1（部分源码） | [2026-11-13 源码审查](memory-reader-source-2026-11-13.md)；未运行测试 |
| tencent-overlay | [repo](https://github.com/ak1NaN/ClashRoyale-tencent-overlay) | P1（部分源码） | [2026-11-13 源码审查](tencent-overlay-source-2026-11-13.md)；未运行测试 |
| tencent-model-harness | [repo](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness) | P1（部分源码） | [2026-11-13 源码审查](tencent-model-harness-source-2026-11-13.md)；未运行测试 |
| hasty-cr | [repo](https://github.com/hastylmao/Hasty-CR) | P0（待逐文件检查） | 待审 |
| royalefish | [repo](https://github.com/fabiospalla9-tech/RoyaleFish) | P1（有限文件） | 既有审计：docs/source-audits/royalefish-2026-11-12.md |
| royalegym | [repo](https://github.com/RoyaleGym/RoyaleGym) | P1（部分源码） | [2026-11-13 源码审查](royalegym-source-2026-11-13.md)：依赖、环境入口、Mock/Rust 区分；未运行测试 |
| royalesim | [repo](https://github.com/RoyaleGym/RoyaleSim) | P1（部分源码） | [2026-11-13 审查](royalesim-source-2026-11-13.md)；未运行测试 |
| crforge | [repo](https://github.com/voonhous/crforge) | P0（待逐文件检查） | 待审 |
| clashback | [repo](https://github.com/ak1NaN/Clashback) | P1（部分源码） | [2026-11-13 审查](clashback-source-2026-11-13.md)；未运行测试 |
| katacr | [repo](https://github.com/wty-yy/KataCR) | P0（待逐文件检查） | 待审 |
| sc-downloader | [repo](https://github.com/Darknighture/sc-downloader-gui) | P0（待逐文件检查） | 待审 |
| itzik-clashenv | [repo](https://github.com/itzik123/ClashRoyaleAi) | P0（待逐文件检查） | 待审 |
| clashai-vegetableleaf | [repo](https://github.com/vegetableleaf/ClashAI) | P0（待逐文件检查） | 待审 |
| crsim-agent-larkindaniel | [repo](https://github.com/larkindaniel/clash-royale-agent) | P0（待逐文件检查） | 待审 |
| build-a-bot | [repo](https://github.com/Pbatch/ClashRoyaleBuildABot) | P0（待逐文件检查） | 待审 |
| sc-extract | [repo](https://github.com/nextonesfaster/sc-extract) | P0（待逐文件检查） | 待审 |
| detection-dataset | [repo](https://github.com/wty-yy/Clash-Royale-Detection-Dataset) | P0（待逐文件检查） | 待审 |
| claude-royale | [repo](https://github.com/houseworthe/claude-royale) | P0（待逐文件检查） | 待审 |
| supercell-csv-decoder | [repo](https://github.com/proydakov/supercell-resource-decoder) | P0（待逐文件检查） | 待审 |
| royaleapi-static-data | [repo](https://github.com/RoyaleAPI/cr-api-data) | P0（待逐文件检查） | 待审 |
| card-tracker | [repo](https://github.com/AmarSaini/Clash-Royale-AI-Card-Tracker) | P0（待逐文件检查） | 待审 |
| native-sandbox-imax9d | [repo](https://github.com/IMAX9D/cr-native-sandbox) | P1（部分源码） | [2026-11-13 原生宿主审查](imax-native-sandbox-source-2026-11-13.md)：环境接口、Worker、版本边界 |
| native-bionic-imax9d | [repo](https://github.com/IMAX9D/cr-native-linux-bionic) | P1（部分源码） | [2026-11-13 审查](native-bionic-imax9d-source-2026-11-13.md)；未运行测试 |
| fl-royale | [repo](https://github.com/Jaasssoooonnnnn/FL-Royale) | P1（部分源码） | [2026-11-13 审查](fl-royale-source-2026-11-13.md)；未运行测试 |
| royaleapi-downloader-imax9d | [repo](https://github.com/IMAX9D/royaleapi-downloader) | P1（部分源码） | [2026-11-13 源码审查](royaleapi-downloader-imax9d-source-2026-11-13.md)；未运行测试 |
| sc-decoder-jason | [repo](https://github.com/Jason-XII/sc-decoder) | P0（待逐文件检查） | 待审 |
| r0-elite-imax9d | [repo](https://github.com/IMAX9D/r0-elite-training) | P0（待逐文件检查） | 待审 |
| cr-collector-arron | [repo](https://github.com/arronwang01/cr-collector) | P0（待逐文件检查） | 待审 |
| clapha-engine | [repo](https://github.com/arronwang01/clapha-engine) | P0（待逐文件检查） | 待审 |
| longling-simulator | [repo](https://github.com/longlingking/clash-royale-simulator) | P0（待逐文件检查） | 待审 |
| royale-bot | [repo](https://github.com/RoyaleGym/RoyaleBot) | P0（待逐文件检查） | 待审 |
| royale-viser | [repo](https://github.com/RoyaleGym/RoyaleViser) | P0（待逐文件检查） | 待审 |
| royale-learn | [repo](https://github.com/RoyaleGym/RoyaleLearn) | P0（待逐文件检查） | 待审 |
| royale-imitate | [repo](https://github.com/RoyaleGym/RoyaleImitate) | P0（待逐文件检查） | 待审 |
| aboufama-research | [repo](https://github.com/aboufama/clash-royale-research) | P0（待逐文件检查） | 待审 |
| crownzero | [repo](https://github.com/anishhchitnis/crownzero) | P0（待逐文件检查） | 待审 |
| clash-royale-pod | [repo](https://github.com/max-miller1204/Clash-Royale-Pod) | P0（待逐文件检查） | 待审 |
| elixir-mcp | [repo](https://github.com/jthingelstad/elixir-mcp) | P0（待逐文件检查） | 待审 |
| elixir-mcp-collector | [repo](https://github.com/jthingelstad/elixir-mcp-collector) | P0（待逐文件检查） | 待审 |
| cr-dataset-browser | [repo](https://github.com/HumaidAlhuthali/clash-royale-dataset-browser) | P0（待逐文件检查） | 待审 |
| sc-fingerprint-rust | [repo](https://github.com/TrixallTR/SC-Fingerprint-Downloader-RUST) | P0（待逐文件检查） | 待审 |
| supercell-asset-decompressor | [repo](https://github.com/abhishek-kumar-14/supercell-asset-decompressor) | P0（待逐文件检查） | 待审 |
| royaleapi-replay-dataset | [repo](https://github.com/Aminiwow/royaleapi-replay-dataset) | P0（待逐文件检查） | 待审 |
| firstlight-zero | [repo](https://github.com/Jaasssoooonnnnn/FirstLight-Zero) | P1（有限文件） | 审计：docs/source-audits/simulator-trial-firstlight-zero-code-2026-11-12.md |
| wty-cr-dataset | [repo](https://github.com/wty-yy/Clash-Royale-Dataset) | P0（待逐文件检查） | 待审 |
| cr-agent-api-docs | [repo](https://github.com/jthingelstad/cr-agent-api-docs) | P0（待逐文件检查） | 待审 |
| elixir-mcp-discord | [repo](https://github.com/jthingelstad/elixir-mcp-discord) | P0（待逐文件检查） | 待审 |
| sc-exportname-extractor | [repo](https://github.com/TrixallTR/SC-ExportName-Extractor) | P0（待逐文件检查） | 待审 |
| cr-new-tilemap | [repo](https://github.com/Darknighture/cr-new-tilemap) | P0（待逐文件检查） | 待审 |
| cr-chest-probability | [repo](https://github.com/Darknighture/cr-chest-probability-calculator) | P0（待逐文件检查） | 待审 |
| royalerating | [repo](https://github.com/RoyaleAPI/royalerating) | P0（待逐文件检查） | 待审 |
| cr-api-assets | [repo](https://github.com/RoyaleAPI/cr-api-assets) | P0（待逐文件检查） | 待审 |

## 注册表外的已发现候选（不可算作已完成项目审计）

- arronwang01/clash-royale-simulator-trial：已检查 preflight.py 及训练/校准记录；有未解决的单位交互和轨迹漂移。见 [限定审查](simulator-trial-firstlight-zero-code-2026-11-12.md)。
- wty-yy/Clash-Royale-Replay-Dataset：无 README，需从文件树/提交记录/数据样本入手。
- RoyaleAPI/cr-api-docs：旧 API 归档，须与现行官方 API 区分。

## 完成标准

逐项目都有可复查的证据链接、实现能力/缺陷/许可结论和明确的未验证项；未通过 P2 的不得标注为“源码审计完成”。项目总体完成需当前 57 项全部逐一达到 P2 或有充分理由判定为纯资源/空仓/文档，并单独注明 P3 运行覆盖范围。

## 维护约束（2026-11-13）

- P0–P3 为审查覆盖进度，与 Implementation 的 R0–R4 复用成熟度完全独立；不做自动换算。
- 项目普查必须追查没有 README 的仓库内部文件；作者仓库枚举、候选筛选与核心代码审计是三个不同完成阶段。
- 每次更新记录实际核查文件、固定提交、测试是否执行、排除原因及未查范围；不得用 P1 代替 P2。
- 完成每批编辑后实际运行仓库校验脚本；未运行或失败必须报告。

## 2026-11-13 本轮续查

- RoyaleGym：检查 README、pyproject.toml、包导出与 env.py 部分实现，新增 [P1 审查记录](royalegym-source-2026-11-13.md)。正式项目总数仍为 58，P1 从 2 项增至 3 项，P2/P3 仍为 0。
- RoyaleSim 的 Cargo.toml 与 Clashback 的 pyproject.toml 在指定路径返回 404；**仅说明该路径不可读取，不表示仓库不存在或无源码**，需继续枚举实际文件树。
- IMAX9D/cr-native-sandbox README 已复核：上游区分旧版 15.535.29 原生宿主与新版 MuMu ARM64 160402002 实验，且训练吞吐数字有采集与完整更新口径差异。仅阅读 README，不提升其 P0 等级。
- 本轮没有运行知识库校验脚本或上游测试；所有结论均为静态检查。

## 2026-11-13 第二轮续查

- [RoyaleGym](royalegym-source-2026-11-13.md)：扩展至 action/replay/rust_engine/state_mutator/protocol 和两份 Rust parity 测试源码，仍 P1，测试未运行。
- [IMAX9D/cr-native-sandbox](imax-native-sandbox-source-2026-11-13.md)：首次检查 env/worker/包配置/技术文档，P0→P1；原生 Android AVD 依赖与无 Surface 的区别明确。
- 当前总账：58 项，**4 项 P1，54 项 P0，0 项 P2/P3**。P1 只是局部审查，不能代表完成。
- 本轮未运行仓库校验脚本和上游测试；尚未冻结完整上游 commit。后续须补齐。

## 2026-11-13 第三轮续查

- [Clashback](clashback-source-2026-11-13.md)：枚举 7600 条 Git tree 条目（其中 6860 个 blob）；抽查原生快照、逐 Tick 缓存和 worker。发现逐 Tick 快照实现；恢复/分支确定性未独立验证。
- [RoyaleSim](royalesim-source-2026-11-13.md)：枚举 679 条 Git tree 条目；Rust 工程入口在 crates/royalesim；抽查 spell.rs 和 hash_continuity.rs。
- [IMAX9D Linux Bionic](native-bionic-imax9d-source-2026-11-13.md)：枚举 18 条 Git tree 条目；抽查 runtime.py 与测试，确认 Android 用户态文件依赖而无需 AVD/KVM。
- 当前总账：58 项，**7 项 P1，51 项 P0，0 项 P2/P3**。以上仅为抽样源码审查；未运行上游测试及知识库校验脚本。

## 2026-11-13 第四轮续查

- [Ashpp Replay](ashpp-replay-source-2026-11-13.md)：实际默认分支为 codex/windows-native-engine-probe，检查 Windows Clashback AVD 适配器、三套 engine profile、分支数据模型。
- [AK Replay Studio](replay-studio-source-2026-11-13.md)：检查 TCP 战斗控制客户端与快照 seek Mock 测试，区分测试设计与实际运行结果。
- 当前总账：58 项，**9 项 P1，49 项 P0，0 项 P2/P3**。未执行测试和仓库校验脚本。

## 2026-11-13 第五轮续查

- [FirstLight_CR](firstlight-cr-source-2026-11-13.md)：操作日志 snapshot 与 ruleset/runner attestation，P0→P1；尚未证明任意状态克隆。
- [FL-Royale](fl-royale-source-2026-11-13.md)：cold clone 诊断代码，P0→P1；根级对象图检查不等于完整别名安全。
- [Jason Python simulator](jason-simulator-source-2026-11-13.md)：独立规则模拟器的实体/伤害/目标源码，P0→P1。
- [Jason memory reader](memory-reader-source-2026-11-13.md)：仅目录和 README，保持 P0。
- Jason-XII/clash-royale-battle-engine 的 GitHub 仓库元信息/默认分支读取异常，未强行认定不存在；需要进一步核实。
- 当前总账：58 项，**12 项 P1，46 项 P0，0 项 P2/P3**。未运行上游测试或知识库校验脚本。

## 2026-11-13 第六轮续查：同仓库重命名去重

- **发现并修复重复登记**：`Jason-XII/clash-royale-battle-engine` 已迁移为 `Jason-XII/daybreak-cr`，GitHub repository ID 均为 `1366867946`；旧 commit 仍可在新仓库访问。注册表保留原 `jason-battle-engine` ID 以保护关联引用，删除重复 `jason-daybreak` 条目；原文档保留为历史别名页。
- [Daybreak 源码审查](jason-daybreak-source-2026-11-13.md)：检查当前 `cr/engine.py`、`cr/live_budget.py`、`tests/test_engine.py` 与 README，P0→P1；未运行测试。当前 main 与历史 `engine.py` 应区分。
- **另发现基础注册表缺陷**：9 个项目引用 `cr-ecosystem`，但 `registry/topics.yaml` 未定义。已补齐专题注册与页面。
- 纠正后总账：**57 项，13 项 P1，44 项 P0，0 项 P2/P3**。先前 58 项口径作历史记录，不追改旧批次日志。
- 尝试通过容器 clone 运行 `scripts/validate.py`，但容器无法解析 github.com，未能运行。仓库已有 push 自动校验工作流；本轮未读取工作流执行结果，不能宣称校验通过。

### 第六轮补充：作者仓库横向普查

- [作者仓库清单与候选分流](author-repository-sweep-2026-11-13.md)：Jason-XII 24、Jaasssoooonnnnn 12、IMAX9D 7、ak1NaN 4 个公开仓库；合计 47 条作者仓库搜索结果（仅四位作者，且可能交叉），对 3c3u-bot、rea、TRACE、DiffuPlan 进一步枚举实际文件树；没有仅凭作者相同就收入 CR 正式注册表。
- 验证风险：`scripts/validate.py` 要求每个注册项目页面有 YAML front matter；抽查 `projects/firstlight-zero.md` 发现没有，说明即使补齐 `cr-ecosystem` 也**不能推定全库校验通过**。待单独系统修复所有基线结构问题并实际执行校验。

## 2026-11-13 第七轮：基线校验修复

- 检查 57 个注册项目的页面，确认其中 **18 个**缺失 YAML front matter（此前预估 19 个，逐项核对后纠正为 18）；已按 `registry/projects.yaml` 添加元数据，原正文保留。新增元数据中的 `status: research` 表示当前审查阶段，不提升任何证据等级。
- 修复 `royalefish` 的专题元数据和反向引用，保留原先的 `source-inspected` 等级；修复历史别名页面 `jason-daybreak.md` 的错误相对链接。
- 根据实际 `scripts/validate.py` 检查规则，补齐六个专题的项目反向引用，并同步六份专题页 front matter。
- **首次实际读取 GitHub Actions 校验日志**：在修复过程中，从 18 项错误逐步降至 3 项（最后三项为尚未同步的专题页）；所有六个专题页现已同步。最新 push 的自动工作流结果待确认，不能提前宣称通过。
- 审查状态不变：57 项，13 项 P1、44 项 P0、0 项 P2/P3。以上为知识库结构修复，不代表上游源码审查等级提升。

## 2026-11-13 第八轮续查

- [Jason memory reader](memory-reader-source-2026-11-13.md)：Frida Hook、下牌事件、root ADB 进程内存读取，P0→P1。
- [AK Tencent Overlay](tencent-overlay-source-2026-11-13.md)：原生圣水/队列 Hook 与身份区分，P0→P1。
- [AK Tencent Model Harness](tencent-model-harness-source-2026-11-13.md)：partial/complete 状态隔离、输入完整性、动作时效及测试代码，P0→P1。
- [IMAX9D RoyaleAPI Downloader](royaleapi-downloader-imax9d-source-2026-11-13.md)：离线回放 schema 与 native contract 校验、队列恢复测试代码，P0→P1。
- 本轮还枚举 [Jason sc-decoder](https://github.com/Jason-XII/sc-decoder) 830 条目录项并读取 README；未检查实际解码源码，**保持 P0**。
- 当前审查总账：**57 项，17 项 P1，40 项 P0，0 项 P2/P3**。未运行上游测试，仍需固定上游完整 commit。
