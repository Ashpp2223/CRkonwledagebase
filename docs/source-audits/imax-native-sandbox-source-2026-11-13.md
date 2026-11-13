# IMAX9D/cr-native-sandbox 局部源码审查（2026-11-13）

等级：**P1**，仅部分源码检查；未运行原生宿主、回归或知识库校验；上游完整 commit 未冻结。本文只核对可见代码与文档，不把作者的性能/验收声明视作独立实测。

## 已读取文件与 blob

- [README.md](https://github.com/IMAX9D/cr-native-sandbox/blob/main/README.md)：上游项目说明，未记录 blob。
- [pyproject.toml](https://github.com/IMAX9D/cr-native-sandbox/blob/main/pyproject.toml)：`00229d88f44ce53f1b1bc1ff646d1dcb653c6808`
- [native_core/__init__.py](https://github.com/IMAX9D/cr-native-sandbox/blob/main/native_core/__init__.py)：`0359b6e5e4794664739b57db2dc5d6bffe2810ac`
- [native_core/env.py](https://github.com/IMAX9D/cr-native-sandbox/blob/main/native_core/env.py)：`12b9828bdccee823d9a6a384153ce1b65509c710`
- [native_core/worker.py](https://github.com/IMAX9D/cr-native-sandbox/blob/main/native_core/worker.py)：`45bb28f24bbae725aca5c4d337b3a55e4dda5d4e`
- [docs/SANDBOX_RUNTIME_TECHNICAL.zh-CN.md](https://github.com/IMAX9D/cr-native-sandbox/blob/main/docs/SANDBOX_RUNTIME_TECHNICAL.zh-CN.md)：`8a1bb88ba210521c9980dae456807037b726bf29`

## 初步结论

1. `NativeRoyaleEnv` 公开 `reset/observe/act/step` 风格的同步 API；`reset` 要求 replay 含 battle 对象，向本地 JSON-line 服务提交 reset，并可 warmup 到指定 tick；`attach` 复用已有 worker 引导状态。这里的 `reset` 是原生服务操作，不能未经验证视作任意帧可逆快照。
2. `worker.py` 明确依赖 rootable Android x86_64 AVD 和 `app_process`；Android 是 ABI/进程容器，运行无 Surface 的原生服务，**不等于完全无 Android 环境**。Linux 无 AVD/KVM 是另一个仓库的部署路线。
3. `pyproject.toml` 要求 Python >=3.11，训练可选依赖 torch>=2.8；Python 包本身不能替代匹配的 APK、libg.so、JNI Bridge、DataTables 与运行时校验。
4. 主技术文档明确绑定 15.535.29 / 150535029 x86_64，20Hz；列出 JNI/Java 宿主、版本锁定、RVA 与原生 Tick 路线。作者称全卡/形态等通过测试，但本轮未复现。
5. 与 RoyaleGym/RoyaleSim 的自建规则模拟器不同，这条路线调用版本锁定的原始 libg；比较复盘分支和确定性时，需额外确认 RNG、进程隔离、快照格式及恢复语义。

## P2 待查

- 实际审阅 `native_core/client.py`、`android_probe/native/jni_bridge.cpp`、`android_probe/java/royale/nativehost/JniHost.java` 的关键函数与错误处理。
- 枚举并阅读 tests，检查版本拒绝、RNG、Replay、重置、Tick、动作与状态哈希的测试实现及覆盖；固定整体上游 commit。
- 审核原生文件来源和许可证限制，条件允许时用合法匹配 Runtime 独立运行 smoke。
- 本次没有运行任何上游测试或知识库校验，维持 P1。
