# Clash Royale Dataset Browser

- **上游**：https://github.com/HumaidAlhuthali/clash-royale-dataset-browser
- **筛选优先级**：B
- **证据等级**：R1（作者文档核对，未固定提交审计、未运行）
- **来源**：[README.md](https://github.com/HumaidAlhuthali/clash-royale-dataset-browser/blob/HEAD/README.md)
- **候选能力**：replay-to-learning, battle-visualization

## 可复用的技术与边界

将 Hugging Face TV replay 帧与出牌标签合并，提供逐帧浏览；数据与标签来自外部，不验证原始标签正确性。

## 中台判断

作为独立来源收录，暂不建立经过源码验证的能力实现关系。下一步需固定上游 commit，审查关键代码、测试和许可证；不能将作者报告的运行结果提升为独立验证。

参见[2026-11-12 增量调查](../landscape/2026-11-12-github-discovery.md)。
