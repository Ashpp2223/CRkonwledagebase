---
id: tencent-model-harness
title: "Tencent Model Harness"
type: project
status: implemented
verification: author-documented
repository: https://github.com/ak1NaN/ClashRoyale-tencent-model-harness
topics: [cr-runtime-observation, cr-ai-environment]
maintainers: []
last_reviewed: "2026-11-10"
license: Apache-2.0
---

# Tencent Model Harness

**原始仓库**：[ak1NaN/ClashRoyale-tencent-model-harness](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness)。目前仅按作者文档编目，并未得到独立运行验证或作者加入确认。

## 公开实现的内容

针对腾讯客户端 38.4.2 的 FirstLight V4 模型部署适配，公开描述了从原生状态映射到模型张量、推理、动作提交及回执记录的流程。

## 版本、运行与复用限制

需要对应的模型权重、ARM64 Android Root 运行环境及匹配的原生偏移；离线推理测试不代表所有真实对局可靠。

## 相关能力

- [对局状态观测](../capabilities/state-observation/README.md)：国服观测转换为 FirstLight V4 模型输入（R1，author-documented）
- [智能体环境与模型对接](../capabilities/agent-environment/README.md)：FirstLight V4 模型在腾讯客户端的推理部署（R1，author-documented）

## 相关研究专题

- [运行时游戏状态观测](../topics/cr-runtime-observation.md)
- [AI 训练环境与决策](../topics/cr-ai-environment.md)

## 来源

- [上游 README](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness)

**待核实**：精确上游提交、运行环境、独立复现测试以及上游作者审阅。

## 2026-11-10 上游维护状态

[2026-11-06 固定 README](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness/blob/f179ad40822bc51fb181c4ba26c1f49b15a861be/README.md) 明确声明旧包体适配项目**停止更新和技术支持**，当前偏移仍以腾讯客户端 `38.4.2` 为前提；仓库的 GitHub `archived` 标志在本次核查时为 `false`。文档描述的 FirstLight V4 张量映射、模型推理和回执日志有结构参考价值，但与后续国服 `38.4.5`/全球服 `16.635` 的接口兼容性未建立，不提高 R1 证据等级。
