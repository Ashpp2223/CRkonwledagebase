---
id: crforge
title: "crforge"
type: project
status: implemented
verification: author-documented
repository: https://github.com/voonhous/crforge
topics: [cr-battle-simulation, cr-game-mechanics, cr-ai-environment]
maintainers: []
last_reviewed: "2026-11-10"
license: Apache-2.0
---

# crforge

**上游**：[voonhous/crforge](https://github.com/voonhous/crforge) · **固定核查提交**：[`d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df`](https://github.com/voonhous/crforge/tree/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df)（2026-11-10）· **能力专项静态审计**：[16.635 逐 Tick 回放对照](../docs/source-audits/crforge-16635-parity-2026-11-10.md)。

## 具体实现与版本

Java 21 独立战斗模拟器：核心将一局拆为每 50 ms 一个整数 Tick，从匹配数据版本的游戏表读取单位、动作、表达式、状态效果和卡牌规则。配有 LibGDX 调试/回放界面、对录制战斗的严格 Tick 对照，以及面向 Python 训练器的批量环境/扁平缓冲区入口；实现结构与早期编目中描述的 ZMQ/Gymnasium 桥接已有变化，选型以[当前环境说明](https://github.com/voonhous/crforge/blob/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df/docs/environment.md)为准。

- **规则参照**：客户端 `16.635.1`（2026-10-28 迁移）；受测数据为 `16.635.3` 与 `16.635.8`；[compatibility](https://github.com/voonhous/crforge/blob/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df/docs/compatibility.md)、[game-versions](https://github.com/voonhous/crforge/blob/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df/docs/game-versions.md) 明确区分客户端版号与资源数据版号。
- **数据身份**：[`crforge-data.lock`](https://github.com/voonhous/crforge/blob/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df/crforge-data.lock) 固定数据仓库提交 `be5575a8a28b201a92b54c3aeefb775545eec685`，工作版本为 `16.635.8`、兼容集合 `16.635.3 16.635.8`。
- **类型边界**：模拟器重新实现规则，不运行官方 `libg.so` 原生战斗对象。真正的原生宿主需另行审查 reset/step、快照和运行环境。

## 2026 年 11 月：觉醒巨人验证

[2026-11-05 #845](https://github.com/voonhous/crforge/commit/1175bef2f1532d947537e692e3ee341ee26bf4b8) 新增了 `Giant_EV1` 攻击序列与狂暴区域相关规则处理，包括新版表达式及对未建模条件的拒绝路径。它将 `16.635.8` 的参考场景 `giant-evo-rage-v1/evo_giant_rage` 登记为 [`diagnostic_match`](https://github.com/voonhous/crforge/blob/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df/conformance/reference-expectations/16.635.8.json)。

该次提交作者报告：此前有 1,602 场包含觉醒巨人的覆盖对局在创建该单位时被拒绝；修复后其 16.635.8 覆盖集合报告为 **20,763/20,763**，参考场景合计 **1,069 匹配、23 不支持 / 1,092**。这属于上游测试报告，本知识库未下载覆盖语料或重跑 Gradle；`diagnostic_match` 的含义限于给定追踪 Schema 上逐 Tick 相等。

[具体行为与另一个实现 RoyaleSim 的证据对照](../research/knowledge-notes/cr-16635-evo-giant-parity-2026-11-10.md)。

## 可复用的验证路线

- [`ReferenceComparison.java`](https://github.com/voonhous/crforge/blob/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df/conformance/src/main/java/org/crforge/conformance/ReferenceComparison.java)：场景身份、摘要和观测字段的无容差比较；首个不同 Tick / 字段可定位。
- [`ReferenceSuite.java`](https://github.com/voonhous/crforge/blob/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df/conformance/src/main/java/org/crforge/conformance/ReferenceSuite.java)：由外部参考数据运行样本并对照版本期望文件。仅此接口能力有 [R2 固定源码审计](../docs/source-audits/crforge-16635-parity-2026-11-10.md)。
- [`conformance/README.md`](https://github.com/voonhous/crforge/blob/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df/conformance/README.md)：`:conformance:referenceTest`、`:conformance:coverageScore` 复验入口与四种结果（匹配、差异、不支持、无效）。

## 关联

[可修改的规则模拟](../capabilities/rules-simulation/README.md) · [模拟器保真验证](../capabilities/simulator-validation/README.md) · [独立战斗模拟器](../topics/cr-battle-simulation.md) · [战斗机制](../topics/cr-game-mechanics.md)

**仍待验证**：完整外部参考轨迹、跨设备运行、未覆盖的复杂规则和形态、与当前其他渠道客户端的兼容性及作者审阅。不得把作者自测转换成中台独立运行验证。

## 2026-11-10 新增接口跟踪：从真实回放时刻启动与觉醒镜像

- [2026-11-05 #854](https://github.com/voonhous/crforge/commit/4be7c013392273c0444ba0a36d3b130faec2cc7d)：环境添加 `startFromReplay(i, replay, tick)` / 向量化入口；通过原始回放配置和逐 Tick 命令推进到合法决策时刻，以生成**真实回放可到达状态**，而非任意写入单位/手牌的状态注入。可供回放中段分支决策实验使用，但不等于官方原生快照恢复。
- [2026-11-05 #859](https://github.com/voonhous/crforge/commit/de262b838ea4ca7640980bba4e85d70be38a4a90)：补充觉醒镜像在英雄牌和 Merge Maiden 之后复制的规则与针对性的拒绝条件，附内部单测。与此前觉醒巨人的 `diagnostic_match` 属不同测试范围，不应将某一种形态的通过状态推广到整个觉醒体系。
- [2026-11-09 #862](https://github.com/voonhous/crforge/commit/c8471087a322f18a110b2b31e281be30542fec33)：修正渔夫钩子目标在矿工转路开始时的特定交互。
- [2026-11-10 #863](https://github.com/voonhous/crforge/commit/d3ae65de1e7cf3c8ecff58185d4269e52c9ab3df)：记录 Google Play 客户端 `16.635.10` 与数据 `16.635.8`；作者仍以 `16.635.1` 规则为基准，未确认旧客户端能否继续登录、数据通过包内还是热更新取得，故**不能凭文档变更推断新版客户端已重新完成行为校准**。

以上为公开提交级别跟踪；既有 `simulator-validation--crforge` R2 审计只覆盖前文固定代码的比较接口，未为本节新增功能升级评级。
