from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual module name

client = TestClient(app)

def test_get_string_to_h3_valid_index():
    response = client.get("/v4/str_to_int/?h=8928308280fffff")
    assert response.status_code == 200
    assert response.json()["h3_integer"] == 617700169958293503

def test_get_string_to_h3_invalid_index():
    response = client.get("/v4/str_to_int/?h=invalid_h3_index")
    assert response.status_code == 400
    assert "invalid literal for int() with base 16: 'invalid_h3_index'" in response.json()["detail"]

def test_get_string_to_h3_empty_index():
    response = client.get("/v4/str_to_int/?h=")
    assert response.status_code == 400
    assert "invalid literal for int() with base 16: ''" in response.json()["detail"]

def test_get_string_to_h3_missing_index():
    response = client.get("/v4/str_to_int/")
    assert response.status_code == 422
    assert "Field required" in response.json()["detail"][0]["msg"]
