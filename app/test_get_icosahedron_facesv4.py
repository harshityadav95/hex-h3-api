from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_icosahedron_faces_valid_index():
    response = client.get("/v4/get_icosahedron_faces/?h=8928308280fffff")
    assert response.status_code == 200
    assert "faces" in response.json()
    assert isinstance(response.json()["faces"], list)


def test_get_icosahedron_faces_invalid_index():
    response = client.get("/v4/get_icosahedron_faces/?h=invalid_index")
    assert response.status_code == 400
    assert "detail" in response.json()


def test_get_icosahedron_faces_missing_index():
    response = client.get("/v4/get_icosahedron_faces/")
    assert response.status_code == 422
    assert "detail" in response.json()
