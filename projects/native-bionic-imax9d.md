---
id: native-bionic-imax9d
title: "CR Native Linux Bionic"
type: project
status: implemented
verification: author-documented
repository: https://github.com/IMAX9D/cr-native-linux-bionic
topics: [cr-native-engine]
maintainers: []
last_reviewed: 2026-10-15
license: MIT
---

# CR Native Linux Bionic

**上游**：[IMAX9D/cr-native-linux-bionic](https://github.com/IMAX9D/cr-native-linux-bionic) · [查阅提交 7840e4e920fb](https://github.com/IMAX9D/cr-native-linux-bionic/tree/7840e4e920fb8c4d63efb16333c9451a16343c76)

## 有证据的技术资产

在 Linux x86_64 宿主中部署 Android API 31 Bionic linker/ART 和 Binderless JniHost，直接驱动版本固定的原版游戏 Worker，不启动 AVD/KVM。

**衍生价值**：与 CR Native Sandbox 搭配；目标 15.535.29，独立 Worker 槽、资源与文件哈希校验，适合离线大规模回放/训练。

## 适用边界

文档的版本与 ABI 锁为 x86_64 150535029，不能拿 ARM64 或其他客户端直接复用；无原生渲染和已证实的完整快照/恢复；中台未运行。

**验证状态**：根据固定提交中的仓库文档及公开代码入口编目；中台没有运行其游戏环境、二进制或完整回归测试。

[2026-10-15 来源网络调查](../landscape/2026-10-15-source-network.md) · [项目目录](README.md)
