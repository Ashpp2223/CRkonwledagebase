---
id: crownzero
title: "CrownZero"
type: project
status: research
verification: author-documented
repository: https://github.com/anishhchitnis/crownzero
topics: [cr-ai-environment, cr-runtime-observation]
maintainers: []
last_reviewed: null
license: unknown
---

# CrownZero

- **上游**：https://github.com/anishhchitnis/crownzero
- **筛选优先级**：A
- **证据等级**：R1（作者文档核对，未固定提交审计、未运行）
- **来源**：[README.md](https://github.com/anishhchitnis/crownzero/blob/HEAD/README.md)
- **候选能力**：lookahead-planning, visual-perception, agent-runtime

## 可复用的技术与边界

RoyaleSim + Build-A-Bot 视觉重建局面、六秒前瞻与动作执行；README 记录多次真实录像中的识别错误与修正；对局成绩未独立复验。

## 中台判断

作为独立来源收录，暂不建立经过源码验证的能力实现关系。下一步需固定上游 commit，审查关键代码、测试和许可证；不能将作者报告的运行结果提升为独立验证。

参见[2026-11-12 增量调查](../landscape/2026-11-12-github-discovery.md)。
