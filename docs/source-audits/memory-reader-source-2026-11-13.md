# memory-reader 源码普查记录（2026-11-13）

级别：P0（仅 README 与目录枚举）。默认分支 tree SHA `9af94ca2f273ce526dda6256bdbd5d5555fb82d4`；仅阅读列出文件，未固定 commit 或运行测试。

- [README.md](https://github.com/Jason-XII/cr-memory-reader/blob/HEAD/README.md) — blob `6e16be5f545fa136cf2de062ae78b787176cdf84`

## 发现与边界

本轮仅读取 README 和完整目录树：作者说明 macOS Frida 与 Windows MuMu 内存读取两条路径，状态流需在 Python 端聚合；尚未读具体采集源码，故保留 P0。

## 后续

补查完整实现、依赖、许可证和测试；核对版本、状态一致性、实际运行结果。不能将作者声明或测试代码视作独立验证。

## 2026-11-13 第八轮补充：P0→P1

上游 Git tree `9af94ca2f273ce526dda6256bdbd5d5555fb82d4`，进一步检查：

- [deploy/hook_raw_capture.js](https://github.com/Jason-XII/cr-memory-reader/blob/main/deploy/hook_raw_capture.js)，blob `3a69c1b60fbc63b89725b970b83e8188e3a483f8`：Frida 以 libg.so 固定 RVA 读取 tick、手牌、塔与单位字段。
- [queue_overlay/hook_queue_deploy.js](https://github.com/Jason-XII/cr-memory-reader/blob/main/queue_overlay/hook_queue_deploy.js)，blob `a7a6cef5531168cdd3952fe5cb2ba14d35e8dad2`：拦截队列构造，10ms 轮询、3s 去重、原生坐标转换。
- [x86_64/deploy/proc_memory.py](https://github.com/Jason-XII/cr-memory-reader/blob/main/x86_64/deploy/proc_memory.py)，blob `f05ba17bcbbd643280b9eaad6ed36159eb2b59a2`：root adbd 读取 /proc/PID/mem，处理映射区域和内存快照读取。

**结论**：本项目是运行时只读观测和部署事件采集，不能由 `_ArenaSnapshot` 类名推断其支持原生战斗状态恢复。偏移强依赖版本。未运行测试，未审查完整采集主流程、许可和样本一致性。
