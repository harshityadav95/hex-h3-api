from fastapi.testclient import TestClient
from main import app  # Assuming your code is in main.py

client = TestClient(app)

def test_valid_input():
    response = client.get("/v4/latlng_to_cell/?latitude=37.7749&longitude=-122.4194&resolution=8")
    assert response.status_code == 200
    assert isinstance(response.json(), str)  # Check if the result is a string (H3 cell ID)

def test_invalid_latitude():
    response = client.get("/v4/latlng_to_cell/?latitude=91&longitude=-122.4194&resolution=8")
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid latitude or longitude"

def test_invalid_longitude():
    response = client.get("/v4/latlng_to_cell/?latitude=37.7749&longitude=181&resolution=8")
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid latitude or longitude"

def test_invalid_resolution():
    response = client.get("/v4/latlng_to_cell/?latitude=37.7749&longitude=-122.4194&resolution=16")
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid resolution (must be between 0 and 15)"

def test_specific_coordinates():
    response = client.get("/v4/latlng_to_cell/?latitude=10.770202546102785&longitude=74.91521589588359&resolution=1")
    assert response.status_code == 200
    assert "81603ffffffffff" in response.text
