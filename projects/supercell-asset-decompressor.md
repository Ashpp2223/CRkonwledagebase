# Supercell Asset Decompressor

- 上游：https://github.com/abhishek-kumar-14/supercell-asset-decompressor
- 证据等级：R1 / author-documented（仅核查 README，未运行）
- 来源：https://github.com/abhishek-kumar-14/supercell-asset-decompressor/blob/HEAD/README.md
- 许可：待核查；第三方游戏文件和素材不可因仓库公开而推定可再分发

## 技术价值与边界

Python 文件/目录资源容器解压工具，README 称支持 SC/SC2/LZMA/Zstd 等包装，SCLZ/LZHAM 仅识别未解压；格式兼容性尚未实测。

## 后续验证

固定上游 commit；核查实现入口、依赖版本、许可证与测试；原生战斗相关项目需核对 Tick、状态恢复、输入与快照的一致性。当前不登记 R2/R3 能力实现。
