# jthingelstad/elixir-mcp-collector 源码局部审查（2026-11-13）

等级 **P1**。上游 commit `5721c3462888db34387afbaba682fb0cbde85e6d` 已经 GitHub commit API 核实。仅阅读列出的实现，未运行上游测试。

- [internal/crapi/crapi.go](https://github.com/jthingelstad/elixir-mcp-collector/blob/5721c3462888db34387afbaba682fb0cbde85e6d/internal/crapi/crapi.go) — blob `7810af4f0fdc1bc2ddb6aa0d89d1ca06ea8471e4`
- [internal/breaker/breaker.go](https://github.com/jthingelstad/elixir-mcp-collector/blob/5721c3462888db34387afbaba682fb0cbde85e6d/internal/breaker/breaker.go) — blob `a98b6560f062748da55a75a7cad4a1ac02b6ec3c`

## 实现与证据限制

Go 采集端将 Clash Royale API 访问集中在单一 fetcher，15s 超时、8MiB 解压后响应体上限、HTTPS→HTTP 重定向拒绝；单次租约只请求一次，将重试决策交给上游调度。403 断路器默认连续五次触发、冷却 300s，配置刷新保留断路器状态；403 的具体原因无法单凭状态码判定。

## 后续

审计剩余调用链、许可证、依赖、测试和真实数据，独立验证后才可评估 P2。
