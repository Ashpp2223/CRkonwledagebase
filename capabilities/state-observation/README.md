---
id: state-observation
title: "对局状态观测"
type: capability
lifecycle: catalogued
standardization: none
last_reviewed: null
---

# 对局状态观测

**需要解决的问题**：如何从原生状态、内存或画面取得结构化观测？

**能力边界**：观测不等于游戏完整隐藏状态，也不保证可控制或恢复。

## 采用前必须回答

- 列明每个字段的来源、采样间隔和时间戳。
- 说明坐标系、阵营、实体 ID 稳定性。
- 区分公开可见信息、推断值及内部状态。
- 明确客户端版本、内存偏移或画面分辨率约束。

## 已公开的相关实现

| 来源项目 | 复用成熟度 / 证据 | 公开描述 | 限制 | 原始来源 |
| --- | --- | --- | --- | --- |
| [CR Memory Reader](../../projects/memory-reader.md) | R1 · author-documented | 内存/原生对象的圣水、手牌、实体观测 | 依赖客户端版本及环境 | [来源](https://github.com/Jason-XII/cr-memory-reader) |
| [Tencent Overlay](../../projects/tencent-overlay.md) | R0 · author-documented | 腾讯版客户端的部署队列覆盖层 | README 声明旧内存偏移在 38.4.2 更新后失效 | [来源](https://github.com/ak1NaN/ClashRoyale-tencent-overlay) |
| [Tencent Model Harness](../../projects/tencent-model-harness.md) | R1 · author-documented | 国服观测转换为 FirstLight V4 模型输入 | 适用 38.4.2 配置；需逐构建校验偏移 | [来源](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness) |
| [KataCR](../../projects/katacr.md) | R1 · author-documented | 基于图像的单位/手牌识别与状态融合 | 依赖视频链路及图像模型/分辨率 | [来源](https://github.com/wty-yy/KataCR) |
| [FirstLight CR](../../projects/firstlight-cr.md) | R1 · author-documented | 离线引擎内结构化观测 | 不是任意正式线上客户端观测接口 | [来源](https://github.com/Jaasssoooonnnnn/FirstLight_CR) |

> 上表为**作者文档层级的能力关联**，未独立检查完整源码或运行测试；R0/R1 并不是可下载即用的组件。细节见 [成熟度规则](../../docs/reuse-maturity.md) 和 [机器登记](../../registry/implementations.yaml)。

## 选择与集成判断

- 视觉路线可减少对原生内存偏移的依赖，但必须测量遮挡、延迟和检测误差。
- 原生读取可提供细粒度状态，但升级可能导致偏移失效，且要处理权限与授权边界。

## 尚缺的中台资产

- 可复现的运行环境及固定提交、版本指纹。
- 统一测试场景下的功能验证、性能数据和错误案例。
- 作者审阅、许可证核对与明确的集成入口（若存在）。

[返回能力目录](../README.md) · [查看项目目录](../../projects/README.md)
