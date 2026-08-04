from services.investigation_runtime.runtime_engine import (
    InvestigationRuntimeEngine
)


def test_investigation_runtime():

    event = (
        "Ransomware actor using PowerShell "
        "attacked finance database servers"
    )

    engine = InvestigationRuntimeEngine()

    result = engine.investigate(
        event
    )

    assert result["status"] == "completed"

    assert (
        result["context"]["event"]
        ==
        event
    )

    assert (
        result["engines"]["status"]
        ==
        "completed"
    )