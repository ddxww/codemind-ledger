"""C1 负责：组合筛选；纯函数，不直接读写 JSON 文件。"""


def filter_records(
    records,
    start_date=None,
    end_date=None,
    record_type=None,
    category=None,
    min_amount=None,
    max_amount=None,
):
    """传入记录列表和可选筛选项，返回符合全部条件的新列表。

    日期和金额上下限均为包含边界；不修改原 records。
    TODO(C1): 独立实现并测试日期、类型、类别和金额条件。
    """
    raise NotImplementedError("C1 尚未实现 filter_records")
