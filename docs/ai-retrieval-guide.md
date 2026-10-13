# AI 检索与回答规则

## 默认检索路径

用户意图 → `registry/capabilities.yaml` → 能力卡 → `registry/implementations.yaml` → 项目资料卡和原始证据 → 相关 `topics/` → 仅在需要时参考 Draft `contracts/` 与 `guides/`。

**示例：**“需要 MCTS 快速克隆任意对局状态” → 查 `snapshot-recovery`；读取 [恢复能力](../capabilities/snapshot-recovery/README.md) 与 [集成验证](../capabilities/snapshot-recovery/integration.md)；区分进程内快照、逐 tick 缓存、日志重放和并行克隆。不能把它们归为同一项已验证功能。

## 每次输出建议包含

- 候选实现（作者、仓库和证据链接）
- 技术路线 / 适用游戏版本与环境（不知道就写未知）
- **复用成熟度** R0–R4、**证据等级**与**集成状态**
- 已知失效、协议差异、法律/许可门槛
- 可行的最小实验及仍未确认的条件

## 不允许的推断

- 从源代码公开直接推断拥有复制、分发权限。
- 从 README 中“测试通过”提升为本中台已复现实验。
- 从 reset/step 推断任意历史状态克隆。
- 从相容回放推断获取全部隐藏初手/原始种子。
- 从前一版本客户端的内存偏移推断新版本仍生效。
- 从 Draft 契约推断第三方已实现该 API。

查“项目是谁”的问题可直接走 `projects/`；查机制学术问题可先看 `topics/`。这些是导航入口，而非统一执行流程。
