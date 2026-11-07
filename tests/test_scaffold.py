"""只测试骨架能启动；各成员需自行补充真实业务测试。"""
from app import app


def test_index_exists():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert "个人记账本" in response.get_data(as_text=True)


def test_health_endpoint():
    response = app.test_client().get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["success"] is True


def test_business_api_is_explicitly_unimplemented():
    response = app.test_client().get("/api/records")
    assert response.status_code == 501
    assert response.get_json()["success"] is False
