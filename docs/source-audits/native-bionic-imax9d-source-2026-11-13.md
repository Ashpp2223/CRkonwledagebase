# native-bionic-imax9d 源码局部审查（2026-11-13）

等级 P1。通过 GitHub API 枚举默认分支文件树（truncated=false），tree SHA `7840e4e920fb8c4d63efb16343c76`；抽样阅读以下文件前段。未冻结整体 commit，未执行测试。

- [cr_native_bionic/runtime.py](https://github.com/IMAX9D/cr-native-linux-bionic/blob/main/cr_native_bionic/runtime.py) — blob `20b1baec0c58fbcb0a1bf0bcac58763f7706112f`
- [tests/test_runtime.py](https://github.com/IMAX9D/cr-native-linux-bionic/blob/main/tests/test_runtime.py) — blob `fc868d4f98e0c6078b9a161177e22333c64b1658`

## 发现与限制

Linux Bionic 方案用 linker64/dalvikvm64 与 Android 用户态文件运行原生 worker，无 AVD/KVM；仍依赖 Bionic/ART 和原生资源。runtime.py 检查版本与 bundle SHA-256；test_runtime.py 定义版本、路径、worker 命令和环境变量测试。未执行测试。

## 待查

完整函数体、测试、依赖、许可证；固定 commit；验证 Tick/RNG/快照/版本一致性，达到标准后再升 P2/P3。
