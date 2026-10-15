---
id: cr-native-sandbox
title: "CR Native Sandbox"
type: project
status: implemented
verification: author-documented
repository: https://github.com/IMAX9D/cr-native-sandbox
topics: [cr-native-engine, cr-replay-state, cr-ai-environment]
maintainers: []
last_reviewed: "2026-10-15"
license: MIT
---

# CR Native Sandbox

**上游：**[https://github.com/IMAX9D/cr-native-sandbox](https://github.com/IMAX9D/cr-native-sandbox)；**证据：**[固定版本](https://github.com/IMAX9D/cr-native-sandbox/tree/8c8443e26c4250f3ae8cd5d09298080ae9d8a782)。

## 已知技术成果

针对原始 x86_64 libg.so（15.535.29）的无画面原生战斗 Worker。使用 JNI/JniHost 与 DataTables，支持创建、逐 Tick 推进、两边动作、观测和回放重驱。

## 适用边界

固定游戏与资源构建；需要匹配的合法 Runtime；无原生画面。未在中台本地运行；作者测量不作为中台集成证据。

## 对中台的可复用价值

- 从 [项目—能力矩阵](../registry/implementations.yaml) 找到这项技术可支撑的具体任务，不由项目整体评分代替单项证据。
- 优先复用**接口语义、版本指纹、验证与实验方法**；需要运行时再核对依赖、资源和授权。
- 目前仅为公开源码/文档证据；中台没有进行第三方集成测试。

[技术网络与开发者追踪](../landscape/2026-10-15-developer-network.md)
