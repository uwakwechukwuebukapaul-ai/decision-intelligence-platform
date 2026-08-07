"""
Investigation Context Tests
"""


from app.intelligence.context import (
    InvestigationContext,
    load_investigation_context,
)



def test_context_creation():

    context = InvestigationContext(
        case_id="INC-001"
    )


    assert (
        context.case_id
        == "INC-001"
    )



def test_context_summary():

    context = InvestigationContext(

        case_id="INC-002",

        evidence=[
            "email"
        ],

        iocs=[
            "evil.com"
        ],

        timeline=[
            "login"
        ],

    )


    summary = context.summary()


    assert (
        summary["evidence_count"]
        == 1
    )


    assert (
        summary["ioc_count"]
        == 1
    )



def test_context_loader():

    context = load_investigation_context(
        "INC-003"
    )


    assert (
        context.case_id
        == "INC-003"
    )


    assert len(
        context.iocs
    ) > 0