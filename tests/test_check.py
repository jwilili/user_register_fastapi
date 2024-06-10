def test_send_verification_code(client):
    client.post("/users/register", json={"email": "test@example.com", "password": "password123"})
    response = client.post("/verification/send-code", json={"email": "test@example.com"})
    assert response.status_code == 200
    assert response.json()["message"] == "Verification code sent"

def test_activate_user(client):
    client.post("/users/register", json={"email": "test@example.com", "password": "password123"})
    client.post("/verification/send-code", json={"email": "test@example.com"})
    # Mock the activation within the allowed time
    response = client.post("/verification/activate", json={"email": "test@example.com", "code": "1234"})
    assert response.status_code == 200
    assert response.json()["message"] == "User activated successfully"
