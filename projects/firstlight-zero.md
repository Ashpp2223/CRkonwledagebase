# FirstLight Zero

- 来源：https://github.com/Jaasssoooonnnnn/FirstLight-Zero
- 证据：R1 / author-documented，仅核对 README；未运行、未完成固定提交审计。
- 许可与第三方资源再分发权限：待核实。

## 价值及边界

从零权重开始的皇室战争 X-Bow 镜像 PPO 自博弈；提供模型检查点、原生环境裁剪层和训练评估文档；README 所述胜率仅为作者报告。

## 验证事项

固定上游提交，审查关键代码、测试、许可证及与已收录项目的依赖关系；不以 README 性能或效果描述代替独立复现。

## 文档交叉核验（2026-11-12）

[审查笔记](../docs/source-audits/firstlight-zero-2026-11-12.md)：明确 20Hz/5 Tick 决策、模型观测、固定卡组评估协议、replay_export/replay_check 的验证边界。R1+，尚非源码审计或独立运行。

## 2026-11-12 限定源码审计

[源码审查记录](../docs/source-audits/simulator-trial-firstlight-zero-code-2026-11-12.md)：已读 `tools/replay_check.py`、`tools/replay_export.py`。`identical` 仅比较 episode、最终 Tick、皇冠、塔血汇总比例和执行出牌事件；未涵盖逐 Tick 全状态，且英雄能力事件未直接进入该谓词。可参考其原生重驱与双层事件格式，不能直接推定支持任意帧恢复。
