# 统一接口契约（开发前必读）

本文件是模块间约定，**不能由某个成员私自改变**。需要改动时先在群中同步并修改文档。

## 记录结构

```json
{
  "id": "rec_001",
  "type": "expense",
  "date": "2026-11-07",
  "amount": 25.50,
  "category": "餐饮",
  "note": "午餐"
}
```

- id: 全局唯一非空字符串，新增时由 B1 生成；客户端新增无需提供
- type: `income` 或 `expense`（不要使用中文作为 type 值）
- date: `YYYY-MM-DD`，必须为真实有效日期
- amount: 数字且严格大于 0；显示保留两位小数
- category: 中文非空字符串，须属于该 type 的允许类别
- note: 字符串，可为空
- JSON 文件: `data/records.json`，内容为记录数组 `[{}, {}]`
- 数据层唯一读写入口：`core.storage.load_records()` 与 `save_records(records)`

## 收支类别

```json
{
  "income": ["工资", "奖学金", "兼职", "其他收入"],
  "expense": ["餐饮", "交通", "购物", "学习", "娱乐", "医疗", "其他支出"]
}
```

## Python 函数签名

| 文件 | 接口 | 输出/规则 |
| --- | --- | --- |
| core/storage.py | load_records() | list[dict]，文件首次不存在时 [] |
| core/storage.py | save_records(records) | None；完整覆盖保存 |
| core/validators.py | validate_record(data) | 合法时 None；非法时 ValueError |
| core/categories.py | get_categories() | income/expense 两组列表 |
| services/record_add.py | add_record(data) | 返回新增、带唯一 id 的字典 |
| services/record_edit.py | update_record(record_id, updates) | 更新后的字典；找不到 None |
| services/record_edit.py | delete_record(record_id) | 成功 True；不存在 False |
| services/record_list.py | get_recent_records(limit=5) | 按日期倒序，最多 limit 条 |
| services/filters.py | filter_records(records, start_date=None, end_date=None, record_type=None, category=None, min_amount=None, max_amount=None) | 满足全部条件的新列表 |
| services/statistics.py | calculate_summary(records) | income/expense/balance/count |
| services/charts.py | category_statistics(records) | 只按 expense 类别汇总列表 |

边界规则：日期范围和金额范围均包含起止值，筛选和统计函数不得修改原始列表。
同日的排序约定为“新添加的记录优先”（如依赖保存顺序，B1/B3/A1 必须保持一致）。
`update_record` 应在合并旧数据与 updates 后做完整校验，不允许改变 id。

## HTTP API（D1、D3 对照联调）

| 方法 | 路径 | 功能 |
| --- | --- | --- |
| GET | / | 页面 |
| GET | /api/health | 仅测试服务器存活 |
| GET | /api/records | 默认最近 5 笔；可带查询参数 |
| POST | /api/records | 新增记录，body 不带 id |
| PUT | /api/records/<id> | 修改记录，body 为待修改字段 |
| DELETE | /api/records/<id> | 删除记录 |
| GET | /api/statistics | 汇总统计，允许相同筛选参数 |
| GET | /api/charts | 类别统计图表数据 |
| GET | /api/categories | 收支类别 |

GET /api/records 与 /api/statistics 支持：`start_date`、`end_date`、
`record_type`、`category`、`min_amount`、`max_amount`；
GET /api/records 另支持正整数 `limit`，默认 5。
GET /api/charts 可选择使用同一套筛选条件，具体由 D1/C3 协调，但不得擅自改动已有字段名。

所有接口统一 JSON：
成功 `{"success": true, "data": ...}`；
失败 `{"success": false, "error": "中文错误信息"}`。

建议使用 HTTP 200/201（成功读取/创建）、400（无效参数）、404（ID 不存在）、500（异常）。
**501 表示业务 API 未实现，不是正常返回。**
空数据的统计结果为 `{"income":0.0,"expense":0.0,"balance":0.0,"count":0}`。
