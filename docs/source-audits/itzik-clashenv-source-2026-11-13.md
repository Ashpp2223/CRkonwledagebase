# itzik123/ClashRoyaleAi 源码局部审查（2026-11-13）

等级 **P1**。GitHub commit API 固定上游 `53a6ef7d029c29f4451bff148b0aba4991b7c7a1`。检查源码和测试定义，**未执行测试**，也未完成依赖、许可证与全流程核验。

- [perception/tests/test_live_freshness.py](https://github.com/itzik123/ClashRoyaleAi/blob/53a6ef7d029c29f4451bff148b0aba4991b7c7a1/perception/tests/test_live_freshness.py) — blob `4641e23ae420c75356a09dda23e8baf7053fa4fd`
- [perception/tests/test_action_gate.py](https://github.com/itzik123/ClashRoyaleAi/blob/53a6ef7d029c29f4451bff148b0aba4991b7c7a1/perception/tests/test_action_gate.py) — blob `aac7850fc8d798f0386bf769d3137c637170cb76`

## 源码证据与限制

实时行动闸门拒绝过时状态和同一画面重复行动；只有执行成功才记录消费，执行器失败允许重试。新画面等待策略根据生产者周期与等待上限判断，避免为了更新状态引入更大动作延迟。测试代码存在，但未运行，且部分依赖 windows_capture 可能跳过。

## 后续

检查完整实现、测试运行前置条件、输入样本来源、依赖及可复现结果，满足后再评估 P2。
