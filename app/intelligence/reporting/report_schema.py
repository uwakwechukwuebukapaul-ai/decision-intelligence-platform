"""
Investigation Report Schema
"""


def create_report(
    case_id,
    assessment,
    findings=None,
    recommendations=None,
):

    return {

        "case_id": case_id,

        "verdict":
            assessment.get(
                "verdict"
            ),

        "confidence":
            assessment.get(
                "confidence"
            ),

        "reasoning":
            assessment.get(
                "reasoning",
                [],
            ),

        "findings":
            findings or [],

        "recommendations":
            recommendations or [],

    }