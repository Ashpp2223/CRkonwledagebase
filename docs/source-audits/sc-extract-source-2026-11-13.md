# nextonesfaster/sc-extract 局部源码审查（2026-11-13）

**等级 P1**。上游 HEAD commit `3a837dee0fbe9aa6b3d72ab99976e3b4497cebfc` 已由 GitHub commit API 核对。仅检查下列文件，未运行测试或完整依赖审计。

- [src/extractors/sc.rs](https://github.com/nextonesfaster/sc-extract/blob/3a837dee0fbe9aa6b3d72ab99976e3b4497cebfc/src/extractors/sc.rs) — blob `a3de005552790f42aca8946222620b447e811c9c`
- [src/extractors/csv.rs](https://github.com/nextonesfaster/sc-extract/blob/3a837dee0fbe9aa6b3d72ab99976e3b4497cebfc/src/extractors/csv.rs) — blob `b2c04b650ecc493ebba856684aae6df1e50e945a`

## 发现与适用边界

Rust 工具：SC sprite 提取要求先通过 QuickBMS 处理 .sc，且关联 _tex.sc PNG 已存在；内部解析 region、旋转、镜像及并行渲染。CSV 提取函数要求原始压缩数据，传入已解压 CSV 将返回解压错误。检查了测试文件目录，但未运行测试。

## 后续

继续核查其余模块、许可证、外部数据与测试可执行性，确认运行条件后再考虑 P2。
