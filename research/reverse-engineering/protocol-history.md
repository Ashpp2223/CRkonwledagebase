# 网络协议逆向：能够观察的边界与历史语义

> 本文梳理**历史研究素材及可继承的分析方法**，不提供现代联网客户端的消息构造、加密规避或未授权操作指南。协议 ID 和字段只属于其来源时代，不能视为当前可用。

## 三类资料的价值

| 来源 | 能确定的研究类型 | 误用风险 |
| --- | --- | --- |
| [royale-proxy/cr-messages](https://github.com/royale-proxy/cr-messages) | 旧版消息名称/ID、字段 Schema 与整数编码说明 | 2017 年历史，当前消息不一定同义 |
| [weeco/supercell-packet-listener](https://github.com/weeco/supercell-packet-listener) | 2018 年被动获取**包头元信息**的思路 | 包头不加密 ≠ 负载明文 |
| [nfirvine/croy-shark](https://github.com/nfirvine/croy-shark) | 2016 年 Wireshark dissector、协议信息展示 | 旧解析器可能不能识别现代包 |
| [iGio90/frida_cr_proxy](https://github.com/iGio90/frida_cr_proxy) | 历史 Frida/Python 消息分析实验 | 旧 x86 客户端和历史协议条件 |
| [Jason-XII My Own Findings](https://github.com/Jason-XII/cr-memory-reader/blob/9af94ca2f273ce526dda6256bdbd5d5555fb82d4/My%20Own%20Findings.md) | 从受控抓包事件关联到 Native 动作消息的探索过程 | 某 Null's 构建的实验，不是官方通用映射 |
| [Giovanni Rocca Part 2](https://www.giovanni-rocca.com/reverse-engineering-supercell-clash-royale-part-2/) | 早期 ECT/OwnHomeData、校验和假设与验证过程 | 作者 2017 年研究，不能套用今天 |
| [caunt/SupercellProxy](https://github.com/caunt/SupercellProxy/tree/6b4984aeec5b1cadf2948cf4e628e60821dc35b6) | .NET 消息 codec、回合结构、抓包归档与版本关联资源快照的实现参考 | 上游跨 Supercell 游戏，未建立当前皇室战争官方客户端的版本化兼容证据；ggggmllll 仓库是其 Fork |

## 关键概念辨析

- **Packet framing**：消息边界、方向、包长和编号。观察到 ID 只表明客户端/服务器交换了某类包，不自动知道负载完整语义。
- **Message Schema**：字段类型与排列。历史 [cr-messages README](https://github.com/royale-proxy/cr-messages/blob/64560f4a3c78005cea53c697fbe8ad2bb55bb82d/README.md) 使用名称、ID、字段类型定义消息；本质是那个时代的编码描述。
- **Semantic mapping**：消息和真实场景的关系，要通过“同条件只改变一个游戏行为”的对照才可能建立。
- **Native action**：运行时游戏内部动作不一定与单个网络消息一一对应，不能假定每次 UI 触摸都会立即产生一个可分辨的服务器指令。
- **Checksum/加密**：历史资料可以学习怎么设立假说和验证依赖，却不能被复用为现今保护机制的事实或实现。

## 值得保存的历史原始参考

Giovanni Rocca 的原站：[2017 Clash Royale Part 2](https://www.giovanni-rocca.com/reverse-engineering-supercell-clash-royale-part-2/)、[2017 October Update Part 3](https://www.giovanni-rocca.com/reverse-engineering-supercell-october-update-part-3/)、[2017 Part 4](https://www.giovanni-rocca.com/reverse-engineering-supercell-part-4/)、[2018 Part 5](https://www.giovanni-rocca.com/journey-finland-reverse-engineering-android-supercell-pt-5/)。

[weeco 历史包头研究](https://github.com/weeco/supercell-packet-listener/blob/dff096ba639e03e109c772885eab2a6ce7cdf2c2/README.md) 特别明确指出：它只能访问未加密的**消息元数据**，未获得加密的负载。这种诚实的研究边界比“支持全部协议”更值得中台保留。

## 2026 年源码补充：协议观测需要携带构建身份

[caunt/SupercellProxy 的 `ClientTurnHeader.cs`](https://github.com/caunt/SupercellProxy/blob/6b4984aeec5b1cadf2948cf4e628e60821dc35b6/src/SupercellProxy.Networking/Protocol/Turns/ClientTurnHeader.cs) 静态源码描述 `checksum`、`subTick`、8 个 `subChecksums` 和命令数量；[`EndClientTurnMessage.cs`](https://github.com/caunt/SupercellProxy/blob/6b4984aeec5b1cadf2948cf4e628e60821dc35b6/src/SupercellProxy.Networking/Protocol/Turns/EndClientTurnMessage.cs) 将命令、调试块与开发构建额外字段按 `CommandEnvironment` 分开编码。它们是**该仓库实现的消息模型**，未通过皇室战争当前官方构建的抓包/回放实测确认。

更适合直接复用的做法来自 [`CaptureArchive.cs`](https://github.com/caunt/SupercellProxy/blob/6b4984aeec5b1cadf2948cf4e628e60821dc35b6/src/SupercellProxy.Networking/Captures/CaptureArchive.cs)：以客户端版本和资源指纹组织录制文件，并独立保留对应资源快照。对皇室战争的协议研究或同场景复验，可借鉴**版本 + 资源指纹 + 捕获数据同存**的证据结构，避免将不同版本的数据混作一份；是否可用在目标客户端仍需单独检验。

## 能沉淀到今天的内容

历史消息 Schema 设计方式、方向/时间/构建标注、基于对照的语义判定、明确未知负载、跨版本废弃标记。这些方法可以复用；历史数据值本身通常不能直接复用。

[发现索引](../../registry/reverse-findings.yaml) · [研究方法](methodology.md)。
