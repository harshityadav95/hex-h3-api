from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual module name

client = TestClient(app)

def test_get_int_to_str_valid_integer():
    response = client.get("/v4/int_to_str/?x=612677851780714495")
    assert response.status_code == 200
    assert response.json()["h3_string"] == "880ab4295238fff"

def test_get_int_to_str_invalid_integer():
    response = client.get("/v4/int_to_str/?x=-1")  # Invalid H3 integer
    assert response.status_code == 500
    assert "Internal server error" in response.json()["detail"]

def test_get_int_to_str_missing_integer():
    response = client.get("/v4/int_to_str/")
    assert response.status_code == 422
    assert "Field required" in response.json()["detail"][0]["msg"]
