---
id: royalefish
title: "RoyaleFish"
type: project
status: implemented
verification: author-documented
repository: https://github.com/fabiospalla9-tech/RoyaleFish
topics: [cr-ai-training, cr-native-engine]
maintainers: []
last_reviewed: "2026-11-12"
license: Apache-2.0
---

# RoyaleFish：基于原生战斗引擎的离线强化学习与自博弈

**上游**：[fabiospalla9-tech/RoyaleFish](https://github.com/fabiospalla9-tech/RoyaleFish) · **证据**：[README](https://github.com/fabiospalla9-tech/RoyaleFish/blob/main/README.md)（2026-11-12 阅读）· **等级**：R1 / author-documented，未进行固定提交源码审计或独立运行验证。

## 项目定位

社区驱动的《皇室战争》离线 AI，目标类似 Stockfish：公开模型基线，允许贡献更强的模型，支持研究和未来的离线对练。对局在本地模拟中进行。

## 模型与作者报告的结果

- `models/A-hog26-v98.pt`：野猪 2.6 专精模型，从预训练模型继续进行 98 次 PPO 更新。
- `models/B-general-v49.pt`：多卡组通用模型，49 次 PPO 更新，作为 A 的主要陪练。
- 两者使用约 1700 万参数的 recurrent V4 actor-critic，包含卡牌与单位 Transformer、竞技场空间编码器、LSTM 记忆。
- 作者报告 A v98 对起始检查点的 1056 场直接对抗胜率为 54.3% 对 45.7%；面对相同通用对手的另一测试中，微调后胜率为 59.7%（600 场），起始模型为 49.6%（561 场）。测试设置不同，不能外推为天梯胜率。

## 工程与性能

- 常驻原生战斗引擎：每进程 16 场、32 进程，最多 512 场并行，不使用 Android 模拟器。
- `ever_server.py`：批量观测、CUDA graphs、fp16、集中式 LSTM 状态表。
- `ever_collector.py`：流水化推进对局与推理；非法落点直接不执行，不自动吸附。
- 稀疏无损轨迹；`ever_learner.py` / `ever_packed.py` 的行打包 PPO 更新；`ever_loader.py` 的独立进程预加载；KL anchor 与弱势卡组加权采样。
- 作者报告 RTX 5060 Ti（对局）+ Tesla V100（学习）配置下约 2100 场完整对局/小时；每次 PPO 更新约 64 场、5.5 万决策，耗时 70–90 秒。均未独立复现。

## 依赖、复用边界

需要 Python 3.12、PyTorch、CUDA、`NOTICE` 中指定的开源 V4 框架及其 `native_runner`，**另需使用者自行提供原生战斗引擎**。仓库不分发游戏二进制、资源、修改客户端或引擎。Apache-2.0 是该项目声明的仓库许可证，不代表第三方游戏资产/引擎获得授权。

该项目的原生引擎具体版本、来源、可复现性，以及与 [Clashback](clashback.md)、[皇室战争复盘器](ashpp-replay.md) 的接口兼容性均未验证。

## 对知识中台的价值与待验证事项

1. **智能体环境**：研究原生对局状态到模型观测、合法动作及动作时序的映射。
2. **训练与评测**：研究自博弈、PPO、专精模型对抗通用模型及跨卡组测试设计。
3. **轨迹与复盘**：评估稀疏轨迹、逐帧状态保存、分支推演与可重复对局之间的接口边界。
4. **跨引擎验证**：需固定引擎构建、资源版本、随机种子和对局输入，逐 Tick 比较状态与行为。
5. **下一轮审查**：固定上游 commit，检查 `NOTICE`、`royalefish/config.py`、`ever_server.py`、`ever_collector.py`、`ever_learner.py` 与模型权重的可用性，再决定是否提升证据等级或登记实现关联。

**暂不新增已验证能力实现**：项目目前仅有 README 级证据，尚不能据此确认其 API 满足中台的能力契约。

[智能体环境](../capabilities/agent-environment/README.md) · [原生战斗驱动](../capabilities/battle-control/README.md) · [状态快照与恢复](../capabilities/snapshot-recovery/README.md)
