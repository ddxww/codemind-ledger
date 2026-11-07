# CodeMind Ledger · 个人记账本

福州大学 H202601 软件工程与软件工程实践 · 2026-11-07 现场编程

> 当前状态：**协作开发骨架**。仓库中的函数占位符尚未实现，**不是已完成的软件**。
> 所有成员必须独立编写自己负责的真实功能并使用本人账号提交，禁止伪造提交记录或代写。

## 技术约定

- Python 3.10+、Flask、原生 HTML/CSS/JavaScript
- JSON 本地文件保存（`data/records.json`，不纳入版本控制）
- 唯一数据契约和 API 约定请看 [docs/CONTRACT.md](docs/CONTRACT.md)
- 12 人模块归属请看 [docs/TEAM_TASKS.md](docs/TEAM_TASKS.md)
- 分支、PR、合并流程请看 [docs/WORKFLOW.md](docs/WORKFLOW.md)

## Windows 本地启动（当前仅有骨架页面）

```powershell
git clone https://github.com/yz-Yezi-Genm/codemind-ledger.git
cd codemind-ledger
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

浏览器打开 http://127.0.0.1:5000 。当前主页与 `/api/health` 可访问，
业务 API 暂时统一返回 HTTP 501，**等模块负责同学自行完成后才能真正记账**。

如 PowerShell 禁止激活，可以不激活环境，直接：
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

## 运行基础检查

```powershell
python -m pytest -q
```

注意：现有测试只检查项目骨架的 HTTP 响应，并不代表记账功能完成；
成员应自行为负责模块编写真实单元测试与边界用例。

## 推荐协作节奏

1. 组长确认数据格式和接口，不再任意更改（如需变更，先群内同步）。
2. 每人克隆仓库，从 `main` 新建自己的 `feat/xxx` 分支。
3. 只修改负责的模块和自己的测试文件；跨文件改动先沟通。
4. 本人运行测试、提交 commit、推送分支、创建 Pull Request。
5. 组长/同伴 Review 后分批合并，集成测试，再在 17:00 前发布 GitHub Release。
6. 演示后收集真实开发记录、截图、视频，23:00 前完成团队博客。

### 截止节点
- 17:00：提交仓库链接并发布可演示版本 Release
- 17:00–17:15：现场演示
- 23:00：团队博客与要求的链接

## 当前模块进度
- [x] 仓库基础骨架、接口文档与协作规范
- [ ] A1~A3 数据层
- [ ] B1~B3 记账功能
- [ ] C1~C3 查询统计
- [ ] D1~D3 Web 界面及路由
- [ ] 全流程联调、演示与 Release

## 说明
`data/sample_records.json` 是可提交的模拟数据；
`data/records.json` 为运行时用户数据，不应提交到 GitHub。
