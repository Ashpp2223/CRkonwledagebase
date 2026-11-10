---
id: replay-studio
title: "Clash Royale Replay Studio"
type: project
status: implemented
verification: author-documented
repository: https://github.com/ak1NaN/ClashRoyale-replay-studio
topics: [cr-replay-state, cr-native-engine]
maintainers: []
last_reviewed: "2026-11-10"
license: unknown
---

# Clash Royale Replay Studio

**原仓库**：[ak1NaN/ClashRoyale-replay-studio](https://github.com/ak1NaN/ClashRoyale-replay-studio)。**初次整理**：2026-10-13。仅依据公开作者文档，尚未得到原作者审核，也未独立测试。

## 公开描述的能力

解析 RoyaleAPI 独立对局 HTML，在本地原生引擎中预演算、缓存并以 0.25×–16× 倍速回放。

## 兼容与限制

HTML 缺少原始随机种子与秘密初手，只能重建相容对局；README 指出 Mac 测试版与游戏卡牌支持限制。

## 相关专题

- [回放、快照与状态恢复](../topics/cr-replay-state.md)
- [原生战斗引擎](../topics/cr-native-engine.md)

## 证据

- [仓库 README](https://github.com/ak1NaN/ClashRoyale-replay-studio)
- [补充来源](https://github.com/ak1NaN/ClashRoyale-replay-studio)

## 待复核

- 实际运行能力、对应提交 SHA、准确兼容版本、维护者确认和授权边界。

## 2026-11-10 维护状态核查

[2026-11-04 固定 README](https://github.com/ak1NaN/ClashRoyale-replay-studio/blob/a12f0b1b88ee31cb7743e75afb80471336bf0c90/README.md) 已在首页明确声明**后续开发迁移至 [Clashback](clashback.md)**，本仓库保留旧版说明与测试版下载。旧 Replay Studio 仍限定 Mac Apple Silicon + MuMu 上的 Nulls Royale `15.535.13`（数据 `15.535.86`）和独立对局 HTML 导入；不得据此推断它已经使用 Clashback 的 `160635001` 原生接口。新功能优先跟踪 Clashback，旧项目作为历史版本/界面路线保留。
