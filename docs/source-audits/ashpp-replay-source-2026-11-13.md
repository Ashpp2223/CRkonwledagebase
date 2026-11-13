# ashpp-replay 源码局部审查（2026-11-13）

等级 P1。已枚举默认分支 Git tree（tree SHA: `45fbab62f56494d23035d2f85414275dc474af6a`），阅读以下源码；尚未冻结 commit 或执行测试。

- [bridge/clashback_engine.py](https://github.com/Ashpp2223/clashroyalereplay/blob/HEAD/bridge/clashback_engine.py) — blob `dff1106c0aadd7bb51a14afbd4f599bea15b17d4`
- [bridge/engine_adapter.py](https://github.com/Ashpp2223/clashroyalereplay/blob/HEAD/bridge/engine_adapter.py) — blob `45ccf4bd82d30f357d92fecda38bfe45dcc0345d`
- [src/domain/nativeReplay.ts](https://github.com/Ashpp2223/clashroyalereplay/blob/HEAD/src/domain/nativeReplay.ts) — blob `c5192be11d281a4a4bf6c1701f55f19d48300032`

## 发现

默认分支 codex/windows-native-engine-probe。Windows Clashback 适配器启动 AVD，ADB 通信，校验 libg.so 与配置指纹；engine_adapter.py 列出 legacy、cn-38.4.5、clashback-160635001 三套 profile。nativeReplay.ts 定义局面树、分支动作、引擎身份与工作分支数据结构。未核查所有调用路径、分支恢复是否可用。

## 待核查

完整接口调用链、快照恢复后续推进、RNG/动作顺序、版本兼容、许可证、测试实际执行结果。不可由 P1 推断为完整审计或可复用组件验证。
