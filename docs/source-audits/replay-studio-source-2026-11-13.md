# replay-studio 源码局部审查（2026-11-13）

等级 P1。已枚举默认分支 Git tree（tree SHA: `a12f0b1b88ee31cb7743e75afb80471336bf0c90`），阅读以下源码；尚未冻结 commit 或执行测试。

- [app/engine.py](https://github.com/ak1NaN/ClashRoyale-replay-studio/blob/HEAD/app/engine.py) — blob `bf9c18d135e343f483d7ba78cccb24fbc36be399`
- [tests/test_precompute_cache.py](https://github.com/ak1NaN/ClashRoyale-replay-studio/blob/HEAD/tests/test_precompute_cache.py) — blob `4205609cbe949905facf478ae26c3c18dbe08901`

## 发现

app/engine.py 通过 TCP session-v1 控制原生战斗进程；RenderedEngine 支持 pause/advance-native、倍速。test_precompute_cache.py 定义 seek 使用 restore 并清空后续调度的 Mock 测试；这属于协议和单元测试证据，不能据此认定真实恢复已独立验证。

## 待核查

完整接口调用链、快照恢复后续推进、RNG/动作顺序、版本兼容、许可证、测试实际执行结果。不可由 P1 推断为完整审计或可复用组件验证。
