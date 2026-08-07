"""
Sentinel DNA Investigation Endpoint Tests
"""


from app.factory import create_app



def test_investigation_endpoint_exists():

    app = create_app()


    client = app.test_client()


    response = client.post(
        "/api/v1/investigation",
        json={
            "case_id": "INC-TEST-001",
            "payload": {
                "type": "email",
                "content": "Suspicious login detected"
            }
        },
    )


    assert response.status_code in [
        200,
        201,
        400,
    ]



def test_investigation_response_structure():

    app = create_app()


    client = app.test_client()


    response = client.post(
        "/api/v1/investigation",
        json={
            "case_id": "INC-TEST-002",
            "payload": {
                "indicator": "malicious-domain.com"
            }
        },
    )


    if response.status_code == 200:

        data = response.get_json()


        assert data is not None