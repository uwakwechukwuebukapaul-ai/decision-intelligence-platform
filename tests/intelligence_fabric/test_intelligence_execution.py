from app import app


def test_intelligence_execution_endpoint():


    client = app.test_client()


    response = client.post(

        "/intelligence/execute",

        json={

            "user_id":
                "test-user",

            "capability":
                "reasoning",

            "objective":
                "test intelligence"

        }

    )


    assert response.status_code == 200


    data = response.get_json()


    assert data["status"] == "success"


    assert (
        data["capability"]
        ==
        "reasoning"
    )



def test_invalid_capability():


    client = app.test_client()


    response = client.post(

        "/intelligence/execute",

        json={

            "user_id":
                "test-user",

            "capability":
                "unknown_engine"

        }

    )


    assert response.status_code == 404