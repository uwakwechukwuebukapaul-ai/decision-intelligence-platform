from services.intelligence_fusion.fusion_engine import (
    IntelligenceFusionEngine
)



def test_intelligence_fusion():


    engine = IntelligenceFusionEngine()


    result = engine.fuse(

        "Ransomware actor using PowerShell attacked finance database servers",

        evidence={
            "risk_score":100
        },

        detection={
            "rules":[
                "PowerShell Detection"
            ]
        },

        threat={
            "malware":"Ransomware"
        },

        cognitive={
            "risk_level":"critical"
        }

    )


    assert result["status"] == "completed"

    assert result["risk"]["risk_level"] == "critical"