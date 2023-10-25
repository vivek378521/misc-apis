from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Test the /convert_ip_to_number/ endpoint
def test_convert_ip_to_number():
    response = client.get("/convert_ip_to_number/")
    assert response.status_code == 200


# Test the /convert_number_to_ip/ endpoint
def test_convert_number_to_ip():
    request_data = {
        "ip_as_number": 3232235777
    }  # Corresponds to IP address "192.168.1.1"
    response = client.post("/convert_number_to_ip/", json=request_data)
    data = response.json()
    assert response.status_code == 200
    assert "ip_address" in data
    assert "ip_as_number" in data
    assert data["ip_address"] == "192.168.1.1"
    assert data["ip_as_number"] == 3232235777


# Test the /convert_number_to_ip/ endpoint with an invalid number
def test_convert_number_to_ip_invalid():
    request_data = {
        "ip_as_number": 50000000000000000000000000000
    }  # Invalid number, outside the range
    response = client.post("/convert_number_to_ip/", json=request_data)
    assert response.status_code == 400


# Test the /convert_number_to_ip/ endpoint with missing data
def test_convert_number_to_ip_missing_data():
    response = client.post("/convert_number_to_ip/")
    assert response.status_code == 422  # Should return a validation error
