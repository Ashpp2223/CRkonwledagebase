# Clash Royale Post-Game Analyzer

- **上游**：https://github.com/max-miller1204/Clash-Royale-Pod
- **筛选优先级**：A
- **证据等级**：R1（作者文档核对，未固定提交审计、未运行）
- **来源**：[README.md](https://github.com/max-miller1204/Clash-Royale-Pod/blob/HEAD/README.md)
- **候选能力**：visual-perception, replay-to-learning

## 可复用的技术与边界

视频帧检测、出牌统计、预测 EV 与异常决策报告；需额外训练的 YOLO 权重与 EV 模型；EV 不是原生对局反事实收益。

## 中台判断

作为独立来源收录，暂不建立经过源码验证的能力实现关系。下一步需固定上游 commit，审查关键代码、测试和许可证；不能将作者报告的运行结果提升为独立验证。

参见[2026-11-12 增量调查](../landscape/2026-11-12-github-discovery.md)。
