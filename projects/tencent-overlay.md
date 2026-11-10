---
id: tencent-overlay
title: "Tencent Overlay"
type: project
status: implemented
verification: author-documented
repository: https://github.com/ak1NaN/ClashRoyale-tencent-overlay
topics: [cr-runtime-observation]
maintainers: []
last_reviewed: "2026-11-10"
license: unknown
---

# Tencent Overlay

**原始仓库**：[ak1NaN/ClashRoyale-tencent-overlay](https://github.com/ak1NaN/ClashRoyale-tencent-overlay)。目前仅按作者文档编目，并未得到独立运行验证或作者加入确认。

## 公开实现的内容

macOS/ARM64 腾讯客户端覆盖层，按 README 显示部署队列事件、半场网格与圣水值。其 README 明确提醒升级到腾讯客户端 38.4.2 后原内存偏移已经不可用。

## 版本、运行与复用限制

旧偏移已失效；受客户端构建、Root/ADB/Frida、模拟器和 macOS 环境约束。不能将其他仓库的新偏移视为本仓库可用。

## 相关能力

- [对局状态观测](../capabilities/state-observation/README.md)：腾讯版客户端的部署队列覆盖层（R0，author-documented）

## 相关研究专题

- [运行时游戏状态观测](../topics/cr-runtime-observation.md)

## 来源

- [上游 README](https://github.com/ak1NaN/ClashRoyale-tencent-overlay)

**待核实**：精确上游提交、运行环境、独立复现测试以及上游作者审阅。

本项目涉及的逆向研究方法与跨版本限制已整理至 [逆向工程知识中心](../research/reverse-engineering/README.md)。

## 2026-11-10 上游维护状态

[2026-11-06 README 固定版本](https://github.com/ak1NaN/ClashRoyale-tencent-overlay/blob/00446d3f77e82acdf37c5ad5d859e68ed3069503/README.md) 顶部声明项目适配的是旧游戏包体，**作者不再更新和提供技术支持**。截至本次核查，GitHub 仓库的 `archived` 元数据仍为 `false`；这里所称“停止维护”依据 README，不能混写为 GitHub 已归档。18×32 网格、10 Hz 圣水覆盖和旧偏移只保留历史参考，不作为 38.4.5 或 16.635 当前可用接口。
