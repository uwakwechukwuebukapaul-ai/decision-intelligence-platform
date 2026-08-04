from services.mitre_engine import MitreEngine



def test_mitre_engine():


    engine = MitreEngine()



    result = engine.analyze(

        "Ransomware actor using PowerShell attacked finance database servers"

    )


    assert result["status"] == "mitre_mapped"


    assert len(
        result["techniques"]
    ) >= 2


    assert "Execution" in result["tactics"]


    assert "Impact" in result["tactics"]