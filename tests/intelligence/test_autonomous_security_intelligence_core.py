from services.intelligence.autonomous_security_intelligence_core import (
    AutonomousSecurityIntelligenceCore
)



def test_autonomous_security_investigation():


    core = AutonomousSecurityIntelligenceCore()


    result = core.investigate(

        "Ransomware actor using PowerShell attacked finance database servers"

    )


    assert result["status"] == "completed"

    assert result["decision"]["risk_level"] == "critical"

    assert result["decision"]["confidence"] == "96%"