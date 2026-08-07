"""
End-to-End Intelligence Investigation Tests

Validates complete Sentinel DNA
investigation execution flow.
"""


from app.intelligence.coordination.coordinator import (
    Coordinator,
)

from app.intelligence.runtime.bootstrap import (
    create_intelligence_runtime,
)



class InvestigationStep:
    """
    Workflow execution step
    """

    def __init__(
        self,
        name,
        capability,
        payload,
    ):
        self.name = name
        self.capability = capability
        self.payload = payload



class InvestigationPlan:
    """
    Fake execution plan
    """

    def __init__(self):

        self.steps = [

            InvestigationStep(
                "classify threat",
                "threat_classification",
                {
                    "email": "phishing attempt"
                },
            ),


            InvestigationStep(
                "calculate risk",
                "risk_scoring",
                {
                    "severity": "high"
                },
            ),


            InvestigationStep(
                "map attack",
                "mitre_mapping",
                {},
            ),

        ]


    def validate(self):
        return True


    def ordered_steps(self):

        return self.steps



def test_complete_investigation_pipeline():

    executor = create_intelligence_runtime()


    coordinator = Coordinator(
        executor=executor
    )


    plan = InvestigationPlan()


    result = coordinator.execute(
        plan
    )


    assert result is not None


    assert (
        "results"
        in result
    )


def test_all_intelligence_steps_execute():

    executor = create_intelligence_runtime()


    coordinator = Coordinator(
        executor=executor
    )


    result = coordinator.execute(
        InvestigationPlan()
    )


    results = result["results"]


    capabilities = [

        item["capability"]

        for item in results

    ]


    assert (
        "threat_classification"
        in capabilities
    )


    assert (
        "risk_scoring"
        in capabilities
    )


    assert (
        "mitre_mapping"
        in capabilities
    )