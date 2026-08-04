from services.autonomous_orchestrator.autonomous_orchestrator import (
    AutonomousOrchestrator
)


def test_autonomous_orchestration():

    event = (
        "Ransomware actor using PowerShell "
        "attacked finance database servers"
    )

    orchestrator = AutonomousOrchestrator()

    result = orchestrator.orchestrate(event)


    assert result["status"] == "completed"

    assert result["decision"]["risk_level"] == "critical"

    assert (
        "Contain affected assets"
        in result["response"]["actions"]
    )