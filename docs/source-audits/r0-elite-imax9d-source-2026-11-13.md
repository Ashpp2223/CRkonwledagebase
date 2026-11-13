# IMAX9D/r0-elite-training 源码审查（2026-11-13）

**审查等级 P1。** 已固定默认分支 HEAD commit `a60db2bebdb1860bdce1f042149fa332264ca90e`（由 GitHub commit API 核实）。未运行测试，未覆盖全部核心文件，不能升级 P2。

## 实际读取源码与 blob SHA

- [expert_v1/native_ingest_contract.py](https://github.com/IMAX9D/r0-elite-training/blob/a60db2bebdb1860bdce1f042149fa332264ca90e/expert_v1/native_ingest_contract.py) — `4fd60d250bb5eaa0ee358227480a0ac1ec7dc5ea`
- [expert_v1/native_replay_runner.py](https://github.com/IMAX9D/r0-elite-training/blob/a60db2bebdb1860bdce1f042149fa332264ca90e/expert_v1/native_replay_runner.py) — `c300b5dc6cf1c35f0b45507c8e5b62ec391bcc59`

## 源码结论

训练数据链以冻结 native ingest contract（schema 3、runtime 150535029、game 15.535.29）限制可接纳的卡牌、塔兵、模式和证据；外部 downloader 不应复制第二套卡表。原生 replay runner 使用持久 Worker，在专家决策 Tick 记录紧凑状态与等待间隔，遇手牌不符、动作拒绝、提前终局、Tick 不符即失败并保存审计记录。该链的 teacher-forced 接受不自动等于源对局全状态一致。

## 后续检查

读取余下依赖、完整接口、测试与许可证，独立运行单元测试并检查数据/原生版本适用性。作者声明与测试代码均不当作运行证据。
