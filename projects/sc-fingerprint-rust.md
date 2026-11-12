# SC Fingerprint Downloader Rust

- 上游：https://github.com/TrixallTR/SC-Fingerprint-Downloader-RUST
- 证据等级：R1 / author-documented（仅核查 README，未运行）
- 来源：https://github.com/TrixallTR/SC-Fingerprint-Downloader-RUST/blob/HEAD/README.md
- 许可：待核查；第三方游戏文件和素材不可因仓库公开而推定可再分发

## 技术价值与边界

Rust/Tokio 读取 Supercell fingerprint 文件，并行下载资源；主要为资产获取工具，不能据此推断解码或战斗规则能力。

## 后续验证

固定上游 commit；核查实现入口、依赖版本、许可证与测试；原生战斗相关项目需核对 Tick、状态恢复、输入与快照的一致性。当前不登记 R2/R3 能力实现。
