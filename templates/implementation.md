# 项目×能力登记检查表

把具体记录放在 `registry/implementations.yaml`，不要为每条关联重复创建文档。

- id: `capability-id--project-id`，全仓唯一。
- capability / project: 均需在注册表中存在。
- reuse_level: R0–R4；详细证据规则见 `docs/reuse-maturity.md`。
- verification: unknown / author-documented / source-inspected / reproduced。
- integration: unverified / tested / maintained（至少提供对应证据）。
- claim: 做到的事情，准确但不要夸大。
- limits: 版本、环境、缺失能力、兼容性。
- evidence: 源仓库或更精确的固定版本文档/源码链接。

引入 R2+ 时，PR 必须附固定提交、具体代码范围和测试/审核记录；R3+ 需要显式处理许可。
