# IMAX9D/royaleapi-downloader 局部源码审查（2026-11-13）

等级 **P1**；默认分支 Git tree SHA `ed80af8eedecbd48e7a49babfee309f41b595e9d`。仅核查列出的文件，未固定完整 commit 或运行测试。

- [crawler/authoritative.py](https://github.com/IMAX9D/royaleapi-downloader/blob/HEAD/crawler/authoritative.py) — blob `f18e6eb845066053a4e3741aa89820883060cace`
- [crawler/authoritative_manifest.py](https://github.com/IMAX9D/royaleapi-downloader/blob/HEAD/crawler/authoritative_manifest.py) — blob `f151b4adca9428b7d2a477947d7a4d5154960ccc`
- [crawler/test_downloader_refactor.py](https://github.com/IMAX9D/royaleapi-downloader/blob/HEAD/crawler/test_downloader_refactor.py) — blob `d07730e4250ec01f02be507687a511ed5a2aaebc`

## 发现

authoritative.py 为离线回放 schema 升级与 native contract 准入检查，验证游戏版本、规范化 SHA-256、卡牌/塔兵及模式映射；明确不访问 RoyaleAPI 或 libg。authoritative_manifest.py 按来源列表 URL 组织历史数据，先升级列表元数据再抓回放详情。测试代码涵盖 SQLite 迁移、并发任务领取去重、恢复与索引；未执行。

## P2 待核查

继续检查 client/queue/parsers/限流、来源许可及回放真实性。
