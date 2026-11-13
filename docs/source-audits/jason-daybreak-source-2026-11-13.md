# Jason-XII/daybreak-cr 源码局部审查（2026-11-13）

审查等级：P1。默认分支 main 的文件树 SHA `693057d14dd6f82f193050659a2bf20479f6f5e2`（86 条，未截断）。未冻结整体 commit；未运行测试。

## 仓库身份纠错

旧 URL `Jason-XII/clash-royale-battle-engine` 返回 GitHub Moved Permanently，repository ID `1366867946`；仓库搜索表明该 ID 当前属于 `Jason-XII/daybreak-cr`。旧源码引用的 commits `2b3361954c189a8ea508f3f54cf94a56c2e045fc` 与 `70a08af6807fa4d59a11c7d52bf6272a96afe30c` 均可通过当前仓库提交 API 查询。历史和当前实现可能有重大变化，不可混用 API 结论。

## 源码锚点

- [cr/engine.py](https://github.com/Jason-XII/daybreak-cr/blob/main/cr/engine.py)，blob `2fd09083a59241137e49048ec507c8e4abbe384b`：通过 `clapha-engine` 的 `CrxEnv` 接入原生模拟，定义 `HandCard`、`Player`、`Entity`、`State`、`Play`、`Transition`，以及下牌延迟与圣水处理。
- [cr/live_budget.py](https://github.com/Jason-XII/daybreak-cr/blob/main/cr/live_budget.py)，blob `e5de3dd79cbdef3b77f7e452f8685d4165fa6a82`：在途动作与延迟回执账本；同 Tick 扣费共同结算，避免遍历顺序制造额外圣水。
- [tests/test_engine.py](https://github.com/Jason-XII/daybreak-cr/blob/main/tests/test_engine.py)，blob `64b8f126d3e6e3d7dd3adf0351ba1ce38433784c`：用 Mock 原生环境检查能力按键、卡牌在途重叠、动作掩码与拒绝规则；测试未运行。
- [README.md](https://github.com/Jason-XII/daybreak-cr/blob/main/README.md)，blob `e1ffae469dcbe024002dcb87f377b4133b3843d5`：作者描述回放转训练样本、IL/PPO、评估与现场部署；性能与复现声明未独立验证。

## 复用判断

与旧版 `engine.py` 的接口、当前 `cr/engine.py` 及仓库外 `clapha-engine` 三者要分开标版本。单独该仓库无法证明完整原生引擎可部署；历史链接仍可用于研究，但新项目登记只保留一个。

## 待完成

完整审查 `convert.py`、`cr/engine.py`、`loop.py`、`tests/`、依赖与许可证；固定 commit；运行单元测试和跨版本回放一致性测试，满足后再升级 P2/P3。
