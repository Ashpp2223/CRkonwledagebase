# 内存与事件流：怎样得到可信的游戏状态

## 两条不能混为一谈的观测路线

**函数事件观测**：在合法受控环境中分析选定 Native 函数执行时的相关对象和字段。Jason [README](https://github.com/Jason-XII/cr-memory-reader/blob/9af94ca2f273ce526dda6256bdbd5d5555fb82d4/README.md) 描述了名为 holder 的战斗状态入口与 hpComponentAccessor 血量组件访问器。这是**作者的研究结论**，不是所有版本的稳定符号。

**只读内存采样**：[Windows 方案技术指南](https://github.com/Jason-XII/cr-memory-reader/blob/9af94ca2f273ce526dda6256bdbd5d5555fb82d4/x86_64/%E5%86%85%E5%AD%98%E8%AF%BB%E5%8F%96%E6%8A%80%E6%9C%AF%E6%8C%87%E5%8D%97.md) 描述 native_stream、proc_mem 和 hybrid 三层，从受控设备采样，再归并到同一个 StateStore。它强调构建不匹配就停止、以只读方式工作，以及用字段范围和关系 canary 而非裸指针猜测。

## 三种地址/身份及生命周期

| 类别 | 范围 | 应记录的验证 |
| --- | --- | --- |
| Native 函数模块相对偏移 | **精确同一原生库构建** | ELF Build ID、库 SHA、机器码锚点 |
| C++ 对象字段偏移 | 结构布局未发生变化的对象 | 对象类型/指针链/范围与相互关系 |
| 堆对象运行时地址 | **仅当前进程、当前对象代际** | 所属进程、对局、存活期和清理规则 |

## 来源等级（来自 Jason 研究的示例分类）

| 数据类型 | 来源 | 为什么要区分 |
| --- | --- | --- |
| memory_exact | 已通过约束检查的直接字段 | 不代表整个游戏内部状态都完整 |
| memory_action_queue | 记录到的已应用战斗动作快照 | 不等于每一次触摸/UI 动画 |
| inferred | 根据公开事件和规则推出的状态 | 例如对手卡牌顺序的假设集合 |
| estimated | 从部分信息推算的范围 | 不可标记为“原生精确读取” |
| uncalibrated | 结构、生命周期、对象身份尚未确认 | 不能作为生产可信字段 |

这是**某个上游项目自己的标签集合**，尚非中台统一协议。

## 事件归并的研究重点

- 一条实体 HP 事件来自一次函数调用，**不证明**同一时刻所有实体已被采样。
- StateStore 应保存来源、时间窗、同局身份及有效期，结束对局或进程重启后清空陈旧指针和缓存。
- 混合来源冲突时，确定性内存读数、动作队列、计算估计不能按到达顺序随意覆盖。
- 采样时延、原生 Tick 与外部事件时钟必须明确转换，未知时保持 unknown。

## 具体反例：国服的偏移更新

[ak1NaN Overlay](https://github.com/ak1NaN/ClashRoyale-tencent-overlay) README 明确说旧偏移在腾讯客户端 38.4.2 已失效。另一个 [Tencent Model Harness](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness) 声称其**自身**配置针对 38.4.2。不能将两个项目的偏移和可用状态混为一谈。

[版本迁移](version-revalidation.md) · [研究方法](methodology.md)。
