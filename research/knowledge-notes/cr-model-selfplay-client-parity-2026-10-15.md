# CR 世界模型、自博弈与跨客户端机制校准（2026-10-15）

这份技术研究来自公开源码和 GitHub 提交，而不是声称完整抓取了这些账号的 Following/Starred 列表。调查对象包括 longlingking、JinxTheCatto、IMAX9D 与 eddyzow，严格区分源码和协作事实。

## 1. 新衍生技术：Longling × R2-Dreamer

[longling 的 CR 模拟器 Fork](../../projects/longling-simulator.md) 相对 [Jason 源](../../projects/jason-simulator.md) 有独有的 R2-Dreamer 环境桥接、循环世界模型对手以及快照采样。GitHub Compare 显示 `ahead 16 / behind 168`（2026-10-15）；不是新的原生引擎。

- 观测：网格 `(32,18,15)`、`hand (5)`、`elixir (1)` 与终局标志。三段 55 维 multi-one-hot 动作（slot 5 / y 32 / x 18），分别 argmax 才进入模拟器。
- 自博弈：对手池支持 recent/base/fixed，策略快照保留 RNN 状态，回收对局结果更新采样权重。采样与策略性能不等价；简单脚本胜率高并不证明对人类玩家的泛化。
- 代码路径和副作用见 [静态审查](../../docs/source-audits/longling-r2dreamer-2026-10-15.md)。迁移到其它环境需要重做 CardId、观测公平性、Tick 及奖励契约，且避免 `os.chdir` 进程污染。

## 2. RoyaleSim：将游戏版本差异表示为规则分支

[JinxTheCatto 的公开 GitHub 个人介绍](https://github.com/JinxTheCatto/JinxTheCatto) 自述参与 RoyaleGym；GitHub 官方提交记录显示其对 [RoyaleSim](../../projects/royalesim.md) 的 2026-10-10 至 10-13 源码/机制校准有贡献。

- [`client_arms.rs`](https://github.com/RoyaleGym/RoyaleSim/blob/39e7d48253877858a064a4df140f01f4c4866d6c/crates/royalesim/src/client_arms.rs) 保留旧版 15.535.29 的规则覆写；16.402 使用当前 ledger 默认，`client_arms(...)` 提供客户端版本入口。**同一个术语的不同版本参数并不相容**。
- [`replay_parity.rs`](https://github.com/RoyaleGym/RoyaleSim/blob/39e7d48253877858a064a4df140f01f4c4866d6c/crates/royalesim/examples/replay_parity.rs) 可输出逐 Tick 状态对比、首个偏差及机制类别；其差异评分由原作者采集数据计算。不能把 README/提交注释中的样本通过率冒充本中台结果。
- [建筑部署末 Tick 的反例测试](https://github.com/RoyaleGym/RoyaleSim/blob/39e7d48253877858a064a4df140f01f4c4866d6c/crates/royalesim/tests/building_deploy_last_tick.rs) 区分 Tesla 等隐藏建筑与普通建筑；相比“整体提前一帧”，它提供可以被证伪的具体分支。
- 上游 [0.1.33–0.1.34 CHANGELOG](https://github.com/RoyaleGym/RoyaleSim/blob/39e7d48253877858a064a4df140f01f4c4866d6c/CHANGELOG.md) 还记录了 `GUARD_FREE_TICK`、`PULSING_AREA_LIFE`、`LINE_TERRITORY` 等机制的独立校准。核查范围和未验证项见 [审查](../../docs/source-audits/royalesim-client-parity-2026-10-15.md)。

**适合纳入中台的长期方法**：固定客户端 build、卡牌数据表和真值轨迹 → 比较 first divergence → 构造两种机制的最小反例 → 对比覆写前后得分 → 按版本合并相符规则。此法比单用胜率评估模拟器保真度更直接。

## 3. RoyaleGym 已完整建模为分层仓库链

| 技术边界 | 项目 | 新增知识 |
| --- | --- | --- |
| 规则执行 | [RoyaleSim](../../projects/royalesim.md) | 原生轨迹差分和版本化校准（单项 R2） |
| 训练环境 | [RoyaleGym](../../projects/royalegym.md) | Gym/PettingZoo 包装与动作观察契约 |
| 模型训练 | [RoyaleLearn](../../projects/royale-learn.md) | 奖励、优化循环、权重保存 |
| 教师迁移 | [RoyaleImitate](../../projects/royale-imitate.md) | 教师权重摘要和 warm start |
| 战斗可视化 | [RoyaleViser](../../projects/royale-viser.md) | `.msgpack` 轨迹、单步、对象检查 |
| 设备部署 | [RoyaleBot](../../projects/royale-bot.md) | Null's 15.535.13 ARM64 与 PC 端模型桥接 |

[轨迹可视化能力](../../capabilities/battle-visualization/README.md) 和 [回放重建能力](../../capabilities/replay-reconstruction/README.md) 现在分别建立索引；仅存在可视化控件不说明具备原生状态恢复。

## 4. 已有来源和排除项

[IMAX9D 的 CR Native Sandbox](../../projects/native-sandbox-imax9d.md)、[Linux Bionic](../../projects/native-bionic-imax9d.md)、[R0 Training](../../projects/r0-elite-imax9d.md) 和 [RoyaleAPI Downloader](../../projects/royaleapi-downloader-imax9d.md) 已有项目卡，应继续追踪具体版本，不再生成重名项目。

eddyzow 的公开仓库未发现专门面向 CR 战斗/复盘/模拟的实现；其通用实时多人项目不能直接算作本知识库的 CR 能力。GitHub Following 关系仍未得到可靠名单，本篇不宣称“这些作者关注了彼此”。

## 5. 下一步可复验问题

1. RoyaleViser 保存的 `.msgpack` 是完整状态序列还是事件增量？逐帧 seek 与随机访问语义是什么？
2. RoyaleBot 的模型输入与执行回执具有哪些时间戳和失败重试语义？存在什么样的安全拒绝条件？
3. Longling 的 Dreamer 训练从同一复盘输入获得的观测是否含隐藏信息？在固定种子/对手集合上是否真正优于 PPO？
4. RoyaleSim 的 `client_arms` 在固定 card-table 和参考客户端下能否重复得到相同首个分叉 Tick？

**验证状态**：仓库源码静态核查，未运行本地冒烟、真实客户端、Rust 测试、AI 训练。
