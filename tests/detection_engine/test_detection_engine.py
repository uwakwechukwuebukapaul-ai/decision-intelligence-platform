from services.detection_engine import DetectionEngine


def test_detection_engine():

    engine = DetectionEngine()

    result = engine.analyze(
        "Ransomware actor using PowerShell attacked finance database servers"
    )

    assert result["status"] == "detection_processed"

    assert len(result["patterns"]) > 0

    assert "PowerShell execution" in result["patterns"]

    assert len(result["rules"]) > 0

    assert result["sigma"][0]["framework"] == "Sigma"