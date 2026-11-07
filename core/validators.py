"""A2 负责：验证收支数据（见 docs/CONTRACT.md）。"""


def validate_record(data):
    """合法时返回 None；不合法时抛出 ValueError(中文错误信息)。

    至少检查：type、date、amount、category；note 可为空。
    TODO(A2): 独立实现验证规则、编辑时的部分字段验证方案。
    """
    raise NotImplementedError("A2 尚未实现 validate_record")
