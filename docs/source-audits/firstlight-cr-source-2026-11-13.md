# firstlight-cr 源码普查记录（2026-11-13）

级别：P1（局部源码）。默认分支 tree SHA `4c82496ad5af49a3c7ea2392f26ff7bac33d9707`；仅阅读列出文件，未固定 commit 或运行测试。

- [native_runner/snapshot.py](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/HEAD/native_runner/snapshot.py) — blob `eaa1024b05a4fa9b2433f973ee394ba3f5720ca7`
- [native_runner/attestation.py](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/HEAD/native_runner/attestation.py) — blob `bf6cde75d465afdf4da27584237205f5c0a2db00`

## 发现与边界

snapshot.py 定义双方动作、起止 Tick 和推进 Tick 的操作日志序列化，不能单独证明完整原生状态快照。attestation.py 要求原生进程与 ruleset 的 libg/probe/content 哈希、包名、ABI 和版本完全对应，且 production_ready 为真；证据兼容性仅允许 probe 哈希及派生摘要变化。

## 后续

补查完整实现、依赖、许可证和测试；核对版本、状态一致性、实际运行结果。不能将作者声明或测试代码视作独立验证。
