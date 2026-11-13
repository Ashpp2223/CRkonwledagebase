# ak1NaN/ClashRoyale-tencent-model-harness 局部源码审查（2026-11-13）

等级 **P1**；默认分支 Git tree SHA `f179ad40822bc51fb181c4ba26c1f49b15a861be`。仅核查列出的文件，未固定完整 commit 或运行测试。

- [ai_client/bridge.py](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness/blob/HEAD/ai_client/bridge.py) — blob `1fcd826c500b8cbdd09a86c8f37fbcdc9c360db2`
- [ai_client/model_input.py](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness/blob/HEAD/ai_client/model_input.py) — blob `9afa181dce2cb58c9f893afe82bec26eca0fbef9`
- [tests/test_bridge.py](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness/blob/HEAD/tests/test_bridge.py) — blob `ca68e9f76c5eabc2adde7e105cae951ad48887ee`
- [tests/test_model_input.py](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness/blob/HEAD/tests/test_model_input.py) — blob `ddccd71e20c3750570d85a76d23163b9925d826c`

## 发现

NativeStream 将 partial 与 complete 状态分流；完整队列溢出时报错，不静默跳过 LSTM 输入。跨 Android/macOS 时钟归一化，动作校验身份、卡槽、形态、圣水与 due_tick；动作状态年龄窗口 -100 至 750ms。inspect_live_input 不伪造缺失状态，四槽完整、coverage 全部齐备才 ready；其报告 execution_allowed=false。单元测试包含错误路径，但未执行。

## P2 待核查

继续审查 control/pipeline/policy/probes、第三方 FirstLight 许可和真实设备回执。
