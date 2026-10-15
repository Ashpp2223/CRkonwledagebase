# 2026-10-15：RoyaleSim 跨客户端校准接口静态审查

**对象**：`simulator-validation--royalesim`；**固定 SHA**：`39e7d48253877858a064a4df140f01f4c4866d6c`；**级别**：R2 / source-inspected；尚未下载对局语料、运行 Cargo 或复核作者差分统计。

## 核查结果

1. [`crates/royalesim/src/client_arms.rs`](https://github.com/RoyaleGym/RoyaleSim/blob/39e7d48253877858a064a4df140f01f4c4866d6c/crates/royalesim/src/client_arms.rs#L1-L30) 通过 `CLIENT15535_ARMS` 保存 15.535.29 的校准覆写；当前 16.402 使用 ledger 默认。对应 [`tests/client_arms.rs`](https://github.com/RoyaleGym/RoyaleSim/blob/39e7d48253877858a064a4df140f01f4c4866d6c/crates/royalesim/tests/client_arms.rs) 定义旧版匹配、新版空覆写、无效版本拒绝测试。
2. [`examples/replay_parity.rs`](https://github.com/RoyaleGym/RoyaleSim/blob/39e7d48253877858a064a4df140f01f4c4866d6c/crates/royalesim/examples/replay_parity.rs) 定义固定 corpus 的**逐 Tick 状态对比**，输出单场和聚合报告、first divergence 机制归因，并支持 `--calibration-override section.KEY=JSON` 的候选规则实验；其中还检查 binary/ledger 漂移。
3. [`tests/building_deploy_last_tick.rs`](https://github.com/RoyaleGym/RoyaleSim/blob/39e7d48253877858a064a4df140f01f4c4866d6c/crates/royalesim/tests/building_deploy_last_tick.rs) 用 `AfterCountdown`、`Client16402ActsOnLastTick`、`Client16402HidersOnly` 的正反用例检验建筑部署末 Tick 的目标获取；Tesla 等隐藏建筑与普通建筑的条件有区别。

## 范围与待验

- 上游 [CHANGELOG](https://github.com/RoyaleGym/RoyaleSim/blob/39e7d48253877858a064a4df140f01f4c4866d6c/CHANGELOG.md) 的 15.535.29 和 16.402 测量数字属于作者报告；本次只证实源码/测试入口存在，**没有复现实测命中数**。
- 不得将某一个校准臂推及任何构建、全部卡牌或所有 Tick；需分别固定客户端、卡牌表、素材、ABI 和真值数据。
- 后续运行 `cargo test --test client_arms` 与 `cargo test --test building_deploy_last_tick`、`cargo run --example replay_parity -- <fixture>`，记录首个错误帧、修复前后差分与环境。
