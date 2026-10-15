# 跨构建原生战斗宿主：15.535、16.402 与腾讯 38.4.2

截至 2026-10-15，本页区分**运行已证实的旧版路径**、**针对新版的静态发现**与**待验证的迁移能力**。

## 同一需求、不同证据状态

| 原生路径 | Build / ABI | 公开证据 | 离线自主 reset/step | 原生画面与快照 |
| --- | --- | --- | --- | --- |
| [FirstLight / Jason](../../projects/firstlight-cr.md) | Nulls 15.535.13，ARM64 | 源码探针与固定构建 | 作者报告可运行 | 渲染、进程内快照可研究；记谱器有固定版本调用 |
| [CR Native Sandbox](../../projects/native-sandbox-imax9d.md) | 15.535.29，Android x86_64 | JNI/Java 宿主、API、固定指纹 | 作者报告可运行 | 无原生画面；未找到可供第三方复用的快照/恢复契约 |
| [Linux Bionic](../../projects/native-bionic-imax9d.md) | 15.535.29，Linux x86_64 / Android API31 userland | linker/ART/Binderless JniHost，无 AVD/KVM | 作者报告可运行，复用 Sandbox Worker | 无原生画面；不是 16.402 迁移 |
| [ClashAI ORACLE v3/v7](../../projects/clashai-vegetableleaf.md) | 160402012，x86_64 | 生命周期静态分析与 staged host；v7 compile/check 通过 | **未取得运行通过证据** | **没有新版渲染/快照通过证据** |
| [AK Tencent Harness](../../projects/tencent-model-harness.md) | 38.4.2，ARM64 | 有原生 step Hook、command 构造、状态读取和提交 | **未公开独立离线创建和 Tick 驱动** | 依赖正在运行的客户端；`snapshot` 是部分观测，不是恢复点 |

各版本编号不能直接按大小推断版本分支与 ABI 互相兼容。

## 16.402.12：ClashAI ORACLE 到底已经发现了什么

来源：[v3 静态研究报告](https://github.com/vegetableleaf/ClashAI/blob/218554aee8b7be9b3ad5298349853d6fe747c90f/scratchpad/gauntlet/L74/oracle/V3_REPORT.md) 与 [v7 验收门禁](https://github.com/vegetableleaf/ClashAI/blob/218554aee8b7be9b3ad5298349853d6fe747c90f/scratchpad/gauntlet/L74/oracle/linux/qualify/jnihost_ro/v7/GATES.md)。

v3 将 `CreateGameMain`、`GameMain::init`、DataTables 范围加载/异步准备、`LoadingState` 更新、地图 FileName/TileDataFileName 请求、Battlefield cache、Manager update、Replay Loader、BattleGameState 和 battle Tick 归入**静态高置信候选**。一个关键发现是 `GameState` 底层更新可能由外层固定步长累加器调度，**调用外层入口一次不必然意味着推进一个 Tick**。

同一个报告将若干渲染/加载 presentation site 列为 `unresolved` 或 `likely`，明确没有合格的补丁与运行验收。

v7 的 `GATES.md`：G1–G4 完成离线测试、源码检查与编译；**G5 Android 运行、G6 Linux worker shell 核验未完成**。因此不能把“18 项高置信静态身份”写成新版无界面原生战斗成功。

## 可直接迁移的知识与不可照搬的字节

**可继承**：游戏引擎生命周期图、依赖初始化顺序、地图及逻辑表装载流程、动作/Tick/玩家对象语义、最小验收条件，以及旧宿主中先后调用关系。

**不可盲用**：`libg.so` 的 RVA、对象字段、vtable、ABI、精确构建资源哈希、渲染跳过点、客户端渠道的命令链。

示例：AK 的 [38.3.1 / 38.4.2 配置](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness/blob/4a2c033e8fa4051dfdadaf7348408b833aecfb28/config/native_offsets.json) 显示 `step` 和 `stock_submit` 的 RVA 迁移幅度不同，无法使用全局地址增量代替重新验证。

## 对记谱器的证据门槛

要将新版作为 [Ashpp 记谱器](../../projects/ashpp-replay.md) 的替代后端，依次要求：

1. 与完整 APK/ABI/资源指纹绑定，**新进程中**离线创建 Battle。
2. 无服务器自然 Tick 依赖，能以已知动作确定性地推进指定 Tick。
3. 双边下牌/技能实际进入原生 GameState，回执可区分接受/执行/终局。
4. 能复现相同种子与事件序列；恢复、分支无污染，故障后的句柄代际明确。
5. 有原生渲染或明确的替代显示渠道；能与现有记谱器帧时间轴校准。

若只完成 1–3，适合作为无画面引擎研究原型，**不能立即替换需要原生画面和快照的用户复盘体验**。

[来源网络](../../landscape/2026-10-15-source-network.md) · [构建与偏移复验](version-revalidation.md) · [逆向知识中心](README.md)
