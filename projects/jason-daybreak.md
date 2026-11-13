# Daybreak CR — 历史登记别名

该仓库与 [Jason Battle Engine / Daybreak CR](jason-battle-engine.md) 是同一个 GitHub repository ID（1366867946），现已合并登记为 `jason-battle-engine`。本文件保留作为旧链接入口；请以主项目页和 [源码审查总账](../docs/source-audits/full-repository-audit-tracker-2026-11-12.md) 为准。

## 合并前的研究笔记

# Daybreak CR — Jason-XII

- 上游：https://github.com/Jason-XII/daybreak-cr
- 证据等级：R1（README 核查，未固定提交源码审计、未运行）
- 与已收录 [Jason Simulator](jason-simulator.md)、[CR Memory Reader](cr-memory-reader.md) 属同作者不同技术路线；不能默认共享引擎或数据契约。

## 价值

- `convert.py`：将真人回放按版本 oracle 的 assignment 分配到匹配原生引擎，重驱并原子写入每场样本；失败标记 rejected。
- `train.py` / `cr/imitation.py`：按游戏样本分块的模仿学习；有 checkpoint、验证和实验消融。
- `arena.py` / `ppo.py` / `loop.py`：原生模型对战、PPO 收集与训练、冻结 champion/challenger、评估晋级、回滚和恢复。
- `play.py`：模拟器客户端内存读取与模型决策执行；客户端 reader 位于仓库外的私有目录。
- `cr/observation.py`、`policy.py`、`engine.py`、`matchmaking.py`、`actors.py`：观测、动作掩码、引擎适配、对手池和采集协议。

## 限制

依赖仓库外的 `clapha-engine`、原生游戏构建/资源、回放与客户端内存 reader；没有据此证明单仓库可复现。README 提及训练性能和消融结果均为作者报告。需核对第三方资源和许可。原生回放重驱的数据样本不等于任意 Tick 的可恢复快照。

## 后续

固定 commit；重点审查 `convert.py` 的版本匹配与拒收逻辑、`cr/engine.py` 的状态/动作接口、`loop.py` 的晋级门禁和 `tests/`；与 FirstLight、ClashBack、IMAX9D 原生沙盒的观测与时间基准做兼容性矩阵。
