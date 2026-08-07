"""
Investigation API Tests
"""


from app.intelligence.api import (
    InvestigationAPI,
)



class FakeOrchestrator:


    def investigate(
        self,
        case_id,
        plan,
    ):

        return {

            "case_id":
                case_id,

            "verdict":
                "malicious",

        }



def test_create_investigation():


    api = InvestigationAPI(

        FakeOrchestrator()

    )


    response = api.create_investigation(

        "INC-500",

        {},

    )


    assert (
        response["status"]
        == "completed"
    )


    assert (

        response["investigation"]["case_id"]

        == "INC-500"

    )