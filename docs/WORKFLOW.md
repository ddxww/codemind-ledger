# GitHub 分支协作操作手册（Windows / PowerShell）

## 初次准备

确保已安装 Git、Python 3.10+；先在仓库 Settings > Collaborators 邀请同学并让大家接受邀请。
每个人在自己的电脑上设置**自己的** git user.name 与 user.email，不要共享同一个身份。

```powershell
git clone https://github.com/yz-Yezi-Genm/codemind-ledger.git
cd codemind-ledger
git switch main
git pull origin main
git switch -c feat/a1-storage
```

分支名称请按分工替换，如 `feat/b1-add`、`feat/c2-statistics`、`feat/d3-interaction`。

## 编码与提交

```powershell
git status
git add core/storage.py tests/test_storage.py
git commit -m "feat(storage): implement JSON persistence"
git push -u origin feat/a1-storage
```

以上路径、提交信息只针对 A1 示例；**必须是自己真实完成的文件和修改**。
第一次推送后，到 GitHub 页面点击 Compare & pull request，目标分支设为 main。
组长审查接口、测试、合并冲突，再点击 Merge pull request。

## 同步主分支

在自己功能分支上整合最新 main：
```powershell
git fetch origin
git switch feat/a1-storage
git merge origin/main
```

如果发生冲突，检查 `git status`，人工解决冲突标记，再运行测试、`git add`、`git commit`。
**不要随意执行 `git push --force` 或 `git reset --hard` 丢掉他人成果。**

如果需要单纯查看集成版本：
```powershell
git switch main
git pull origin main
python -m pytest -q
python app.py
```

## 集成与 Release

- 建议每完成一个模块就提交 PR，不要等最后十分钟批量合并。
- 修改共享接口前必须先通知依赖该接口的成员。
- Release 前由组长在 main 上跑完整功能测试、手工操作一次新增/查看/查询/统计/重启持久化。
- 仓库顶部 Releases > Draft a new release > 创建 tag（如 `v1.0.0`）> Publish release。
- 17:00 前确认 Release 已发布、所需链接可正常访问，现场可演示。
- 如果仓库为 Private，**未获得授权的助教可能无法访问**。应由组长提前确认课程允许私有仓库与审核人员权限；必要时在 GitHub 设置中改成 Public，避免提交失效。

## 演示与博客佐证

保存真实 PR/commit 页面、测试结果、软件运行截图和视频；
记录至少 3 个开发过程中较耗时的实际问题；每位成员独立提供编程心得。
