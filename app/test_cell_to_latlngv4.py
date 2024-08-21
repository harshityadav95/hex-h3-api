from fastapi.testclient import TestClient
from main import app  # Assuming your code is in main.py

client = TestClient(app)

def test_valid_cell_id():
    response = client.get("/v4/cell_to_latlng/?cell=8928308280fffff")
    assert response.status_code == 200
    assert "latitude" in response.json()
    assert "longitude" in response.json()

def test_invalid_cell_id():
    response = client.get("/v4/cell_to_latlng/?cell=invalid_cell_id")
    assert response.status_code == 400
    assert "detail" in response.json()

def test_specific_cell_id():
    response = client.get("/v4/cell_to_latlng/?cell=81603ffffffffff")
    assert response.status_code == 200
    data = response.json()
    # Adjust the tolerance as needed based on the expected precision
    assert abs(data["latitude"] - 10.770202546102785) < 1e-6
    assert abs(data["longitude"] - 74.91521589588359) < 1e-6
