# vegetableleaf/ClashAI 源码局部审查（2026-11-13）

等级 **P1**。GitHub commit API 固定上游 `21e28ae2b101a70e7f3a1218d149d343b860b49d`。检查源码和测试定义，**未执行测试**，也未完成依赖、许可证与全流程核验。

- [pipeline/tests/test_tornado_river.py](https://github.com/vegetableleaf/ClashAI/blob/21e28ae2b101a70e7f3a1218d149d343b860b49d/pipeline/tests/test_tornado_river.py) — blob `8cc6f16ed1f8ba425dde430a36f292a079ed967e`
- [pipeline/tests/test_branch_score.py](https://github.com/vegetableleaf/ClashAI/blob/21e28ae2b101a70e7f3a1218d149d343b860b49d/pipeline/tests/test_branch_score.py) — blob `442ec920aa0eb79ed70b8be873e7fe38acecaabf`

## 源码证据与限制

旋风河道测试将地面单位的跨河吸引限制在岸边/桥面边界，并与空中单位区分；测试注释引用 RoyaleSim 0.1.33，仍须追溯真实客户端证据。分支评分比较 play/hold，终局优先按胜负打分，未终局可使用塔/phi 评价；标签包含多次采样的标准误差权重，刻意不把已花圣水当作独立惩罚。

## 后续

检查完整实现、测试运行前置条件、输入样本来源、依赖及可复现结果，满足后再评估 P2。
