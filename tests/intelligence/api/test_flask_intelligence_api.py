"""
Flask Intelligence API Tests
"""


from flask import Flask

from app.api.intelligence_routes import (
    intelligence_bp,
)



def test_investigation_endpoint():


    app = Flask(__name__)


    app.register_blueprint(
        intelligence_bp
    )


    client = app.test_client()



    response = client.post(

        "/api/investigate",

        json={
            "case_id":
                "INC-900"
        },

    )


    assert response.status_code == 200


    data = response.get_json()


    assert (
        data["status"]
        == "completed"
    )