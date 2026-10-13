# 技术中台：架构与信息模型

## 定位

**能力是检索主轴，项目是实现来源，专题是研究网络，契约是候选兼容协议，指南是任务路径。** 不持有他人代码，不主张不同版本的 ABI 相同。

```text
开发需求 / AI 查询
      ↓
capabilities/ + registry/capabilities.yaml  # 能力定义与验收问题
      ↓
registry/implementations.yaml               # 项目×能力×成熟度×证据
      ├── projects/                           # 作者、源码、许可、版本
      ├── topics/                             # 原理、差异、未解问题
      ├── contracts/                          # 候选协议（Draft，非现实 API）
      └── guides/                             # 任务接入与验证步骤
```

## 实体边界和不变量

- **ReverseFinding**：单条带版本、来源、状态的逆向事实或研究线索，保存在 [reverse-findings.yaml](../registry/reverse-findings.yaml)。它不等同于 Project/Implementation，也不是 R3 的可集成组件。历史协议或失效偏移只能作为历史证据。

- **Project**：一个可追踪的上游仓库；不同仓库不能因为同一作者而被合并为一条（已将 Tencent Overlay/Model Harness 与 RoyaleGym/RoyaleSim 分开）。
- **Capability**：一个稳定的开发需求/复用能力，`id` 不随文案修改。它不代表某个软件已经提供公共 SDK。
- **Implementation**：一个 `(capability, project)` 关联；保留说明、限制、证据、独立成熟度和集成状态，唯一 `id` 为 `capability--project`。
- **Topic**：跨项目研究主题，描述实现原理和技术争议，不作为能力的第二份重复注册表。
- **Contract**：**建议中的**规范，不能称为现有上游接口；任何社区标准化须经协商和明确版本。
- **Evidence**：源链接可确认结论来源，但不能单独证明其运行正确；`last_reviewed: null` 表示未有人工作废/时效复核。

所有 ID 使用小写英文与短横线。注册表只保存结构化链接和精简说明；正文以 Markdown 为准。不要在项目与能力两侧重复维护同一张可修改的实现矩阵。

## 兼容性与版本

无统一动作/状态 ABI。最少应显式表达：游戏构建、资源指纹、座标单位和朝向、Tick 时基、输入生效时刻、实体 ID 生命周期、可观测性与失败处理。

[状态协议草案](../contracts/battle-state-v0-draft.md) 与 [动作协议草案](../contracts/battle-action-v0-draft.md) 是未来适配器设计参考，**不可冒充已被任何项目支持**。

## 生命周期与迁移

首期维持 GitHub + Markdown + YAML，无后端、数据库或 RAG 依赖。只有当索引检索已不能满足社区需求，并能提供证据版本过滤与引用追溯时，才考虑搜索服务。

已有 `topics/` 路径保持不变（避免旧链接失效）；旧的 `projects/tencent-tools.md` 保留迁移指引，不再作为独立仓库索引。

[架构决策记录](adr/0001-capability-center.md) · [证据/成熟度规则](reuse-maturity.md)

## 长期维护协议

`AGENTS.md` 记录不变量，`.agents/skills/` 记录按任务激活的操作步骤，`docs/maintainer-handbook.md` 记录面向人的维护/移交规则，`docs/editorial-standards.md` 规范技术写作，`scripts/validate*.py` 是自动化结构检查。不同职责不应复制粘贴同一份长规则。
