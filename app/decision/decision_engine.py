"""
Sentinel DNA Decision Engine

Transforms intelligence fusion into SOC decisions.
"""


from .decision_schema import DecisionSchema
from .recommendation_engine import RecommendationEngine
from .decision_repository import DecisionRepository




class DecisionEngine:



    def __init__(self):

        self.recommendations = (
            RecommendationEngine()
        )

        self.repository = (
            DecisionRepository()
        )



    def decide(
        self,
        investigation: dict
    ):


        incident = investigation.get(
            "incident",
            {}
        )


        severity = incident.get(
            "severity",
            "medium"
        )


        threat = investigation.get(
            "threat_intelligence",
            {}
        )


        threat_level = threat.get(
            "threat_level",
            "low"
        )



        reasoning = []



        confidence = 0.50



        if severity == "critical":

            confidence += 0.25

            reasoning.append(
                "Critical severity incident detected"
            )


        if threat_level == "high":

            confidence += 0.20

            reasoning.append(
                "High confidence threat intelligence available"
            )



        if threat.get(
            "ioc"
        ):

            reasoning.append(
                "IOC intelligence correlated"
            )



        if confidence >= 0.85:

            decision = "contain"

        elif confidence >= 0.65:

            decision = "investigate"

        else:

            decision = "monitor"



        actions = (
            self.recommendations
            .recommend(
                investigation
            )
        )



        result = DecisionSchema(

            incident_id=
                incident.get(
                    "incident_id"
                ),

            decision=
                decision,

            priority=
                severity,

            confidence=
                round(
                    confidence,
                    2
                ),

            actions=
                actions,

            reasoning=
                reasoning

        ).to_dict()



        return self.repository.save(
            result
        )