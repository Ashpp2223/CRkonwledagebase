# RoyaleGym 源码局部审查（2026-11-13）

审查层级：**P1（部分源码）**；Implementation 复用等级维持原状。未安装依赖、未运行测试、未完成全文件/全测试覆盖。上游默认分支 main；本轮记录所读文件 blob SHA，**尚未冻结完整上游 commit**。

## 实际读取的文件

- [README.md](https://github.com/RoyaleGym/RoyaleGym/blob/main/README.md)：本次未取得可信 blob SHA，待固定
- [pyproject.toml](https://github.com/RoyaleGym/RoyaleGym/blob/main/pyproject.toml)：blob `c7afe3b5423e9b2fadc7273abf4ac1fe37dfc4e0`
- [royalegym/__init__.py](https://github.com/RoyaleGym/RoyaleGym/blob/main/royalegym/__init__.py)：blob `087beec5365ab9576072cfded457fb4a12164d58`
- [royalegym/env.py](https://github.com/RoyaleGym/RoyaleGym/blob/main/royalegym/env.py)：本次读取但未记录 blob SHA，待固定 commit 后复核

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

## 2026-11-13 第二轮：跨模块源码与测试检查

以下均读取上游默认分支文件，记录文件 blob SHA；**未冻结仓库整体 commit**，也未运行测试。

| 文件 | blob SHA | 核查要点 |
| --- | --- | --- |
| [royalegym/action.py](https://github.com/RoyaleGym/RoyaleGym/blob/main/royalegym/action.py) | `17ed83a7880dfe85ecd190887ab36cc2d5b96a6f` | `Discrete(2305)`，卡牌/落点联合掩码，PlacementOracle 与引擎独立判断 |
| [royalegym/replay.py](https://github.com/RoyaleGym/RoyaleGym/blob/main/royalegym/replay.py) | `071726945836e700072b12bf7a12a681f0d3de3f` | 初始配置+动作+周期状态哈希重模拟；frame 含实体、法术、弹体、手牌和 next card |
| [royalegym/rust_engine.py](https://github.com/RoyaleGym/RoyaleGym/blob/main/royalegym/rust_engine.py) | `50fba2ac4b04a7b35489fad1efd4c531fdf38abb` | Rust core adapter，部署理由映射，卡表哈希、编译校准防陈旧检查 |
| [royalegym/state_mutator.py](https://github.com/RoyaleGym/RoyaleGym/blob/main/royalegym/state_mutator.py) | `3ccd8f0c4a70b22e74b101b8c02cf15cf1ac11ed` | Snapshot.blob、观察记忆 memory、seat/max_ticks/tag；msgpack bank 版本检查 |
| [royalegym/protocol.py](https://github.com/RoyaleGym/RoyaleGym/blob/main/royalegym/protocol.py) | `23d63524b340f282366bb8a7ad084bba51f4a741` | 整数 subtile 坐标、双方 180° 旋转、千分之一圣水、引擎数据目录 |
| [tests/test_rust_engine.py](https://github.com/RoyaleGym/RoyaleGym/blob/main/tests/test_rust_engine.py) | `64adae16bdd67147a244b75f0df3d10131aa2e1a` | 定义动作合法性、500 步随机掩码、确定性、分段 Tick、快照恢复、旋转对称等测试 |
| [tests/test_parity_hardening.py](https://github.com/RoyaleGym/RoyaleGym/blob/main/tests/test_parity_hardening.py) | `e88a52ee79aaa2c527d09cba8e9a191aa2d1892d` | 生成顺序、非法初始值、卡表差异和 Mock/Rust 协议边界；缺 Rust 扩展会跳过测试 |

### 技术价值与限制

- **动作接口**：联合动作掩码避免卡牌与位置分开掩码导致的非法组合；与原版客户端动作的对应关系仍需独立校准。
- **回放**：动作序列+哈希可以验证同引擎同版本重演；不能据此推出跨版本或与官方客户端逐 Tick 相同。
- **分支**：引擎状态快照与观察记忆分离，对保留复盘分支的信息集有参考价值；尚未验证任意帧快照和可重复分支的全部实现。
- **一致性**：测试源码包含对抗回归用例，但未运行，因此仅证明有测试设计，不证明当前版本通过。

### 后续未完成

完整审阅各文件剩余函数体、实际枚举所有测试、固定 commit、核对 RoyaleSim Rust 端实现及其依赖与 CI、独立运行。维持 P1，不提升 P2。
