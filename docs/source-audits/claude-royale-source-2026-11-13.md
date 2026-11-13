# houseworthe/claude-royale 局部源码审查（2026-11-13）

**等级 P1**。上游 HEAD commit `70ecc8cc0c2622e3af501cdd3ee757d215a04a92` 已由 GitHub commit API 核对。仅检查下列文件，未运行测试或完整依赖审计。

- [scripts/play_card.sh](https://github.com/houseworthe/claude-royale/blob/70ecc8cc0c2622e3af501cdd3ee757d215a04a92/scripts/play_card.sh) — blob `e1dc5df52dc7645bc892ccf23fc9da5770d8df63`
- [eval/EVAL_DESIGN.md](https://github.com/houseworthe/claude-royale/blob/70ecc8cc0c2622e3af501cdd3ee757d215a04a92/eval/EVAL_DESIGN.md) — blob `f8037aba77e88db23bc7cb90a66fa88850d509ca`

## 发现与适用边界

BlueStacks/macOS UI 自动操作，通过 jq 配置映射手牌槽与 8×8 格坐标，越界下牌只警告仍执行，不能视为严格合法动作闸门。作者定义 25 张截图评测、感知 40 分与决策 60 分，并区分截图能力评测与实时延迟监测；评分方案尚未运行验证。

## 后续

继续核查其余模块、许可证、外部数据与测试可执行性，确认运行条件后再考虑 P2。
