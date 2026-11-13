# larkindaniel/clash-royale-agent 局部审查（2026-11-13）

等级 **P1（部分源码）**。固定上游 commit `c283c698ad74fcc1304b612b11c2f399160d1055`。已读取的文件与 blob：

- [docs/information-boundary-audit.md](https://github.com/larkindaniel/clash-royale-agent/blob/c283c698ad74fcc1304b612b11c2f399160d1055/docs/information-boundary-audit.md) — `86fae8d5232577a370bd8166fa8bf6bfac8042d6`
- [docs/known-differences.md](https://github.com/larkindaniel/clash-royale-agent/blob/c283c698ad74fcc1304b612b11c2f399160d1055/docs/known-differences.md) — `d6ff3fb0954c0c06d89efdf1f7eecdd0b09241ef`

## 发现

作者设计文档规定 PPO 只能使用公开 Observation，敌方圣水通过公共信息估计上下界；禁止访问对方手牌、牌序、精确圣水、未来 RNG 和内部冷却。已明确列出桥梁寻路、质量/推挤、Tick 先后、仇恨等近似。本轮补查了训练观测源码，确认编码器仅接收公开 Observation。

## 待验证

尚未运行测试；待检查剩余关键源码、许可、数据来源与运行环境。不得把文档断言视为实际测试结果。

## 同轮补查的核心源码（P1 依据）

- [src/crsim/rl/encoding.py](https://github.com/larkindaniel/clash-royale-agent/blob/c283c698ad74fcc1304b612b11c2f399160d1055/src/crsim/rl/encoding.py)，blob `8dd61b0cf5d4c04db8c7070cffaecf3014817b11`：公开 Observation 编码器，18×32、4 手槽、动作空间 2305，玩家 1 坐标旋转；对手圣水用公共历史推定区间。
- [src/crsim/rl/env.py](https://github.com/larkindaniel/clash-royale-agent/blob/c283c698ad74fcc1304b612b11c2f399160d1055/src/crsim/rl/env.py)，blob `c7f37bfb0939c1b075bd5df8593c012ea35f767b`：公开塔生命势函数、公开场面兵力势函数、自己圣水溢出估计，按双方视角零和计算；未见在已检查路径中直接读取敌方私有手牌。

当前仅能支持“已检查的编码与奖励函数按公开信息设计”，尚不能保证整套训练系统绝无私有信息泄漏；需继续静态检查调用图并运行相关单元测试。
