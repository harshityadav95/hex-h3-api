from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual name of your app file

client = TestClient(app)

def test_get_local_ij_to_cell_valid_input():
    response = client.get("/v4/get_local_ij_to_cell/?origin=8928308280fffff&i=0&j=1")
    assert response.status_code == 200
    assert "h3_index" in response.json()
    assert isinstance(response.json()["h3_index"], str)

def test_get_local_ij_to_cell_invalid_origin():
    response = client.get("/v4/get_local_ij_to_cell/?origin=invalid_h3_index&i=0&j=1")
    assert response.status_code == 400
    assert "detail" in response.json()

def test_get_local_ij_to_cell_invalid_i():
    response = client.get("/v4/get_local_ij_to_cell/?origin=8928308280fffff&i=invalid_i_value&j=1")
    assert response.status_code == 422
    assert "detail" in response.json()

def test_get_local_ij_to_cell_invalid_j():
    response = client.get("/v4/get_local_ij_to_cell/?origin=8928308280fffff&i=0&j=invalid_j_value")
    assert response.status_code == 400
    assert "detail" in response.json()
