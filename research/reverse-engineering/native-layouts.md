# 原生战斗结构与规则语义：从布局假说到可测试约束

## 研究重点不是“记一个地址”

FirstLight 的 [native_runner/probe](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/probe/combat_deployment_layout.h) 展示了更可复用的方式：把某个**精确客户端构建下的对象结构发现**变成带命名、边界和断言的 C++ 逻辑，并用主机侧小型测试约束特殊卡牌行为。

### 案例 A：部署选择 Descriptor

[combat_deployment_layout.h](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/probe/combat_deployment_layout.h) 明确将研究绑定至 Null's Royale 15.535.13 的 NativeCardSelection 描述，并将普通选择、Hero Form、Mirror 的身份关系分别约束。它甚至注明某些相关字段的实际类型还没有证明，因此**不允许凭推测把它强制解释成确定子类型**。

可复用的并非固定字段数字本身，而是这种“**字段语义—不变量—特殊情况—未证明部分**”的文档方式。

### 案例 B：原生战斗事件与读写观察

[FirstLight 原生探针目录](https://github.com/Jaasssoooonnnnn/FirstLight_CR/tree/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/probe) 的组件包含：
- 战斗部署 descriptor 及其 host-side tests；
- 动作/移动状态、生命值/伤害、效果状态及可见性布局；
- 原生观测/命令与 JSON/事件环的分离；
- 大量测试文件，适合作为“布局事实应能写成测试”的参考。

**没有执行这些测试**。看到源码与测试文件，只能确认存在可定位的实现与断言，不说明它们针对任意 APK 版本仍然正确。

### 案例 C：状态快照生命周期

[NativeClashEnv Python 接口](https://github.com/Jaasssoooonnnnn/FirstLight_CR/blob/3ade158c52bf33de3ffcea600ce380946b7de0d8/native_runner/cr_native_env.py) 包含 create_snapshot、restore、release_snapshot 等进程内快照功能，但句柄绑定当前应用与管理器代际。可将其用于研究状态恢复语义，**不能**因此推断存在跨进程恢复或并行克隆。

## 每条布局证据的最小字段

- 固定构建及原生库 Hash。
- 原生对象身份如何确认。
- 字段/函数的来源、关联对象和读写时机。
- 至少一条正例、一条反例，以及异常值的处理。
- 是否发生普通/觉醒/英雄/镜像的语义分歧。
- 哪些推断尚未证明；什么客户端更新会让结论失效。

参阅 [FirstLight 项目卡](../../projects/firstlight-cr.md) 和 [原生源码审计](../../docs/source-audits/native-engine-2026-10-13.md)。
