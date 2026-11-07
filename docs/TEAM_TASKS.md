# 12 人独立开发分工

**以下为角色占位编号，不代表已分配到具体姓名。**
每个模块必须由对应成员独立编写真实功能并留下本人账号的 commit；骨架中现有的 TODO/NotImplementedError 不属于成员贡献。

| 编号 | 模块 | 主要文件 | 交付标准 |
| --- | --- | --- | --- |
| A1 | JSON 存储 | core/storage.py | 首次读取、读写持久化、中文内容 |
| A2 | 记录校验 | core/validators.py | 合法/非法类型、金额、日期、类别 |
| A3 | 类别管理 | core/categories.py | 类别列表、类型与类别规则 |
| B1 | 添加记录 | services/record_add.py | 创建唯一 ID、保存、异常处理 |
| B2 | 修改/删除 | services/record_edit.py | ID 查询、更新、删除、找不到 |
| B3 | 最近记录 | services/record_list.py | 按日期排序、limit |
| C1 | 组合筛选 | services/filters.py | 日期、类别、类型、金额上下限 |
| C2 | 收支汇总 | services/statistics.py | 收入、支出、结余、笔数 |
| C3 | 分类图表数据 | services/charts.py | 支出分组、汇总结果 |
| D1 | Flask API 整合 | app.py | 路由调用各模块、HTTP 错误处理 |
| D2 | 前端页面 | templates/index.html、static/style.css | 表单、列表、统计区、自适应 |
| D3 | 前端交互 | static/app.js | 请求接口、提示信息、图表 |

组长负责维护分工表、决定接口变更、安排代码复审与最终 Release；
若组长兼任 D1，必须亲自编写 D1 的实际功能。

## 自查要求

1. 功能由本人完成，不使用其他人代写的实现代码。
2. 每人使用自己的 GitHub 账号提交有意义的 commit。
3. 尽量只改自己负责的文件；自己的测试放入 `tests/test_<module>.py`。
4. 本地测试通过后提交 Pull Request，写清功能、测试方法和截图。
5. 经 Review 并成功合并后，检查 main 分支的整体运行状况。
6. 博客据实记录贡献和过程，不用 commit 数量冒充质量。

建议先由 A 组确定存储与验证的具体行为，B/C 用模拟数据并行开发。
