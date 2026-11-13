# Jason-XII/sc-decoder 源码审查（2026-11-13）

**审查等级 P1。** 已固定默认分支 HEAD commit `7b639d6b6a949522a71ebb8ae19552e58d71c157`（由 GitHub commit API 核实）。未运行测试，未覆盖全部核心文件，不能升级 P2。

## 实际读取源码与 blob SHA

- [sc_decoder.py](https://github.com/Jason-XII/sc-decoder/blob/7b639d6b6a949522a71ebb8ae19552e58d71c157/sc_decoder.py) — `c8dee4bcb58a2ca48be10c715b6f48cc1d40054b`
- [sc_pipeline.py](https://github.com/Jason-XII/sc-decoder/blob/7b639d6b6a949522a71ebb8ae19552e58d71c157/sc_pipeline.py) — `9b969f4713b8ec7e897af15995c51150c5086de6`

## 源码结论

SC 二进制读取器处理 little-endian tag stream、SC v4/v5 外层头、Zstd、KTX ASTC 纹理元信息及 shape/movie clip。pipeline 串联 .sc→JSON、纹理提取、精灵图预渲染和 pygame 查看器。大量 .sc 资源存在，但尚未独立运行解码；部分输入边界依赖文件格式正确。

## 后续检查

读取余下依赖、完整接口、测试与许可证，独立运行单元测试并检查数据/原生版本适用性。作者声明与测试代码均不当作运行证据。
