# TrixallTR/SC-Fingerprint-Downloader-RUST 局部源码审查（2026-11-13）

**等级 P1**。上游 HEAD commit `0849a4e4d21ef5387568151c4943ad77b256d963` 已由 GitHub commit API 核对。仅检查下列文件，未运行测试或完整依赖审计。

- [src/main.rs](https://github.com/TrixallTR/SC-Fingerprint-Downloader-RUST/blob/0849a4e4d21ef5387568151c4943ad77b256d963/src/main.rs) — blob `4ce631d7db5dfa99db338dd7d6312bd7f1a2633e`

## 发现与适用边界

Rust/Tokio fingerprint 下载器读取本地 fingerprint.json 或远程 sha 对应清单，拼接 {url}/{sha}/{file}，用 Semaphore 将并发上限设为 10，已存在目标路径则跳过。未见写入后哈希校验、临时文件原子提交或重试；直接创建目标文件可能留下部分下载文件。

## 后续

继续核查其余模块、许可证、外部数据与测试可执行性，确认运行条件后再考虑 P2。
