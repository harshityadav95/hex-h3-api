from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual module name

client = TestClient(app)

def test_get_is_res_class_iii_valid_class_iii_cell():
    response = client.get("/v4/is_res_class_iii/?h=85283473fffffff")  # Resolution 5
    assert response.status_code == 200
    assert response.json()["is_class_iii"] == True

def test_get_is_res_class_iii_valid_non_class_iii_cell():
    response = client.get("/v4/is_res_class_iii/?h=8228347ffffffff")  # Resolution 2
    assert response.status_code == 200
    assert response.json()["is_class_iii"] == False

def test_get_is_res_class_iii_invalid_cell():
    response = client.get("/v4/is_res_class_iii/?h=invalid_cell_id")
    assert response.status_code == 400
    assert "invalid literal for int() with base 16: 'invalid_cell_id'" in response.json()["detail"]

def test_get_is_res_class_iii_empty_cell():
    response = client.get("/v4/is_res_class_iii/?h=")
    assert response.status_code == 400
    assert "invalid literal for int() with base 16: ''" in response.json()["detail"]

def test_get_is_res_class_iii_missing_cell():
    response = client.get("/v4/is_res_class_iii/")
    assert response.status_code == 422
    assert "Field required" in response.json()["detail"][0]["msg"]
