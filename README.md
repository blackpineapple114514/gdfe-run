# gdfe-run · 广财阳光跑

一个**本地运行**的「阳光跑」记录生成器（**广东财经大学 · 广州校区田径场** 定制版）。
它在你的电脑上起一个本地服务 + 一个手机尺寸的页面：按标准 400 m 跑道生成一段跑步轨迹，
自动完成人脸打卡与上传。

> ⚠️ **仅供学习与个人研究。** 请遵守你所在学校的规定与相关服务条款，使用风险自负。
> 本仓库不含任何个人凭据、真机设备码或真实记录号。

## 特性
- 一键生成标准 400 m 跑道轨迹（起点随机、方向固定逆时针）
- 自动人脸打卡（起 / 中 / 末按服务器要求）与上传
- 登录 → 开跑 → 中途停止（按已跑段上传 / 放弃）→ 查询历史
- 机型下拉（**带搜索**）+「设为默认」+ 找不到机型时手填 / 粘贴 AI 返回的 JSON
- 默认参数即可落在有效区间：**2.00 km · 400 m 跑道 · 6′00″/km**

## 运行
```bash
pip install -r requirements.txt
python gdfe_launch.py      # 或 python app.py
```
默认起本地服务并打开**手机尺寸**窗口；没有 pywebview 时回退系统浏览器。
只起服务不开窗口（自测/无桌面环境）：
```bash
python app.py --no-window
```

## 打包（Windows 单文件）
```bash
pip install pyinstaller
pyinstaller --noconfirm --clean gdfe-run.spec
# 产物：dist/gdfe-run.exe（onefile，无控制台）
```

## 依赖
- Python 3.10+
- `pywebview`（桌面窗口；可选，缺失则回退系统浏览器）
- `pycryptodome`（请求信封加解密）
- `Pillow`（人脸图）

## 目录
```
gdfe_launch.py     入口：塞 --gdfe 后走 app.main()
app.py             一键启动：本地 mock + 工作台 + 窗口
server.py          本地 HTTP 服务（/gdfe 页面 + 各 API）
tracklib.py        轨迹生成（几何 / 配速 / 噪声 / 点字段）
flow.py            上传流程编排（配置 / 打卡 / 提交 / 读回）
v2client.py        新链路客户端（信封 / 签名 / 表单）
v2_chain.py        签名与加解密工具
w8b_sign_probe.py  签名探针
mock_boxkj.py      本地 mock 服务器（默认只监听本机）
device_profile.py  设备 / app 身份（默认档 + 机型目录）
device_catalog.py  机型目录（自动生成）
envlib.py          环境 / 路径
static/gdfe.html   「广财阳光跑」页面
static/geo.js      跑道几何
static/schools.json 学校快照
```

## 安全与隐私
- **账号密码不在代码里**：只在运行时于本机读取（默认 `~/Desktop/p.txt`，或页面手输）。
- **数据留本机**：日志与「记住账号密码」都落在本机（后者为 `~/.gdfe_run_creds.json`，明文、仅本机，可随时清除）。
- **一账号一机**：机型固定、iOS 设备码**每台机首启随机生成并持久化**。
- 仓库已脱敏。

## 范围说明
本仓库**只含广财定制版**（`/gdfe` 页面及其运行所需引擎）。
通用「路线工作台」UI 不在本仓库。

## License
MIT
