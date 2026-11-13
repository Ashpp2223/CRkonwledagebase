# voonhous/crforge 源码局部审查（2026-11-13）

等级 **P1**。GitHub commit API 固定上游 `69277c1002499da7c23932c303c41ac00bd82eaa`。检查源码和测试定义，**未执行测试**，也未完成依赖、许可证与全流程核验。

- [conformance/src/main/java/org/crforge/conformance/ReferenceComparison.java](https://github.com/voonhous/crforge/blob/69277c1002499da7c23932c303c41ac00bd82eaa/conformance/src/main/java/org/crforge/conformance/ReferenceComparison.java) — blob `29944729c61312a86fe72cfca1aa474274af53ff`
- [conformance/src/test/java/org/crforge/conformance/ReferenceBattlesTest.java](https://github.com/voonhous/crforge/blob/69277c1002499da7c23932c303c41ac00bd82eaa/conformance/src/test/java/org/crforge/conformance/ReferenceBattlesTest.java) — blob `2b7629b5b39be7750d7425a55073f7d2dde72482`

## 源码证据与限制

参考对局比较器校验 trace SHA256、tick 连续性、终止状态与身份，逐字段严格比较首次差异，不容忍整数/小数类型差异。参考战斗测试依赖外部 reference 目录和游戏表；未配置时使用 JUnit assumeTrue 跳过，因此 CI 成功不自动意味着参考对局一致性通过。

## 后续

检查完整实现、测试运行前置条件、输入样本来源、依赖及可复现结果，满足后再评估 P2。
