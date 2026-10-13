# 战斗状态恢复的四种语义：快照、分叉、序列化、动作重放

## 问题

“可以恢复某个历史局面”至少包含四种不同操作。如果不区分，开发者可能把一个支持复盘时间轴的项目误选为 MCTS 并行搜索底座。

## 可以定位的来源

| 项目 | 现有实现/资料 | 有效范围 |
| --- | --- | --- |
| FirstLight CR | [`NativeClashEnv.create_snapshot/restore/release_snapshot`](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/cr_native_env.py#L2828-L2860) | 当前原生应用进程及 headless manager generation；静态源码检查 |
| ClashRoyaleEnv | [`GameManager::snapshot`](https://github.com/itzik123/ClashRoyaleAi/blob/2f172925a15b17f973291f41a789b19a29f0fc43/include/core/GameManager.h#L254-L268) 及 [Python 绑定](https://github.com/itzik123/ClashRoyaleAi/blob/2f172925a15b17f973291f41a789b19a29f0fc43/src/bindings.cpp#L170-L180) | 自建 C++ 模拟器的状态深拷贝，不是原生游戏内存；静态源码检查 |
| RoyaleSim | [Rust 引擎 API](https://github.com/RoyaleGym/RoyaleSim/blob/main/docs/api.md) 中 `save/load` 与状态哈希的作者说明 | 独立模拟器自身的状态格式，未在中台设备或测试程序独立复现 |
| Ashpp 复盘器 | [快照恢复与调度清理](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L286-L312) 和 [动作日志恢复](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L314-L385) | 原生进程内句柄和应用层重放，两套不同持久性约束；静态源码检查 |

## 机制差异

| 机制 | 保存的对象 | 生命周期 | 后续典型用途 |
| --- | --- | --- | --- |
| **进程内快照句柄** | 引擎内部在当前进程中管理的状态映像/引用 | 通常有进程与 manager 代际约束 | 同进程复盘跳转与反复恢复 |
| **深拷贝状态分叉** | 复制到独立的模拟器状态实例 | 由自建引擎的数据结构与内存决定 | 搜索树不同动作后缀、反事实实验 |
| **序列化状态保存** | 对引擎状态按格式编码的字节/记录 | 可能跨进程，取决于格式和版本兼容 | 持久化、回归测试、状态比较 |
| **动作日志重放** | 初始配置和事件/动作的有序序列 | 不依赖保留旧进程内句柄，但依赖输入完整性 | 重启后重建、分支历史、审计 |

上述是**概念分类**，不是任何上游仓库统一采纳的 API 定义。

## 可迁移的不变量与不成立的推断

- **恢复正确性**不仅需要可见单位位置，还可能依赖随机数状态、未来动作调度、延迟事件、卡牌循环和已发生但未表现的效果。
- FirstLight 有原生快照接口，但这**不证明**能跨进程保存，也不证明能并行复制成独立原生进程。
- ClashRoyaleEnv 的自建模拟器具备深拷贝代码，但分支的独立性不直接证明其规则与目标游戏版本相同。
- 应用层即使恢复了原生状态，旧分支的外部命令队列仍可能残留。Ashpp 的源码显式在快照恢复后清理调度；这是**组合系统状态不止于引擎内部**的具体案例。
- `save/load` 存在不代表不同版本数据格式稳定；跨构建读档、RNG 与事件队列完整性需要专门测试。

## 由证据支持的工程建议

**只是拖动时间轴**：优先检查缓存与动作重放，不必一开始就设计多进程分叉。

**需要策略树搜索**：优先要求“分叉独立性 + RNG 复制 + 单次成本 + 规则保真”的四项证据，而不是仅查询函数名 `snapshot`。

**需要断线或重启恢复**：定义初始配置、动作有序性、资源构建和摘要覆盖范围；不能把进程内 handle 当作存档。

## 下一步测试（尚未执行）

针对完全相同的局面和动作后缀，分别验证：同一初始状态的重复输出、不同分支互不污染、进程/manager 更换后的句柄失效、序列化字段完整性、50/95 分位耗时。每次测试固定游戏构建、资源版本、代码 SHA、硬件及随机源；失败用例同样记录。

[快照能力](../../capabilities/snapshot-recovery/README.md) · [原生与应用源码审计](../../docs/source-audits/native-engine-2026-10-13.md) · [ClashRoyaleEnv 审计](../../docs/source-audits/itzik-clashenv-2026-10-13.md)
