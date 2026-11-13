# Darknighture/sc-downloader-gui 局部审查（2026-11-13）

等级 **P1（部分源码）**。固定上游 commit `787fef20c2076ae2e71dfe3f9c49e019438f5185`。已读取的文件与 blob：

- [lib/worker.py](https://github.com/Darknighture/sc-downloader-gui/blob/787fef20c2076ae2e71dfe3f9c49e019438f5185/lib/worker.py) — `fc9ada3bc55c9e7a40b228ce36334e7d87ee47aa`
- [lib/reader.py](https://github.com/Darknighture/sc-downloader-gui/blob/787fef20c2076ae2e71dfe3f9c49e019438f5185/lib/reader.py) — `cca800fd26a28e697092287af0cef00e0d859049`

## 发现

PyQt 下载线程三次重试（HTTP 502/503/504 和网络错误）、退避、Queue task_done 防止停机死锁。可选对 csv/sc/toml 解压，解压失败保留原始压缩字节；Reader 包含 VInt 和 zlib 字符串解析。

## 待验证

尚未运行测试；待检查剩余关键源码、许可、数据来源与运行环境。不得把文档断言视为实际测试结果。
