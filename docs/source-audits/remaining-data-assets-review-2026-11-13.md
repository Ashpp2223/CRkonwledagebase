# 剩余数据与文档仓库分类审查（2026-11-13）

此文记录**资产/文档审查**，不把无可执行源码的项目虚升为 P1。未执行数据集全量统计、文件完整性或上游测试。

## RoyaleAPI/cr-api-data

- HEAD `d5461b0a59bff33c4da2fc845b07275b66b2d6ff`，47 tree entries。
- [docs/json/cards.json](https://github.com/RoyaleAPI/cr-api-data/blob/d5461b0a59bff33c4da2fc845b07275b66b2d6ff/docs/json/cards.json) blob `3194825bf0349a2bd75110099ead148d212c6d65`：卡牌 id、sc_key、费用、稀有度、进化字段。
- [docs/json/battle_timelines.json](https://github.com/RoyaleAPI/cr-api-data/blob/d5461b0a59bff33c4da2fc845b07275b66b2d6ff/docs/json/battle_timelines.json) blob `8419ec707b2e41afb643d28722c02a69f4c4a9ad`：Default 模式 180s 正常 + 120s 加时，初始圣水 6，阶段圣水补满时间 28000/14000/9300 ms。仅对该仓库所记录版本成立；须与具体游戏构建版本交叉验证。
- 数据仓库保留 P0，后续应审查 schema、字段主键、版本、来源与全量 JSON 有效性。

## RoyaleAPI/cr-api-assets

- HEAD `b4530a1043b213ee2baf9c50a3d0d7fae22c2313`，3409 tree entries，以 PNG 图片为主。
- LICENSE blob `fbfe035da59383e147f99ed931cc8a96ee914ac8` 为非官方声明及 Supercell Fan Content Policy 链接，**不能自动视为开放源码许可或任意再分发授权**。
- 保留 P0，后续做资产清单、文件头抽样、命名匹配、许可审查。

## RoyaleAPI/royalerating

- HEAD `644a4a495f9b276c09187dfc997fdc6ddefd1762`，28 tree entries，主要为文档与图片。
- [docs/rr-math.md](https://github.com/RoyaleAPI/royalerating/blob/644a4a495f9b276c09187dfc997fdc6ddefd1762/docs/rr-math.md) blob `a73bec6701180ae4ce3dfd38f184978ad6756f21`：公开 RR = μ − 3σ 及胜负/对手强度影响的定性说明；没有足够源码证明 μ、σ 的具体更新公式。保留 P0。

## Aminiwow/royaleapi-replay-dataset

- HEAD `210137cdd6f72438491fc3b369ee4191e26f5b51`，仅 README，blob `8d32108da53e4986c159a0e30691ec05b56945ae`。
- README 声称匿名回放导出数据在 Releases；本轮**未检查 Releases 文件及实际数据样本**。保留 P0。

## wty-yy 两个数据集仓库

- Detection Dataset HEAD `31b4151fedb1b914e99c3c122c16dca61cb2b905`，27041 tree entries。
- Clash Royale Dataset HEAD `7df93642047d4df541225755bca61c301788bebe`，32027 tree entries。
- 两者的 `images/part2/ClashRoyale_detection.yaml` 具有相同 blob `02990874e94bc52234e63d54629c929a1b875868`，包含检测类别映射、`val: annotation.txt`、本机绝对路径及 `train: null`。这仅证明该文件内容相同，**不能证明整个数据集重复或完整一致**。
- 两者保留 P0，下一步应统计各自图片/标注路径交集、缺失标注、类别 ID 范围与划分泄漏。

## 待确认仓库

- `arronwang01/clapha-engine` 此前 GitHub API 返回 404；不可直接判定为已删除，需检查改名、转移、私有化和镜像。
