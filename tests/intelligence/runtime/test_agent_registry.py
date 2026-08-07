"""
Agent Registry Tests
"""


from app.intelligence.runtime.bootstrap import (
    create_intelligence_runtime,
)



class FakeRiskEngine:

    def execute(self, payload):

        return {
            "risk": "high"
        }



def test_runtime_bootstrap():

    executor = create_intelligence_runtime(
        {
            "risk_scoring": FakeRiskEngine()
        }
    )


    assert executor is not None



def test_registered_engine_execution():

    executor = create_intelligence_runtime(
        {
            "risk_scoring": FakeRiskEngine()
        }
    )


    from app.intelligence.runtime.job import (
        IntelligenceJob,
    )


    result = executor.execute(
        IntelligenceJob(
            capability="risk_scoring",
            payload={}
        )
    )


    assert result["status"] == "completed"

    assert (
        result["capability"]
        == "risk_scoring"
    )