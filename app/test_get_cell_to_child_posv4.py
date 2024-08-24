from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual name of your app file

client = TestClient(app)

# def test_get_cell_to_child_pos_valid_input():
#     response = client.get("/v4/get_cell_to_child_pos/?child=85283473fffffff&parent_res=3")
#     assert response.status_code == 200
#     assert "child_position" in response.json()
#     assert response.json()["child_position"] == 25

# def test_get_cell_to_child_pos_invalid_child():
#     response = client.get("/v4/get_cell_to_child_pos/?child=invalid_h3_index&parent_res=3")
#     assert response.status_code == 400
#     assert "detail" in response.json()

# def test_get_cell_to_child_pos_invalid_parent_res():
#     response = client.get("/v4/get_cell_to_child_pos/?child=85283473fffffff&parent_res=invalid_resolution")
#     assert response.status_code == 400
#     assert "detail" in response.json()

# def test_get_cell_to_child_pos_parent_res_too_high():
#     response = client.get("/v4/get_cell_to_child_pos/?child=85283473fffffff&parent_res=7")  # Assuming child resolution is 6
#     assert response.status_code == 400
#     assert "detail" in response.json()
