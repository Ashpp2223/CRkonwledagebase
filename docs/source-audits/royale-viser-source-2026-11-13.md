# RoyaleGym/RoyaleViser 源码审查（2026-11-13）

**审查等级 P1。** 已固定默认分支 HEAD commit `d56f8fd4c76b112659d8a7a9582a5aaa3d7c21ba`（由 GitHub commit API 核实）。未运行测试，未覆盖全部核心文件，不能升级 P2。

## 实际读取源码与 blob SHA

- [royaleviser/parity.py](https://github.com/RoyaleGym/RoyaleViser/blob/d56f8fd4c76b112659d8a7a9582a5aaa3d7c21ba/royaleviser/parity.py) — `462e7069237e1ec4128b85064a3ba80f990b7ef9`
- [tests/test_first_divergence.py](https://github.com/RoyaleGym/RoyaleViser/blob/d56f8fd4c76b112659d8a7a9582a5aaa3d7c21ba/tests/test_first_divergence.py) — `81370472a9f3423ca61712821bc80279487ee9b2`

## 源码结论

可将 RoyaleSim 录制对比数据两侧渲染并定位首次分歧 Tick；坐标采用 native millitiles（1000/tile）。源码明确指出 parity 行仅覆盖匹配到的单位，未匹配实体需另读计数；缺圣水、手牌、牌组、最大生命时展示未知而不补造。首次分歧测试包括阈值变化、单侧实体缺失、单单位过滤；未运行。

## 后续检查

读取余下依赖、完整接口、测试与许可证，独立运行单元测试并检查数据/原生版本适用性。作者声明与测试代码均不当作运行证据。
