---
id: battle-control
title: "原生战斗驱动"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 原生战斗驱动

**需要解决的问题**：如何在离线环境初始化、推进和控制原生战斗？

**能力边界**：以游戏原生逻辑执行对局；不等同于重写游戏规则。

## 采用前必须回答

- 明确游戏客户端/资源构建与 ABI。
- 提供对局配置、初始化、按 tick 推进和终局识别。
- 声明动作提交延迟及失败语义。
- 说明是否要求 Android、模拟器及原生探针。

## 已公开的相关实现

| 来源项目 | 复用成熟度 / 证据 | 公开描述 | 限制 | 原始来源 |
| --- | --- | --- | --- | --- |
| [FirstLight CR](../../projects/firstlight-cr.md) | R1 · author-documented | 原生离线战斗环境与 reset/step | 需匹配游戏和资源构建；未审查完整接口 | [来源](https://github.com/Jaasssoooonnnnn/FirstLight_CR) |
| [Jason Clash Royale Battle Engine](../../projects/jason-battle-engine.md) | R1 · author-documented | 封装原生引擎接口及控制流程 | 运行平台与固定原生库需核对 | [来源](https://github.com/Jason-XII/clash-royale-battle-engine) |
| [Clash Royale Replay Studio](../../projects/replay-studio.md) | R1 · author-documented | 回放应用内部调用原生战斗探针 | 未提供可独立复用的稳定 SDK | [来源](https://github.com/ak1NaN/ClashRoyale-replay-studio) |
| [皇室战争复盘器](../../projects/ashpp-replay.md) | R1 · author-documented | 复盘器桥接提供原生对战和动作控制 | 内部接口，未宣称可供第三方直接集成 | [来源](https://github.com/Ashpp2223/clashroyalereplay) |

> 上表为**作者文档层级的能力关联**，未独立检查完整源码或运行测试；R0/R1 并不是可下载即用的组件。细节见 [成熟度规则](../../docs/reuse-maturity.md) 和 [机器登记](../../registry/implementations.yaml)。

## 选择与集成判断

- 需要严格接近目标客户端规则时，先评估原生引擎路线。
- 训练吞吐量不是唯一指标；初始化、通信和版本锁定也是成本。

## 尚缺的中台资产

- 可复现的运行环境及固定提交、版本指纹。
- 统一测试场景下的功能验证、性能数据和错误案例。
- 作者审阅、许可证核对与明确的集成入口（若存在）。

[返回能力目录](../README.md) · [查看项目目录](../../projects/README.md)
