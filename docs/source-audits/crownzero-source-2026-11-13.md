# anishhchitnis/crownzero 源码局部审查（2026-11-13）

**等级 P1**。上游 commit `d07049ddb42f00528890983c83400088d1c7ff34`，已检查以下源码；未执行上游测试或完整依赖审计。

- [crownzero/real/fairplay.py](https://github.com/anishhchitnis/crownzero/blob/d07049ddb42f00528890983c83400088d1c7ff34/crownzero/real/fairplay.py) — blob `d786b322b2bf9971b4bb001cc78c18e6f3a01b1a`
- [crownzero/real/adapter.py](https://github.com/anishhchitnis/crownzero/blob/d07049ddb42f00528890983c83400088d1c7ff34/crownzero/real/adapter.py) — blob `ceb408a3b9073fdf535f64bc12f373e45e8c9f44`

## 发现与边界

实时适配器使用 Build-A-Bot 的画面识别结果，将手牌、圣水、单位、塔血条转换为学生策略的 View，且游戏时钟由首次在场画面估算。公平使用闸门通过“Searching for opponent”截图模板判断是否匹配陌生玩家，并在此后整场观战不出牌；截图模板识别有误判可能，需查实行动调用链是否始终执行闸门。

## 后续

补查调用链、边界输入、许可、版本、测试和实际可复现性，完成后才可考虑 P2。
