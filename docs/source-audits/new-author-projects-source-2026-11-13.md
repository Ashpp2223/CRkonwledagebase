# 作者全量扫仓后新增项目源码初查（2026-11-13）

本页记录**尚未正式纳入 57 项 registry 的候选**，与 P0/P1 正式项目评级分开。已检查实际源码而非仅 README，未运行上游测试。

## arronwang01/clash-royale-simulator-trial

- [源码](https://github.com/arronwang01/clash-royale-simulator-trial/blob/main/src/clasher_new/battle.py)，blob `17a87d0da7fedef36a36a688e775fc58831e9901`，43,532 字符。
- 实现 Entity、生命/护盾、攻击冷却、目标状态、跳河、速度增益/减益、特殊单位机制委托。
- `Entity.__init__` 使用 `eval(f"{self.card_name}(self)")` 按卡名创建特殊机制处理器，虽然仅当卡名在 globals 且非 Projectile 时执行，仍需核对卡名来源与输入可信边界。
- 仓库另含 MECHANIC_AUDIT、CALIBRATION_PLAYBOOK、SIMULATOR_STATUS 等文档。应与已登记 Jason-XII/clash-royale-simulator 及 longlingking 版本做文件级比较，判断同源、独立演化和新增机制，**避免误收录为独立原创引擎**。

## jthingelstad/elixir-bot

- [pyproject.toml](https://github.com/jthingelstad/elixir-bot/blob/main/pyproject.toml)，blob `de338c8ce8e7194ac0d75accc0f18dbe317a5e10`。
- Python `>=3.14,<3.15`，Discord.py、Anthropic、APScheduler、aiohttp、jsonschema、Jinja2 等依赖，pytest/mypy/ruff 开发测试，包含独立事件驱动 Discord 公会运营系统；repo tree 612 entries。
- 与已登记的 elixir-mcp-discord 和 elixir-mcp 主仓库需要核对数据流和职责关系，后续再正式收录。

## TrixallTR/SC-Server

- [src/stream/packet.rs](https://github.com/TrixallTR/SC-Server/blob/master/src/stream/packet.rs)，blob `e1a4da5ec1edf836d7c3da3f6186b2fc8f6fa2a4`。
- Rust 构造 Supercell 风格数据包，头部 u16 message ID + u24 payload length + u16 reserved；包体含 major/minor/build 版本字段。
- 当前读到的 `build` 方法会向持久 Writer 追加数据而不清空缓冲；如果重复调用同一 Packet 实例，可能累计前次包体和头部。需要查看调用处与测试才能判断是否真实缺陷。
- 仅能确认 Supercell 协议相关，**不能仅凭 packet 结构断言适配现行皇室战争服务器**。

## Fork 身份已核实

- `arronwang01/clash-royale-battle-engine`：fork parent `Jason-XII/daybreak-cr`。
- `max-miller1204/KataCR`：fork parent `wty-yy/KataCR`。
- `Ashpp2223/ClashRoyale`：fork parent `retroroyale/ClashRoyale`，包含 C# 战斗/服务器模块。
- `Ashpp2223/Clash-Royale-v1-Client-Leak`：fork parent `clashRoyaleClients/Clash-Royale-v1-Client-Leak`，含 C++ 客户端源码，须特别审查原始版权/再分发边界。

## 收录优先级

优先：simulator-trial、elixir-bot；其次：SC-Server（需核对游戏版本）；fork 先核实相对于上游的独立差异再决定是否登记独立项目。此页不修改正式项目总数。
