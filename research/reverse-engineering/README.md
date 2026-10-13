# 皇室战争逆向知识中心

这里整理可复验的逆向研究方法、技术发现、适用构建和失效边界，不复制原作者代码、专有二进制或完整文章。**发现源码与功能存在，不意味着本中台运行或独立验证成功。**

## 知识路线

| 需要回答的问题 | 阅读入口 | 参考研究 |
| --- | --- | --- |
| APK、Java 入口、JNI 与原生战斗库怎样关联 | [APK 与 Native](native-binary.md) | [Jason 研究记录](https://github.com/Jason-XII/cr-memory-reader/blob/9af94ca2f273ce526dda6256bdbd5d5555fb82d4/My%20Own%20Findings.md) |
| 如何从函数/字段位置得到可靠状态 | [内存与事件流](runtime-memory.md) | [Windows 只读内存技术指南](https://github.com/Jason-XII/cr-memory-reader/blob/9af94ca2f273ce526dda6256bdbd5d5555fb82d4/x86_64/%E5%86%85%E5%AD%98%E8%AF%BB%E5%8F%96%E6%8A%80%E6%9C%AF%E6%8C%87%E5%8D%97.md) |
| 原生结构布局与游戏规则如何形成可测试证据 | [原生布局与战斗语义](native-layouts.md) | [FirstLight C++ 结构约束](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/probe/combat_deployment_layout.h) |
| 从网络数据能确认什么 | [协议与消息史](protocol-history.md) | [旧版消息定义](https://github.com/royale-proxy/cr-messages) |
| SC、CSV 等游戏资源怎样研究 | [资源格式研究](resource-formats.md) | [cr-sc-dump](https://github.com/123456abcdef/cr-sc-dump) |
| 版本升级后旧结论还能不能用 | [构建与偏移复验](version-revalidation.md) | [腾讯 Overlay 失效案例](https://github.com/ak1NaN/ClashRoyale-tencent-overlay) |
| 怎样保存 AI/人工研究的假设、证据与失败 | [研究方法](methodology.md) | [逆向发现机器索引](../../registry/reverse-findings.yaml) |

## 原始知识来源（不代表当前兼容）

**2026 年相关原生研究**

- [Jason-XII/cr-memory-reader](https://github.com/Jason-XII/cr-memory-reader)：分阶段逆向过程、对象定位、内存采样、状态推断与 x86_64 只读读取方案。
- [FirstLight_CR](https://github.com/Jaasssoooonnnnn/FirstLight_CR)：Native Probe、版本相关布局、原生行为测试和训练层契约。
- [Jason-XII/clash-royale-battle-engine](https://github.com/Jason-XII/clash-royale-battle-engine)：将原生战斗封装为客户端 API 的研究。
- [ak1NaN Tencent Overlay](https://github.com/ak1NaN/ClashRoyale-tencent-overlay) 与 [Model Harness](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness)：不同客户端偏移移植、版本失效及原生数据映射。

**历史协议与工具研究（2016–2018 年为主）**

- [Giovanni Rocca 原作者文章](https://www.giovanni-rocca.com/reverse-engineering-supercell-clash-royale-part-2/)：逆向假设、协议数据结构、校验逻辑等历史研究方法。
- [royale-proxy/cr-messages](https://github.com/royale-proxy/cr-messages)：旧版消息类型与结构字典。
- [weeco/supercell-packet-listener](https://github.com/weeco/supercell-packet-listener)：只解析未加密包头元数据的历史分析思路。
- [nfirvine/croy-shark](https://github.com/nfirvine/croy-shark)：Wireshark Lua 历史解析器。
- [iGio90/frida_cr_proxy](https://github.com/iGio90/frida_cr_proxy)：2017 年的 Frida/Python 客户端消息分析实验。

**资源格式研究**

- [cr-sc-dump](https://github.com/123456abcdef/cr-sc-dump)、[sc_extract](https://github.com/nextonesfaster/sc-extract)、[Darknighture Downloader](https://github.com/Darknighture/sc-downloader-gui)。

## 知识抽象方式

一条逆向发现必须说明：对象/消息的语义、构建身份、证据来源、验证方式、适用范围、已知反例及下一次需要核实的条件。状态值需区分直接观测、作者报告、推断与未知；不得把某个客户端构建的内存偏移搬到另一个客户端作为事实。

本目录保存研究与出处；实际能力选择请回到 [状态观测](../../capabilities/state-observation/README.md)、[原生驱动](../../capabilities/battle-control/README.md)、[资源解析](../../capabilities/asset-ingestion/README.md)。涉及专有客户端的工作应限于获得许可的测试环境，不提供在线作弊、规避保护或未授权修改说明。

[研究入口](../README.md) · [技术中台首页](../../README.md)
