# TrixallTR/SC-ExportName-Extractor 局部源码审查（2026-11-13）

等级 **P1**。GitHub commit API 核实上游 commit `ecabf5dca5fc0dad02e3541d0fd27d81fa0a1484`。本轮仅阅读下列源码，未运行上游测试。

- [src/main.rs](https://github.com/TrixallTR/SC-ExportName-Extractor/blob/ecabf5dca5fc0dad02e3541d0fd27d81fa0a1484/src/main.rs) — blob `6a6db183b52775901eb7bdacd4c1d2cd3eaa3ad1`
- [src/reader.rs](https://github.com/TrixallTR/SC-ExportName-Extractor/blob/ecabf5dca5fc0dad02e3541d0fd27d81fa0a1484/src/reader.rs) — blob `f641b471d2ba555b9721ca72b458ec98aced47ff`

## 发现与限制

Rust 工具遍历当前目录非 _tex.sc 的 .sc 文件，按固定字节特征查找 export 名称，跳过 28 字节后读取小端 u32 长度 UTF-8 字符串，输出 extracted_*.txt。Reader 使用未显式检查边界的切片及 panic，特征匹配可能产生误报或越界；仅适合有格式证据的文件。

## 后续

补查完整实现、许可、依赖、边界输入与测试可执行性，达到完整证据链后再考虑 P2。
