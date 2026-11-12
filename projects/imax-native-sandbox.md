# CR Native Sandbox

- 上游：https://github.com/IMAX9D/cr-native-sandbox
- 证据等级：R1 / author-documented（仅核查 README，未运行）
- 来源：https://github.com/IMAX9D/cr-native-sandbox/blob/HEAD/README.md
- 许可：待核查；第三方游戏文件和素材不可因仓库公开而推定可再分发

## 技术价值与边界

原版 Android x86_64 libg.so 20Hz headless 1v1、reset、观测与 TCP JSON-line API；绑定 150535029 构建。训练分支、MuMu ARM64 另有不同的验证边界；原版游戏文件不随仓库提供。

## 后续验证

固定上游 commit；核查实现入口、依赖版本、许可证与测试；原生战斗相关项目需核对 Tick、状态恢复、输入与快照的一致性。当前不登记 R2/R3 能力实现。
