# ak1NaN/ClashRoyale-tencent-overlay 局部源码审查（2026-11-13）

等级 **P1**；默认分支 Git tree SHA `00446d3f77e82acdf37c5ad5d859e68ed3069503`。仅核查列出的文件，未固定完整 commit 或运行测试。

- [overlay/hook_opponent_elixir.js](https://github.com/ak1NaN/ClashRoyale-tencent-overlay/blob/HEAD/overlay/hook_opponent_elixir.js) — blob `f71ebbb9187638b7e63e146d57a0e99d3a5cf4ef`

## 发现

Frida hook 从 libg.so 读取圣水 raw 值，按 /10000 换算；使用账户身份和玩家指针区分 self/opponent，监听下牌队列构造、卡牌 ID、坐标，并进行事件去重。依赖固定 RVA，内存观测值不保证等于服务端权威值。

## P2 待核查

继续检查 Python overlay、部署脚本、版本适配与实际运行校准。
