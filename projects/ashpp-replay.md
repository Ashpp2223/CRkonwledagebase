---
id: ashpp-replay
title: "皇室战争复盘器"
type: project
status: implemented
verification: author-documented
repository: https://github.com/Ashpp2223/clashroyalereplay
topics: [cr-replay-state, cr-native-engine]
maintainers: []
last_reviewed: "2026-10-31"
license: unknown
---

# 皇室战争复盘器

[上游仓库](https://github.com/Ashpp2223/clashroyalereplay) · [固定源码核查](../docs/source-audits/native-engine-2026-10-13.md)

Tauri + React 复盘器，带原生渲染、分支节点、原生进程内快照和重放恢复。源码在 [`BattleController`](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L43-L59) 中封装基本对局控制：`reset`、`step`、`play_card`；另有 [`snapshot_restore`](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L286-L312) 清理未来调度，防止分支污染。重放时检查动作顺序与预期摘要。[摘要构造](https://github.com/Ashpp2223/clashroyalereplay/blob/de46d7ea3831a64565140cdb9d4b947f9fe21916/bridge/controller.py#L15-L35) 不等于完整原生 GameState 内容。

此程序的集成行为与客户端资源依赖于固定的构建与本地环境；**进程内快照句柄不跨进程**。尚未作为通用第三方 SDK 发布，许可证需单独确认，不能因为代码可见就默认具有复制许可。

[原生控制能力](../capabilities/battle-control/README.md) · [快照能力](../capabilities/snapshot-recovery/README.md) · [接入验收](../capabilities/snapshot-recovery/integration.md)

## 2026-10-31 复查：国服原生引擎与版本隔离

[2026-10-18 固定提交](https://github.com/Ashpp2223/clashroyalereplay/tree/7b4d18270e7476610f20d24c8808bb7c69b9730a) 的 [国服引擎接入说明](https://github.com/Ashpp2223/clashroyalereplay/blob/7b4d18270e7476610f20d24c8808bb7c69b9730a/docs/cn-engine-integration.md) 与 [升级手册](https://github.com/Ashpp2223/clashroyalereplay/blob/7b4d18270e7476610f20d24c8808bb7c69b9730a/docs/engine-upgrade-playbook.md) 记录了一个适配层下的双版本复盘：

| 维度 | 原引擎（保留） | 新接入国服引擎 |
| --- | --- | --- |
| 选择配置 | `legacy`（默认） | `cn-38.4.5` |
| 游戏/内容版本 | 旧内容 `15.535.86` | 国服 `38.4.5` |
| 控制协议 | `native-bridge.v1` / `cr-minimal.v3` | `cr-camp-control.v1` |
| 卡牌/觉醒/精英及英雄形态 | 122 / 42 / 24 | 123 / 43 / 26 |
| 默认等级 | 16 | 11 |

新版本 `0.4.1` 的作者文档报告：全 69 种形态完成原生消耗检查，补齐精英冰法和精英电法的出牌、技能与恢复验证；0.4.0 的冻结发行版曾完成分支切换、连续播放、终局和关闭重开等桌面验收。**这些是上游在特定本机环境的报告**，本中台没有执行同机或异机复验；0.4.1 没有重新进行完整终局回归，不能沿用 0.4.0 报告宣称新版已重跑全套验收。

**可迁移的版本契约**：存档绑定 APK/`libg`、适配器、内容与协议等身份；跨规则版本拒绝按原局继续；原生快照句柄只在同一进程/局面有效，重启靠初始配置、固定 seed 与动作日志重放。不同版本的塔兵 ID 命名空间、手牌槽含义、Tick/动作边界和画面坐标须通过适配与验收逐项转换，而非只替换函数地址。

原项目文件格式继续使用 `cr-native-replay.v2`，但这**不表示**不同规则版本的存档可相互当作同一局面载入。此次复查不改变既有项目×能力 R 等级。
