# 2026-11-10：16.635 新客户端与觉醒巨人（Giant_EV1）的规则复现

**问题**：2026 年 11 月是否已有可研究的新客户端战斗规则、觉醒巨人原理及跨引擎验证证据？

**结论（2026-11-10 补充）**：现有三条来源：crforge（Java）和 RoyaleSim（Rust）是独立战斗**模拟器**；[Clashback](../../projects/clashback.md) 则直接运行并封装新版 x86_64 **原生 `libg.so`（构建 `160635001`，资源 `16.635.8`）**，拥有 `CrxEnv.create_match/step/observe/queue_card_at` 和原生快照接口。crforge 的 `Giant_EV1` 有参考回放 `diagnostic_match`，RoyaleSim 有数据表与单测；Clashback 的觉醒巨人专项原生测试未找到，其已公开资源清单中也未直接出现 `giant_ev1.toml`。要区分“新版本原生接口已经存在”和“所有新卡原生效果均已验证”。

## 版本与证据锚点

| 维度 | crforge | RoyaleSim |
| --- | --- | --- |
| 固定源码 | [`d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df`](https://github.com/voonhous/crforge/tree/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df)（2026-11-10） | [`d62501352d7995b352a167730c4a31e49f4ed570`](https://github.com/RoyaleGym/RoyaleSim/tree/d62501352d7995b352a167730c4a31e49f4ed570)（0.1.51，2026-11-08） |
| 客户端/数据版本 | 以 `16.635.1` 为参考客户端；`16.635.3`、`16.635.8` 数据；[兼容说明](https://github.com/voonhous/crforge/blob/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df/docs/compatibility.md) | 选用 `client160635007_20261103` 表，对应 16.635 系列、11 月 3 日内容；[版本变更](https://github.com/RoyaleGym/RoyaleSim/blob/d62501352d7995b352a167730c4a31e49f4ed570/CHANGELOG.md) |
| 觉醒巨人 | [#845 实现](https://github.com/voonhous/crforge/commit/1175bef2f1532d947537e692e3ee341ee26bf4b8)，[固定期望结果](https://github.com/voonhous/crforge/blob/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df/conformance/reference-expectations/16.635.8.json) | [11 月 3 日机制提交](https://github.com/RoyaleGym/RoyaleSim/commit/aef9a3d8894915f5542ae82128cefe43459076b6)，[专项测试](https://github.com/RoyaleGym/RoyaleSim/blob/d62501352d7995b352a167730c4a31e49f4ed570/crates/royalesim/tests/evo_giant.rs) |
| 证据差异 | 上游记录 `giant-evo-rage-v1/evo_giant_rage: diagnostic_match`；逐 Tick 接口已做指定范围静态核查 | 测试源码检查、表字段断言与模拟器内部状态检查；测试明确注明 `not measured`，没有该形态的 16.635 真实回放样本 |

[crforge 版本身份](https://github.com/voonhous/crforge/blob/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df/docs/game-versions.md) 的参考客户端为 16.635.1；16.635.10 于 11 月 5 日出现，内容仍为 16.635.8，但原作者尚未确认 16.635.1 是否继续被服务器接受，不能据此肯定后续每个客户端规则都相同。国服 `38.4.x` 与国际服 `16.635.x` 的版本编号不可直接互换。

## Giant_EV1：来自 RoyaleSim 数据表与测试的条件化规则

在 [`evo_giant.rs`](https://github.com/RoyaleGym/RoyaleSim/blob/d62501352d7995b352a167730c4a31e49f4ed570/crates/royalesim/tests/evo_giant.rs) 与 [表读取检查](https://github.com/RoyaleGym/RoyaleSim/blob/d62501352d7995b352a167730c4a31e49f4ed570/tests/test_rage_areas_block.py) 中：

- 一次普通巨人出牌后可触发觉醒形态（`evo.cycles = 1`）；生命值达到最大值的 **50% 或以下**时启动狂暴区域生成序列。
- 区域生成沿巨人**面向的反方向**偏移 2,500 个 millitile（表中 `offset=-2500`）；开始后每 1,500 ms 产生一个区域。四档半径为 2 / 2.5 / 3 / 3.5 格，分档由进入狂暴阶段之后累计的攻击命中次数 0 / 1 / 2 / ≥3 决定。
- 区域作用于**友方单位**，伤害为 0；测试中的狂暴 Buff 对移速和攻速使用 130% 比例。范围效果的产生、首个 Buff 生效、持续时间和冻结暂停时钟均有独立断言。
- 克隆得到普通巨人；已经生成的区域可以在原觉醒巨人死亡后继续存在。以上数值和时序是**当前实现及表定义**，精确客户端行为仍需真实回放核对。

## crforge 的回放对照能证明什么

[差分审计](../../docs/source-audits/crforge-16635-parity-2026-11-10.md) 证实：`ReferenceComparison` 对相同 `scenario_sha256` / 表版本的逐 Tick 状态做严格字段比较；参考观测范围包括 RNG、实体位置、血量、状态、圣水与手牌。上游 #845 更新后，觉醒巨人半血在塔前生成狂暴区域的参考用例被登记为 `diagnostic_match`，提交报告 16.635.8 的 20,763 场覆盖对局匹配。该结论受**参考数据版本、观测字段、对局样本**限制；仍不能拿它替代新版原生 Tick 或进程内快照验证。

## 最小复验建议

1. 固定客户端 build、数据版本、`content_sha`、项目提交与回放种子；优先以 `giant-evo-rage-v1/evo_giant_rage` 重跑 `crforge` 的参考差分，检查结论和首差异位置。
2. 对低血量临界点（51% / 50%）、狂暴生成 Tick、方向偏移、攻击次数档位、冻结与克隆各建立可重复场景；逐场记录原版轨迹、模拟轨迹与状态字段。
3. 若用于复盘器或 AI 训练，单独测 **reset/step、出牌延迟、随机源、状态快照/重放、跨版本卡表**，不能因模拟器 `diagnostic_match` 就宣称已有可用新版原生战斗接口。

[crforge 档案](../../projects/crforge.md) · [RoyaleSim 档案](../../projects/royalesim.md) · [原生宿主迁移](../reverse-engineering/client-build-migration-2026-10.md)

## 补充发现：Clashback 的原生调用和快照（2026-11-10）

[固定提交](https://github.com/ak1NaN/Clashback/tree/45c1f26b942ae1d706f2004791e73013e4330099) 同时提供 [160635001 函数/字段映射](https://github.com/ak1NaN/Clashback/blob/45c1f26b942ae1d706f2004791e73013e4330099/vendor/crx/bindings/160635001.json)、[CrxEnv 原生控制层](https://github.com/ak1NaN/Clashback/blob/45c1f26b942ae1d706f2004791e73013e4330099/vendor/crx/env.py) 和 [NativeSnapshotStream](https://github.com/ak1NaN/Clashback/blob/45c1f26b942ae1d706f2004791e73013e4330099/neo_replay/native_snapshots.py)。宿主为 Apple Silicon Mac 上的 x86_64 Python/Rosetta，已有 HTML 重建回放和 Tick 快照的代码实现。本知识库已经针对控制及快照入口完成 [R2 限定范围源码审计](../../docs/source-audits/clashback-160635001-2026-11-10.md)，但未运行原生环境；其构建和资源版本固定，不可推及国服 38.4.5 或未来更新。下游复盘器对接前需测真实觉醒巨人对局、重复建局稳定性、快照分支与 Windows 运行条件。

**复核补充**：[`observed-160635001.json`](https://github.com/ak1NaN/Clashback/blob/45c1f26b942ae1d706f2004791e73013e4330099/updater/profiles/observed-160635001.json) 确认包含 `giant.toml`，没有与 `giant_ev1.toml` 精确匹配的独立文件路径。因此把“Clashback 已能运行觉醒巨人”维持为 **unknown**；若它通过其他表定义或热更新加载，需要实验和资源来源证据。只要资源版本为 `16.635.8` 并不足以升级这个结论。
