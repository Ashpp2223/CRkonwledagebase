# 新客户端版本的逆向结论复验

## 最重要的约束

**不允许跨游戏构建直接继承函数偏移、对象偏移、运行时指针或协议消息含义。**

[Jason Windows 内存读取指南](https://github.com/Jason-XII/cr-memory-reader/blob/9af94ca2f273ce526dda6256bdbd5d5555fb82d4/x86_64/%E5%86%85%E5%AD%98%E8%AF%BB%E5%8F%96%E6%8A%80%E6%9C%AF%E6%8C%87%E5%8D%97.md) 所描述的思路是：先核验精确构建身份，再确认布局和字段证据，最后运行；若不匹配则拒绝，而不是回退到猜测地址。阅读时以[原始文件路径](https://github.com/Jason-XII/cr-memory-reader/blob/9af94ca2f273ce526dda6256bdbd5d5555fb82d4/x86_64/%E5%86%85%E5%AD%98%E8%AF%BB%E5%8F%96%E6%8A%80%E6%9C%AF%E6%8C%87%E5%8D%97.md)为准。

## 复验矩阵

| 变化 | 旧结论哪些可能仍然有效 | 必须重新检查 |
| --- | --- | --- |
| 仅资源 Fingerprint / 卡牌表变化 | 部分 Native 控制入口可能保持 | card ID、变体、数值与资源语义 |
| 同 ABI 的新 libg 构建 | 一些语义和对象关系可能保持 | ELF 指纹、函数与字段偏移、对象大小 |
| ARM64 ↔ x86_64 | 规则思想、外部数据格式有时可复用 | ABI、结构对齐、指针宽度、Hook 路线 |
| Null's ↔ 腾讯客户端 | 部分游戏逻辑概念可能相近 | 启动层、客户端版本、对象布局、控制/验证语义 |
| 切换对局或重启进程 | 持久化的研究解释可能仍有意义 | 所有堆指针、缓存、原生句柄与观测代际 |
| 老版历史网络协议 → 新版 | 包头/消息分类思想可参考 | 消息号、编码、加密负载和时序含义 |

## 案例：两个腾讯客户端仓库

- [Overlay](https://github.com/ak1NaN/ClashRoyale-tencent-overlay) README 明示旧内存偏移在 38.4.2 已失效。
- [Model Harness](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness) 声明自身偏移配置针对 38.4.2。

这意味着不能把“腾讯版 38.4.2”看作一份通用偏移表，更不能推断两个项目在 2026 年 10 月仍可互换。

## 每条更新记录建议保存

1. 精确 Build ID / SHA / 资源版本。
2. 原有假设依赖的对象、函数、位置和证据。
3. 新版本对照场景与**首次可确认失效的环节**。
4. 使用受控环境验证后的替代发现，或者明确标记不支持。
5. 缺失字段应使用 unknown / uncalibrated，禁止悄悄降级为精确数值。
6. 任何通过结果都注明测试人、时间和独立运行证据。

[发现登记](../../registry/reverse-findings.yaml) · [逆向入口](README.md)。
