# max-miller1204/Clash-Royale-Pod 源码局部审查（2026-11-13）

**等级 P1**。上游 commit `5df4d6f860fe2b8bc734b8c052778530c96cd28e`，已检查以下源码；未执行上游测试或完整依赖审计。

- [src/crpod/analysis/blunders.py](https://github.com/max-miller1204/Clash-Royale-Pod/blob/5df4d6f860fe2b8bc734b8c052778530c96cd28e/src/crpod/analysis/blunders.py) — blob `651e9b3a4f7b9d0d1f3f5f76e48d638eb5f381bf`
- [src/crpod/modeling/ev.py](https://github.com/max-miller1204/Clash-Royale-Pod/blob/5df4d6f860fe2b8bc734b8c052778530c96cd28e/src/crpod/modeling/ev.py) — blob `aa039af71d63c4a6aaf64e540f2707f7544004ca`

## 发现与边界

基于视频识别与交互特征估计防御塔血量收益，按每张卡训练集的 EV 中位数和标准差标记低于中位数 1σ 的行动；样本少于五次的卡牌不判定，零方差跳过。该“失误”是模型相对统计指标，不代表已求解反事实最优操作。

## 后续

补查调用链、边界输入、许可、版本、测试和实际可复现性，完成后才可考虑 P2。
