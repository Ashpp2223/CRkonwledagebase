# 2026-10-15 皇室战争研究者公开项目与 Fork/依赖网络

调查对象：vegetableleaf、ak1NaN、Jason-XII、arronwang01、IMAX9D、Jaasssoooonnnnn。**本次完成的是这些账号可检索的公开仓库、部分公开 Fork 与依赖引用审查**；GitHub 连接不支持读取完整关注用户列表、完整 Starred 列表或代替用户执行 Follow。不得把未访问的星标/关注网络写成已审计事实。

## 新发现：优先阅读顺序

| 优先级 | 项目 | 实质技术资产 | 对原生战斗记谱器的意义 | 当前成熟度边界 |
| --- | --- | --- | --- | --- |
| A | [CR Native Sandbox](../projects/native-sandbox-imax9d.md) | x86_64 原版 `libg.so` 的 JNI/Java 独立宿主与 reset/step/动作/观测 | 无画面重演、状态对照和新版宿主研究基线 | 冻结 15.535.29；不是最新版接口 |
| A | [CR Native Linux Bionic](../projects/native-bionic-imax9d.md) | 不用 AVD/KVM 的 Linux Bionic/ART/Binderless JniHost | 可研究轻量化 Worker 和可移植宿主 | 只验证声称的 x86_64 150535029；无原生渲染或通用快照 |
| A | [FL Royale](../projects/fl-royale.md) | 原生安卓离线可玩游戏壳与竞技场显示 | 研究原生画面、大厅和运行封装 | 基于 FirstLight，不能当作已开放外部记谱器 SDK |
| B | [RoyaleAPI Downloader](../projects/royaleapi-downloader-imax9d.md) | SQLite 任务队列、赛季采集、回放去重、检查点 | 原生重建的资料来源 | 不能保证真实回放所有隐含字段完整 |
| B | [R0 Elite Training](../projects/r0-elite-imax9d.md) | 原生样本准入、版本化特征契约与训练一致性验证 | 复现回放数据与 AI 流水线 | 需外部大规模数据，不提供战斗引擎 |
| B | [SC Decoder](../projects/sc-decoder-jason.md) | SC 精灵解码与角色/表情动画预览 | 有助检查静态/动画资源，不是原生战场渲染 | 新格式覆盖、许可证待核查 |
| B | [Arron CR Collector](../projects/cr-collector-arron.md) | 开放回放数据协作采集与协调服务 | 研究可追溯的事件来源/分发 | 站点自动化限制与字段缺失 |

## 源码关联图

```text
FirstLight_CR
   ├── Jason-XII/clash-royale-battle-engine (原生引擎 API、PPO 训练)
   │      └── clapha.py → arronwang01/clapha-engine (私有，Linux x86_64 进程内原生加载)
   └── FL-Royale (Android 离线游戏与渲染壳)

IMAX9D/cr-native-sandbox (15.535.29 x86_64 原生 Worker)
   ├── cr-native-linux-bionic (直接在 Linux 用户态运行，无 AVD/KVM)
   └── vegetableleaf/ClashAI 的原生回放重驱与数据采集
             ├── RoyaleSim：与原生轨迹对照的独立模拟器
             └── ORACLE 160402012：新版生命周期静态映射，尚未完成独立运行

ak1NaN/tencent-model-harness (Tencent 38.4.2)
   └── 活动客户端 Frida Hook + 原生动作提交；未建立公开的离线 reset/step/snapshot
```

连接表示上游 README/源码中能够核对的依赖或调用**关系**，而非各仓库作者之间的身份/协作关系或版本互兼容保证。

## 公开 Fork：哪些带来新技术，哪些只是镜像

- [vegetableleaf/cr-memory-reader](https://github.com/vegetableleaf/cr-memory-reader) 是 [Jason-XII/cr-memory-reader](https://github.com/Jason-XII/cr-memory-reader) 的公开 Fork；2026-10-15 GitHub Compare `Jason-XII:main...vegetableleaf:main` 显示 **identical（ahead 0 / behind 0）**。因此不额外建立一份重复的项目/实现实体。
- [arronwang01/clash-royale-battle-engine](https://github.com/arronwang01/clash-royale-battle-engine) 是 Jason Battle Engine 的公开 Fork；同日 Compare 为 **behind 39 / ahead 0**。可以用于追踪协作，不应作为新引擎发现。
- [vegetableleaf/KataCR](https://github.com/vegetableleaf/KataCR) 是 [wty-yy/KataCR](https://github.com/wty-yy/KataCR) 的 Fork；未完成有效的共同基点差异检查，**不作原创增强结论**。
- [arronwang01/clash-ai-releases](https://github.com/arronwang01/clash-ai-releases) 的 README 仅说明“Moved. Nothing is published here any more.”，不编目为技术成果。
- [arronwang01/clapha-engine](https://github.com/arronwang01/clapha-engine) 当前无法公开访问（404）；[Jason 的合作说明](https://github.com/Jason-XII/clash-royale-battle-engine/blob/70a08af6807fa4d59a11c7d52bf6272a96afe30c/docs/COLLABORATION.md) 明确将它列为私有。公开的 [clapha.py](https://github.com/Jason-XII/clash-royale-battle-engine/blob/70a08af6807fa4d59a11c7d52bf6272a96afe30c/clapha.py) 证明其被调用，但**不足以审计私有加载器**。

## 需要纳入更新跟踪的源

| 账号 | 高价值公开仓库 | 重点观察的变化 |
| --- | --- | --- |
| vegetableleaf | [ClashAI](https://github.com/vegetableleaf/ClashAI) | ORACLE 160402012 是否首次通过 `runtime gate`，能否独立 reset/step |
| IMAX9D | [cr-native-sandbox](https://github.com/IMAX9D/cr-native-sandbox)、[cr-native-linux-bionic](https://github.com/IMAX9D/cr-native-linux-bionic) | 新 libg 构建、原生状态/快照、无 AVD 宿主改动 |
| Jaasssoooonnnnn | [FirstLight_CR](https://github.com/Jaasssoooonnnnn/FirstLight_CR)、[FL-Royale](https://github.com/Jaasssoooonnnnn/FL-Royale) | 新版原生渲染、Android 离线客户端和兼容性 |
| ak1NaN | [Tencent Harness](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness) | 38.4.2 之后是否新增离线初始化、快照/恢复 |
| Jason-XII | [Battle Engine](https://github.com/Jason-XII/clash-royale-battle-engine)、[sc-decoder](https://github.com/Jason-XII/sc-decoder) | Native API、GPU 集群封装与资产工具改动 |
| arronwang01 | [cr-collector](https://github.com/arronwang01/cr-collector)、[battle engine Fork](https://github.com/arronwang01/clash-royale-battle-engine) | 公共采集技术；私有 clapha-engine 仅等待获授权证据 |

## 研究结论

就**可迁移的新版本原生战斗引擎**而言，存在两个不同的待突破点：

1. **16.402.12**：vegetableleaf ORACLE v3 静态识别了生命周期、DataTables、地图、状态机与 Tick 入口；v7 Android 独立运行门禁尚未通过。见 [跨版本逆向证据](../research/reverse-engineering/client-build-migration-2026-10.md)。
2. **Tencent 38.4.2**：AK 的可操作原生 Hook 属于正在运行的联网/常规客户端控制；不能替代 `reset/step/snapshot/restore` 离线战斗 API。

应优先跟踪**真实独立 Battle 创建+Tick 成功**与**可恢复状态完整性**，而不是用地址数量或 Star 数评价进度。
