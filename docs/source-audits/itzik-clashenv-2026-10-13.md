# ClashRoyaleEnv 快照与搜索：静态审计（2026-10-13）

核查的固定版本：[`2f172925a15b`](https://github.com/itzik123/ClashRoyaleAi/tree/2f172925a15b17f973291f41a789b19a29f0fc43)。

- [`include/core/GameManager.h#L254-L268`](https://github.com/itzik123/ClashRoyaleAi/blob/2f172925a15b17f973291f41a789b19a29f0fc43/include/core/GameManager.h#L254-L268)：`snapshot()` 构造复制对象、对棋盘执行 deepCopy、复制统计数据，避免分支间共享实体。
- [`src/bindings.cpp#L170-L180`](https://github.com/itzik123/ClashRoyaleAi/blob/2f172925a15b17f973291f41a789b19a29f0fc43/src/bindings.cpp#L170-L180)：把 `ClashEnv::snapshot` 作为 Python `snapshot()` 暴露，并返回独立对象。
- [`tests/core/test_game_manager_snapshot.cpp`](https://github.com/itzik123/ClashRoyaleAi/blob/2f172925a15b17f973291f41a789b19a29f0fc43/tests/core/test_game_manager_snapshot.cpp)：包含深拷贝一致、原件无污染、双方手牌圣水、随机一致性等源代码测试。
- [`python_ai/search/search.py#L211-L238`](https://github.com/itzik123/ClashRoyaleAi/blob/2f172925a15b17f973291f41a789b19a29f0fc43/python_ai/search/search.py#L211-L238)：每个候选前创建 snapshot 并 rollout，展示了快照能力如何衍生出前瞻搜索。

**判断范围**：R2/source-inspected 仅确认上述源代码存在、设计思路及可定位的测试源码；没有运行 Catch2、Python 或真实对局测试。README 报告的 7–20 微秒分叉、约 10ms 完整对局和卡牌覆盖都没有独立验证。

**核心差别**：这是**作者自行重写的 C++ 模拟器状态深拷贝**，不同于 FirstLight/复盘器的原生游戏进程句柄。前者适合可分叉搜索，但仿真和真实客户端的一致性需要另外证明。

## 中台可衍生的技术规范

- 将 `fork(source_state)` 视为**候选接口设计问题**，不能声称所有引擎已支持相同 ABI。
- 搜索引擎须记录状态复制成本、每秒完成 rollout 数、是否可并行、是否复制 RNG/未来事件与统计。
- 对搜索的候选动作评分必须防止原局污染，对相同 seed/动作可复现。
- 实机对照与真实比赛强度不能由模拟器内对局自动推断。
