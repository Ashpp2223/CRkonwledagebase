# 16.402.12：新版原生离线战斗生命周期证据与缺口

## 研究对象

[vegetableleaf/ClashAI](https://github.com/vegetableleaf/ClashAI) 的 ORACLE L74 分支研究，固定查看提交 [ec4ef8e9](https://github.com/vegetableleaf/ClashAI/tree/ec4ef8e9dcaaaa4169ff8768bd36323e93840f9c)。构建 `160402012`（16.402.12）是 **x86_64 客户端构建号**，不等于 AK 的腾讯 38.4.2 编号，也不能直接使用旧版 15.535 的 RVA。

## 已公开的成果与证据等级

| 层级 | 当前可确定事项 | 证据 |
| --- | --- | --- |
| **静态结构定位** | v3 记录 18 个生命周期目标达到作者所称 high static confidence，包括 CreateGameMain、DataTables、LoadingState、地图资源、Replay Loader、GameState 和 Tick | [V3_REPORT](https://github.com/vegetableleaf/ClashAI/blob/ec4ef8e9dcaaaa4169ff8768bd36323e93840f9c/scratchpad/gauntlet/L74/oracle/V3_REPORT.md) |
| **静态部署工件** | v7 有分阶段原生调用设计与本地源码、编译门槛；提供独立的 build/verify/test 脚本 | [v7 README](https://github.com/vegetableleaf/ClashAI/blob/ec4ef8e9dcaaaa4169ff8768bd36323e93840f9c/scratchpad/gauntlet/L74/oracle/linux/qualify/jnihost_ro/v7/README.md) |
| **实际新版离线运行** | **未证明**：v7 G5 Android 目标机执行未完成；尚不能宣称 16.402.12 独立 reset/step 已通过 | [v7 GATES](https://github.com/vegetableleaf/ClashAI/blob/ec4ef8e9dcaaaa4169ff8768bd36323e93840f9c/scratchpad/gauntlet/L74/oracle/linux/qualify/jnihost_ro/v7/GATES.md) |
| **新版资源数据** | APKTABLES 记录本地从 160402012 安装包及 2026-10-12 设备更新目录抽取和比较数据的流程 | [APKTABLES](https://github.com/vegetableleaf/ClashAI/blob/ec4ef8e9dcaaaa4169ff8768bd36323e93840f9c/scratchpad/gauntlet/L74/apktables/README.md) |

v3 报告还指出：presentation/shim 站点尚未完成资格审核，**没有已认证的渲染跳过补丁**。不能将“定位到 Tick 函数”直接换算成“有可控制的离线战斗引擎”。

## 三种既有原生运行路线

| 方案 | 已有来源证明 | 必需补充证据 |
| --- | --- | --- |
| [FirstLight / Jason](../../projects/firstlight-cr.md) ARM64 旧版 | Android 原生渲染、reset/step、快照/恢复，版号 15.535.13 | 移植新的 ARM64 客户端：入口、资源、对象、渲染与快照，全部复验 |
| [CR Native Sandbox](../../projects/cr-native-sandbox.md) / [Linux Bionic](../../projects/cr-native-linux-bionic.md) | x86_64 15.535.29 原生无画面 Tick、自定义 Replay 与两边出牌；Bionic 运行无需 AVD | 新版 Runtime 适配；特别是加载和初始化时的版本依赖；无原生渲染 |
| [AK 腾讯 Harness](../../projects/tencent-model-harness.md) | 38.4.2 正常客户端进程内状态读取与命令提交 | 还没有离线初始化、完整快照或独立 Tick 控制证据 |
| [Clapha Engine](../../projects/clapha-engine.md) | Jason 的公开封装显示 15.535.29 x86_64 进程内 `create_match` / `step` | 加载器私有、未公开快照和渲染接口；不代表已移植 16.402 |

## 记谱器验收关卡

1. **构建身份**：APK Split / ABI / `libg` 哈希及资源指纹一致。
2. **生命周期**：合法地独立初始化两边配置、固定 seed、新建/销毁对局；不是在线游戏中触发 `step` Hook。
3. **自主时间**：受控 Tick 推进、暂停、终局规则及回合时序；明确真实接口的回执。
4. **分支状态**：原生快照和恢复后，RNG、命令队列、技能和事件的相同后缀必须一致；不允许只保存部分观测叫“快照”。
5. **展示与应用**：原生画面渲染、进程代际、分支恢复、环境故障处理与现有记谱器协议。
6. **回归**：至少基准正常牌、英雄技能、觉醒、法术、多目标行为；记录新旧版差异与失败。

**结论**：16.402.12 的静态入口知识已经有独立研究价值，最新版离线原生执行和记谱器替代引擎尚未得到公开实证。中台没有自行运行这些实验。
