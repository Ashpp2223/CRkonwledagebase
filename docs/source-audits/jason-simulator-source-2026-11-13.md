# jason-simulator 源码普查记录（2026-11-13）

级别：P1（局部源码）。默认分支 tree SHA `82bcbf3088102318125fc0193f0e5bc38e7886b2`；仅阅读列出文件，未固定 commit 或运行测试。

- [src/clasher_new/battle.py](https://github.com/Jason-XII/clash-royale-simulator/blob/HEAD/src/clasher_new/battle.py) — blob `be1955822d96ffeef39cc910b0ceff7f92a2cf56`
- [src/clasher_new/core.py](https://github.com/Jason-XII/clash-royale-simulator/blob/HEAD/src/clasher_new/core.py) — blob `1f4cfd18144fae1067f82f72377e02d65fa0c49d`

## 发现与边界

独立 Python 规则模拟器，battle.py 定义实体生命、护盾、目标、状态更新与延迟伤害；特殊卡牌委托 BasicCharacter/专属类。此实现不能视为官方原生引擎。

## 后续

补查完整实现、依赖、许可证和测试；核对版本、状态一致性、实际运行结果。不能将作者声明或测试代码视作独立验证。
