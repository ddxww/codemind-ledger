"""只测试骨架基础设施；各成员必须自行补充业务测试。

注意：这里不应固定断言 /api/records 返回 501，
因为 D1 实现该接口后必须允许测试继续通过。
"""
from app import app


def test_index_exists():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert "个人记账本" in response.get_data(as_text=True)


def test_health_endpoint():
    response = app.test_client().get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["success"] is True
