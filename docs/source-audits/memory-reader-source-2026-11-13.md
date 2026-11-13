# memory-reader 源码普查记录（2026-11-13）

级别：P0（仅 README 与目录枚举）。默认分支 tree SHA `9af94ca2f273ce526dda6256bdbd5d5555fb82d4`；仅阅读列出文件，未固定 commit 或运行测试。

- [README.md](https://github.com/Jason-XII/cr-memory-reader/blob/HEAD/README.md) — blob `6e16be5f545fa136cf2de062ae78b787176cdf84`

## 发现与边界

本轮仅读取 README 和完整目录树：作者说明 macOS Frida 与 Windows MuMu 内存读取两条路径，状态流需在 Python 端聚合；尚未读具体采集源码，故保留 P0。

## 后续

补查完整实现、依赖、许可证和测试；核对版本、状态一致性、实际运行结果。不能将作者声明或测试代码视作独立验证。
