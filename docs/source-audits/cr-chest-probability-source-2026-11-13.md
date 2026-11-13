# Darknighture/cr-chest-probability-calculator 源码局部审查（2026-11-13）

**等级 P1**。上游 commit `4465a4ca5fc1131a5c4e1949e62a6569f84f53f1`，已检查以下源码；未执行上游测试或完整依赖审计。

- [chest_probability_calculator.py](https://github.com/Darknighture/cr-chest-probability-calculator/blob/4465a4ca5fc1131a5c4e1949e62a6569f84f53f1/chest_probability_calculator.py) — blob `15dfdd2f57cae317f3e9f8d6f1c8ce77e046c1cc`

## 发现与边界

Tkinter/Matplotlib 中文英文双语概率计算 GUI，输入宝箱等级、起始等级、每级升级概率及次数，输出等级分布。是否严格对应当前皇室战争宝箱机制尚无客户端数值证据。

## 后续

补查调用链、边界输入、许可、版本、测试和实际可复现性，完成后才可考虑 P2。
