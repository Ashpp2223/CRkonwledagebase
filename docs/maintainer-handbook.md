# 维护者手册

## 仓库目标

持续积累皇室战争相关技术的**可追溯知识、实现能力与复验方法**。维护成功的衡量标准是开发者能通过需求定位已有成果、知道哪些版本适用、如何验证，而非项目卡数量。

## 结构与单一事实源

| 实体 | 单一索引 | 正文职责 |
| --- | --- | --- |
| Project | `registry/projects.yaml` | `projects/`：仓库身份、作者、技术范围和限制 |
| Capability | `registry/capabilities.yaml` | `capabilities/`：开发需求、候选实现、选择条件 |
| Implementation | `registry/implementations.yaml` | 不为关联另建重复记录；能力卡用于有价值的比较 |
| Topic | `registry/topics.yaml` | `topics/`：原理、技术路线、分歧与反例 |
| ReverseFinding | `registry/reverse-findings.yaml` | `research/reverse-engineering/`：构建限定的可证据事实 |
| Relationship | `registry/relationships.yaml` | 有证据的派生/依赖关系；不是兼容保证 |
| Contract/Guide | Markdown 正文 | `contracts/` 是 Draft；`guides/` 是任务验证路径 |

**身份与关联**：Project ID 指向单个上游仓库；Capability ID 指向稳定的需求边界；Implementation ID 格式为 `capability--project`。更名优先调整显示标题，禁止无迁移计划地改变 ID。

## 接手仓库：15 分钟路线

1. 阅读 [README](../README.md)、[AGENTS](../AGENTS.md)、[架构说明](architecture.md)。
2. 看 [能力索引](../registry/capabilities.yaml) 和 [实现索引](../registry/implementations.yaml)，理解“能力≠组件可安装”。
3. 阅读 [复用成熟度](reuse-maturity.md) 与 [逆向发现规范](../research/reverse-engineering/methodology.md)。
4. 跑 `python scripts/validate.py` 与 `python scripts/validate_skills.py`，确认基线没有结构/链接问题。
5. 选择一个真实修正任务，从最小 PR 开始；不需要先阅读所有项目文章。

## 知识生产与长期复用

遇到新的技术问题，使用 [知识研究 Skill](../.agents/skills/research-cr-knowledge/SKILL.md) 抽取版本化证据；需要跨来源解释时使用 [知识综合 Skill](../.agents/skills/synthesize-cr-knowledge/SKILL.md)，并按 [知识生命周期规范](knowledge-workflow.md) 保留命题、适用域、反例与下一步实验。之后由取证审查和编目流程写回中台。

遇到开发者复用请求，使用 [知识应用 Skill](../.agents/skills/apply-cr-knowledge/SKILL.md) 从具体需求返回候选技术、依赖差异与可检验的接入方法。**没有必要为每个问题增加 Markdown 文件**；优先更新已存在的能力卡或技术专题。

第一份具体范例：[快照/深拷贝/序列化/重放之间的语义差异](../research/knowledge-notes/snapshot-semantics.md)。

## 维护任务的标准流程

1. **界定变化**：新增/修订的是项目事实、能力、实现关系、逆向发现、接口草案还是文章解释。
2. **检查重复**：先检索已存在 ID 与同义功能。优先更新已有实体，而不是泛滥新增能力分类。
3. **固定证据**：为重要结论记录来源、Git SHA、适用构建和负面条件。仅作者文档的陈述不得标记为中台实测。
4. **改正文与索引**：保证人类阅读入口和 YAML 数据一致。一次 PR 尽量围绕单个意图；批量迁移要写明映射。
5. **验证**：运行两个验证命令，更新模板/Skill 时还要核查路径、激活描述和指令冲突。
6. **审查与合并**：按 [PR 审查 Skill](../.agents/skills/review-cr-pr/SKILL.md) 自检，记录未验证项、来源风险和修改范围。合并以实际 CI 为准。

## PR 级别和审核重点

| 改动 | 必审内容 |
| --- | --- |
| 文字纠错 | 术语精度、链接、是否改变既有结论 |
| 新项目 | 仓库身份、许可证、是否已有重复 ID、专题双向关联 |
| 新能力 | 使用场景是否独立、是否至少有一个具体来源实现、索引完整性 |
| 实现评级变更 | 只评某项目的某项能力；R2 固定源码/审计，R3 真实集成证据 |
| 逆向记录 | Build/ABI/libg SHA、作者事实和推断区分、历史适用性 |
| Contract | Draft 标签、兼容边界、不要假定现有仓库已有该 API |
| Skill/CI | Agent Skills 元数据格式、路径、误触发风险、CI 能真实运行 |

## 事实过期与争议

- 上游仓库删除/归档：保留历史事实和可定位来源，降低当前可用性评估，避免直接删除有价值的研究。
- 游戏更新导致字段失效：标注 `invalidated` 或调整适用范围；保留旧版本证据，不把旧数据覆盖为“新的真实偏移”。
- 作者声明与第三方实验矛盾：分别列出证据、条件和无法解释的差异，必要时降级复用等级。
- 作者反馈资料错误：尽快修正并保留必要的修订记录；邀请作者审阅不等于自动授予合并权限。
- 涉及权属、隐私或专有游戏文件的提交：在确认允许前不要合并。

## 维护责任移交

维护者退出前应说明未合并 PR、争议中的证据、未验证的高成熟度记录和待修复 CI；不要在仓库里留专有资源或未公开凭证。未来如建立 CODEOWNERS，只列实际具有权限且同意审阅的成员。

## 常见故障

| 现象 | 首先检查 |
| --- | --- |
| Python 验证失败 | `PyYAML>=6,<7`、YAML 语法、是否存在无效 ID/路径 |
| Topic 双向错误 | `registry/projects.yaml` 与 `registry/topics.yaml` 和 Topic front matter |
| 能力端点缺失 | `registry/capabilities.yaml` / `registry/implementations.yaml` 的 ID |
| R2 证据失败 | `reviewed_commit`、固定源链接、`audit_path` |
| 逆向发现失败 | `source_sha` 与 GitHub blob URL、`game_build`、`applicability` |
| 链接失败 | 相对路径按**当前 Markdown 所在目录**解析，重命名须修复全部引用 |
| Skill 验证失败 | `name` 与目录名一致、`description` 非空、front matter 正确 |

[写作规范](editorial-standards.md) · [Skill 入口](skills.md) · [贡献指南](../CONTRIBUTING.md)
