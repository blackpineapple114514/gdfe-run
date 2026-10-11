# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller 打包配置：「广财阳光跑」独立小程序。

    pyinstaller --noconfirm --clean gdfe-run.spec

产物：dist/gdfe-run.exe（onefile，**windowed 无控制台**）。
"""
import os

HERE = os.path.dirname(os.path.abspath(SPEC)) if "SPEC" in globals() else os.getcwd()

HIDDEN = [
    # 延迟导入（写在函数里的 import），静态分析容易漏，显式点一下
    "app", "mock_boxkj", "server", "flow", "v2client", "tracklib", "envlib",
    "device_profile", "device_catalog", "w8b_sign_probe", "v2_chain",
    "webview.platforms.winforms", "clr_loader", "pythonnet",
]

a = Analysis(
    [os.path.join(HERE, "gdfe_launch.py")],
    pathex=[HERE],
    binaries=[],
    datas=[(os.path.join(HERE, "static"), "static")],
    hiddenimports=HIDDEN,
    hookspath=[], hooksconfig={}, runtime_hooks=[],
    excludes=["PIL", "tkinter", "matplotlib", "numpy", "pandas", "scipy", "pytest"],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz, a.scripts, a.binaries, a.datas, [],
    name="gdfe-run",
    debug=False, bootloader_ignore_signals=False, strip=False, upx=False,
    runtime_tmpdir=None, console=False,
    disable_windowed_traceback=False, argv_emulation=False,
    target_arch=None, codesign_identity=None, entitlements_file=None,
)
