from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual module name

client = TestClient(app)

expected_boundary = [
  [
    9.84467337590314,
    79.17056508080195
  ],
  [
    14.16248410542495,
    77.80091702536666
  ],
  [
    14.946524398275951,
    73.55297085152047
  ],
  [
    11.593032005402348,
    70.86172974036968
  ],
  [
    7.473863638092713,
    72.19363429195394
  ],
  [
    6.511600732441482,
    76.26408541439848
  ]
]

def test_get_cell_to_boundary_valid_cell():
    response = client.get("/v4/cell_to_boundary/?cell=81603ffffffffff")
    assert response.status_code == 200
    assert response.json() == expected_boundary

def test_get_cell_to_boundary_invalid_cell():
    response = client.get("/v4/cell_to_boundary/?cell=?")
    assert response.status_code == 400
    assert response.json()["detail"] == "invalid literal for int() with base 16: '?'"


