# RoyaleGym 源码局部审查（2026-11-13）

审查层级：**P1（部分源码）**；Implementation 复用等级维持原状。未安装依赖、未运行测试、未完成全文件/全测试覆盖。上游默认分支 main；本轮记录所读文件 blob SHA，**尚未冻结完整上游 commit**。

## 实际读取的文件

- [README.md](https://github.com/RoyaleGym/RoyaleGym/blob/main/README.md)：blob `488c2e2f37dc6f9f98f7f981533946055f2c08c4`
- [pyproject.toml](https://github.com/RoyaleGym/RoyaleGym/blob/main/pyproject.toml)：blob `c7afe3b5423e9b2fadc7273abf4ac1fe37dfc4e0`
- [royalegym/__init__.py](https://github.com/RoyaleGym/RoyaleGym/blob/main/royalegym/__init__.py)：blob `087beec5365ab9576072cfded457fb4a12164d58`
- [royalegym/env.py](https://github.com/RoyaleGym/RoyaleGym/blob/main/royalegym/env.py)：blob `见上游当前文件；本次读取内容未取得 blob SHA 的完整固定提交证明`（待固定 commit 后复核）

## 直接可核对的实现与边界

1. `pyproject.toml` 定义 Python >=3.12，`gymnasium>=1.3,<2.0`、`pettingzoo>=1.27,<2.0`、`numpy>=2.0`、`msgspec>=0.19`；`sim` 额外依赖 `royalesim>=0.1.46`，`all` 还包含 RoyaleLearn、RoyaleViser、RoyaleImitate。此为最低版本约束，**不能当作精确可复现锁定版本**。
2. `__init__.py` 导出 `ClashParallelEnv`、`ClashGymEnv`、`ClashSelfPlayVecEnv`、`RustEngine`、`MockEngine`、`ReplayRecorder`、`verify_trace`、状态初始化器与观测/动作/奖励组件；注册显式 Mock/Rust Gym ID。
3. `env.py` 代码注释及可见定义区分 `MockEngine` 和 `RustEngine`：默认未指定引擎会警告，Mock 的法术、击退、眩晕等行为与 Rust/游戏存在差异。**不能用 Mock 训练结果证明原版战斗能力**。
4. `env.py` 说明决策步长按引擎 Tick 向上取整，双方动作针对同一前置状态验证；观测携带 `action_mask` 与 `mask_planes`，非法动作转换为 no-op 并写入部署状态。以上时序和异常处理还需追踪完整函数体及测试核实。
5. `pyproject.toml` 配置 pytest 测试目录和 Ruff 规则，**仅证明存在测试配置，不证明 CI 或测试通过**。

## 后续 P2 必须完成

- 固定仓库 commit；核对 `protocol.py`、`rust_engine.py`、`action.py`、`obs.py`、`replay.py`、`state_mutator.py` 的实际函数体和跨模块调用。
- 枚举 `tests/`，验证 action mask、双玩家动作顺序、Mock/Rust 分离、轨迹验证、快照恢复、Gym/PettingZoo API 合同及测试是否覆盖。
- 明确 RoyaleSim 版本和数据校准覆盖；评估确定性、状态序列化和跨引擎一致性的边界。
- 本轮未运行仓库校验脚本，亦未运行 RoyaleGym 测试；不能标 P2/P3。
