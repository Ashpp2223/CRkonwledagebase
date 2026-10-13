---
name: review-cr-evidence
description: "Verify technical claims, review pinned source code, assess reverse-engineering findings and version applicability, and decide R0-R4 reuse maturity for this Clash Royale technical knowledge base. Use when auditing evidence or upgrading verification grades; not for merely listing projects."
---

# 源码证据、逆向发现和成熟度审查

此 Skill **只审核可证据化的具体陈述**，而不是为整个项目打笼统的“可信分数”。

## 审核路径

1. 先准确摘出**要审核的 claim**，确认关联的 Project、Capability 或 ReverseFinding 以及记录中的游戏构建、ABI、资源版本、客户端分支。
2. 读取上游原始文档或源码，优先固定 Git SHA 及具体文件/行区间；把作者的声称和自己实际检查过的内容分开。
3. 区分 `author-documented`（文档声称）、`source-inspected`（静态源码已定位实现）、`reproduced`（独立复现实验）。不能通过阅读 README 获得 `reproduced`。
4. 审核相反证据、测试失败、版本迁移：旧内存偏移、错误的模拟器保真、已失效功能不得默默保留“当前可用”表述。
5. 只提升**被审核的单条 Implementation 或 ReverseFinding**，不得因某个函数的存在提升整个仓库等级。
6. 保存核查报告：对象、固定提交、代码入口、前置依赖、观察、负例、未验证部分和对接用途。文档路径用仓库相对路径，所有结论可从入口页定位。

## 等级门槛

| 记录级别 | 必须具有 |
| --- | --- |
| R0/R1 | 可追踪来源、能力边界与未知条件 |
| R2 | `reviewed_commit` 40 位 SHA、`evidence` 固定 permalink、现存 `audit_path`、审查内容与排除范围 |
| R3 | 可复现的独立集成证据、环境与版本、许可结论、测试日志；`verification: reproduced` |
| R4 | R3 加实际维护责任、支持范围、回归机制与维护证据 |

详细门槛见 [成熟度标准](../../../docs/reuse-maturity.md)。`R2` 只证明指定实现源码被审查，**不等于设备执行成功**。

## 逆向专项

- 按 [逆向研究方法](../../../research/reverse-engineering/methodology.md) 记录假设、反例、字段身份、验证方式和失效条件。
- 区分模块偏移、对象字段偏移及运行时堆地址；跨 `libg.so` SHA、ABI、客户端渠道或 manager generation，重新核验后方可复用。
- 将 `memory_exact`、`inferred`、`estimated` 与未知字段分开，不将合成事件流伪装成同一 Tick 的完整状态。
- 无权限或无可用实验环境时，明确保留 `unknown` / `not-run`，不能补造结果。

## 提交前检查

对受影响的 YAML/Markdown 同步更新来源与链接，执行两个验证命令，PR 中列出“证明了什么 / 未证明什么”。