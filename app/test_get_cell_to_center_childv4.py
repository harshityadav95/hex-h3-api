from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual name of your app file

client = TestClient(app)

def test_get_cell_to_center_child_valid_input():
    response = client.get("/v4/get_cell_to_center_child/?cell=85283473fffffff&child_res=7")
    assert response.status_code == 200
    assert "center_child" in response.json()
    assert response.json()["center_child"] == "872834700ffffff"

def test_get_cell_to_center_child_invalid_cell():
    response = client.get("/v4/get_cell_to_center_child/?cell=invalid_h3_index&child_res=7")
    assert response.status_code == 400
    assert "detail" in response.json()

def test_get_cell_to_center_child_invalid_child_res():
    response = client.get("/v4/get_cell_to_center_child/?cell=85283473fffffff&child_res=invalid_resolution")
    assert response.status_code == 422
    assert "detail" in response.json()

def test_get_cell_to_center_child_child_res_too_low():
    response = client.get("/v4/get_cell_to_center_child/?cell=85283473fffffff&child_res=4")  # Assuming cell resolution is 6
    assert response.status_code == 400
    assert "detail" in response.json()
