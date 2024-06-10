def test_register_user(client):
    response = client.post("/users/register", json={"email": "test@example.com", "password": "password123"})
    assert response.status_code == 201
    assert response.json()["message"] == "User registered successfully"
