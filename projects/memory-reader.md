---
id: memory-reader
title: "CR Memory Reader"
type: project
status: implemented
verification: author-documented
repository: https://github.com/Jason-XII/cr-memory-reader
topics: [cr-runtime-observation]
maintainers: []
last_reviewed: null
license: unknown
---

# CR Memory Reader

**原仓库**：[Jason-XII/cr-memory-reader](https://github.com/Jason-XII/cr-memory-reader)。**初次整理**：2026-10-13。仅依据公开作者文档，尚未得到原作者审核，也未独立测试。

## 公开描述的能力

通过原生内存/探针研究读取圣水、手牌、皇家塔血量及场上实体；包含 My Own Findings 阶段研究记录。

## 兼容与限制

内存布局与游戏版本紧耦合；Windows 和 macOS 路线有差异。

## 相关专题

- [运行时游戏状态观测](../topics/cr-runtime-observation.md)

## 证据

- [仓库 README](https://github.com/Jason-XII/cr-memory-reader)
- [补充来源](https://github.com/Jason-XII/cr-memory-reader/blob/main/My%20Own%20Findings.md)

## 待复核

- 实际运行能力、对应提交 SHA、准确兼容版本、维护者确认和授权边界。

本项目涉及的逆向研究方法与跨版本限制已整理至 [逆向工程知识中心](../research/reverse-engineering/README.md)。
