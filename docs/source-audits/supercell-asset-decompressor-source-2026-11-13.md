# abhishek-kumar-14/supercell-asset-decompressor 源码局部审查（2026-11-13）

**等级 P1**。上游 commit `5cbcd328fdd166632c67673b4a3a8bc4e1400f04`，已检查以下源码；未执行上游测试或完整依赖审计。

- [main.py](https://github.com/abhishek-kumar-14/supercell-asset-decompressor/blob/5cbcd328fdd166632c67673b4a3a8bc4e1400f04/main.py) — blob `cfb7216f8b2fbfd6e4d986b77b38ea1dcebedc5a`

## 发现与边界

Python 文件头探测并支持 none/LZMA/SC/SC2/Sig/Zstandard 等封装，重建 9 字节 Supercell LZMA 长度头为标准 13 字节 LZMA Alone 头，2 GiB 输出限制；识别 SCLZ/LZHAM 但明确不支持纯 Python 解压。未运行格式回归样本。

## 后续

补查调用链、边界输入、许可、版本、测试和实际可复现性，完成后才可考虑 P2。
