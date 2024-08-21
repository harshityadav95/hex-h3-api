from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual module name

client = TestClient(app)

def test_get_h3_base_cell_number_valid_cell():
    response = client.get("/v4/get_base_cell_number/?h=85283473fffffff")
    assert response.status_code == 200
    assert response.json()["base_cell_number"] == 20

def test_get_h3_base_cell_number_invalid_cell():
    response = client.get("/v4/get_base_cell_number/?h=invalid_cell_id")
    assert response.status_code == 400
    assert "invalid literal for int() with base 16: 'invalid_cell_id'" in response.json()["detail"]

def test_get_h3_base_cell_number_empty_cell():
    response = client.get("/v4/get_base_cell_number/?h=")
    assert response.status_code == 400
    assert "invalid literal for int() with base 16: ''" in response.json()["detail"]

def test_get_h3_base_cell_number_missing_cell():
    response = client.get("/v4/get_base_cell_number/")
    assert response.status_code == 422
    assert "Field required" in response.json()["detail"][0]["msg"]
