---
id: cr-native-linux-bionic
title: "CR Native Linux Bionic"
type: project
status: implemented
verification: author-documented
repository: https://github.com/IMAX9D/cr-native-linux-bionic
topics: [cr-native-engine]
maintainers: []
last_reviewed: "2026-10-15"
license: MIT
---

# CR Native Linux Bionic

**上游：**[https://github.com/IMAX9D/cr-native-linux-bionic](https://github.com/IMAX9D/cr-native-linux-bionic)；**证据：**[固定版本](https://github.com/IMAX9D/cr-native-linux-bionic/tree/7840e4e920fb8c4d63efb16333c9451a16343c76)。

## 已知技术成果

Linux x86_64 的 Android Bionic linker + ART 用户态；在不启动 AVD/KVM 的前提下加载构建 150535029 的原始 libg.so，启动进程隔离的 Worker 并提供原生 JSON-line TCP 接口。

## 适用边界

版本锁定 15.535.29 x86_64/API31；依赖独立 Runtime Bundle 与 root 部署；目前不是 ARM64/16.402 的现成方案，不带原生渲染或可任意恢复的快照。

## 对中台的可复用价值

- 从 [项目—能力矩阵](../registry/implementations.yaml) 找到这项技术可支撑的具体任务，不由项目整体评分代替单项证据。
- 优先复用**接口语义、版本指纹、验证与实验方法**；需要运行时再核对依赖、资源和授权。
- 目前仅为公开源码/文档证据；中台没有进行第三方集成测试。

[技术网络与开发者追踪](../landscape/2026-10-15-developer-network.md)
