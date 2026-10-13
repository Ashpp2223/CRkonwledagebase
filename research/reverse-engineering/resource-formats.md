# 资源格式逆向：SC / CSV / Fingerprint

资源解析研究和原生战斗代码逆向相互关联，但**资源表与原生代码具有各自的版本生命周期**，不能使用单一“游戏版本”来隐藏差异。

## 值得研究的工具

| 来源 | 研究范围 | 限制 |
| --- | --- | --- |
| [123456abcdef/cr-sc-dump](https://github.com/123456abcdef/cr-sc-dump) | Python 解析 SC、DL/纹理、SCTX、CSV、KTX 等资源格式 | 实际新版本的格式兼容性需核对 |
| [nextonesfaster/sc-extract](https://github.com/nextonesfaster/sc-extract) | Rust CLI/库与测试，从资源中提取图像/CSV | 具体游戏资源版权独立 |
| [Jason-XII/sc-decoder](https://github.com/Jason-XII/sc-decoder) | SC 动画/精灵的格式研究与视觉调试 | 版本范围须复核 |
| [Darknighture/sc-downloader-gui](https://github.com/Darknighture/sc-downloader-gui) | 资源版本发现、Masterhash/Fingerprint、下载恢复 | README 提到 CR 最新补丁协商存在限制 |
| [RoyaleAPI Static Data](https://github.com/RoyaleAPI/cr-api-data) | 第三方卡牌 JSON、显示名和数据字段 | 不应默认与当前客户端精确一致 |

## 中台应当沉淀的是“格式契约”

- 哪个文件版本/指纹能被哪个解码器成功解析。
- 原始字段名、来源表和数据类型；是否来自真实客户端或第三方整理。
- card ID 的意义与稳定性，以及变体/觉醒/英雄是否共用基表。
- 由逻辑数据转为可视化资产时，转换是否有损，以及动画结构是否完整。
- 针对错误头、截断字节、未知数据块的失败日志与测试用例。

**不要直接镜像 Supercell 的原始游戏资产或未授权 APK**。工具的 MIT/GPL 许可证只说明工具代码的复制条件，不能把游戏内容产权转让给技术中台。

[资源获取能力](../../capabilities/asset-ingestion/README.md) · [构建复验](version-revalidation.md)。
