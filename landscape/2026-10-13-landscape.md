# 2026-10-13 皇室战争 GitHub 技术生态与衍生能力筛选

> **调查范围**：以 Darknighture、Jaasssoooonnnnn、ak1NaN、Jason-XII、clashRoyaleClients 等账号为起点，对 GitHub 公开仓库进行关键词扩展，覆盖原生战斗、独立模拟、训练、感知、回放、资源和数据服务。**这不是 GitHub 全部仓库的穷尽清单**；只收录能确认仓库存在或有明确公开研究线索的条目。扫描当天的公开状态可能随上游更新。每项具体实现以来源链接与固定版本为准。

## 什么是“衍生战斗力”

评价的是**下一位开发者能用现有成果创造什么**，而不是 Star 或 README 宣称的战斗胜率：

1. **基础设施杠杆**：能否被多个项目用作底层模块（例如可重复的引擎、快照、结构化观测）。
2. **组合潜力**：能否把 A 的输出作为 B 的输入，组成可追踪的下一代工具。
3. **可验证性**：是否有代码入口、测试、反例与可复现基准；是否区分历史数据与当前规则。
4. **适配成本**：游戏构建、CPU/系统、模拟器、私有资源、显卡及版本耦合程度。
5. **权利边界**：代码许可、第三方游戏素材、回放权属、模型与客户端行为能否合法使用。

评级：**A**＝优先进入能力中台并准备验证；**B**＝有明确专业知识或场景，作为配套能力；**C**＝历史/存疑/范围有限，只放研究索引。**A 不是 R3 可集成**：A/B/C 是编目优先级，R0–R4 才是具体“项目×能力”的复用成熟度。

## A 级：高衍生能力 / 主干技术

