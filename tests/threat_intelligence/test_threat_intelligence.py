from services.threat_intelligence import ThreatIntelligenceEngine


def test_threat_intelligence_engine():

    engine = ThreatIntelligenceEngine()

    result = engine.analyze(
        "Ransomware actor using PowerShell attacked finance database servers"
    )

    assert result["status"] == "threat_intelligence_processed"

    assert "ransomware" in result["indicators"]

    assert result["reputation"]["risk_level"] == "HIGH"