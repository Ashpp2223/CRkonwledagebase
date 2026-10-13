# 技术协作地图：怎样利用已有成果衍生新能力

**核心方法**：每条连接必须列出数据契约、验证方式和故障模式；某项目被列为上游不表示它已经符合本中台的 Draft 接口。

## 1. 模拟分支与搜索

```text
已知局面 (Provenance + Replay/Observation)
  └─> SimStateAdapter （需补状态同构与不确定性）
       └─> Snapshot / Fork
             ├─ 候选A：rollout -> score
             ├─ 候选B：rollout -> score
             └─ 候选C：rollout -> score
                   └─> 选择动作 / 标注训练样本 / 蒸馏
```

- 候选引擎：[itzik](../projects/itzik-clashenv.md) 的 [GameManager::snapshot](https://github.com/itzik123/ClashRoyaleAi/blob/2f172925a15b17f973291f41a789b19a29f0fc43/include/core/GameManager.h#L254-L268) 与 [Python 搜索](https://github.com/itzik123/ClashRoyaleAi/blob/2f172925a15b17f973291f41a789b19a29f0fc43/python_ai/search/search.py#L211-L238)；[RoyaleSim](../projects/royalesim.md) 的字节存储；[FirstLight](../projects/firstlight-cr.md) 的**单进程**原生句柄。
- 不可混淆：深拷贝一个自建 C++ 引擎，与把原生游戏进程内部状态安全克隆为独立副本不是同一回事。
- 最小证据：Fork 不污染原状态、随机生成序列稳定、耗时分布、候选对照试验、真实对局校准差异。

## 2. 回放资料转模型

```text
原始回放标识+作者许可+客户端版本
  -> EventTimeline（动作时刻/位置、缺失字段）
  -> Native/Sim Replay（可复现等级）
  -> Observation-Action Samples（FAIR 公开信息）
  -> IL 数据集
  -> RL 自博弈环境与版本指纹
  -> 训练/验证门禁
```

- [FirstLight](../projects/firstlight-cr.md)、[Jason](../projects/jason-battle-engine.md)、[ClashAI](../projects/clashai-vegetableleaf.md) 提供不同阶段参考。
- 重点复用 **数据契约和验证手段**，不要复制第三方回放/权重当成获得了新版权。
- 注意潜在数据泄漏：对手手牌、未来出牌、隐藏圣水、随机种子及实体调试 ID 不能误作为公平策略输入。
- 即使游戏状态来自“原生”，缺原始初手与 RNG 的回放仍可能只是**相容重建**。

## 3. 视觉代理与可解释复盘

```text
屏幕流 -> 画面标定 -> 单位/牌组/状态检测
      -> 观测置信度 + 丢帧/延迟
      -> 离线状态估计/模拟器推进
      -> 可解释事件、对局时间轴和人工检验
```

- 输入候选：[KataCR](../projects/katacr.md)、[BuildABot](../projects/build-a-bot.md)、[视觉数据集](../projects/detection-dataset.md)。
- 状态外推候选：[ClashAI](../projects/clashai-vegetableleaf.md)、[ClashRoyaleEnv](../projects/itzik-clashenv.md)。
- 输出候选：[Replay Studio](../projects/replay-studio.md)、[Ashpp 复盘器](../projects/ashpp-replay.md)。
- 必须记录屏幕采样时刻、游戏原生 Tick 对齐关系、动作来源置信度；**视觉猜测不应污染已验证的真实对局日志**。

## 4. 游戏内容数据与机制准确度

```text
合法获取的原始资源+版本 -> Fingerprint+Hash
  -> SC/CSV Decoder -> CardTable / MechanicsCatalog
  -> 差分测试基准 -> 机制误差/不确定性文档
  -> 更新项目源码/测试和中台能力来源
```

- [SC Downloader](../projects/sc-downloader.md)、[sc_extract](../projects/sc-extract.md)、[Supercell decoder](../projects/supercell-csv-decoder.md) 可拆分为不同环节。
- [RoyaleAPI Static Data](../projects/royaleapi-static-data.md) 适合显示/数据字段索引，不能代替精确的客户端规则版本。
- [Hasty-CR](../projects/hasty-cr.md)、[RoyaleSim](../projects/royalesim.md)、[CRSim](../projects/crsim-agent-larkindaniel.md) 的可复现机制证据，比“完全复刻”宣称更重要。

## 5. LLM Agent 的运行时与风险

- [Claude Royale](../projects/claude-royale.md) 关注 UI 工作流和多 Agent 延迟；[ClashAI](../projects/clashai-vegetableleaf.md) 关注训练到推理端的状态契约与版本门禁。
- 设备自动化可违反游戏条款；研究工作应优先在允许的离线/模拟环境中验证，技术中台不提供绕过游戏限制的工作流。
- 对未确认回执的指令**禁止盲重试副作用动作**；与模拟器不同，真实 UI 接收不等于对局状态已改变。

更多细节参考 [能力中心](../capabilities/README.md)。
