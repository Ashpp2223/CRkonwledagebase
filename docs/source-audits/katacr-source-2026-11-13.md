# wty-yy/KataCR 局部源码审查（2026-11-13）

等级 **P1**。GitHub commit API 固定上游 commit `36ceb9fcfbd117c2ce3d97eacee435c1898eb7b8`。仅检查列出的源码，未执行测试，未独立核实性能或训练数据。

- [katacr/detection/predict.py](https://github.com/wty-yy/KataCR/blob/36ceb9fcfbd117c2ce3d97eacee435c1898eb7b8/katacr/detection/predict.py) — blob `9866a0958972000e992fc0b963c9569625c247f7`
- [katacr/classification/elixir/predict.py](https://github.com/wty-yy/KataCR/blob/36ceb9fcfbd117c2ce3d97eacee435c1898eb7b8/katacr/classification/elixir/predict.py) — blob `7c1e4d5c45728e72622afaf49cc925ba2caa827d`

## 源码结论

JAX/Flax 目标检测预测器输出位置、宽高、置信度、类别及状态字段；当前代码仅启用一个二值状态通道，其余状态通道注释掉。圣水识别使用灰度预处理、ResNet 权重与分类映射；运行依赖本地 checkpoint，示例脚本含开发者绝对路径。不能将检测输出视为完整游戏状态。

## 后续

检查其他核心模块、依赖和许可证，阅读测试代码并实际运行可复现验证；验证版本兼容和输入数据的缺失/偏差处理。
