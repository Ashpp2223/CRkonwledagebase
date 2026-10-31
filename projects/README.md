# 项目来源目录

这里记录**来源归属**，不是中台的首要查询入口。要找技术方案请先访问 [共享能力目录](../capabilities/README.md)；项目与能力的实际关联以 [实现矩阵](../registry/implementations.yaml) 为准。

| 项目 | 上游 |
| --- | --- |
| [FirstLight CR](firstlight-cr.md) | [Jaasssoooonnnnn/FirstLight_CR](https://github.com/Jaasssoooonnnnn/FirstLight_CR) |
| [Jason Clash Royale Battle Engine](jason-battle-engine.md) | [Jason-XII/clash-royale-battle-engine](https://github.com/Jason-XII/clash-royale-battle-engine) |
| [Jason Clash Royale Simulator](jason-simulator.md) | [Jason-XII/clash-royale-simulator](https://github.com/Jason-XII/clash-royale-simulator) |
| [Clash Royale Replay Studio](replay-studio.md) | [ak1NaN/ClashRoyale-replay-studio](https://github.com/ak1NaN/ClashRoyale-replay-studio) |
| [皇室战争复盘器](ashpp-replay.md) | [Ashpp2223/clashroyalereplay](https://github.com/Ashpp2223/clashroyalereplay) |
| [CR Memory Reader](memory-reader.md) | [Jason-XII/cr-memory-reader](https://github.com/Jason-XII/cr-memory-reader) |
| [Tencent Overlay](tencent-overlay.md) | [ak1NaN/ClashRoyale-tencent-overlay](https://github.com/ak1NaN/ClashRoyale-tencent-overlay) |
| [Tencent Model Harness](tencent-model-harness.md) | [ak1NaN/ClashRoyale-tencent-model-harness](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness) |
| [Hasty-CR](hasty-cr.md) | [hastylmao/Hasty-CR](https://github.com/hastylmao/Hasty-CR) |
| [RoyaleGym](royalegym.md) | [RoyaleGym/RoyaleGym](https://github.com/RoyaleGym/RoyaleGym) |
| [RoyaleSim](royalesim.md) | [RoyaleGym/RoyaleSim](https://github.com/RoyaleGym/RoyaleSim) |
| [crforge](crforge.md) | [voonhous/crforge](https://github.com/voonhous/crforge) |
| [KataCR](katacr.md) | [wty-yy/KataCR](https://github.com/wty-yy/KataCR) |
| [SC Downloader GUI](sc-downloader.md) | [Darknighture/sc-downloader-gui](https://github.com/Darknighture/sc-downloader-gui) |

[其他待深入的项目](additional-projects.md) 暂列为扩展线索。这里按**一个外部 GitHub 仓库一个项目 ID** 建档，原 `tencent-tools` 聚合页仅作为迁移说明。

## 本次生态扩展项目索引

| 项目 | 主要可衍生技术 |
| --- | --- |
| [ClashRoyaleEnv](itzik-clashenv.md) | 独立状态分叉、规划、AI 训练 |
| [ClashAI](clashai-vegetableleaf.md) | 真实回放/公开观测/IL→RL |
| [CRSim Agent](crsim-agent-larkindaniel.md) | 受控实验和可验证模拟器 |
| [BuildABot](build-a-bot.md) | 屏幕状态解析 |
| [sc_extract](sc-extract.md) | Rust SC/CSV 资源解析 |
| [Detection Dataset](detection-dataset.md) | CV 合成训练样本 |
| [Claude Royale](claude-royale.md) | Agent 调度与延迟管理 |
| [Supercell CSV Decoder](supercell-csv-decoder.md) | 历史 CSV 解码 |
| [RoyaleAPI Static Data](royaleapi-static-data.md) | 数据常量归档 |
| [AI Card Tracker](card-tracker.md) | 历史对手卡序视觉估计 |

完整收录逻辑和低优先级项目见 [GitHub 技术生态调查](../landscape/2026-10-13-landscape.md)。

## 2026-10-15 作者仓库和 Fork 来源网络

| 新收录来源 | 为什么值得研究 |
| --- | --- |
| [CR Native Sandbox](native-sandbox-imax9d.md) | 原版 x86_64 libg 无画面战斗服务、Replay 驱动 |
| [CR Native Linux Bionic](native-bionic-imax9d.md) | Linux 无 AVD/KVM 的原生 Worker 宿主 |
| [FL Royale](fl-royale.md) | Android 离线原生可玩客户端和画面壳 |
| [RoyaleAPI Downloader](royaleapi-downloader-imax9d.md) | 回放采集、历史批次、去重和断点恢复 |
| [R0 Elite Training](r0-elite-imax9d.md) | 原生采集→数据契约→训练验收 |
| [Jason SC Decoder](sc-decoder-jason.md) | SC 动画解码及可视化 |
| [Arron CR Collector](cr-collector-arron.md) | 公开回放协作采集 |

[作者/Fork/依赖追踪与不纳入理由](../landscape/2026-10-15-source-network.md)

## 2026-10-15 开发者网络发现

| 项目 | 关键能力 |
| --- | --- |
| [CR Native Sandbox](cr-native-sandbox.md) | 原生 15.535.29 x86_64 无画面 reset/step / replay |
| [CR Native Linux Bionic](cr-native-linux-bionic.md) | 无 AVD/KVM 直接部署原生 Worker |
| [Clapha Engine（私有）](clapha-engine.md) | Jason 公布的 Linux x86_64 进程内原生控制封装，loader 不可审 |
| [R0 Elite Training](r0-elite-training.md) | 数据契约、原生样本编译、TBPTT 模仿训练验证 |
| [RoyaleAPI Downloader](royaleapi-downloader.md) | 对局事件持久采集、队列去重和采集校验 |
| [Arron CR Collector](cr-collector.md) | 分布式志愿者采集/协调（注意网站使用条款） |

开发者与明确 Fork 关系及未收录原因见 [网络调查](../landscape/2026-10-15-developer-network.md)。

## 2026-10-15 正式收录：世界模型、自博弈与 RoyaleGym 配套组件

| 新项目 | 具体价值 |
| --- | --- |
| [Longling Simulator × R2-Dreamer](longling-simulator.md) | Jason Fork 的 Dreamer 桥接、55 维动作、自博弈池；部分接口 R2 |
| [RoyaleLearn](royale-learn.md) | RoyaleGym 的独立训练器 |
| [RoyaleImitate](royale-imitate.md) | 教师权重、warm start、模仿约束 |
| [RoyaleViser](royale-viser.md) | .msgpack / 实时模拟轨迹查看 |
| [RoyaleBot](royale-bot.md) | 限定 Null's Royale 客户端的模型部署 |

[新发现及去重依据](../research/knowledge-notes/cr-model-selfplay-client-parity-2026-10-15.md) · [项目/能力注册表](../registry/implementations.yaml)

## 2026-10-31 上游复查（不新增 Project ID）

| 既有项目 | 新的版本/文档证据 |
| --- | --- |
| [皇室战争复盘器](ashpp-replay.md) | 国服 38.4.5 / 0.4.1 双引擎版本身份及恢复验收 |
| [RoyaleSim](royalesim.md) | 0.1.42 校准差异；可选 2026-10-19 卡表 |
| [RoyaleLearn](royale-learn.md) | 0.5.20 观测编码诊断与 float16 配置 |
| [RoyaleGym](royalegym.md) | FAQ 文档入口与独立模块职责复核 |

以上改动更新的是**已有项目的来源档案**，不产生新的项目—能力实现关联，也不将作者验收改写为中台独立实测。
