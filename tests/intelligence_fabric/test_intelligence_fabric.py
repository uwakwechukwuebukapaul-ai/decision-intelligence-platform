from services.intelligence_fabric import IntelligenceFabricEngine


def test_intelligence_fabric():

    engine = IntelligenceFabricEngine()


    result = engine.analyze(

        "Ransomware attack detected"

    )


    assert result["status"] == "fabric_processed"

    assert len(result["route"]) == 4