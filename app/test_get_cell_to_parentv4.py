from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual name of your app file

client = TestClient(app)

def test_get_cell_to_parent_valid_input():
    response = client.get("/v4/get_cell_to_parent/?cell=8928308280fffff&parent_res=5")
    assert response.status_code == 200
    assert "parent_cell" in response.json()
    assert isinstance(response.json()["parent_cell"], str)

def test_get_cell_to_parent_invalid_cell():
    response = client.get("/v4/get_cell_to_parent/?cell=invalid_h3_index&parent_res=5")
    assert response.status_code == 400
    assert "detail" in response.json()

def test_get_cell_to_parent_invalid_parent_res():
    response = client.get("/v4/get_cell_to_parent/?cell=8928308280fffff&parent_res=invalid_resolution")
    assert response.status_code == 422
    assert "detail" in response.json()

def test_get_cell_to_parent_parent_res_too_high():
    response = client.get("/v4/get_cell_to_parent/?cell=8928308280fffff&parent_res=16")  # Assuming max resolution is 15
    assert response.status_code == 400
    assert "detail" in response.json()
