"""A1 负责：JSON 数据文件读写。

统一文件路径：data/records.json（运行时生成，不提交）。
与 B1/B2/B3 的接口已经约定，请勿擅自更名。
"""


def load_records():
    """读取所有记录，返回 list[dict]；首次不存在文件时返回空列表。

    TODO(A1): 独立实现读取、缺失文件处理、坏数据处理。
    """
    raise NotImplementedError("A1 尚未实现 load_records")


def save_records(records):
    """将完整记录列表写入 JSON 文件；成功时返回 None。

    TODO(A1): 独立实现文件创建、UTF-8 中文写入等。
    """
    raise NotImplementedError("A1 尚未实现 save_records")
