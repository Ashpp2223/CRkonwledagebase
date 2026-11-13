# jthingelstad/cr-agent-api-docs 局部源码审查（2026-11-13）

**等级 P1**。固定上游 commit `4e3229d1507ae9add4250612626c4afdba0ff22f`。本轮读取以下文件，未运行测试。

- [tools/cr-probe/crprobe/client.py](https://github.com/jthingelstad/cr-agent-api-docs/blob/4e3229d1507ae9add4250612626c4afdba0ff22f/tools/cr-probe/crprobe/client.py) — blob `df5c5ab4c92090c81dfec5df30001dadd155fa7b`
- [tools/cr-probe/crprobe/timeline.py](https://github.com/jthingelstad/cr-agent-api-docs/blob/4e3229d1507ae9add4250612626c4afdba0ff22f/tools/cr-probe/crprobe/timeline.py) — blob `b30dde0cf495e7090fbe0a069ab9550e93bfda0a`

## 发现与限制

仓库除 API 文档外含可运行的 cr-probe Python 采样器及测试。Client 区分 403 invalid IP、404、限流等失败，将标签 # 规范为 %23 以避免 URL fragment 截断；timeline 将非 200 状态变化保留在两次采样之间的时间窗，给出持续时间上下界，不虚构精确切换时间。尚未运行测试，也未核验线上 API 数据。

## 后续

继续查剩余实现、依赖、许可、测试与真实数据；达到可重复证据链后再评估 P2。
