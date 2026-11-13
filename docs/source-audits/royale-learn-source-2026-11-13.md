# RoyaleGym/RoyaleLearn 局部源码审查（2026-11-13）

等级 **P1**。GitHub commit API 固定上游 commit `e5b5ddfcf892d146d8a68a8a46b533586330a05e`。仅检查列出的源码，未执行测试，未独立核实性能或训练数据。

- [royalelearn/determinism.py](https://github.com/RoyaleGym/RoyaleLearn/blob/e5b5ddfcf892d146d8a68a8a46b533586330a05e/royalelearn/determinism.py) — blob `35545bc3fdaddc134c5f0f89450b7d7488d256d0`
- [royalelearn/checkpoint.py](https://github.com/RoyaleGym/RoyaleLearn/blob/e5b5ddfcf892d146d8a68a8a46b533586330a05e/royalelearn/checkpoint.py) — blob `abeb07bd9988c663d4b2d06a292c6eb8953b736c`

## 源码结论

三档复现语义：T1 环境精确、T2 同设备/依赖梯度与指标精确、T3 吞吐优先；CUDA/BLAS 环境变量必须在导入前设置。checkpoint 按组件目录、SHA256 清单、partial 原子重命名保存，采用 safetensors/msgspec JSON 并约束恢复时身份。以上为源码实现意图，未运行跨设备复现。

## 后续

检查其他核心模块、依赖和许可证，阅读测试代码并实际运行可复现验证；验证版本兼容和输入数据的缺失/偏差处理。
