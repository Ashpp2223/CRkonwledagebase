# aboufama/clash-royale-research 局部源码审查（2026-11-13）

**等级 P1**。固定上游 commit `d8511d40135f0b5d6e93ddc124767d080c8a376d`。本轮读取以下文件，未运行测试。

- [sim/core/src/battle.ts](https://github.com/aboufama/clash-royale-research/blob/d8511d40135f0b5d6e93ddc124767d080c8a376d/sim/core/src/battle.ts) — blob `d56cf2a8f6221c254737bde8d693f41df3393e24`
- [sim/core/test/differential.test.ts](https://github.com/aboufama/clash-royale-research/blob/d8511d40135f0b5d6e93ddc124767d080c8a376d/sim/core/test/differential.test.ts) — blob `ed5d8aa91b4c7982ec08d5aa6a7a06c1db0e2df0`
- [docs/FIDELITY.md](https://github.com/aboufama/clash-royale-research/blob/d8511d40135f0b5d6e93ddc124767d080c8a376d/docs/FIDELITY.md) — blob `5a6239d5f786c07bb248d3cbb3cd929da6eaec4f`
- [docs/MECHANICS_BRIEF.md](https://github.com/aboufama/clash-royale-research/blob/d8511d40135f0b5d6e93ddc124767d080c8a376d/docs/MECHANICS_BRIEF.md) — blob `fa58e648cd2d07c0308440b25edd49743254b7a8`

## 发现与限制

TypeScript 20Hz、整数单位、seeded RNG 的战斗模拟器，按命令、圣水、世界更新、结算顺序推进。Fidelity 以 V(原始代码移植并差分验证)、P(反编译移植)、D(游戏数据驱动)、A(近似) 标注机制来源，另设 Native check，避免把单次 native trace 匹配当成所有机制已证实。differential.test.ts 从记录的 tick-0 状态启动 400-tick 原生轨迹比较，涉及位置、HP、投射物；尚未运行。仓库含原始 APK/资产包，必须另外审查再分发许可与安全边界。

## 后续

继续查剩余实现、依赖、许可、测试与真实数据；达到可重复证据链后再评估 P2。
