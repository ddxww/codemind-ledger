"""B2 负责：编辑与删除记录。"""


def update_record(record_id, updates):
    """根据 id 更新记录；成功返回更新后的 dict，不存在返回 None。

    应保留原 id，并验证合并后的完整记录。
    TODO(B2): 独立实现并测试。
    """
    raise NotImplementedError("B2 尚未实现 update_record")


def delete_record(record_id):
    """根据 id 删除记录；成功返回 True，不存在返回 False。

    TODO(B2): 独立实现并测试。
    """
    raise NotImplementedError("B2 尚未实现 delete_record")
