# FirstLight Zero：文档交叉核验（2026-11-12）

上游：https://github.com/Jaasssoooonnnnn/FirstLight-Zero

证据：README、docs/architecture.md、docs/evaluation.md、docs/training_metrics.md；仅文档交叉核对（R1+），未固定 commit 审计源码，未执行环境与模型。

## 训练/观测合同

- 对战限定：11 级 X-Bow 镜像，8 张固定牌；两侧手牌顺序不同。
- 20Hz 引擎，策略每 5 Tick 决策（250ms）；每次至多出 1 张；部署延迟离散为 0/50/100/150/200ms；15 秒无动作时强制出牌。
- 观测：31 标量、8×5 我方卡、8×3 敌方卡、5×3 可选动作、最多 40×17 单位；本方坐标归一化。
- 模型：1.17M 参数，18×32 棋盘 CNN、LSTM 256、等待/出牌、卡牌、位置及价值头；来自 FirstLight V4 剪枝。
- 训练：当前策略与自身/历史快照对战，PFSP 抽样；终局 ±1、塔血 potential、溢费和激活己方国王塔惩罚；奖励零和。

## 评估与回放验证

- 对手 argmax，双方使用最早合法延迟；不加执行 jitter；40 局相同 seed 的版本扫描；作者报告的胜率是特定卡组、特定对手、特定协议下的结果。
- replay_export 生成 Parquet，payload_json 为 royaleapi-battle-actions.v1；附加 zero 块保存原始 episode 和全部动作。
- --check 验证 owner/card/position/tick 通过 loader 往返不变；replay_check 重驱后比较最终 Tick、皇冠、塔血、每次实际出牌。该验证范围不等于逐 Tick 全状态完全相等，也不等于支持任意 Tick 快照恢复。
- 训练 metrics 中 v151–200 explained variance 约 0.981，但作者称当时对 Boss 全败，说明价值函数拟合度不可直接等同于策略强度。

## 对复盘器的意义

可借鉴：原始动作轨迹 + 结构化 replay payload 双层保存、回放重驱校验、固定对局种子与版本契约、同一场对局的事件级差分。不能将重驱回放直接当作可分支的原生引擎快照。要支持逐帧分支，仍需核查 RNG、事件队列、内部实体状态和资源版本。

## 后续源码审计

检查 tools/replay_export.py、tools/replay_check.py、native_runner/royaleapi_replay.py、firstlight_zero/features.py、native_runner/probe/ 及测试；固定 commit 并独立执行 replay round-trip。
