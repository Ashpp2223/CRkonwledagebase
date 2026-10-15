# 2026-10-15：Longling CR / R2-Dreamer 环境桥接源码审查

**对象**：`agent-environment--longling-simulator`；**固定 SHA**：`6086b9cac917cbdd479405091f90bca85b9bd66b`；**级别**：R2 / source-inspected，未运行本地/训练/实机测试。

## 静态确认

1. [`r2dreamer/envs/cr.py`](https://github.com/longlingking/clash-royale-simulator/blob/6086b9cac917cbdd479405091f90bca85b9bd66b/r2dreamer/envs/cr.py#L52-L153) 包装 `CREnv`，观测 `grid(32,18,15)`、`hand(5)`、`elixir(1)`、`is_first/is_last/is_terminal`，网格尺度归一化并处理 NaN/inf。
2. 同一文件设置 `Box(shape=(5,32,18))` 且 `multi_discrete=True`；实际由三段多 one-hot 构成，**合计 55 维**，不是 5×32×18 个独立动作；`step` 按 slot(5)、y(32)、x(18) 的 argmax 投到 `CREnv.step((slot,y,x))`。
3. [`envs/cr_opponents.py`](https://github.com/longlingking/clash-royale-simulator/blob/6086b9cac917cbdd479405091f90bca85b9bd66b/r2dreamer/envs/cr_opponents.py) 提供对手快照池与 RSSM 隐状态管理，配套 [测试定义](https://github.com/longlingking/clash-royale-simulator/blob/6086b9cac917cbdd479405091f90bca85b9bd66b/tests/test_cr_selfplay.py)。测试代码存在**不代表已在本中台运行通过**。
4. `cr.py` 在 import 时改变 `os.getcwd()`；主进程中的对手模块避免提前 import 它，否则日志和 checkpoint 路径可能错误。

## 否定范围/复验门槛

- 原生客户端逐 Tick 保真、模型收敛、显存与训练吞吐、对战水平都未独立核验；部分训练用例因未提供 checkpoint 可跳过。
- 先固定 Python 3.11、卡牌 JSON、依赖与模拟器提交，在隔离环境执行 `python smoke_cr.py`、`pytest tests/test_cr_selfplay.py`，记录 stdout/退出码，再测试训练/原生对照才可考虑 R3。
