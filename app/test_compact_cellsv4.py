from fastapi.testclient import TestClient
from main import app  # Replace your_app with the actual name of your app file

client = TestClient(app)


def test_compact_cells_valid_input():
    """Tests the /v4/compact_cells/ endpoint with valid input."""
    input_data = [
        '8928308280fffff', '8928308280bffff', '89283082873ffff', '89283082877ffff',
        '8928308283bffff', '89283082807ffff', '89283082803ffff', '8928308281bffff',
        '89283082857ffff', '89283082847ffff', '8928308287bffff', '89283082863ffff',
        '89283082867ffff', '8928308282bffff', '89283082823ffff', '89283082833ffff',
        '892830828abffff', '89283082817ffff', '89283082813ffff', '892830828c7ffff',
        '892830828cfffff', '89283082853ffff', '89283082843ffff', '8928308284fffff',
        '89283082ab7ffff', '8928308286bffff', '8928308286fffff', '89283082b9bffff',
        '89283082b93ffff', '8928308282fffff', '89283082827ffff', '89283082837ffff',
        '892830828afffff', '892830828a3ffff', '892830828bbffff', '8928308288fffff',
        '8928308288bffff', '892830828d7ffff', '892830828c3ffff', '892830828cbffff',
        '89283082e27ffff', '8928308285bffff', '8928308284bffff', '89283082ab3ffff',
        '89283082aa3ffff', '89283082aa7ffff', '89283082bd3ffff', '89283082bd7ffff',
        '89283082b8bffff', '89283082b83ffff', '89283082b97ffff', '8928308295bffff',
        '89283082953ffff', '892830829cbffff', '892830829dbffff', '892830828a7ffff',
        '892830828b7ffff', '892830828b3ffff', '89283082887ffff', '89283082883ffff',
        '8928308289bffff'
    ]
    output_data = [
        '892830828c7ffff', '892830828cfffff', '89283082ab7ffff', '89283082b9bffff',
        '89283082b93ffff', '8928308288fffff', '8928308288bffff', '892830828d7ffff',
        '892830828c3ffff', '892830828cbffff', '89283082e27ffff', '89283082ab3ffff',
        '89283082aa3ffff', '89283082aa7ffff', '89283082bd3ffff', '89283082bd7ffff',
        '89283082b8bffff', '89283082b83ffff', '89283082b97ffff', '8928308295bffff',
        '89283082953ffff', '892830829cbffff', '892830829dbffff', '89283082887ffff',
        '89283082883ffff', '8928308289bffff', '8828308281fffff', '8828308285fffff',
        '8828308283fffff', '8828308287fffff', '882830828bfffff'] 
    
    response = client.post("/v4/compact_cells/", json=input_data)
    assert response.status_code == 200
    assert "compacted_cells" in response.json()
    print(response.json()["compacted_cells"])
    assert response.json()["compacted_cells"] == output_data


def test_compact_cells_invalid_input():
    """Tests the /v4/compact_cells/ endpoint with invalid input."""
    response = client.post("/v4/compact_cells/", json=["8928308280fffff", "invalid_h3_index", "89283082803ffff"])
    assert response.status_code == 400
    assert "detail" in response.json()


def test_compact_cells_empty_input():
    """Tests the /v4/compact_cells/ endpoint with empty input."""
    response = client.post("/v4/compact_cells/", json=[])
    assert response.status_code == 200  # Should handle empty input gracefully
    assert "compacted_cells" in response.json()
    assert response.json()["compacted_cells"] == []  # Expected output for empty input


def test_compact_cells_non_list_input():
    """Tests the /v4/compact_cells/ endpoint with non-list input."""
    response = client.post("/v4/compact_cells/", json="not_a_list")
    assert response.status_code == 422  # Or another appropriate error code for invalid request body
