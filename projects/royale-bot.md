---
id: royale-bot
title: "RoyaleBot"
type: project
status: implemented
verification: author-documented
repository: https://github.com/RoyaleGym/RoyaleBot
topics: [cr-ai-environment, cr-runtime-observation]
maintainers: []
last_reviewed: "2026-10-15"
license: MIT
---

# RoyaleBot

**GitHub**：[RoyaleGym/RoyaleBot](https://github.com/RoyaleGym/RoyaleBot) · **固定源码提交**：`a2ff261d7323b64fe78455c9c50a06cc4846ca5e`

## 具体能力
[固定 README](https://github.com/RoyaleGym/RoyaleBot/blob/a2ff261d7323b64fe78455c9c50a06cc4846ca5e/README.md)：通过 `royalebot-play` 将 RoyaleLearn 的模型与经过准备的 Null's Royale Android 客户端联动，PC 端推理并回传卡牌动作；提供 `--dry-run`，可配合 RoyaleViser 调试。

## 适用构建
- 作者限定 **Null's Royale 客户端 15.535.13 / ARM64**；模型训练推荐 RoyaleGym `make_env(client="15.535.29")` 的规则配置，不能混淆设备客户端和仿真规则两个版本。
- 客户端准备工具 `rb-build` 单独发布，不属于该 Python 包源码。
- 不能推断官方客户端支持、原生离线 reset/step/snapshot/restore 或跨版本兼容。
- 本项目 R1 / author-documented / unverified；尚未实机测试。

[Agent 运行时](../capabilities/agent-runtime/README.md)
