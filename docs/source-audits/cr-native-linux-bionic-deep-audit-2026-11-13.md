# IMAX9D/cr-native-linux-bionic 深入审查（2026-11-13）

**审查结论：保持 P1，暂不升级 P2。** 上游 `IMAX9D/cr-native-linux-bionic`，核查了完整 Git tree（18 entries，含目录）、MIT LICENSE、Python 包入口、CLI、runtime、构建脚本、两份 manifest、测试源码。此前已有 runtime/测试局部审查记录。**未执行上游测试、未取得 273 MB runtime bundle、未运行真实 worker**。

## 已核对实现与证据

- [runtime.py](https://github.com/IMAX9D/cr-native-linux-bionic/blob/main/cr_native_bionic/runtime.py) blob `20b1baec0c58fbcb0a1bf0bcac58763f7706112f`：固定版本 `15.535.29` / `150535029`、`x86_64`；使用 Android 31 userspace 的 `/apex/com.android.runtime/bin/linker64` + `/apex/com.android.art/bin/dalvikvm64`，直接启动 `royale.nativehost.JniHost serve-direct`，无需完整 Android AVD/KVM，但仍依赖 Bionic/ART/Android 文件系统和二进制 bundle。归档及 worker 文件验证 size + SHA256，安装写原子 receipt。
- [CLI](https://github.com/IMAX9D/cr-native-linux-bionic/blob/main/cr_native_bionic/cli.py) blob `08a66f1ace80b3c55069c1b8b038c110054079d4`：verify-bundle、install、doctor、start、status、stop、smoke；install 要求 `--apply`，写系统绝对根时需 root；smoke 检查 ping/status 返回。
- [manifest](https://github.com/IMAX9D/cr-native-linux-bionic/blob/main/manifests/runtime-150535029-linux-bionic.json) blob `86fd75ad1c483f605ee9a224f228bd957005cd20`：8 归档及 6 worker 文件 hash/size；`libg.so` SHA256 `fa6704b83cb9c5b8eecb7b56c9671b834d636a3a6d9ac446e698e1262dc246ba`。
- [bundle receipt](https://github.com/IMAX9D/cr-native-linux-bionic/blob/main/manifests/runtime-150535029-linux-bionic.bundle.json) blob `4dd1f010841a0267746865bdcec1e0b46e8cb8db`：发布包 `273274290` bytes，SHA256 `e25f6484e888c175cadddaed4be9fbb69bf92d2f6f9b75f3f3c4c17629830db0`。此为**仓库声明**，本轮未下载校验。
- [build_bundle.py](https://github.com/IMAX9D/cr-native-linux-bionic/blob/main/scripts/build_bundle.py) blob `e6e869358a4214dc9639ea9212a1a594ec721cca`：构建前核对 archive size/SHA256，输出 ZIP 和收据，拒绝覆盖现有目标。
- [test_runtime.py](https://github.com/IMAX9D/cr-native-linux-bionic/blob/main/tests/test_runtime.py) blob `fc868d4f98e0c6078b9a161177e22333c64b1658`：5 个 unittest 覆盖版本约束、根目录映射、命令、环境变量、非法 manifest。**只确认测试存在，没有执行**。
- [pyproject.toml](https://github.com/IMAX9D/cr-native-linux-bionic/blob/main/pyproject.toml) blob `1d97753d782bf2f03f562a0589a74ed390d2c509`：Python >=3.11，setuptools >=69，版本 0.1.0，无额外运行依赖声明。
- [LICENSE](https://github.com/IMAX9D/cr-native-linux-bionic/blob/main/LICENSE) blob `73a0f34a3337ed85da9b50c18f785cb7f81b23ad`：Python 仓库 MIT；**不推定 APK、libg.so 或 Android userspace 同属 MIT**。

## 发现的风险与待验证边界

1. `rooted(system_root, absolute)` 仅做 `lstrip('/')` 后 Path 拼接，**不防止调用者提供 `..` 路径逃逸**；现有测试名 `test_root_mapping_does_not_escape_prefix` 只检查正常绝对路径。当前代码内部大多传入常量路径，风险取决于上层调用边界；建议增加恶意输入单测。
2. `_tar` 调用系统 `tar -xzf` 解压发布包；manifest 哈希验证可以防止意外篡改，但未见独立归档路径/符号链接成员安全检查。应验证 bundle 来源及安装隔离。
3. `tcp_request` 持续收包直到换行或 EOF，未见响应大小上限；应增加最大响应字节数及测试。
4. 安装会写 `/apex`、`/system`、`/linkerconfig`、`/dev/__properties__`，并可能复制到 `/data/local/tmp`；应在隔离 Linux 容器或虚拟机执行，勿在日常宿主系统直接安装。
5. 完整可运行性依赖未随源码仓库提供的约 273MB runtime bundle；需验证真实包 SHA256、Linux x86_64 环境、doctor/smoke、worker 多实例稳定性和授权来源。

## P2 门槛

在隔离环境拉取固定 commit，执行 `python -m unittest discover -s tests -v`；验证 bundle 的 SHA256；完成 install/doctor/smoke 的实际运行和失败注入，核对授权/版本边界，再更新评级。当前 **P1 深审完成，P2 未达标**。
