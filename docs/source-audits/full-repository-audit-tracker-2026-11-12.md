# 全库源码普查总账（2026-11-12 启动）

范围：注册表 58 个独立 GitHub 项目；本表按**项目**而非作者计数。此表的“源码已读”只表示此前存在可追溯的部分文件检查，不代表全项目审计完成。

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
| firstlight-cr | [repo](https://github.com/Jaasssoooonnnnn/FirstLight_CR) | P0（待逐文件检查） | 待审 |
| jason-battle-engine | [repo](https://github.com/Jason-XII/clash-royale-battle-engine) | P0（待逐文件检查） | 待审 |
| jason-simulator | [repo](https://github.com/Jason-XII/clash-royale-simulator) | P0（待逐文件检查） | 待审 |
| replay-studio | [repo](https://github.com/ak1NaN/ClashRoyale-replay-studio) | P0（待逐文件检查） | 待审 |
| ashpp-replay | [repo](https://github.com/Ashpp2223/clashroyalereplay) | P0（待逐文件检查） | 待审 |
| memory-reader | [repo](https://github.com/Jason-XII/cr-memory-reader) | P0（待逐文件检查） | 待审 |
| tencent-overlay | [repo](https://github.com/ak1NaN/ClashRoyale-tencent-overlay) | P0（待逐文件检查） | 待审 |
| tencent-model-harness | [repo](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness) | P0（待逐文件检查） | 待审 |
| hasty-cr | [repo](https://github.com/hastylmao/Hasty-CR) | P0（待逐文件检查） | 待审 |
| royalefish | [repo](https://github.com/fabiospalla9-tech/RoyaleFish) | P1（有限文件） | 既有审计：docs/source-audits/royalefish-2026-11-12.md |
| royalegym | [repo](https://github.com/RoyaleGym/RoyaleGym) | P0（待逐文件检查） | 待审 |
| royalesim | [repo](https://github.com/RoyaleGym/RoyaleSim) | P0（待逐文件检查） | 待审 |
| crforge | [repo](https://github.com/voonhous/crforge) | P0（待逐文件检查） | 待审 |
| clashback | [repo](https://github.com/ak1NaN/Clashback) | P0（待逐文件检查） | 待审 |
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
| native-sandbox-imax9d | [repo](https://github.com/IMAX9D/cr-native-sandbox) | P0（待逐文件检查） | 待审 |
| native-bionic-imax9d | [repo](https://github.com/IMAX9D/cr-native-linux-bionic) | P0（待逐文件检查） | 待审 |
| fl-royale | [repo](https://github.com/Jaasssoooonnnnn/FL-Royale) | P0（待逐文件检查） | 待审 |
| royaleapi-downloader-imax9d | [repo](https://github.com/IMAX9D/royaleapi-downloader) | P0（待逐文件检查） | 待审 |
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
| jason-daybreak | [repo](https://github.com/Jason-XII/daybreak-cr) | P0（待逐文件检查） | 待审 |
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

逐项目都有可复查的证据链接、实现能力/缺陷/许可结论和明确的未验证项；未通过 P2 的不得标注为“源码审计完成”。项目总体完成需 58 项全部逐一达到 P2 或有充分理由判定为纯资源/空仓/文档，并单独注明 P3 运行覆盖范围。

## 维护约束（2026-11-13）

- P0–P3 为审查覆盖进度，与 Implementation 的 R0–R4 复用成熟度完全独立；不做自动换算。
- 项目普查必须追查没有 README 的仓库内部文件；作者仓库枚举、候选筛选与核心代码审计是三个不同完成阶段。
- 每次更新记录实际核查文件、固定提交、测试是否执行、排除原因及未查范围；不得用 P1 代替 P2。
- 完成每批编辑后实际运行仓库校验脚本；未运行或失败必须报告。
