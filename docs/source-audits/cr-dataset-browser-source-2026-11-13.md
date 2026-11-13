# HumaidAlhuthali/clash-royale-dataset-browser 源码局部审查（2026-11-13）

等级 **P1**。上游 commit `8976803f2cbbaf5bd631a8616a9686fcc7bd12d1` 已经 GitHub commit API 核实。仅阅读列出的实现，未运行上游测试。

- [build_index.py](https://github.com/HumaidAlhuthali/clash-royale-dataset-browser/blob/8976803f2cbbaf5bd631a8616a9686fcc7bd12d1/build_index.py) — blob `133576a6417e49026bf42906ce4425d07aa1a441`
- [extract_one.py](https://github.com/HumaidAlhuthali/clash-royale-dataset-browser/blob/8976803f2cbbaf5bd631a8616a9686fcc7bd12d1/extract_one.py) — blob `b980e00caf2b9d39594c42af91417a4054b83c86`

## 实现与证据限制

Hugging Face TV Replays 数据集浏览器：读取 Parquet 帧和图像哈希，输出 JPEG/frames.json/manifest.json，再构造可 file:// 打开的 window.DATASET 索引。默认 WIPE=True 会删除旧 browser/data；标签由 patch_labels.py 另行写入。JPEG 转码会改变原始图像字节，不能把导出图像当成原始帧的哈希一致性证据。

## 后续

审计剩余调用链、许可证、依赖、测试和真实数据，独立验证后才可评估 P2。