| 仓库 | 值得复用的“具体资产” | 最大衍生方向 | 主要边界 |
| --- | --- | --- | --- |
| [FirstLight CR](https://github.com/Jaasssoooonnnnn/FirstLight_CR) | 原生战斗 `BattleEnvV1` / `NativeClashEnv`、快照、FAIR 观测、训练数据 | 原生复盘、离线 AI 训练、规则实验基准 | APK/资源/ARM64、原生句柄生命周期 |
| [Jason Battle Engine](https://github.com/Jason-XII/clash-royale-battle-engine) | 极简 `Engine`/ `State`、分离的原生探针通信 | 低接入门槛的引擎调用、自动化测试 | 上游依赖/游戏构建与许可需核查 |
| [ClashRoyaleEnv](https://github.com/itzik123/ClashRoyaleAi) | C++ 深拷贝快照、Python 绑定、search teacher、PPO、WASM 示例 | 任意局面分支、前瞻搜索、策略蒸馏、交互教学 | **重写模拟**不等于原生精确；运行结果是作者报告 |
| [RoyaleSim](https://github.com/RoyaleGym/RoyaleSim) | Rust 逻辑引擎、`save/load`、状态哈希、API 和版本校准 | 状态复盘、仿真测试、训练后端 | 逐 tick 保真度需逐机制检验 |
| [RoyaleGym](https://github.com/RoyaleGym/RoyaleGym) | Gymnasium/PettingZoo 包装、训练示例、可见信息/作弊信息分离 | 多种策略算法与统一仿真入口 | 必须绑定 RoyaleSim 版本和观测 schema |
| [Hasty-CR](https://github.com/hastylmao/Hasty-CR) | 行为级测试、已知 `xfail`、校准日志、完整训练流程 | 机制回归、原生差分、反例驱动开发 | README 显示仍有碰撞与冲锋缺陷 |
| [ClashAI](https://github.com/vegetableleaf/ClashAI) | 真人回放重驱、公开观测、IL→RL、分组对比、部署门禁 | 模型训练数据工厂、统一感知/策略版本链 | 权属/客户端依赖及实验结果需复核 |
| [crforge](https://github.com/voonhous/crforge) | Java ECS、JSON 卡牌、ZMQ-Gym 桥接、调试渲染 | 自定义机制、卡牌数据驱动、混合语言训练 | 完整度/数值并不保证原生一致 |
| [KataCR](https://github.com/wty-yy/KataCR) | 目标检测/OCR、数据生成、视觉感知管线 | 视频回放理解、纯视觉 AI 与标注工具 | 历史视觉版本与模型生态 |
| [CR Memory Reader](https://github.com/Jason-XII/cr-memory-reader) | 状态与内存研究记录、对象/手牌/圣水映射 | 观测解析、版本变更追踪 | 偏移和结构依赖特定客户端 |
| [Replay Studio](https://github.com/ak1NaN/ClashRoyale-replay-studio) | HTML 事件解析、逐 tick 预演算与时间轴 | 真人对局审阅、模拟版本对照、分析 UI | 缺原始 RNG/隐藏初手，可能只得相容重建 |
| [Ashpp 复盘器](https://github.com/Ashpp2223/clashroyalereplay) | 节点树、原生进程内快照、动作日志续放、摘要校验 | 假设分叉、战术研究、可重复交互实验 | 快照不能跨进程保留；产品内部接口 |

**理由**：这些项目中至少有一个清晰的、可为其他用途组合的技术子系统，而非只是一份成品演示。核心条目的实际接口见 [能力实现矩阵](../registry/implementations.yaml)。

## B 级：支撑、专用场景与研究方法

| 仓库 | 独特技术资产 | 收录位置/处理方式 |
| --- | --- | --- |
| [CRSim Agent](https://github.com/larkindaniel/clash-royale-agent) | 冻结八卡规则；PPO 训练重现；信息泄漏负向测试 | [项目卡](../projects/crsim-agent-larkindaniel.md)；优先复用方法 |
| [ClashRoyaleBuildABot](https://github.com/Pbatch/ClashRoyaleBuildABot) | 屏幕状态识别与策略动作分层 | [项目卡](../projects/build-a-bot.md)；视觉输入方案 |
| [CR Detection Dataset](https://github.com/wty-yy/Clash-Royale-Detection-Dataset) | 切片合成目标检测训练数据 | [项目卡](../projects/detection-dataset.md)，勿镜像素材 |
| [Claude Royale](https://github.com/houseworthe/claude-royale) | UI 生命周期、指挥/执行 Agent、延迟管理 | [项目卡](../projects/claude-royale.md)，运维模式参考 |
| [Tencent Model Harness](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness) | 原生观测→FirstLight 张量→执行回执 | [项目卡](../projects/tencent-model-harness.md)，版本绑定 |
| [Tencent Overlay](https://github.com/ak1NaN/ClashRoyale-tencent-overlay) | 腾讯客户端部署队列可视化 | [项目卡](../projects/tencent-overlay.md)，旧偏移已失效 |
| [SC Downloader GUI](https://github.com/Darknighture/sc-downloader-gui) | 指纹驱动资源下载、断点补齐/可选解码 | [项目卡](../projects/sc-downloader.md) |
| [sc_extract](https://github.com/nextonesfaster/sc-extract) | Rust SC/纹理/CSV 解析、跨平台 CLI | [项目卡](../projects/sc-extract.md)，资源可观察性 |
| [Supercell Resource Decoder](https://github.com/proydakov/supercell-resource-decoder) | Python CSV 旧格式解码/实验编码 | [项目卡](../projects/supercell-csv-decoder.md) |
| [RoyaleAPI Static Data](https://github.com/RoyaleAPI/cr-api-data) | 第三方卡牌 JSON 与常量 | [项目卡](../projects/royaleapi-static-data.md) |
| [AI Card Tracker](https://github.com/AmarSaini/Clash-Royale-AI-Card-Tracker) | 早期双 CNN 的卡序/圣水预测 | [项目卡](../projects/card-tracker.md)，历史思路 |
| [FL-Royale](https://github.com/Jaasssoooonnnnn/FL-Royale) | 原生对局与推理封装为离线 Android 产品 | 继续调查，上游 APK/授权边界 |
| [SC Decoder](https://github.com/Jason-XII/sc-decoder) | SC 动画资源解析/预览 | [扩展项目目录](../projects/additional-projects.md) |
| [cr-new-tilemap](https://github.com/Darknighture/cr-new-tilemap) | CSV 地图/网格 PDF 转换 | Fork 来源记为 smlbiobot/cr-tilemap |
| [cr-chest-probability-calculator](https://github.com/Darknighture/cr-chest-probability-calculator) | 宝箱数值概率分析 | 不属于战斗主干；进入数据研究线索 |
| [RoyaleAPI Assets](https://github.com/RoyaleAPI/cr-api-assets) | UI/卡图参考素材目录 | 只引用，不复制专有素材 |
| [Clash-Royale-Replay-Dataset](https://github.com/wty-yy/Clash-Royale-Replay-Dataset) | 离线 RL 回放数据方向 | 暂无可解析 README，须核实格式/授权 |
| [Pbatch 之外的视觉链](https://github.com/HummingNerd/Clash_Royale_Enemy_Card_Tracker) | 视觉卡牌追踪专用实现 | 有仓库但缺完整独立评估，待调查 |
| [Royale API official wrapper](https://github.com/AndreVarandas/clash-royale-api) | 官方 API 包装与玩家统计 | 可为外部统计/卡牌分析服务，不提供战斗 Tick 控制 |
| [ClashRoyaleBuildABot 相关简易实现](https://github.com/AngelFireLA/Clash-Royale-AI) | 视觉到行动的不同接口原型 | 与主干视觉系统比较，尚不进入正式能力矩阵 |

## C 级：历史参照、同源 Fork 或目前不建议纳入核心

| 仓库/来源 | 原因 | 处理 |
| --- | --- | --- |
| [RoyaleAPI/cr-api](https://github.com/RoyaleAPI/cr-api) | **已归档**；旧 API 不再公开维护，应使用官方 API | 历史 API 资料，不作为当前接口 |
| [martincarrera/clash-royale-api](https://github.com/martincarrera/clash-royale-api) | 已归档的旧 API 服务 | 不纳入实时数据接口 |
| [MSU-AI/clash-royale-gym](https://github.com/MSU-AI/clash-royale-gym) | README 版本历史承认初版为 mock API、示例可能过期 | 可作为旧版接口设计参考，非当前训练底座 |
| [Ofredy/Clash-Royale-RL-Bot](https://github.com/Ofredy/Clash-Royale-RL-Bot) | Fork 且 README 自称过期 | 不采纳其性能主张，另核原始项目 |
| [NymphCore/sc-extract](https://github.com/NymphCore/sc-extract) | 与后来维护的 sc_extract 技术谱系有重叠 | 保留原作者/派生线索，优先审阅最新维护版本 |
| [ThalesGitHubUser/SC-CSV-Decoder](https://github.com/ThalesGitHubUser/SC-CSV-Decoder) | Fork 早期 Python decoder | 优先索引 [上游](https://github.com/proydakov/supercell-resource-decoder) |
| [smlbiobot/cr](https://github.com/smlbiobot/cr) | 历史 APK 数据挖掘，年代较早 | 不用作当前客户端基准 |
| [royale-proxy/cr-messages](https://github.com/royale-proxy/cr-messages) | 旧版通信协议字典，非战斗引擎 | 只保留历史协议知识 |
| [SpringFsm/CR-reverse-engineering](https://github.com/SpringFsm/CR-reverse-engineering) | Unity 玩法重写的教学/研究性质 | 难以替代更成熟的原生/模拟器路径 |
| [clashRoyaleClients/V1 Client Leak](https://github.com/clashRoyaleClients/Clash-Royale-v1-Client-Leak) | 仓库自称泄露源码，来源/权利存在重大疑问 | **不复制、不衍生、不纳入技术实现库** |
| [arronwang01/clapha-engine](https://github.com/arronwang01/clapha-engine) | 被 Jason 等上游 README 作为依赖引用，但当前 GitHub 查询返回 **404/无法访问** | 仅保存未核实外部依赖，不能假装已审计 |
| [Galaxy1036/SC-Assets-Downloader-GUI](https://github.com/Galaxy1036/SC-Assets-Downloader-GUI) | 公开资源下载工具，需与已有 Downloader 比较实际差异 | 暂不重复登记等价能力 |
| [Ofredy 系、HuggingFace 权重/数据镜像](https://github.com/Ofredy/Clash-Royale-RL-Bot) | 可访问性、文件来源与授权未核验 | 不镜像二进制权重/回放原件 |

另有大量纯游戏 UI 克隆、收藏/卡组营销应用、无独立说明的短期 Fork、专有资源打包以及与皇室战争战斗机制无关的同名项目，未作为中台主干收录。**此筛选不代表它们全部无价值，只代表目前缺乏足以优先复用的证据。**

## 四条高价值组合路线

1. **原生事实 → 快速模拟 → 搜索决策**：FirstLight/Jason 原生引擎提供机制参照；Hasty/RoyaleSim/ClashRoyaleEnv 提供可改写/可复制引擎；ClashRoyaleEnv 的 lookahead teacher 可作为策略搜索案例。**风险**：模拟误差进入搜索会被放大。
2. **真人回放 → 数据抽取 → 模仿学习 → RL**：FirstLight/Jason/ClashAI 的回放重驱提供可观察训练样本；RoyaleGym 提供 RL 包装；ClashAI 维护观测公平性和实验门禁。**风险**：隐藏信息泄漏、版本漂移和同一回放跨集合重复。
3. **视频 → 结构化事件 → 状态估计 → 解释性工具**：KataCR、BuildABot、视觉数据集输出检测；模拟器负责外推状态；Replay Studio/复盘器以时间轴和分支展示结果。**风险**：检测误差和时序错位累计。
4. **资源文件 → 解析/版本指纹 → 机制目录 → 校准测试**：SC Downloader、sc_extract、RoyaleAPI 静态数据用于观察内容版本；Hasty 和 RoyaleSim 的行为差分验证逻辑。**风险**：素材权利、同名卡牌 ID 不稳定及数据更新滞后。

详细的组合约束与结构见 [技术协作地图](composition-patterns.md)；对优先顺序和里程碑见 [衍生能力路线图](roadmap-derivative-power.md)。

## 调查没有做的事

没有把所有被搜索结果返回的仓库逐行审计，没有在设备里安装各个游戏版本，没有运行仓库全部测试，没有独立验证作者性能数据；因权限不足或 404 的仓库不会被写成“已经评估其源码”。后续更新应以固定提交补证据，未知就是未知。

## 原生与协议逆向知识补充

本次另建立 [逆向工程知识中心](../research/reverse-engineering/README.md) 和 [逐条发现登记](../registry/reverse-findings.yaml)。重点增加 Jason 内存研究笔记、FirstLight Native 布局测试、腾讯版本失效案例、Giovanni Rocca 早期协议研究，以及历史消息解析工具。严格区分历史原理与现行有效实现。
