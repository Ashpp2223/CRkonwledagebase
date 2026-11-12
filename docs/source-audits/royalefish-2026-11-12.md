# RoyaleFish 固定提交源码核查（2026-11-12）

**上游固定提交**：[`e94f9d6b3c17c5e308272d01d6fdfe0e312201e9`](https://github.com/fabiospalla9-tech/RoyaleFish/tree/e94f9d6b3c17c5e308272d01d6fdfe0e312201e9)。**范围**：README、NOTICE、LICENSE、`royalefish/config.py`、`ever_server.py`、`ever_collector.py`、`ever_learner.py`、`ever_loader.py`、`ever_packed.py`；均位于 `royalefish/` 包内（配置亦然）。仅静态源码审查，未执行 Python、CUDA、原生引擎或对局。

## 已从源码确认

| 子系统 | 代码入口 | 静态结论 |
| --- | --- | --- |
| 模型推理 | [ever_server.py](https://github.com/fabiospalla9-tech/RoyaleFish/blob/e94f9d6b3c17c5e308272d01d6fdfe0e312201e9/royalefish/ever_server.py) | `load_policy_v4` 来自 FirstLight `native_runner`；使用 TCP + pickle 消息、批量推理、CUDA Graph、GPU 上的 LSTM 状态池；支持从 `latest.pt` 热加载权重 |
| 对局采集 | [ever_collector.py](https://github.com/fabiospalla9-tech/RoyaleFish/blob/e94f9d6b3c17c5e308272d01d6fdfe0e312201e9/royalefish/ever_collector.py) | 导入 `ResidentNativeClashEnv`、`ResidentBatchCoordinatorV1` 等 FirstLight 接口；合法性检查保留模型原选落点，不合法则跳过 |
| 训练 | [ever_learner.py](https://github.com/fabiospalla9-tech/RoyaleFish/blob/e94f9d6b3c17c5e308272d01d6fdfe0e312201e9/royalefish/ever_learner.py) | 使用 V4 PPO 数据结构，维护训练/参考模型、KL anchor、critic warmup、优化器与检查点 |
| 训练数据 | [ever_loader.py](https://github.com/fabiospalla9-tech/RoyaleFish/blob/e94f9d6b3c17c5e308272d01d6fdfe0e312201e9/royalefish/ever_loader.py) / [ever_packed.py](https://github.com/fabiospalla9-tech/RoyaleFish/blob/e94f9d6b3c17c5e308272d01d6fdfe0e312201e9/royalefish/ever_packed.py) | 按长度与观测 schema 分组；解包稀疏轨迹；将数据转换为按 dtype 分缓冲区的行打包格式 |
| 配置 | [config.py](https://github.com/fabiospalla9-tech/RoyaleFish/blob/e94f9d6b3c17c5e308272d01d6fdfe0e312201e9/royalefish/config.py) | 默认 `decision_ticks=5`、`GAMEPLAY_END_TICK=6000`、`BASE_LATENCY_TICKS=1`、headless |
| 依赖与许可 | [NOTICE](https://github.com/fabiospalla9-tech/RoyaleFish/blob/e94f9d6b3c17c5e308272d01d6fdfe0e312201e9/NOTICE) / [LICENSE](https://github.com/fabiospalla9-tech/RoyaleFish/blob/e94f9d6b3c17c5e308272d01d6fdfe0e312201e9/LICENSE) | 模型权重基于 FirstLight CR 已发布检查点微调，代码依赖 FirstLight V4；仓库 Apache-2.0，不包含第三方游戏引擎和资源 |

**复用判断**：可确认“训练流水线代码存在”，但该仓库本身不是可独立启动的完整游戏引擎。可登记 `agent-environment` 的**限定范围 R2 静态源码审查**；不能据此提升 `battle-control`、`snapshot-recovery` 或模拟器保真等级。

## 具体风险与待复验条件

1. **LSTM 池满后的状态丢弃**：`ever_server.py` 的 `row_for` 在池满时按最近使用时间回收旧 key。重入 key 会被标记为新状态并重置 LSTM；需要压测并核对最大并发 key 数、驱逐频率和对策略的影响。
2. **权重热更新与隐藏状态版本**：`maybe_reload` 直接复制新权重；已有比赛的 LSTM 状态池不会整体清空。应核查混合版本状态是否影响训练行为，以及 collector 对返回版本号的处理。
3. **异常轨迹边界**：`ever_loader.py` 计算 `L=min(len(rew),len(data),len(act))` 后直接访问 `e['data'][L-1]`、`term[L-1,j]`。若出现零长度轨迹，可能索引错误或错误标记；需要加入输入有效性约束与测试。此处是源码层面的潜在缺陷，尚未实际复现。
4. **推理服务信任边界**：`ever_server.py` 通过 `pickle.loads` 解码 TCP 消息，默认监听 `127.0.0.1`。只应在受信任本机环境使用，不应直接暴露到不可信网络。
5. **上游依赖强耦合**：`native_runner`、V4 观测 schema、动作序列和模型检查点需匹配 FirstLight 的特定接口；尚未建立依赖版本锁定或跨版本兼容矩阵。
6. **性能/胜率**：README 的 512 并发、约 2100 场/小时、4 倍更新提速及胜率均为作者报告；静态源码无法确认实际吞吐、统计误差、实验随机性和独立可复现性。
7. **逐帧存档与分叉**：该训练流水线的轨迹保存用于 PPO 数据，不能等同于 Clashback 的原生逐 Tick 可恢复快照，也不能证明可任意分叉、跨进程恢复或与用户复盘器兼容。

## 最小验收建议

- 固定 FirstLight 框架提交、原生 `libg.so` 构建、资源版本、模型 checkpoint SHA256 与 CUDA/PyTorch 版本。
- 用同一随机种子与动作序列复跑，验证原生 Tick、动作合法性和轨迹一致性。
- 压测 LSTM 状态池容量及热加载前后同场策略，统计隐状态被回收的次数。
- 制造空轨迹、损坏 NPZ、缺失 schema、异常网络断线和模型热加载失败，验证是否丢数据或错误更新。
- 按 README 两种胜率测试口径分别复现，并记录对手池、换边、样本量、置信区间和完整日志。

**结论**：RoyaleFish 是值得纳入知识库的 FirstLight V4 原生训练工程案例，当前可静态确认其数据/模型流水线。对战强度、吞吐量、快照分支及跨引擎一致性仍属未验证项。
