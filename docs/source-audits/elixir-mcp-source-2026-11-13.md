# jthingelstad/elixir-mcp 局部源码审查（2026-11-13）

**等级 P1**。固定上游 commit `0e0a463ada7e8ec4935edf5fc5753c48d5cf746a`。本轮读取以下文件，未运行测试。

- [packages/contracts/src/battle-link.ts](https://github.com/jthingelstad/elixir-mcp/blob/0e0a463ada7e8ec4935edf5fc5753c48d5cf746a/packages/contracts/src/battle-link.ts) — blob `2fe9f73b12fe404809188f24bc200dda58457410`
- [apps/web/e2e/battle.spec.ts](https://github.com/jthingelstad/elixir-mcp/blob/0e0a463ada7e8ec4935edf5fc5753c48d5cf746a/apps/web/e2e/battle.spec.ts) — blob `5704fe6d238806bba98e6d2d35bc5a3b4773ecf1`

## 发现与限制

大型 Node workspace（Git tree 3620 项）。战斗公开链接使用 SHA256 ID 的至少 12 位前缀，依据邻近 ID 冲突延长；支持公开页面与 PNG 分享。Playwright e2e 通过 mockApi 测试匿名访问、双方卡组、结果与 WCAG 严重/致命问题；属于 Web 应用回放展示而非原生战斗状态快照。仅检查这两个模块，其他服务和采集链仍待审。

## 后续

继续查剩余实现、依赖、许可、测试与真实数据；达到可重复证据链后再评估 P2。
