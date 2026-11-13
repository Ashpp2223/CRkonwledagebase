# proydakov/supercell-resource-decoder 局部源码审查（2026-11-13）

等级 **P1**。GitHub commit API 核实上游 commit `7b8bb5a8d1b1ef74b05842b6c4c73b599e3d31d4`。本轮仅阅读下列源码，未运行上游测试。

- [lib_csv.py](https://github.com/proydakov/supercell-resource-decoder/blob/7b8bb5a8d1b1ef74b05842b6c4c73b599e3d31d4/lib_csv.py) — blob `6baa1632f6d69d08440d4d833c8f2d51b1e7fc05`
- [decoder_csv.py](https://github.com/proydakov/supercell-resource-decoder/blob/7b8bb5a8d1b1ef74b05842b6c4c73b599e3d31d4/decoder_csv.py) — blob `d46fe33e19f2ba9420d8565f39db9ca074fce55b`

## 发现与限制

旧版 Supercell CSV LZMA 编解码：解码时在前 8 字节后补四个零以恢复 LZMA Alone 长度头；编码使用 FILTER_LZMA1 与 256 KiB 字典，重排头部。批处理递归遍历 .csv。异常处理为裸 except，缺乏输入长度和校验；版本适用性待测。

## 后续

补查完整实现、许可、依赖、边界输入与测试可执行性，达到完整证据链后再考虑 P2。
