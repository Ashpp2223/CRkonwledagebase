# arronwang01/cr-collector 局部源码审查（2026-11-13）

等级 **P1**。GitHub commit API 核实上游 commit `e70ceafcfd64d78d332dae16ccfc05071da3a803`。本轮仅阅读下列源码，未运行上游测试。

- [royale/pipeline.py](https://github.com/arronwang01/cr-collector/blob/e70ceafcfd64d78d332dae16ccfc05071da3a803/royale/pipeline.py) — blob `96353b7d47815db52f261832e7e10b84b0e40f1a`
- [royale/limiter.py](https://github.com/arronwang01/cr-collector/blob/e70ceafcfd64d78d332dae16ccfc05071da3a803/royale/limiter.py) — blob `1fe9178278f486e9be075506dace7cda12a366ec`

## 发现与限制

RoyaleAPI 网页抓取流水线：根据卡牌签名筛选卡组，读取玩家排行榜和历史战斗分页，以 replay_tag 去重，并使用分页 cursor 防循环。共享 Limiter 通过线程锁统一限速，成功时增速、HTTP 429 时减半并暂停；实际 transport 的限速接线尚未验证。

## 后续

补查完整实现、许可、依赖、边界输入与测试可执行性，达到完整证据链后再考虑 P2。
