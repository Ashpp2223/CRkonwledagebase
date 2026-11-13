# royalesim 源码局部审查（2026-11-13）

等级 P1。通过 GitHub API 枚举默认分支文件树（truncated=false），tree SHA `a83f55c20bdb157a15af7877c7758ff331c0d1c3`；抽样阅读以下文件前段。未冻结整体 commit，未执行测试。

- [crates/royalesim/src/spell.rs](https://github.com/RoyaleGym/RoyaleSim/blob/main/crates/royalesim/src/spell.rs) — blob `1a24a11435367c348af7918bf8915031969c1341`
- [crates/royalesim/tests/hash_continuity.rs](https://github.com/RoyaleGym/RoyaleSim/blob/main/crates/royalesim/tests/hash_continuity.rs) — blob `285f28c703e5ea1001c8429abea7b92517bbd1f7`

## 发现与限制

Rust 工程位于 crates/royalesim/Cargo.toml。spell.rs 包含法术、击退、眩晕缓冲和 Tick 阶段的实现；hash_continuity.rs 定义固定脚本对局的逐 Tick 哈希跨变更对比，处理卡表索引变化。未运行 cargo test。

## 待查

完整函数体、测试、依赖、许可证；固定 commit；验证 Tick/RNG/快照/版本一致性，达到标准后再升 P2/P3。
