# Pbatch/ClashRoyaleBuildABot 局部审查（2026-11-13）

等级 **P1（部分源码）**。固定上游 commit `f89ecbf309e698cb9fccdfb64a6ff2a930e6541e`。已读取的文件与 blob：

- [clashroyalebuildabot/bot/bot.py](https://github.com/Pbatch/ClashRoyaleBuildABot/blob/f89ecbf309e698cb9fccdfb64a6ff2a930e6541e/clashroyalebuildabot/bot/bot.py) — `4c3eb22be3e37e5a293525782ecc418ecc717f80`
- [clashroyalebuildabot/emulator/emulator.py](https://github.com/Pbatch/ClashRoyaleBuildABot/blob/f89ecbf309e698cb9fccdfb64a6ff2a930e6541e/clashroyalebuildabot/emulator/emulator.py) — `df36181bf20c7f04869180d53f6c546c28d85a92`

## 发现

视觉检测→策略动作→ADB 操作链；Bot 要求 8 张卡，含暂停、网格坐标换算和下牌。Emulator 使用 ADB 设备发现、H264 screenrecord 连续抓帧及 PyAV 解码，缺少可用设备时不能完整运行。

## 待验证

尚未运行测试；待检查剩余关键源码、许可、数据来源与运行环境。不得把文档断言视为实际测试结果。
