# jthingelstad/elixir-mcp-discord 源码局部审查（2026-11-13）

等级 **P1**。上游 commit `6ec6badfc330026393cccc0d66c15262d8e7b542` 已经 GitHub commit API 核实。仅阅读列出的实现，未运行上游测试。

- [src/eligibility.js](https://github.com/jthingelstad/elixir-mcp-discord/blob/6ec6badfc330026393cccc0d66c15262d8e7b542/src/eligibility.js) — blob `831a515577b3762f1de31074ef30d9d65513deff`
- [src/budget.js](https://github.com/jthingelstad/elixir-mcp-discord/blob/6ec6badfc330026393cccc0d66c15262d8e7b542/src/budget.js) — blob `3af07b6b7b962641173d396bbddae9ce097a7857`

## 实现与证据限制

Discord 机器人将公会参与政策作为自动任务的许可门槛，读取 clans_directory 并验证字段、时效（60s）及状态；未知/无效政策应拒绝依赖操作。模型费用按 routines/ask/review 三条预算通道隔离，启动前按历史最大单轮费用预留额度，避免月末超支。

## 后续

审计剩余调用链、许可证、依赖、测试和真实数据，独立验证后才可评估 P2。
