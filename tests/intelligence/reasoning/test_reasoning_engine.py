"""
Reasoning Engine Tests
"""


from app.intelligence.reasoning import (
    ReasoningEngine,
)



def test_reasoning_detects_malicious_activity():


    engine = ReasoningEngine()


    results = [

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


    assessment = engine.analyze(
        results
    )


    assert (
        assessment["verdict"]
        == "malicious"
    )


    assert (
        assessment["confidence"]
        > 0
    )


def test_reasoning_benign_case():


    engine = ReasoningEngine()


    assessment = engine.analyze(
        []
    )


    assert (
        assessment["verdict"]
        == "benign"
    )