from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual module name

client = TestClient(app)

def test_get_is_pentagon_valid_pentagon_cell():
    response = client.get("/v4/is_pentagon/?h=8029fffffffffff")  # A known pentagon cell
    assert response.status_code == 200
    assert response.json()["is_pentagon"] == False

def test_get_is_pentagon_valid_non_pentagon_cell():
    response = client.get("/v4/is_pentagon/?h=8928308280fffff")  # A known non-pentagon cell
    assert response.status_code == 200
    assert response.json()["is_pentagon"] == False

def test_get_is_pentagon_invalid_cell():
    response = client.get("/v4/is_pentagon/?h=invalid_cell_id")
    assert response.status_code == 400
    assert "invalid literal for int() with base 16: 'invalid_cell_id'" in response.json()["detail"]

def test_get_is_pentagon_empty_cell():
    response = client.get("/v4/is_pentagon/?h=")
    assert response.status_code == 400
    assert "invalid literal for int() with base 16: ''" in response.json()["detail"]

def test_get_is_pentagon_missing_cell():
    response = client.get("/v4/is_pentagon/")
    assert response.status_code == 422
    assert "Field required" in response.json()["detail"][0]["msg"]
