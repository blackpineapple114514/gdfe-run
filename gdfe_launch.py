# -*- coding: utf-8 -*-
"""gdfe_launch.py —— 「广财阳光跑」独立入口：把 --gdfe 塞进 argv 后走 app.main()。

打包成 gdfe-run.exe：双击只开「广财阳光跑」精简页（手机尺寸）。
仍然自带本地 mock（只监听本机、**默认绝不连真服**）；要连真服必须在页面
「高级设置」里手动切到「真服」并在确认框点确定 —— 那一刻才会现读 p.txt 并提交。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (HERE, os.path.dirname(HERE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

if "--gdfe" not in sys.argv:
    sys.argv = [sys.argv[0], "--gdfe"] + sys.argv[1:]

from app import main            # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
