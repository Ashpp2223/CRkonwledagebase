# 重点作者仓库横向枚举（2026-11-13）

目的：按作者搜索所有公开仓库，不以项目名称是否含 Clash Royale 作为初筛排除条件。**仅完成仓库清单和部分文件树抽样**，尚未逐仓源码审查；不自动入正式项目注册表。

| 作者 | 搜索到的公开仓库数 | 已登记皇室战争项目 | 本轮新注意项 |
| --- | ---: | --- | --- |
| [Jason-XII](https://github.com/Jason-XII?tab=repositories) | 24 | daybreak-cr（旧名 clash-royale-battle-engine）、clash-royale-simulator、cr-memory-reader、sc-decoder | [3c3u-bot](https://github.com/Jason-XII/3c3u-bot) |
| [Jaasssoooonnnnn](https://github.com/Jaasssoooonnnnn?tab=repositories) | 12 | FirstLight_CR、FirstLight-Zero、FL-Royale | [rea](https://github.com/Jaasssoooonnnnn/rea)、[TRACE](https://github.com/Jaasssoooonnnnn/TRACE)、[DiffuPlan](https://github.com/Jaasssoooonnnnn/DiffuPlan) |
| [IMAX9D](https://github.com/IMAX9D?tab=repositories) | 7 | cr-native-sandbox、cr-native-linux-bionic、royaleapi-downloader、r0-elite-training | 另有 Minecraft/启动器工具，未发现明显皇室战争直接关联 |
| [ak1NaN](https://github.com/ak1NaN?tab=repositories) | 4 | Clashback、ClashRoyale-replay-studio、ClashRoyale-tencent-overlay、ClashRoyale-tencent-model-harness | 当前公开仓库四项均已登记 |

## 非显名仓库的实际文件树检查

- Jason-XII/3c3u-bot：tree `869928445da07796ae689e49884796c195b46ed2`，15 条；含 `bot.py`、`telemetry_parser.py`、`stream_processor.py`，仓库描述为 3c3u 聊天/敌对玩家监控；**暂未发现皇室战争直接关联**，不入库。
- Jaasssoooonnnnn/rea：tree `fe297e56e804130dd49cc0a95fcf2d115c183ae3`，2379 条；通用逆向代理框架，含大量真实二进制/浏览器测试工作流；可列为**跨项目研究方法候选**，但未证实 CR 专用功能。
- Jaasssoooonnnnn/TRACE：tree `77509554ee3b5184f84c7599189e3cd27fdd2f9e`，39 条；轨迹选择与搜索智能体，含训练、评估、测试代码；可研究 AI 方法迁移，未发现 CR 专用实现。
- Jaasssoooonnnnn/DiffuPlan：tree `251d30e34fb43aeb2fd2a17caba97742e10cfdd6`，404 条；扩散语言模型智能体可编辑规划状态；未发现 CR 专用实现。

## 待续查

对其余作者重复全仓库枚举；对上述候选读取关键源码与引用链，只有发现明确的 CR 关联或直接复用价值后才登记。作者公开仓库数量为本次搜索快照，不能当作永久不变的总数。
