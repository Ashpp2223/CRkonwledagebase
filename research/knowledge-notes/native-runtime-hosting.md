# 同一个 libg.so，为什么原生战斗可以在三类宿主中运行？

## 对应的三个已公开路径

| 宿主 | 具体实现 | 用到什么 | 与记谱器的区别 |
| --- | --- | --- | --- |
| Android ARM64 设备/模拟器 | [FirstLight CR](../../projects/firstlight-cr.md) / [Jason](../../projects/jason-battle-engine.md) | APK、Java/JNI、原生探针、原始渲染环境 | 现有记谱器继承的渲染、回退和快照路径 |
| Android x86_64 无窗口模拟器 | [CR Native Sandbox](../../projects/cr-native-sandbox.md) | 原始 libg、Android 用户态，伪 Java 宿主与资源，禁用原生画面 | 有头less `reset/step`，但不能直接供 UI 输出帧 |
| Linux x86_64 Bionic 用户态 | [CR Native Linux Bionic](../../projects/cr-native-linux-bionic.md) | Android linker64、ART、框架/属性区、JniHost 与原生库 | 不启动完整 AVD/KVM，保持原始战斗逻辑；部署与 ABI 受限 |
| Linux x86_64 进程内加载器 | [Clapha Engine](../../projects/clapha-engine.md) 的 [公开 Jason 包装](https://github.com/Jason-XII/clash-royale-battle-engine/blob/70a08af6807fa4d59a11c7d52bf6272a96afe30c/clapha.py) | `CrxEnv`、原生 libg、兼容加载器/依赖 shim | 适合大量 headless 自博弈；私有 loader 细节不可审 |

分类依据：[Sandbox README](https://github.com/IMAX9D/cr-native-sandbox/blob/8c8443e26c4250f3ae8cd5d09298080ae9d8a782/README.md)、[Bionic README](https://github.com/IMAX9D/cr-native-linux-bionic/blob/7840e4e920fb8c4d63efb16333c9451a16343c76/README.md)、[Jason clapha.py](https://github.com/Jason-XII/clash-royale-battle-engine/blob/70a08af6807fa4d59a11c7d52bf6272a96afe30c/clapha.py)。

## 可迁移的知识

1. **宿主 ≠ 游戏引擎**：同一原生逻辑库依赖 Java/JNI、Bionic、资源及游戏全局状态；缩小宿主环境不意味着重写了规则。
2. **Tick 可控 ≠ 战斗可分叉**：`reset/step` 可从开局复现；任意历史节点需要引擎内部状态、外部动作队列、随机源和持久性契约。
3. **Headless ≠ 可渲染**：无 Surface 与游戏渲染器被跳过后，不能只靠坐标生成“原生帧”。
4. **x86_64 ≠ ARM64 可互换**：同一规则版本也需要不同 ELF/ABI 和可能不同的对象布局与版本指纹。
5. **独立进程隔离 ≠ 快照 API**：多 Worker 可以各自 `reset`，不代表能瞬间克隆任意状态或跨进程导入内部指针。

## 应优先回答的工程问题

- 需求是**原生画面复盘**还是**高速无画面搜索**？两者的最佳宿主未必相同。
- 资源和 `libg` 是否匹配同一构建，初始化 DataTables 的调用条件是否有验证？
- 主引擎 `step` 的线程、调度、全局状态与对局销毁是否经实验验证？
- 快照重试是否跨进程？外部事件调度与恢复代际是否一起更新？

**尚未证明的泛化**：Bionic 15.535.29 成功并不能外推到 16.402.12；Clapha 的私有进程内 loader 也没有被中台审核。任何新版本都必须单独完成环境和行为验证。

[16.402.12 逆向现状](../reverse-engineering/client-upgrade-160402.md) · [快照语义](snapshot-semantics.md)
