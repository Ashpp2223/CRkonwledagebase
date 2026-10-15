# 2026-10-15：开发者社交线索复查与 RoyaleGym 模块补充

> 本文补充 [开发者关系调查](2026-10-15-developer-network.md) 和 [研究者项目/Fork 网络](2026-10-15-source-network.md)，**不覆盖其已有项目档案**。核查对象包括 `vegetableleaf`、`Jason-XII`、`Jaasssoooonnnnn` 与 `Ashpp2223`；另沿已发现的战斗模拟生态拓展到 RoyaleGym 组织。证据等级：GitHub 公开元数据/README 及 GitHub Compare；未执行本地集成测试。

## 社交图访问边界

已访问四个 GitHub 个人主页，页面可读 Following/Stars **数量**，但 GitHub 网页的 `?tab=following` / `?tab=stars` 列表在本次查询中未能抓取，现有 GitHub 连接未提供用户关注/星标目录接口。**本轮没有得到准确的关注账号名单或完整星标列表，不得声称已沿 Following 边穷举扫描**；GitHub 网页公开资料与 Fork/依赖关联不等于关注关系。

下述 RoyaleGym 扩展是**仓库生态与跨仓 README 明示的依赖发现**，不能说它被上述四位开发者关注或加星。

## 原有项目库尚未正式登记的四个模块

已有 `RoyaleGym/RoyaleGym` 与 `RoyaleGym/RoyaleSim` 项目卡。本轮新增以下独立公开仓库线索；目前仍属**候选**，尚未创建 Project/Implementation 正式登记，不改变 README 中已验证的登记总数。

| 候选仓库 | 核查的固定提交与证据 | 实质能力 | 对 CR 知识库/复盘器的意义 | 准入判断 |
| --- | --- | --- | --- | --- |
| [RoyaleBot](https://github.com/RoyaleGym/RoyaleBot) | [README @ a2ff261d](https://github.com/RoyaleGym/RoyaleBot/blob/a2ff261d7323b64fe78455c9c50a06cc4846ca5e/README.md) | `royalebot-play` 将 RoyaleLearn 保存的策略经电脑端发送给经过准备的 Null's Royale Android 客户端；支持 dry-run 和可视化 | 研究**设备端观测→PC 策略→动作确认**桥接、版本匹配与策略部署边界 | A（优先技术调研），R1 作者文档；仅声明 Null's Royale 15.535.13 客户端、ARM64，训练环境建议 15.535.29。不能视为官方/新版原生复盘宿主 |
| [RoyaleViser](https://github.com/RoyaleGym/RoyaleViser) | [README @ 8aada19c](https://github.com/RoyaleGym/RoyaleViser/blob/8aada19cdf95f3e18b6bf7f3a33c521fc6b01a26/README.md) | Pygame/Python 战场查看器；可显示实时训练或 `.msgpack` 保存的模拟器战斗，暂停与逐步控制 | 研究**与模拟器解耦的战斗可视化**、可观察状态和离线轨迹调试 UI | A（优先技术调研），R1；输入是 RoyaleGym 体系轨迹，不是原生 Supercell 渲染或可恢复 libg 状态 |
| [RoyaleLearn](https://github.com/RoyaleGym/RoyaleLearn) | [README @ bd497751](https://github.com/RoyaleGym/RoyaleLearn/blob/bd497751321127a8e4934a18f18ab9ef927c5cc9/README.md) | `Learner(make_env)`、自定义奖励、多次训练与策略存档 | 补齐已登记 RoyaleGym 的**训练后端**来源，帮助区分 Env、Trainer 与模型打包 | B，R1；AI 训练层，不是战斗规则模拟或原生引擎 |
| [RoyaleImitate](https://github.com/RoyaleGym/RoyaleImitate) | [README @ 357cd55b](https://github.com/RoyaleGym/RoyaleImitate/blob/357cd55bf77f5c5d591de523ae9336cae3ab8f9c/README.md) | `save_actor` + SHA-256 策略包、`warm_start` 扩展，学生策略权重初始化与模仿约束 | 补齐**教师策略→学生策略→持续训练**的可溯源模型接口 | B，R1；不提供新的原生回放/快照能力 |

### 真实的跨仓关系（不是 Follow/Star 关系）

```text
RoyaleSim (Rust 规则模拟器)
   └─ RoyaleGym (Gym/PettingZoo Env / save battle)
        ├─ RoyaleLearn (训练、存档)
        │    └─ RoyaleImitate (教师权重 / warm start 扩展)
        ├─ RoyaleViser (live replay / saved .msgpack viewer)
        └─ RoyaleBot (受限 Null's Android 部署、关联 RoyaleLearn / RoyaleViser)
```

`RoyaleBot` 中的客户端准备工具 `rb-build` 独立发布，非该 Python 包的源码交付一部分。此处仅登记架构事实，**不镜像 APK、资源或二进制工具**。

## Fork 核查：不要重复计为新技术

- [xiaozhejiya/FirstLight_CR](https://github.com/xiaozhejiya/FirstLight_CR)、[kqnan/FirstLight_CR](https://github.com/kqnan/FirstLight_CR)、[luody21/FirstLight_CR](https://github.com/luody21/FirstLight_CR) 相对于 `Jaasssoooonnnnn:main`，2026-10-15 GitHub Compare 均显示 `behind 6 / ahead 0`。尚无独立增加的提交可作新能力来源。xiaozhejiya Fork 页面也明确指向 Jaasssoooonnnnn/FirstLight_CR 作为当前推荐项目入口。
- 已有调查显示 `vegetableleaf/cr-memory-reader` 与 Jason 源完全同线、`arronwang01/clash-royale-battle-engine` 落后上游；延续“Fork 不自动增加 Project”规则。
- `vegetableleaf/KataCR` 的上游 Compare 本轮 404，**未完成独立增量审查**；不能推断它有或没有新增实现。

## 面向记谱器的后续验证任务

1. **RoyaleViser**：静态核查轨迹 schema（`.msgpack` 保存内容是状态帧、增量事件还是动作日志），与现有 `clashroyalereplay` 的动作日志/状态摘要语义逐项比较；必要时检查暂停、单步与 seek 的实现成本。
2. **RoyaleBot**：静态核查客户端数据同步时序、可观察状态字段、执行回执与断线恢复方式；尤其确认是否暴露独立的 `reset/step/snapshot/restore`（README 未声明，不得推断）。
3. **版本隔离**：把 RoyaleBot 的 `15.535.13` 客户端及 `15.535.29` 训练规则配置与其他 FirstLight / AK / vegetableleaf Oracle 版本分开；只在有实测记录时说明互操作。
4. **正式登记**：完成源码核查、许可证复核后按 [项目模板](../templates/project.md) 为四个仓库分别登记 Project，并给已有能力建立 `capability--project` Implementation；未经本地测试不得升级到 R3。

## 本轮非成果与边界

没有读到完整 Following/Starred 人员名单、没有逐行审查四个候选全部源码、没有运行 Android/训练环境、没有核验真实回放与原生 Tick 一致性。当前补充说明是**有证据的候选线索文档**，并非已复现或已集成四项能力。