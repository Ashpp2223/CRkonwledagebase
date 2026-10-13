# 原生战斗能力：环境与兼容性对照

下表记录**每个项目在指定公开文档/源码版本的边界**，不是统一“兼容矩阵”。标记“未知”表示缺少证据，不允许自动补齐。

| 维度 | FirstLight CR | Jason Battle Engine | Ashpp 复盘器 | Replay Studio |
| --- | --- | --- | --- | --- |
| 审阅提交 | `3ade158c52` | `2b3361954c` | `de46d7ea38` | `04d48bdcf2` |
| 上游使用场景 | Windows MuMu ARM64 离线原生引擎、训练 | Mac ARM64 原生探针+GPU Linux 训练管线 | Windows Android SDK 模拟器原生复盘 | Mac Apple Silicon MuMu 原生回放 |
| 游戏/内容版本证据 | APK 15.535.13 / 资源 15.535.86 | PPO 段提到 150535029；原生探针版本应单独校验 | README 记录 15.535.86 资源基线 | Nulls Royale 15.535.13 / 资源 15.535.86 |
| 引擎外部依赖 | 用户提供的 APK/资源、原生探针、Android/构建工具 | 原生探针及指定平台，训练另依赖 clapha-engine | 用户提供的游戏资源和原生库；桥接与安卓开发镜像 | 用户本地安装的 Nulls Royale 与 MuMu |
| 主要控制入口 | NativeClashEnv 与 BattleEnvV1 | Engine / RenderedEngine | BattleController | app/engine.py |
| 原生快照能力 | **确认存在进程内接口** | 本次只确认 Engine 的 reset/step；快照接口需继续审阅 | **进程内快照＋动作重放** | 本次主要验证重建/回放控制，非任意节点公共 snapshot |
| 是否有统一 SDK | 否 | 否 | 否 | 否 |
| 中台设备实测 | 未进行 | 未进行 | 未进行 | 未进行 |

**来源**：
- [FirstLight 安装要求](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/docs/getting_started.md#L13-L23)、[快照源码](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/cr_native_env.py#L2835-L2859)。
- [Jason README 的分阶段环境](https://github.com/Jason-XII/clash-royale-battle-engine/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/README.md#L7-L17)、[clapha build](https://github.com/Jason-XII/clash-royale-battle-engine/blob/2b3361954c189a8ea508f3f54cf94a56c2e045fc/README.md#L69-L74)。
- [复盘器 README](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/README.md)、[控制器](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L43-L58)。
- [Replay Studio README](https://github.com/ak1NaN/ClashRoyale-replay-studio/blob/04d48bdcf2f54cf81dc809e56d9bc08691a167e2/README.md)。

## 不能跨项目混用的概念

1. **tick 与动作生效位置**：`reset` 后的起始 Tick、出牌执行 Tick、模型每次决策采样间隔可能不同。
2. **观察层**：`BattleEnvV1` 提供 FAIR 观测，底层原生控制器可能得到更完整内部状态。两者不能直接等同。
3. **动作结构**：FirstLight 的 `ActionV1` 有目标类型和执行偏移；Jason 的 `Play` 为 owner/slot/x/y；Ashpp UI 另外需要 expected_tick 和持久化动作日志。
4. **坐标与单位**：即使都是数字 `x`/`y`，也必须验证整数尺度、阵营旋转、塔楼禁放区及特定技能目标规则。
5. **快照生命周期**：句柄可能只在一个原生进程和 manager generation 内存在；复盘的序列化记录通常保存的是动作路径，而不是原生 snapshot。
6. **模型训练≠设备控制**：Jason 在 GPU 的 `clapha-engine` 阶段与 Mac 原生探针阶段并不是同一实例实现。
7. **授权**：游戏客户端、原生库、源码和模型权重分别具有不同权利状态。

具体 API 差异和先行检查见 [接口接入对照](integration.md)；精确代码出处见 [源码核查](../../docs/source-audits/native-engine-2026-10-13.md)。
