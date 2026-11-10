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
| 16.402.12 是否已经有独立新版离线引擎 | [新版生命周期证据与缺口](client-upgrade-160402.md) | [vegetableleaf Oracle v7](https://github.com/vegetableleaf/ClashAI/blob/ec4ef8e9dcaaaa4169ff8768bd36323e93840f9c/scratchpad/gauntlet/L74/oracle/linux/qualify/jnihost_ro/v7/GATES.md) |
| 2026 年 11 月 16.635 规则与觉醒巨人是否可复现 | [跨模拟器规则/回放证据](../knowledge-notes/cr-16635-evo-giant-parity-2026-11-10.md) | [crforge 逐 Tick 校验源码审计](../../docs/source-audits/crforge-16635-parity-2026-11-10.md)；两者是自建模拟器，不等于新版原生宿主 |
| 11 月 16.635 是否存在直接调用 `libg.so` 的原生战斗接口 | [Clashback 新版原生接口档案](../../projects/clashback.md) | [固定构建 160635001 绑定](https://github.com/ak1NaN/Clashback/blob/45c1f26b942ae1d706f2004791e73013e4330099/vendor/crx/bindings/160635001.json) 和 [CrxEnv](https://github.com/ak1NaN/Clashback/blob/45c1f26b942ae1d706f2004791e73013e4330099/vendor/crx/env.py) |
| 版本升级后旧结论还能不能用 | [构建与偏移复验](version-revalidation.md) | [腾讯 Overlay 失效案例](https://github.com/ak1NaN/ClashRoyale-tencent-overlay) |
| 离线引擎在 15.535/16.402/腾讯 38.4.2 分别完成了什么 | [跨构建原生宿主进展](client-build-migration-2026-10.md) | [ClashAI ORACLE v7 门禁](https://github.com/vegetableleaf/ClashAI/blob/218554aee8b7be9b3ad5298349853d6fe747c90f/scratchpad/gauntlet/L74/oracle/linux/qualify/jnihost_ro/v7/GATES.md) |
| 怎样保存 AI/人工研究的假设、证据与失败 | [研究方法](methodology.md) | [逆向发现机器索引](../../registry/reverse-findings.yaml) |
| 如何判断客户端加固分析中的解密、派发与完整性检测证据 | [研究方法](methodology.md) | [看雪：Clash Royale 加固逆向笔记（2026-06-21）](https://bbs.kanxue.com/thread-291737.htm)，未复验 |

## 原始知识来源（不代表当前兼容）

**2026 年相关原生研究**

- [Jason-XII/cr-memory-reader](https://github.com/Jason-XII/cr-memory-reader)：分阶段逆向过程、对象定位、内存采样、状态推断与 x86_64 只读读取方案。
- [FirstLight_CR](https://github.com/Jaasssoooonnnnn/FirstLight_CR)：Native Probe、版本相关布局、原生行为测试和训练层契约。
- [Jason-XII/clash-royale-battle-engine](https://github.com/Jason-XII/clash-royale-battle-engine)：将原生战斗封装为客户端 API 的研究。
- [ak1NaN Tencent Overlay](https://github.com/ak1NaN/ClashRoyale-tencent-overlay) 与 [Model Harness](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness)：不同客户端偏移移植、版本失效及原生数据映射。

**新的原生宿主与版本迁移资料**

- [Clashback](../../projects/clashback.md)（2026-11-04 固定源码）：macOS/Rosetta 下直接调用原版 x86_64 `libg.so` 构建 `160635001`，配置数据 `16.635.8`，具有 Python 建局、逐 Tick 推进、出牌、技能、观察和原生快照；后续跨平台适配与觉醒巨人专项测试待审。

- [CR Native Sandbox](../../projects/cr-native-sandbox.md)：15.535.29 原始 `libg` 无画面 Worker；[Linux Bionic](../../projects/cr-native-linux-bionic.md) 在同版本消除 AVD/KVM 依赖。
- [Clapha Engine（私有）](../../projects/clapha-engine.md)：Jason 的公开包装层证明使用了另一条 Linux 进程内加载路线，但无法审查私有 loader。
- [vegetableleaf Oracle 16.402.12](client-upgrade-160402.md)：18 个生命周期静态条目和 Android 真正执行尚未通过的门槛；版本迁移不可误标已完成。
- [原生宿主架构比较](../knowledge-notes/native-runtime-hosting.md)：区分有画面/无画面、Android/纯 Linux、进程内快照与对局重放。

**2026-11-07 补充：客户端加固分析（外部研究线索）**

- [看雪《尝试分析某海外加固》（2026-06-21）](https://bbs.kanxue.com/thread-291737.htm)：文章自述以 Clash Royale 为样本，讨论 `libsupercell_clashroyale.so` 的 ChaCha20、按需解密线程、间接函数派发、XXH64 代码完整性检测及检测事件记录。作者明确说明正文由 AI 生成，且记录了多次推翻早期假设的过程。
- **证据状态：第三方作者报告，未独立验证。** 页面附部分反编译片段和 RVA，但未给出可唯一绑定客户端的版本号、ELF Build ID、原始二进制 SHA-256、可复用测试日志。文中提到的具体 RVA 不登记为本中台已确认的逆向发现，也不向其他客户端版本外推。
- **需保留的竞争解释**：识别到加密常量与 4096 字节边界，不足以单独证明某缓冲区是可执行代码页；静态内容全为 `0xFF` 也可能是未初始化/哨兵填充值，不能单凭它证明表项已加密；线程局部存储的初始化标记不必然对应“代码页已解密”。
- **待复验条件**：先确定样本构建及库指纹，再在授权测试环境中验证解密前后内存区的权限与内容、间接派发的真实调用关系、哈希输入地址与长度、校验失败路径和事件记录链，逐项保留可反证的原始观察。尚无这些材料时，保持各实现细节为 `unknown`。
- **知识定位**：属于客户端保护层/逆向方法来源；不能作为战斗 Tick、卡牌规则或跨引擎一致性结论的依据。本文不收录绕过完整性检测的修改步骤。

**2026-11-07 补充：作者公开源码与可复用边界**

- **[AndProxyDemo](https://github.com/ggggmllll/AndProxyDemo/tree/4dbd3bfc369436babc18ee7aae2585f611421a2e)**（原创仓库，GPL-2.0）：[BinderHook.cpp](https://github.com/ggggmllll/AndProxyDemo/blob/4dbd3bfc369436babc18ee7aae2585f611421a2e/AndProxy/src/main/cpp/BinderHook.cpp) 可静态核查 `libbinder.so` 的 `ioctl` GOT 拦截与 JNI 事件分发；[seccomp_hook.cpp](https://github.com/ggggmllll/AndProxyDemo/blob/4dbd3bfc369436babc18ee7aae2585f611421a2e/AndProxy/src/main/cpp/seccomp_hook.cpp) 实现 `SECCOMP_RET_USER_NOTIF` 通知、supervisor 进程与寄存器采集流程；[SvcInterceptorTest.java](https://github.com/ggggmllll/AndProxyDemo/blob/4dbd3bfc369436babc18ee7aae2585f611421a2e/AndProxy/src/androidTest/java/com/gumuluo/proxy/SvcInterceptorTest.java) 有 `getpid` 的允许、拒绝、修改返回值测试**源码**。这是源码静态核查，未运行 Android 测试，也没有皇室战争样本的回归日志。
- **与游戏的关系**：[作者在看雪的 2026-03-28 文章](https://bbs.kanxue.com/thread-290553.htm) 自述工具起源于《皇室战争》原生进程异常退出的观察；它提供的是 Android 运行时研究手段，**没有公开证明能恢复任何战斗逻辑**。仓库 README 标注 ARM64 和 Linux 内核 ≥5.10 的 `seccomp` 通知前提。
- **区分文章与代码**：[2026-05-04 后续文章](https://bbs.kanxue.com/thread-291098.htm) 介绍无 Hook 的 Binder 代理方案；上述固定提交的 [BinderHook.cpp](https://github.com/ggggmllll/AndProxyDemo/blob/4dbd3bfc369436babc18ee7aae2585f611421a2e/AndProxy/src/main/cpp/BinderHook.cpp) 仍含 GOT Hook。不能将后续文章的方案默认为此仓库已实现并测试。
- **[SupercellProxy](https://github.com/caunt/SupercellProxy/tree/6b4984aeec5b1cadf2948cf4e628e60821dc35b6)**（原创上游，MIT）：`ggggmllll/SupercellProxy` 为 [caunt/SupercellProxy](https://github.com/caunt/SupercellProxy) 的 Fork，核查时 [Fork 提交](https://github.com/ggggmllll/SupercellProxy/tree/471f8aba367a5657728fc9237b6e49d34dd98b64) 落后上游 11 个提交且无独立领先提交。应以原仓库归属原作者；其 .NET 协议、抓包归档及资源 CSV 解析代码作为**跨 Supercell 游戏的研究参考**，没有证明当前皇室战争线上协议兼容。具体源码入口见 [协议与消息史](protocol-history.md)。
- **暂不独立登记**：[rustfrida-ab](https://github.com/ggggmllll/rustfrida-ab)、[elf-patcher](https://github.com/ggggmllll/elf-patcher)、[TInjector](https://github.com/ggggmllll/TInjector)、[GlossHook](https://github.com/ggggmllll/GlossHook) 属通用逆向/运行时工具，本次未发现直接对应皇室战争构建的实验材料。暂不新增 Project、Implementation、ReverseFinding 或成熟度等级。

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
