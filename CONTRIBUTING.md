# 贡献指南｜按能力沉淀可复用成果

欢迎项目作者和研究者贡献原始知识与验证材料。请优先从 [能力目录](capabilities/README.md) 检索，避免重复创建新概念。

初次维护请阅读 [维护者手册](docs/maintainer-handbook.md) 和 [文档写作规范](docs/editorial-standards.md)。常见维护任务可以按 [仓库级 Skills](docs/skills.md) 直接执行。

## 三种贡献路径

1. **登记项目**：参照 [项目模板](templates/project.md) 新建单仓库项目卡，登记 `registry/projects.yaml`，并维护相关专题双向引用。
2. **补充能力实现**：若已有能力，将来源项目加入 `registry/implementations.yaml`，在对应能力卡中补充准确、带证据的说明；没有现成能力则根据 [能力模板](templates/capability.md) 新增。
3. **技术研究/验证**：提交完整实验环境、复现步骤、日志和局限。可使用 [研究模板](templates/research.md)；证据充分时再申请提高某项实现的复用等级。

## 审核原则

- 有来源但未运行的描述只能标为 `author-documented`，通常 R1；不能自行升级为 Verified。
- 某个作者自述“完整逆向”不能替代明确实现范围及实验结果。
- 原作者尚未加入本项目时不要虚构维护权；项目资料可先公开编目并接受纠错。
- 从外部项目集成源码前必须核对许可证、第三方游戏素材和具体版本。
- 标准接口提案全部先放 `contracts/` 且写 Draft，不得暗示作者们已达成统一 ABI。
- PR 应指出影响的项目 ID、能力 ID、验证范围及链接。

## 自检

安装 Python 3.12 与 `PyYAML>=6,<7`，运行 `python scripts/validate.py` 和 `python scripts/validate_skills.py`；CI 在提交/PR 时执行同样的检查。无需数据库与 AI API。

[成熟度标准](docs/reuse-maturity.md) · [协作治理](GOVERNANCE.md)
