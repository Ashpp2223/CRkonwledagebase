# 源码审查：Simulator Trial 与 FirstLight Zero（2026-11-12）

审查方式：直接读取 GitHub 文件内容及其 blob SHA，未本地执行。R2 为**限定文件的源码核查**，不代表完整项目 R2 或 R3。

## 1. arronwang01/clash-royale-simulator-trial

上游：https://github.com/arronwang01/clash-royale-simulator-trial

读取：
- `src/clasher_new/preflight.py` blob `3b788540033c4a098014c16d622612daaef7c087`
- `SIMULATOR_STATUS.md` blob `290a2f930a4664210a4b9242bc17a46a0d7b9d5a`
- `TRAINING.md` blob `5fe52f064399ca94789a3490cf5cc6c0d728d4b6`

源码确认：preflight 实际调用 `test_action_masks.main()` 对照 mask 与引擎、检查两侧 mask 非空、单进程 256 步训练、2 局 eval 非法动作率必须为 0；只有 `--n-envs > 1` 才检查并行训练。默认运行并不覆盖多进程；设备检查默认要求 CUDA（显式 cpu 除外）。这些是存在的**验证入口**，并不等于我们运行通过。

项目自己的状态报告明确留下严重未决问题：玩家报告单位交互表现异常；最后一轮摆放修复后未重新验证单位互斗；全局轨迹对齐误差随时间增长，中局达到 1–2+ 格。塔射程校准曾因伤害归属错误产生伪精确结论，后续纠正。训练报告还指出早期动作非法率曾达 91%，旧实验对比因此不可信。

判定：有独立价值的八卡 Python 模拟器实验及验证反例；**不应作为高保真皇室战争战斗引擎**收录。应标为“存在已知严重行为偏差、研究/实验用途”。

## 2. Jaasssoooonnnnn/FirstLight-Zero

上游：https://github.com/Jaasssoooonnnnn/FirstLight-Zero

读取：
- `tools/replay_check.py` blob `019862d9adbe4109ea54cd0de1ab97cbaf797d8c`
- `tools/replay_export.py` blob `b756ea1276b9785748d4244d0f636c38cc4ec6a9`

源码确认：`replay_check.py` 用记录的 matchup/seed/level 构造 episode，按记录 tick 向原生环境送出 ActionV1，收集 `action_executed` 事件。判定 identical 要求 episode 相等、最终 tick、皇冠、按 owner 汇总的塔血比例（四位小数）及动作事件列表一致。**不会比较每个 Tick 的单位位置、血量、弹道、内部随机状态**。因此其“exact replay”含义严格限于该脚本的比较谓词。

源码边界：`collect()` 忽略没有 `card_id` 的事件（包括英雄能力），代码注释写“ability compared via ability_events”，但此文件的 `identical` 谓词未见单独比较 ability_events；需进一步追踪外层记录和其他测试。最终塔血是各方塔 HP 总和 / 总最大 HP，且 round(...,4)，不能证明逐塔精确一致。

`replay_export.py` 将执行事件转换成 `royaleapi-battle-actions.v1` 的 `play_card` / `activate_ability`，另保留 `zero.native` 的原始 episode、逐次提交动作及 fate。坐标转换根据 owner 翻转、18×32 格子离散化，保留 native 原始坐标作为补充；同 tick 多次出牌根据提交动作顺序排序，避免仅靠 card_id 事件顺序破坏牌序推断。

判定：**回放事件导出与原生重驱验证的优秀实现参考**，但并无证据证明任意帧完整快照/分支恢复。对复盘器可借鉴双层事件格式、动作顺序与版本/种子合同、严格区分执行动作和提交动作。

## 后续优先源码

- Simulator Trial：`src/clasher_new/battle.py`、`pathfinding.py`、`environment.py`、`test_action_masks.py`，验证异常交互的实际路径。
- FirstLight Zero：`native_runner/royaleapi_replay.py`、`firstlight_zero/actions.py`、`tools/replay_export.py` 后半段、`native_runner/probe/`；核实英雄能力和事件漏检。
- 所有项目仍需固定 commit 和独立运行，不能以 blob 检查替代端到端一致性实验。
