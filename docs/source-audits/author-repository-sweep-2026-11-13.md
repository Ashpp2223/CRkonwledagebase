# 重点作者仓库横向枚举（2026-11-13）

目的：按作者搜索所有公开仓库，不以项目名称是否含 Clash Royale 作为初筛排除条件。**仅完成仓库清单和部分文件树抽样**，尚未逐仓源码审查；不自动入正式项目注册表。

| 作者 | 搜索到的公开仓库数 | 已登记皇室战争项目 | 本轮新注意项 |
| --- | ---: | --- | --- |
| [Jason-XII](https://github.com/Jason-XII?tab=repositories) | 24 | daybreak-cr（旧名 clash-royale-battle-engine）、clash-royale-simulator、cr-memory-reader、sc-decoder | [3c3u-bot](https://github.com/Jason-XII/3c3u-bot) |
| [Jaasssoooonnnnn](https://github.com/Jaasssoooonnnnn?tab=repositories) | 12 | FirstLight_CR、FirstLight-Zero、FL-Royale | [rea](https://github.com/Jaasssoooonnnnn/rea)、[TRACE](https://github.com/Jaasssoooonnnnn/TRACE)、[DiffuPlan](https://github.com/Jaasssoooonnnnn/DiffuPlan) |
| [IMAX9D](https://github.com/IMAX9D?tab=repositories) | 7 | cr-native-sandbox、cr-native-linux-bionic、royaleapi-downloader、r0-elite-training | 另有 Minecraft/启动器工具，未发现明显皇室战争直接关联 |
| [ak1NaN](https://github.com/ak1NaN?tab=repositories) | 4 | Clashback、ClashRoyale-replay-studio、ClashRoyale-tencent-overlay、ClashRoyale-tencent-model-harness | 当前公开仓库四项均已登记 |

## 非显名仓库的实际文件树检查

- Jason-XII/3c3u-bot：tree `869928445da07796ae689e49884796c195b46ed2`，15 条；含 `bot.py`、`telemetry_parser.py`、`stream_processor.py`，仓库描述为 3c3u 聊天/敌对玩家监控；**暂未发现皇室战争直接关联**，不入库。
- Jaasssoooonnnnn/rea：tree `fe297e56e804130dd49cc0a95fcf2d115c183ae3`，2379 条；通用逆向代理框架，含大量真实二进制/浏览器测试工作流；可列为**跨项目研究方法候选**，但未证实 CR 专用功能。
- Jaasssoooonnnnn/TRACE：tree `77509554ee3b5184f84c7599189e3cd27fdd2f9e`，39 条；轨迹选择与搜索智能体，含训练、评估、测试代码；可研究 AI 方法迁移，未发现 CR 专用实现。
- Jaasssoooonnnnn/DiffuPlan：tree `251d30e34fb43aeb2fd2a17caba97742e10cfdd6`，404 条；扩散语言模型智能体可编辑规划状态；未发现 CR 专用实现。

## 待续查

对其余作者重复全仓库枚举；对上述候选读取关键源码与引用链，只有发现明确的 CR 关联或直接复用价值后才登记。作者公开仓库数量为本次搜索快照，不能当作永久不变的总数。


## 2026-11-13 补扫：新增 10 位作者全量公开仓库枚举

通过 GitHub `user:<owner>` 仓库搜索（每位最多 100 条；本批均不足 100），逐一读取全部公开仓库名称，优先对模糊命名的仓库进一步打开目录树。本批覆盖：

| 作者 | 搜索返回公开仓库数 | 新发现与处理 |
|---|---:|---|
| hastylmao | 3 | Hasty-CR 已登记；SwiftLog 和 swiftlogger-legal 未发现 CR 指向 |
| fabiospalla9-tech | 2 | RoyaleFish 已登记；Limitless 需按源码语义再判断 |
| voonhous | 9 | crforge 已登记；其余主要是 Flink/Hudi/Trino 数据基础设施 |
| wty-yy | 56 | **新发现 Clash-Royale-Replay-Dataset**（master，349 tree entries，全部为 .npy.xz 压缩二进制，目录 fast_hog_2.6/golem_ai）；KataCR 与两个检测数据集已登记；KataBot 为机器人仿真（已检查目录），其余需二次关键词/源码核查 |
| Darknighture | 5 | SC Downloader、Chest Probability、New Tilemap 已登记；另两项尚无明确 CR 证据 |
| itzik123 | 3 | ClashRoyaleAi 已登记；其他为 PaletteAtlas、JavaRayTracer |
| vegetableleaf | 7 | ClashAI 已登记；**KataCR 和 cr-memory-reader** 亦公开，已打开树，可能与 wty-yy/KataCR、Jason-XII/cr-memory-reader 是关联副本，待比较 git 身份与提交；不得仅按同名合并 |
| larkindaniel | 16 | clash-royale-agent 已登记；其余如 EndGame、ranked、scout 需继续查看源码排除隐性 CR 项目 |
| Pbatch | 17 | ClashRoyaleBuildABot 已登记；其余以 ChessCam/ChessCamResearch 等视觉项目为主，未确认 CR 专项 |
| nextonesfaster | 18 | sc-extract 已登记；lzham 为潜在 Supercell 资源解压底层依赖，需检查实现与具体格式关系 |

### 重要新增候选

- [wty-yy/Clash-Royale-Replay-Dataset](https://github.com/wty-yy/Clash-Royale-Replay-Dataset)：master 分支含 349 tree entries，顶层 `fast_hog_2.6/` 与 `golem_ai/`，均为 `.npy.xz`。**没有 README 或直接可读的 schema**。先列为“待收录数据资产候选”，不擅自宣称标签、时间戳或动作格式；需检查样本元数据、来源、版权与训练/测试划分后决定登记。此仓库名称明确相关，优先补录。
- [vegetableleaf/KataCR](https://github.com/vegetableleaf/KataCR)、[vegetableleaf/cr-memory-reader](https://github.com/vegetableleaf/cr-memory-reader)：检查 GitHub repo ID、fork parent、tree SHA、源代码与已登记同名项目的关系，必要时作为来源镜像/派生项目独立登记。

**进度口径**：本批新增枚举 10 位作者；此前已完成 Jason-XII、Jaasssoooonnnnn、IMAX9D、ak1NaN 四位。登记表提取出 30 位不同 owner，仍有 16 位待完整枚举。枚举不等于逐仓完整源码审查。


### 关联仓库身份已核实

- `vegetableleaf/KataCR`：GitHub repo ID `1328413445`，`fork: true`，parent **`wty-yy/KataCR`**（ID `701588460`）。
- `vegetableleaf/cr-memory-reader`：GitHub repo ID `1327819989`，`fork: true`，parent **`Jason-XII/cr-memory-reader`**（ID `1314885072`）。
- 两项均为**不同 repo ID 的 fork**，不能作为原仓库别名或重复计数消失；应作为衍生来源建立关系，后续 diff 判断是否存在独立功能。


## 2026-11-13 补扫：剩余 16 位作者公开仓库枚举完成

通过 GitHub `user:<owner>` 搜索逐一枚举，每位最多 100 条，当前返回数均小于 100。**至此 registry/projects.yaml 提取的 30 位不同 owner 已全部完成公开仓库名称枚举**；这不代表每个仓库已完成源码审查。

| 作者 | 搜索返回数 | 发现与后续 |
|---|---:|---|
| Ashpp2223 | 18 | **ClashRoyale**（fork retroroyale/ClashRoyale，C# 服务端/战斗代码）、**Clash-Royale-v1-Client-Leak**（fork clashRoyaleClients 原始客户端 C++）、FirstLight_CR、royaleapi-downloader、clash-royale-simulator、cr-memory-reader、clash-royale-battle-engine 等未全部作为独立来源记录；优先确认 fork 关系、差异与版权边界 |
| RoyaleGym | 7 | RoyaleGym/RoyaleLearn/RoyaleSim/RoyaleBot/RoyaleViser/RoyaleImitate 均已登记；另 .github |
| RoyaleAPI | 8 | cr-api、cr-api-assets、cr-api-data、cr-api-docs、royalerating 等已登记，family-config/cr-api-ux/brand 待查数据价值 |
| AmarSaini | 27 | Card Tracker 已登记，其他以 ML/课程项目为主 |
| arronwang01 | 8 | **clash-royale-simulator-trial**（独立仓库，160 tree entries，含 Python 战斗模拟与 calibration 文档）；**clash-royale-battle-engine**（fork Jason-XII/daybreak-cr）；**clash-ai-releases**（仅 README）；cr-collector 已登记。原 clapha-engine 仍需确认是否改名 |
| longlingking | 6 | clash-royale-simulator 已登记，其余未见明确 CR 专项 |
| aboufama | 40 | clash-royale-research 已登记；clash-game 目录 42593 entries，但描述是 **Clash of Clans 风格** Web 游戏，不能仅按 clash 名称当成皇室战争项目 |
| anishhchitnis | 6 | crownzero 已登记，其余未见明确 CR 专项 |
| max-miller1204 | 62 | Clash-Royale-Pod 已登记；**KataCR** 为 fork wty-yy/KataCR（GitHub repo ID 1170276082），后续比较 diff |
| jthingelstad | 49 | elixir-mcp、elixir-mcp-collector、elixir-mcp-discord、cr-agent-api-docs 已登记；**elixir-bot**（612 tree entries）明确服务 POAP KINGS Clash Royale 公会，含事件驱动 Discord agent，建议补录 |
| HumaidAlhuthali | 1 | Dataset Browser 已登记 |
| TrixallTR | 3 | 两个 SC 工具已登记；**SC-Server** Rust packet reader/writer（10 tree entries），需核查 Supercell 通信协议相关性和版本 |
| abhishek-kumar-14 | 8 | supercell-asset-decompressor 已登记；**coc-asset-mapping**、**coc-memory-identifier-scanner** 为 Clash of Clans 关联工具，跨游戏技术可参考但需独立标签 |
| Aminiwow | 3 | royaleapi-replay-dataset 已登记 |
| proydakov | 46 | supercell-resource-decoder 已登记，其余主要通用 C++/Rust/Android 工具 |
| houseworthe | 9 | claude-royale 已登记，其余多为通用 agent/MCP/素材项目 |

### 本批新增明确候选与来源身份

1. [arronwang01/clash-royale-simulator-trial](https://github.com/arronwang01/clash-royale-simulator-trial)：独立仓库，Python 战斗模拟器，含 `MECHANIC_AUDIT.md`、`CALIBRATION_PLAYBOOK.md` 和 `src/clasher_new/battle.py`，待与 Jason-XII simulator 的实现/来源比较。
2. [arronwang01/clash-royale-battle-engine](https://github.com/arronwang01/clash-royale-battle-engine)：GitHub repo ID `1414417845`，`fork: true`，parent `Jason-XII/daybreak-cr`；独立 fork，不能误判为原仓库改名。
3. [jthingelstad/elixir-bot](https://github.com/jthingelstad/elixir-bot)：独立仓库，明确服务 Clash Royale 公会，事件驱动自动化。
4. [Ashpp2223/ClashRoyale](https://github.com/Ashpp2223/ClashRoyale)：GitHub repo ID `1218071653`，fork parent `retroroyale/ClashRoyale`，包含 C# battle/server 项目。
5. [Ashpp2223/Clash-Royale-v1-Client-Leak](https://github.com/Ashpp2223/Clash-Royale-v1-Client-Leak)：GitHub repo ID `1305406867`，fork parent `clashRoyaleClients/Clash-Royale-v1-Client-Leak`；存在原版客户端版权/再分发风险，知识库宜仅保存元数据与研究结论。
6. [TrixallTR/SC-Server](https://github.com/TrixallTR/SC-Server)：Rust Supercell packet reader/writer，待检查具体游戏协议适用性。

**覆盖口径：30/30 位 owner 已枚举；已发现新候选，但本轮尚未将候选全部加入 57 项正式登记表。** 后续按源码价值、独立性与授权边界逐项收录。
