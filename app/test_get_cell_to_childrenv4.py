from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual name of your app file

client = TestClient(app)

def test_get_cell_to_children_valid_input():
    response = client.get("/v4/get_cell_to_children/?cell=8928308280fffff&child_res=9")
    assert response.status_code == 200
    assert "children" in response.json()
    assert isinstance(response.json()["children"], list)
    # Check if each element in the list is a string (H3 index)
    for child in response.json()["children"]:
        assert isinstance(child, str)

def test_get_cell_to_children_invalid_cell():
    response = client.get("/v4/get_cell_to_children/?cell=invalid_h3_index&child_res=9")
    assert response.status_code == 400
    assert "detail" in response.json()

def test_get_cell_to_children_invalid_child_res():
    response = client.get("/v4/get_cell_to_children/?cell=8928308280fffff&child_res=invalid_resolution")
    assert response.status_code == 422
    assert "detail" in response.json()

def test_get_cell_to_children_child_res_too_low():
    response = client.get("/v4/get_cell_to_children/?cell=8928308280fffff&child_res=4")  # Assuming cell resolution is 8
    assert response.status_code == 400
    assert "detail" in response.json()
