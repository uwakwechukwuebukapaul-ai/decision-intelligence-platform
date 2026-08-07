"""
Default Engine Tests
"""

from app.intelligence.runtime.bootstrap import (
    create_intelligence_runtime,
)

from app.intelligence.runtime.job import (
    IntelligenceJob,
)



def test_default_runtime_loads_engines():

    executor = create_intelligence_runtime()

    assert executor is not None



def test_risk_engine_execution():

    executor = create_intelligence_runtime()


    result = executor.execute(
        IntelligenceJob(
            capability="risk_scoring",
            payload={
                "severity": "high"
            },
        )
    )


    assert result["status"] == "completed"


    assert (
        result["capability"]
        == "risk_scoring"
    )



def test_mitre_engine_execution():

    executor = create_intelligence_runtime()


    result = executor.execute(
        IntelligenceJob(
            capability="mitre_mapping",
            payload={}
        )
    )


    assert result["status"] == "completed"