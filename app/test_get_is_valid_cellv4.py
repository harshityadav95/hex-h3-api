from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual module name

client = TestClient(app)

def test_get_is_valid_cell_valid_cell():
    response = client.get("/v4/is_valid_cell/?cell=8928308280fffff")
    assert response.status_code == 200
    assert response.json()["is_valid"] == True

def test_get_is_valid_cell_invalid_cell():
    response = client.get("/v4/is_valid_cell/?cell=invalid_cell_id")
    assert response.status_code == 200  # Note: This should return 200 with is_valid=False
    assert response.json()["is_valid"] == False

def test_get_is_valid_cell_empty_cell():
    response = client.get("/v4/is_valid_cell/?cell=")
    assert response.status_code == 200  # Note: This should return 200 with is_valid=False
    assert response.json()["is_valid"] == False

def test_get_is_valid_cell_missing_cell():
    response = client.get("/v4/is_valid_cell/")
    assert response.status_code == 422
    assert "Field required" in response.json()["detail"][0]["msg"]
