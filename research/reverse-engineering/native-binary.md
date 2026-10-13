# APK、JNI 与 libg.so：研究对象的边界

## 为什么先确认装载路径

一个皇室战争客户端并不等于单个战斗库。APK 包装层可能含 Manifest、Java Activity、第三方启动模块、native 游戏逻辑库、音频/网络组件和资源 Fingerprint。把这些来源混在一起，会把私服启动器的特性错误归因于 Supercell 原生游戏。

[Jason APK 调查](https://github.com/Jason-XII/cr-memory-reader/blob/9af94ca2f273ce526dda6256bdbd5d5555fb82d4/My%20Own%20Findings.md) 记录了某个 Null's Royale 安装包的原生库与启动路径。其中 libwildcat 等组件属该研究对象的特殊启动层，**不应作为所有正式客户端的通用事实**。

## 固定构建的建议字段

| 字段 | 作用 |
| --- | --- |
| APK 文件 SHA-256、包名、版本号 | 确认被研究的客户端 |
| Android ABI、模拟器/真机架构 | 区分 ARM64 与 x86_64 逻辑 |
| libg.so SHA-256、ELF Build ID、文件大小 | 绑定静态函数位置与字段布局 |
| 资源 Fingerprint、卡牌表 Hash | 防止逻辑库与内容表错配 |
| 研究 Commit、测试时间 | 支持回溯旧结论 |

## 地址语义区分

- 模块偏移属于**精确库构建**，不是所有新版本的绝对地址。
- 对象字段偏移属于**具体对象布局**，不是任意堆指针的合法解释。
- 运行时对象地址属于**特定进程/特定对局生命周期**，重启后不应该沿用。
- 静态反编译猜测需靠受控运行时证据证明，不能只凭一个函数名签收。

## 研究的技术链

APK/Manifest 定位 → JNI/原生库构建身份 → 静态调用图候选 → 受控实验观测 → 对象关系/状态推断 → 可测规则和版本适配。

可参考的通用工具文档：[Ghidra](https://github.com/NationalSecurityAgency/ghidra) 用于 ELF 静态分析，[Frida](https://frida.re/docs/) 用于经许可的动态观察，[JADX](https://github.com/skylot/jadx) 用于 Java/DEX 结构研究。中台不提供规避保护或未授权修改真实客户端的操作配方。

[布局知识](native-layouts.md) · [证据流程](methodology.md)。
