# larkindaniel/clash-royale-agent 局部审查（2026-11-13）

等级 **P0（文档/目录）**。固定上游 commit `c283c698ad74fcc1304b612b11c2f399160d1055`。已读取的文件与 blob：

- [docs/information-boundary-audit.md](https://github.com/larkindaniel/clash-royale-agent/blob/c283c698ad74fcc1304b612b11c2f399160d1055/docs/information-boundary-audit.md) — `86fae8d5232577a370bd8166fa8bf6bfac8042d6`
- [docs/known-differences.md](https://github.com/larkindaniel/clash-royale-agent/blob/c283c698ad74fcc1304b612b11c2f399160d1055/docs/known-differences.md) — `d6ff3fb0954c0c06d89efdf1f7eecdd0b09241ef`

## 发现

作者设计文档规定 PPO 只能使用公开 Observation，敌方圣水通过公共信息估计上下界；禁止访问对方手牌、牌序、精确圣水、未来 RNG 和内部冷却。已明确列出桥梁寻路、质量/推挤、Tick 先后、仇恨等近似。此次只读文档与目录树，**未直接检查训练/观测源码，严格保持 P0**。

## 待验证

尚未运行测试；待检查剩余关键源码、许可、数据来源与运行环境。不得把文档断言视为实际测试结果。
