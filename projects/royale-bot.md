---
id: royale-bot
title: "RoyaleBot"
type: project
status: implemented
verification: author-documented
repository: https://github.com/RoyaleGym/RoyaleBot
topics: [cr-ai-environment, cr-runtime-observation]
maintainers: []
last_reviewed: "2026-11-10"
license: MIT
---

# RoyaleBot

**GitHub**：[RoyaleGym/RoyaleBot](https://github.com/RoyaleGym/RoyaleBot) · **最新核对提交**：`2dc24cea2576deac46a79bca099438d9d23b8ed6`（2026-11-05）

## 具体能力
[固定 README](https://github.com/RoyaleGym/RoyaleBot/blob/2dc24cea2576deac46a79bca099438d9d23b8ed6/README.md)：通过 `royalebot-play` 将 RoyaleLearn 的模型与经过准备的 Null's Royale Android 客户端联动，PC 端推理并回传卡牌动作；提供 `--dry-run`，可配合 RoyaleViser 调试。

## 适用构建
- [2026-11-05 固定 README](https://github.com/RoyaleGym/RoyaleBot/blob/2dc24cea2576deac46a79bca099438d9d23b8ed6/README.md) 声明 `rb-build 0.1.2` 已支持 **Null's Royale 16.635.1 与 15.535.13 / ARM64**；可用 `rb-build.exe check` 判断本地 APK 是否匹配。此工具为另行下载的 Windows 构建工具，非 Python 包自带。
- 新版训练配置由 [RoyaleGym 的 Null's 指南](https://github.com/RoyaleGym/RoyaleGym/blob/75075e5d1211b34cad6092a483e4f49111b74196/docs/site/pages/clash-royale/nulls-royale.md) 推荐 `cards.CARD_TABLE=client160635007_20261103`，但其对 Null's 16.635 实战录像尚无逐 Tick 校准证据；旧版 `15.535` 的模型成绩不能外推到新版。
- 不能推断官方客户端支持、原生离线 reset/step/snapshot/restore 或跨版本兼容。
- 本项目 R1 / author-documented / unverified；尚未实机测试。

[Agent 运行时](../capabilities/agent-runtime/README.md)
