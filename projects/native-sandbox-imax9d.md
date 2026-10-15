---
id: native-sandbox-imax9d
title: "CR Native Sandbox"
type: project
status: implemented
verification: author-documented
repository: https://github.com/IMAX9D/cr-native-sandbox
topics: [cr-native-engine, cr-ai-environment]
maintainers: []
last_reviewed: 2026-10-15
license: MIT
---

# CR Native Sandbox

**上游**：[IMAX9D/cr-native-sandbox](https://github.com/IMAX9D/cr-native-sandbox) · [查阅提交 8c8443e26c42](https://github.com/IMAX9D/cr-native-sandbox/tree/8c8443e26c4250f3ae8cd5d09298080ae9d8a782)

## 有证据的技术资产

原版 Android x86_64 `libg.so` 离线无画面战斗宿主；通过 JniHost/AssetManager/JNI 初始化，提供 reset、step、双方动作、原生观测与 JSON-line Worker。

**衍生价值**：固定 15.535.29 / 150535029，20Hz，按客户端、资源与哈希冻结；可作为回放重建、模拟器差分与训练数据真值来源。

## 适用边界

依赖精确的 x86_64 APK/资源及受控宿主；不能推出 16.402.12 或腾讯 38.4.2 已可用；不提供记谱器所需的原生战场画面或有证据的通用快照契约。

**验证状态**：根据固定提交中的仓库文档及公开代码入口编目；中台没有运行其游戏环境、二进制或完整回归测试。

[2026-10-15 来源网络调查](../landscape/2026-10-15-source-network.md) · [项目目录](README.md)
