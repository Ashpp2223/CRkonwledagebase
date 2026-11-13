# RoyaleGym/RoyaleBot 源码审查（2026-11-13）

**审查等级 P1。** 已固定默认分支 HEAD commit `2dc24cea2576deac46a79bca099438d9d23b8ed6`（由 GitHub commit API 核实）。未运行测试，未覆盖全部核心文件，不能升级 P2。

## 实际读取源码与 blob SHA

- [royalebot/bridge.py](https://github.com/RoyaleGym/RoyaleBot/blob/2dc24cea2576deac46a79bca099438d9d23b8ed6/royalebot/bridge.py) — `15b1d307380f0f667dca01b5d3bd372906b84a2f`
- [tests/test_play_channel.py](https://github.com/RoyaleGym/RoyaleBot/blob/2dc24cea2576deac46a79bca099438d9d23b8ed6/tests/test_play_channel.py) — `977b3a79d1a2a744adade3196b2d3ba78040830b`

## 源码结论

Bridge 将 RoyaleViser 实时帧转为 RoyaleGym/RoyaleLearn 的 BattleState，推理后生成手牌槽与落点；wire 1000/tile、engine 18000/tile，换算 18 倍。每席位只允许一条在途下牌；40 Tick 后仍未换手牌视作未生效，累计三次停止。play channel 测试覆盖消息格式、protocol/1、拒绝回执、在途与错误席位；未运行。

## 后续检查

读取余下依赖、完整接口、测试与许可证，独立运行单元测试并检查数据/原生版本适用性。作者声明与测试代码均不当作运行证据。
