# clashback 源码局部审查（2026-11-13）

等级 P1。通过 GitHub API 枚举默认分支文件树（truncated=false），tree SHA `45c1f26b942ae1d706f2004791e73013e4330099`；抽样阅读以下文件前段。未冻结整体 commit，未执行测试。

- [neo_replay/native_snapshots.py](https://github.com/ak1NaN/Clashback/blob/main/neo_replay/native_snapshots.py) — blob `94f4d1e5e9224ac381a6de797c5f7ad6a48aac08`
- [neo_replay/tick_cache.py](https://github.com/ak1NaN/Clashback/blob/main/neo_replay/tick_cache.py) — blob `e16f909ed6ac3619889b27ac8ffd662dcc309b2e`
- [neo_replay/native_worker.py](https://github.com/ak1NaN/Clashback/blob/main/neo_replay/native_worker.py) — blob `8426daf04cbdaadd7ab751976b8e4556331bc0bf`

## 发现与限制

原生快照支持 build 160402020/160635001，原生编码/恢复须在战斗所属线程执行；tick_cache 使用 zlib、SHA-256、索引最后发布、严格大小限制（最多 7201 ticks、256MiB 总量）；native_worker 明示 x86_64 Python，不需要 Android/ADB，HTML 无 RNG seed 时用起手/牌序相容性搜索候选。尚未验证恢复后的继续推进与分支一致性。

## 待查

完整函数体、测试、依赖、许可证；固定 commit；验证 Tick/RNG/快照/版本一致性，达到标准后再升 P2/P3。
