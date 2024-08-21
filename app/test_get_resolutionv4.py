from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual module name

client = TestClient(app)

def test_get_h3_resolution_valid_cell():
    response = client.get("/v4/get_resolution/?h=81603ffffffffff")
    assert response.status_code == 200
    assert response.json()["resolution"] == 1

def test_get_h3_resolution_invalid_cell():
    response = client.get("/v4/get_resolution/?h=invalid_cell_id")
    assert response.status_code == 400
    assert "invalid literal for int() with base 16: 'invalid_cell_id'" in response.json()["detail"]

def test_get_h3_resolution_empty_cell():
    response = client.get("/v4/get_resolution/?h=")
    assert response.status_code == 400
    assert "invalid literal for int() with base 16: ''" in response.json()["detail"]

def test_get_h3_resolution_missing_cell():
    response = client.get("/v4/get_resolution/")
    assert response.status_code == 422
    assert "Field required" in response.json()["detail"][0]["msg"]
