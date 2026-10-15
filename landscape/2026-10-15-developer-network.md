# 2026-10-15：开发者关系与派生技术调查

本次从开发者**公开持有的仓库、GitHub Fork 元数据、上游 README 的明确依赖以及已提交的技术文档**出发；没有把不可读取的 Star/Following 列表推定为已审计。GitHub 用户关注操作不等于中台的研究追踪。

## 持续观察的开发者

| 开发者 | 公开入口 | 本次关键线索 |
| --- | --- | --- |
| vegetableleaf | [GitHub](https://github.com/vegetableleaf) | [ClashAI](https://github.com/vegetableleaf/ClashAI) 新版 16.402.12 Oracle 研究、只读观测/模拟保真；其 cr-memory-reader 与 KataCR 是 Fork |
| arronwang01（Arron） | [GitHub](https://github.com/arronwang01) | [clapha-engine](https://github.com/arronwang01/clapha-engine) **非公开**，由 Jason 的公开适配器印证；[cr-collector](https://github.com/arronwang01/cr-collector)；其 battle-engine 是 Jason 的 Fork |
| IMAX9D | [GitHub](https://github.com/IMAX9D) | [cr-native-sandbox](https://github.com/IMAX9D/cr-native-sandbox)、[cr-native-linux-bionic](https://github.com/IMAX9D/cr-native-linux-bionic)、[r0-elite-training](https://github.com/IMAX9D/r0-elite-training)、[royaleapi-downloader](https://github.com/IMAX9D/royaleapi-downloader) |
| Jason-XII | [GitHub](https://github.com/Jason-XII) | [Battle Engine](https://github.com/Jason-XII/clash-royale-battle-engine) 的 `clapha.py` / `docs/COLLABORATION.md` 提供与 Arron 的实质协作证据；[Memory Reader](https://github.com/Jason-XII/cr-memory-reader) |
| ak1NaN（AK） | [GitHub](https://github.com/ak1NaN) | [腾讯 38.4.2 运行时 Harness](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness)；[Replay Studio](https://github.com/ak1NaN/ClashRoyale-replay-studio) |
| Jaasssoooonnnnn | [GitHub](https://github.com/Jaasssoooonnnnn) | [FirstLight_CR](https://github.com/Jaasssoooonnnnn/FirstLight_CR) 原生生命周期、原生画面和进程内快照基线 |

## 新发现的高价值仓库

| 价值 | 项目 | 为什么值得研究 | 重要限制 |
| --- | --- | --- | --- |
| A | [CR Native Sandbox](../projects/cr-native-sandbox.md) | 原始 15.535.29 x86_64 `libg` 的离线 reset/step、Replay、命令与状态接口 | 无原生渲染；依赖特定 runtime |
| A | [CR Native Linux Bionic](../projects/cr-native-linux-bionic.md) | 不启动 AVD/KVM，原始 `libg` 依赖 Android 用户态的最小运行层 | 仅固定 x86_64 旧构建；不是新版引擎 |
| A（源码暂不可取） | [Clapha Engine](../projects/clapha-engine.md) | Jason 公开 `ClaphaEngine` 封装显示进程内原生 reset/step、批量 PPO 场景 | 私有，不能审计 loader/原生实现；不证明渲染/快照 |
| B | [RoyaleAPI Downloader](../projects/royaleapi-downloader.md) | 可恢复采集、跨玩家去重、格式化事件与赛季筛选 | 网站条款、会话及源数据完备性 |
| B | [R0 Elite Training](../projects/r0-elite-training.md) | 原生状态数据到训练数据的强契约和自测链路 | 模型训练，而非可用于记谱器的渲染引擎 |
| C | [Arron CR Collector](../projects/cr-collector.md) | 分布式志愿采集/任务协调结构 | 数据站点访问限制、协调服务依赖 |

**实际检查了什么？** 以上项目的公开 README、代码目录及 GitHub 仓库元数据；本轮不代表在本地拉起引擎。固定源版本在各项目卡。所谓“开发者追踪”是知识库观察清单，不代表账号已执行 GitHub Follow。

## Fork、协作与排除项

- [arronwang01/clash-royale-battle-engine](https://github.com/arronwang01/clash-royale-battle-engine) 的 GitHub `parent` 为 [Jason-XII/clash-royale-battle-engine](https://github.com/Jason-XII/clash-royale-battle-engine)。它不是 `clapha-engine` 的开源替代仓库；没有发现应作为另一项独立引擎能力登记的验证材料。
- [vegetableleaf/cr-memory-reader](https://github.com/vegetableleaf/cr-memory-reader) 的 `parent` 为 [Jason-XII/cr-memory-reader](https://github.com/Jason-XII/cr-memory-reader)，[vegetableleaf/KataCR](https://github.com/vegetableleaf/KataCR) 的 `parent` 为 [wty-yy/KataCR](https://github.com/wty-yy/KataCR)。只凭 Fork 身份不复制成三个新的技术项目；如未来发现独有提交，再单独评价。
- [arronwang01/clash-ai-releases](https://github.com/arronwang01/clash-ai-releases) 现有 README 明确“Moved. Nothing is published here any more”；暂不收录为能力来源。
- Arron 的非公开 [clapha-engine](https://github.com/arronwang01/clapha-engine) 在 [Jason 合作文档](https://github.com/Jason-XII/clash-royale-battle-engine/blob/70a08af6807fa4d59a11c7d52bf6272a96afe30c/docs/COLLABORATION.md) 中明确标记 private。中台仅能审查 [公开的封装层](https://github.com/Jason-XII/clash-royale-battle-engine/blob/70a08af6807fa4d59a11c7d52bf6272a96afe30c/clapha.py)，无法声称底层已经由中台源码核验。
- **Star/Following 列表**：本轮 GitHub 连接不支持访问个人公开 starred/following 动态或执行关注用户操作；网页公开列表亦未能可靠获取。此次扫描**不宣称**覆盖他们的 Star 或关注图谱，后续有合法读接口时再补。

## 16.402 与记谱器升级的下一步

[新版 Oracle 案例与准入关卡](../research/reverse-engineering/client-upgrade-160402.md) 是关键研究入口。对于记谱器，原生画面、reset/step、双边动作、完整快照/恢复的可运行证据优先于所谓“最新 offset”。不要把旧版 15.535 的已运行沙盒、腾讯 38.4.2 的在线 Hook 与 16.402.12 的静态生命周期定位混为一谈。
