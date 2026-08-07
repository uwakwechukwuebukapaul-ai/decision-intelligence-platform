"""
Investigation Orchestrator Tests
"""


from app.intelligence.orchestration import (
    InvestigationOrchestrator,
)


class FakeCoordinator:


    def execute(
        self,
        plan,
    ):

        return {

            "results": [

                {

                    "capability":
                        "risk_scoring",

                    "result":
                        {
                            "risk_score": 90
                        },

                },

                {

                    "capability":
                        "threat_classification",

                    "result":
                        {
                            "classification":
                            "malicious"
                        },

                },

            ]

        }



class FakeReasoningEngine:


    def analyze(
        self,
        results,
    ):

        return {

            "verdict":
                "malicious",

            "confidence":
                0.95,

            "reasoning":
                [
                    "Threat detected"
                ],

        }



class FakeReportGenerator:


    def generate(
        self,
        case_id,
        assessment,
        results,
    ):

        return {

            "case_id":
                case_id,

            "verdict":
                assessment["verdict"],

        }



def test_complete_investigation_flow():


    orchestrator = InvestigationOrchestrator(

        FakeCoordinator(),

        FakeReasoningEngine(),

        FakeReportGenerator(),

    )


    report = orchestrator.investigate(

        "INC-100",

        {},

    )


    assert (
        report["case_id"]
        == "INC-100"
    )


    assert (
        report["verdict"]
        == "malicious"
    )