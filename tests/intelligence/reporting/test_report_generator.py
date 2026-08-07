"""
Report Generator Tests
"""


from app.intelligence.reporting import (
    ReportGenerator,
)



def test_generate_security_report():


    generator = ReportGenerator()


    assessment = {

        "verdict":
            "malicious",

        "confidence":
            0.95,

        "reasoning":
            [
                "High risk"
            ],

    }


    intelligence = [

        {

            "capability":
                "risk_scoring",

            "result":
                {
                    "risk_score": 90
                },

        }

    ]


    report = generator.generate(

        "INC-001",

        assessment,

        intelligence,

    )


    assert (
        report["case_id"]
        == "INC-001"
    )


    assert (
        report["verdict"]
        == "malicious"
    )


    assert len(
        report["recommendations"]
    ) > 0



def test_benign_report():


    generator = ReportGenerator()


    report = generator.generate(

        "INC-002",

        {

            "verdict":
                "benign",

            "confidence":
                0.5,

        },

        [],

    )


    assert (
        report["verdict"]
        == "benign"
    )