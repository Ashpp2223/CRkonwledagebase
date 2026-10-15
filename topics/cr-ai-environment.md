---
id: cr-ai-environment
title: "AI 训练环境与决策"
type: topic
status: investigating
verification: author-documented
projects: [firstlight-cr, jason-battle-engine, jason-simulator, tencent-model-harness, hasty-cr, royalegym, royalesim, crforge, katacr, itzik-clashenv, clashai-vegetableleaf, crsim-agent-larkindaniel, build-a-bot, detection-dataset, claude-royale, native-sandbox-imax9d, r0-elite-imax9d, cr-native-sandbox, clapha-engine, r0-elite-training, royaleapi-downloader, cr-collector]
last_reviewed: null
---

# AI 训练环境与决策

本页是**跨项目研究专题**；面向开发任务优先查看 [智能体环境与模型对接](../capabilities/agent-environment/README.md)、[对局状态观测](../capabilities/state-observation/README.md)。

## 相关项目与路线（依据公开文档）

| 项目 | 技术来源 |
| --- | --- |
| [FirstLight CR](../projects/firstlight-cr.md) | [作者仓库](https://github.com/Jaasssoooonnnnn/FirstLight_CR) |
| [Jason Clash Royale Battle Engine](../projects/jason-battle-engine.md) | [作者仓库](https://github.com/Jason-XII/clash-royale-battle-engine) |
| [Jason Clash Royale Simulator](../projects/jason-simulator.md) | [作者仓库](https://github.com/Jason-XII/clash-royale-simulator) |
| [Tencent Model Harness](../projects/tencent-model-harness.md) | [作者仓库](https://github.com/ak1NaN/ClashRoyale-tencent-model-harness) |
| [Hasty-CR](../projects/hasty-cr.md) | [作者仓库](https://github.com/hastylmao/Hasty-CR) |
| [RoyaleGym](../projects/royalegym.md) | [作者仓库](https://github.com/RoyaleGym/RoyaleGym) |
| [RoyaleSim](../projects/royalesim.md) | [作者仓库](https://github.com/RoyaleGym/RoyaleSim) |
| [crforge](../projects/crforge.md) | [作者仓库](https://github.com/voonhous/crforge) |
| [KataCR](../projects/katacr.md) | [作者仓库](https://github.com/wty-yy/KataCR) |

## 研究边界与差异

模仿学习、PPO、视觉识别、实时模型部署是不同流水线环节。不能把模型训练成果等同于已经有可部署的统一接口。

## 需要补充的证据

- 固定游戏客户端、资源和源代码提交版本。
- 反例、差分对照测试、性能测量的条件。
- 作者审核与具体许可证影响（公开不代表可直接复制）。

[能力总入口](../capabilities/README.md) · [项目索引](../projects/README.md)

## 新增技术来源（2026-10-13）

- [ClashRoyaleEnv](../projects/itzik-clashenv.md)：C++17确定性模拟器、独立深拷贝分支、搜索教师、PPO训练及浏览器可视化。
- [ClashAI](../projects/clashai-vegetableleaf.md)：原生回放重驱、公开观测、模仿学习和强化学习部署流水线。
- [CRSim Agent](../projects/crsim-agent-larkindaniel.md)：冻结八卡的确定性模拟、信息公平性审计、PPO复现实验。
- [ClashRoyaleBuildABot](../projects/build-a-bot.md)：屏幕视觉检测器、结构化状态和动作策略分层。
- [CR Detection Dataset](../projects/detection-dataset.md)：历史图像切片及合成目标检测样本生成方法。
- [Claude Royale](../projects/claude-royale.md)：截图—LLM决策—输入的多智能体调度与UI生命周期经验。

## 新增研究来源（2026-10-15）

- [CR Native Sandbox](../projects/native-sandbox-imax9d.md)：原版 Android x86_64 `libg.so` 离线无画面战斗宿主；通过 JniHost/AssetManager/JNI 初始化，提供 reset、step、双方动作、原生观测与 JSON-line Worker。
- [R0 Elite Training](../projects/r0-elite-imax9d.md)：原生对局采集数据的版本化编译/准入/认证/训练流程，包含 tensorizer、分批训练、后端共享内存和一致性测试。

## 2026-10-15 开发者网络新增来源

- [CR Native Sandbox](../projects/cr-native-sandbox.md)：参见固定构建及相应技术边界；统一评价以实现登记为准。
- [Clapha Engine (private)](../projects/clapha-engine.md)：参见固定构建及相应技术边界；统一评价以实现登记为准。
- [R0 Elite Training](../projects/r0-elite-training.md)：参见固定构建及相应技术边界；统一评价以实现登记为准。
- [RoyaleAPI Downloader](../projects/royaleapi-downloader.md)：参见固定构建及相应技术边界；统一评价以实现登记为准。
- [Arron CR Collector](../projects/cr-collector.md)：参见固定构建及相应技术边界；统一评价以实现登记为准。
