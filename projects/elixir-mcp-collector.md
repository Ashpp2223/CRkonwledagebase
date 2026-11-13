---
id: elixir-mcp-collector
title: "Elixir MCP Collector"
type: project
status: research
verification: author-documented
repository: https://github.com/jthingelstad/elixir-mcp-collector
topics: [cr-assets-data]
maintainers: []
last_reviewed: null
license: unknown
---

# Elixir MCP Collector

- **上游**：https://github.com/jthingelstad/elixir-mcp-collector
- **筛选优先级**：B
- **证据等级**：R1（作者文档核对，未固定提交审计、未运行）
- **来源**：[README.md](https://github.com/jthingelstad/elixir-mcp-collector/blob/HEAD/README.md)
- **候选能力**：asset-ingestion

## 可复用的技术与边界

Go 采集 Worker，租约/HTTPS 提交/限流，依赖 Elixir MCP 服务与官方 API key；非逐帧回放。

## 中台判断

作为独立来源收录，暂不建立经过源码验证的能力实现关系。下一步需固定上游 commit，审查关键代码、测试和许可证；不能将作者报告的运行结果提升为独立验证。

参见[2026-11-12 增量调查](../landscape/2026-11-12-github-discovery.md)。
