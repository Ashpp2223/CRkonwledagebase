# hastylmao/Hasty-CR 源码局部审查（2026-11-13）

等级 **P1**。GitHub commit API 固定上游 `ac4ef71194167e97f34550fc91c026b6d707a0cd`。检查源码和测试定义，**未执行测试**，也未完成依赖、许可证与全流程核验。

- [sim/engine.py](https://github.com/hastylmao/Hasty-CR/blob/ac4ef71194167e97f34550fc91c026b6d707a0cd/sim/engine.py) — blob `2f6c25e4dec45deb1248ceeb3ef03dab8bcbfa22`
- [tests/test_calibration_evidence.py](https://github.com/hastylmao/Hasty-CR/blob/ac4ef71194167e97f34550fc91c026b6d707a0cd/tests/test_calibration_evidence.py) — blob `09c6adbe2a0ae4747fec7c48b06aaf4270e4d602`

## 源码证据与限制

引擎源码区分客户端数据给出的生命、伤害、射程、移速、质量等参数与仍属近似的寻敌、路径、碰撞、Tick 顺序。校准测试明确断言 real_measurements == 0、readiness == NOT_READY、cross_implementation_is_truth == false；这是重要的证据成熟度警告。

## 后续

检查完整实现、测试运行前置条件、输入样本来源、依赖及可复现结果，满足后再评估 P2。
