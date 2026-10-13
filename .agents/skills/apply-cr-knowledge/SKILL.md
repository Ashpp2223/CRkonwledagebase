---
name: apply-cr-knowledge
description: "Answer a developer's concrete Clash Royale engineering question using this knowledge base: locate reusable capabilities, compare implementations, provide version-aware source-backed recommendations and minimum validation steps. Use when choosing an engine, designing a replay/AI tool, or deciding whether to reuse an upstream result; not for changing repository records."
---

# 将中台知识应用到具体开发任务

**目标**：让开发者从“要做什么”直接走到“已有方案、能够复用的部分、必须验证的边界”。

## 检索路径

1. 将问题写成**实际工程条件**：用户要的结果、输入、运行平台、游戏构建（如果已知）、性能或精度约束。没有的条件标为未知，不自行补全。
2. 查 [能力目录](../../../capabilities/README.md) / [能力注册表](../../../registry/capabilities.yaml) 定位目标需求；若查询的是原理、旧版偏移或研究事实，则查 [专题](../../../topics/README.md) / [逆向知识中心](../../../research/reverse-engineering/README.md)。
3. 查 [实现矩阵](../../../registry/implementations.yaml) 与相关 [项目卡](../../../projects/README.md)，选出**真实候选**；对每项读取它的 `reuse_level`、`verification`、`integration`、`limits`、`evidence`。
4. 对含有版本或接口比较的推荐，核对源地址、固定 SHA 和领域差异（原生/重写模拟器、FAIR/完整观测、进程快照/深拷贝等）。
5. 根据用户用途给**最少但足够的候选**，输出推荐依据、明确不适用的条件和可执行的最小验证，不堆砌 GitHub 仓库名。

## 结果结构（按任务调整）

- **建议路线**：优先使用何类技术及原因；如果没有已验证方案，必须写明。
- **候选实现**：项目、已知接口或研究、版本/依赖、证据级别、许可状态。
- **接入差距**：需要自行写适配器的字段、Tick、坐标或状态生命周期问题。
- **最小实验**：用什么可重复场景证明“适合本项目”，怎样记录失败。
- **来源**：直接给原仓库源码或测试的固定版本链接、对应中台知识页。

问“能否直接集成”时，`R1/R2` 不能回答“可以直接集成”；**只表示知识可参考或特定源码已检查**。如果用户只想学原理，优先给技术解释而不是大量权限/许可套话。

## 不得混淆

- 项目 A/B/C 编辑优先级 ≠ R0–R4 复用成熟度。
- 私有原生探针和公众可安装库不是同一个交付物。
- 原生进程内 snapshot、重写引擎 fork、状态序列化、动作日志重放不是同一个契约。
- 模拟器中赢得比赛不能直接外推为真实游戏胜率。
- 历史逆向 offset/协议不能当作最新客户端的已验证事实。
- 无法访问的源码/测试不能被表述为已经检查完成。

仅需回答问题时**不要修改中台索引**。发现文档明显失真，可给出待修订事项并调用 [research-cr-knowledge](../research-cr-knowledge/SKILL.md) 和 [curate-cr-knowledge](../curate-cr-knowledge/SKILL.md) 的流程处理后续变更。
