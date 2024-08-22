from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual name of your app file

client = TestClient(app)

# Test cases for /v4/get_grid_disk/
def test_get_grid_disk_valid_input():
    response = client.get("/v4/get_grid_disk/?origin=8928308280fffff&k=2")
    assert response.status_code == 200
    assert "grid_disk" in response.json()
    assert isinstance(response.json()["grid_disk"], list)

def test_get_grid_disk_invalid_origin():
    response = client.get("/v4/get_grid_disk/?origin=invalid_h3_index&k=2")
    assert response.status_code == 400
    assert "detail" in response.json()

def test_get_grid_disk_invalid_k():
    response = client.get("/v4/get_grid_disk/?origin=8928308280fffff&k=-1")
    assert response.status_code == 400
    assert "detail" in response.json()

# Test cases for /v4/get_icosahedron_faces/
def test_get_icosahedron_faces_valid_input():
    response = client.get("/v4/get_icosahedron_faces/?h=8928308280fffff")
    assert response.status_code == 200
    assert "faces" in response.json()
    assert isinstance(response.json()["faces"], list)

def test_get_icosahedron_faces_invalid_input():
    response = client.get("/v4/get_icosahedron_faces/?h=invalid_h3_index")
    assert response.status_code == 400
    assert "detail" in response.json()
