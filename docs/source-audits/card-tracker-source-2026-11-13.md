# AmarSaini/Clash-Royale-AI-Card-Tracker 局部审查（2026-11-13）

等级 **P1（部分源码）**。固定上游 commit `8cc85f71946921a13e6ffc4e33e155937de32873`。已读取的文件与 blob：

- [Clash Royale Helper/Clash Royale Helper/Clash_Royale_Helper.py](https://github.com/AmarSaini/Clash-Royale-AI-Card-Tracker/blob/8cc85f71946921a13e6ffc4e33e155937de32873/Clash%20Royale%20Helper/Clash%20Royale%20Helper/Clash_Royale_Helper.py) — `d55ccfeb2f8600144dad327f088d566a3806a74c`

## 发现

旧版 Keras 双网络识别卡牌/圣水，Tkinter 显示对手手牌、后续牌与圣水估计。识别使用三次连续分类确认，圣水由时间推算并按 10 封顶，依赖训练图片和模型权重。版本机制与现代客户端的适用性未验证。

## 待验证

尚未运行测试；待检查剩余关键源码、许可、数据来源与运行环境。不得把文档断言视为实际测试结果。
