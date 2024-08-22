from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual name of your app file

client = TestClient(app)

def test_get_cell_to_local_ij_valid_input():
    response = client.get("/v4/get_cell_to_local_ij/?origin=8928308280fffff&h=8928308280bffff")
    assert response.status_code == 200
    assert "i" in response.json()
    assert "j" in response.json()
    assert isinstance(response.json()["i"], int)
    assert isinstance(response.json()["j"], int)

def test_get_cell_to_local_ij_invalid_origin():
    response = client.get("/v4/get_cell_to_local_ij/?origin=invalid_h3_index&h=8928308280bffff")
    assert response.status_code == 400
    assert "detail" in response.json()

def test_get_cell_to_local_ij_invalid_h():
    response = client.get("/v4/get_cell_to_local_ij/?origin=8928308280fffff&h=invalid_h3_index")
    assert response.status_code == 400
    assert "detail" in response.json()
