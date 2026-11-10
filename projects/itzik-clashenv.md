---
id: itzik-clashenv
title: "ClashRoyaleEnv"
type: project
status: implemented
verification: author-documented
repository: https://github.com/itzik123/ClashRoyaleAi
topics: [cr-battle-simulation, cr-ai-environment, cr-game-mechanics]
maintainers: []
last_reviewed: "2026-11-10"
license: MIT
---

# ClashRoyaleEnv

**来源**：[itzik123/ClashRoyaleAi](https://github.com/itzik123/ClashRoyaleAi)，参考提交 [2f172925a15b](https://github.com/itzik123/ClashRoyaleAi/tree/2f172925a15b17f973291f41a789b19a29f0fc43)。目前以作者公开资料编目；尚未完成第三方设备/性能测试，原作者也未确认加入中台。

## 核心可衍生资产

C++17确定性模拟器、独立深拷贝分支、搜索教师、PPO训练及浏览器可视化。

## 能力入口

- [snapshot-recovery](../capabilities/snapshot-recovery/README.md)
- [lookahead-planning](../capabilities/lookahead-planning/README.md)
- [rules-simulation](../capabilities/rules-simulation/README.md)
- [agent-environment](../capabilities/agent-environment/README.md)

## 研究网络

- [独立战斗模拟器](../topics/cr-battle-simulation.md)
- [AI 训练环境与决策](../topics/cr-ai-environment.md)
- [战斗机制、寻路与数值](../topics/cr-game-mechanics.md)

## 限制

请将作者声称的性能、准确率、游戏版本支持与独立复现区分开来。代码开源许可证不自动涵盖游戏素材/模型/回放权属。项目入目录不等于当前即可集成；按 [复用成熟度](../docs/reuse-maturity.md) 处理。

## 2026-11-10 上游跟踪：实时教师与随机种子可移植性

- [11 月 9 日教师接入提交](https://github.com/itzik123/ClashRoyaleAi/commit/a7d7a5692aa5038fa4236fb246827941e02722a1)：`mvp_loop.py --policy teacher` 将屏幕观测逐次映射为独立环境，调用 `UtilityTeacher` 决策；新增 `MirrorGaps` 记录伪造/缺失字段。属于**感知→模拟器镜像→规划**原型，不能等同于忠实重建游戏隐藏状态。
- [11 月 9 日实时路径审查](https://github.com/itzik123/ClashRoyaleAi/commit/310c814f0f4eb138b4c58da8abd87177f23112bb)：修正静态画面被误判为圣水消费、跨局账本泄漏、丢弃动作被记为已执行、录制帧与实时时钟混用等问题。作者的 `--frames` 回归验证不等于手机联机成功。
- [11 月 10 日 S36 文档与实验](https://github.com/itzik123/ClashRoyaleAi/commit/53a6ef7d029c29f4451bff148b0aba4991b7c7a1)：`mt19937` 原始随机数跨 `libstdc++` / `libc++` 一致，但 `uniform_int_distribution` 和 `shuffle` 结果不同，导致相同 seed 的牌序/初手跨构建不一致。仓库新增 `tools/audit/portable_random_check.cpp` 演示使用底层随机数的替代算法，**引擎主代码尚未应用该修复**，MSVC 路径未检验。
- [固定 TODO](https://github.com/itzik123/ClashRoyaleAi/blob/53a6ef7d029c29f4451bff148b0aba4991b7c7a1/docs/TODO.md) 将真实 Android 物理手机采集/触控列为未启动的 P0；目前实时路径依赖 Windows/BlueStacks，仍需完成带教师策略的模拟器 dry run、设备分辨率重新校准及延迟验证。

这些变更不改变现有 `snapshot-recovery` / `lookahead-planning` / `rules-simulation` / `agent-environment` 的 R 评级。跨机器对比应固定 C++ 标准库、编译选项和种子派发方式，待统一算法实际进入引擎后重建黄金样本。
