# RoyaleGym/RoyaleImitate 局部源码审查（2026-11-13）

等级 **P1**。GitHub commit API 固定上游 commit `9d11681d4efe5d65290e492d9cabf14ad6a252d3`。仅检查列出的源码，未执行测试，未独立核实性能或训练数据。

- [royaleimitate/replays.py](https://github.com/RoyaleGym/RoyaleImitate/blob/9d11681d4efe5d65290e492d9cabf14ad6a252d3/royaleimitate/replays.py) — blob `27d6185d38560f2f3cd71a25b66a5fa9c39a93ec`
- [royaleimitate/alarms.py](https://github.com/RoyaleGym/RoyaleImitate/blob/9d11681d4efe5d65290e492d9cabf14ad6a252d3/royaleimitate/alarms.py) — blob `ae0a17759e3646f0add39e1cb2bc884380bc3a58`

## 源码结论

使用 IL_Replay 人类对局生成 imitation shards：按可解释的初始发牌顺序回放，未知卡、手牌无法解释、引擎拒绝、同决策冲突时跳过并计数；形态归一化为基础形态，不回放主动技能。对参考策略 KL 过高、约束系数饱和设警报。不能将这些样本视为无损原始对局。

## 后续

检查其他核心模块、依赖和许可证，阅读测试代码并实际运行可复现验证；验证版本兼容和输入数据的缺失/偏差处理。
