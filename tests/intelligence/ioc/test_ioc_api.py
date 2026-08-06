from app.app import app


def test_ioc_api_ip():

    client = app.test_client()

    response = client.get(
        "/api/v1/intelligence/ioc/8.8.8.8"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["indicator"] == "8.8.8.8"

    assert data["result"]["type"] == "ip"



def test_ioc_api_domain():

    client = app.test_client()

    response = client.get(
        "/api/v1/intelligence/ioc/example.xyz"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["result"]["type"] == "domain"