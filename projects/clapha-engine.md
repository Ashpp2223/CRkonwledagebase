---
id: clapha-engine
title: "Clapha Engine（非公开）"
type: project
status: research
verification: author-documented
repository: https://github.com/arronwang01/clapha-engine
topics: [cr-native-engine, cr-ai-environment]
maintainers: []
last_reviewed: "2026-10-15"
license: unknown
---

# Clapha Engine（非公开）

**上游：**[https://github.com/arronwang01/clapha-engine](https://github.com/arronwang01/clapha-engine)；**证据：**[固定版本](https://github.com/Jason-XII/clash-royale-battle-engine/blob/70a08af6807fa4d59a11c7d52bf6272a96afe30c/clapha.py)。

## 已知技术成果

由 Jason-XII 在公开 clapha.py 与协作文档中间接证明的第三方原生引擎：Linux x86_64、进程内加载 libg.so、无模拟器、CrxEnv.create_match / step；可供 PPO 自博弈。

## 适用边界

上游仓库为私有，无法审查加载器、具体函数偏移、快照或版本升级方法；仅引用 Jason 的公开适配器，不称为中台可直接安装的组件。公开适配记录针对构建 150535029。

## 对中台的可复用价值

- 从 [项目—能力矩阵](../registry/implementations.yaml) 找到这项技术可支撑的具体任务，不由项目整体评分代替单项证据。
- 优先复用**接口语义、版本指纹、验证与实验方法**；需要运行时再核对依赖、资源和授权。
- 目前仅为公开源码/文档证据；中台没有进行第三方集成测试。

[技术网络与开发者追踪](../landscape/2026-10-15-developer-network.md)
