"""
Sentinel DNA - Case Intelligence Orchestrator

Combines all analyst decision engines
into a unified investigation intelligence object.
"""


from .priority_engine import (
    PriorityEngine,
)

from .decision_engine import (
    DecisionEngine,
)

from .analyst_recommendation import (
    AnalystRecommendationEngine,
)

from .escalation_engine import (
    EscalationEngine,
)

from .case_lifecycle import (
    CaseLifecycle,
)



class CaseIntelligenceOrchestrator:


    def __init__(self):

        self.priority_engine = PriorityEngine()

        self.decision_engine = DecisionEngine()

        self.recommendation_engine = (
            AnalystRecommendationEngine()
        )

        self.escalation_engine = EscalationEngine()

        self.lifecycle_engine = CaseLifecycle()



    def analyze(
        self,
        intelligence: dict,
    ):


        priority = (
            self.priority_engine.evaluate(
                intelligence
            )
        )


        decision = (
            self.decision_engine.analyze(
                intelligence
            )
        )


        recommendations = (
            self.recommendation_engine.generate(
                intelligence
            )
        )


        escalation = (
            self.escalation_engine.evaluate(
                intelligence
            )
        )


        lifecycle = (
            self.lifecycle_engine.transition(
                "OPEN",
                "TRIAGED",
            )
        )



        return {


            "case_intelligence": {


                "indicator":

                    intelligence.get(
                        "indicator",
                        "unknown",
                    ),


                "priority":

                    priority,


                "decision":

                    decision,


                "escalation":

                    escalation,


                "recommendations":

                    recommendations,


                "lifecycle":

                    lifecycle,

            }

        }