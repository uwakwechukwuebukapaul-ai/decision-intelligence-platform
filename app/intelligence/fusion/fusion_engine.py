"""
Sentinel DNA - Intelligence Fusion Engine

Combines all intelligence subsystems
into one analyst investigation view.
"""

from __future__ import annotations


from app.intelligence.ioc.fusion import IntelligenceFusion

from app.intelligence.correlation import (
    CorrelationEngine,
)

from app.intelligence.campaign import (
    CampaignEngine,
)

from app.intelligence.threat_actor import (
    ThreatActorEngine,
)

from app.intelligence.graph import (
    GraphEngine,
)

from app.intelligence.memory import (
    InvestigationMemory,
)


from .fusion_schema import FusionResult





class SentinelIntelligenceEngine:
    """
    Main intelligence fusion controller.
    """



    def __init__(self):

        self.ioc_engine = IntelligenceFusion()

        self.correlation_engine = (
            CorrelationEngine()
        )

        self.campaign_engine = (
            CampaignEngine()
        )

        self.actor_engine = (
            ThreatActorEngine()
        )

        self.graph_engine = (
            GraphEngine()
        )

        self.memory = (
            InvestigationMemory()
        )





    def investigate(
        self,
        indicator: str,
    ) -> dict:


        intelligence = (
            self.ioc_engine.analyze(
                indicator
            )
        )


        correlation = (
            self.correlation_engine.analyze(
                intelligence
            )
        )


        campaign = (
            self.campaign_engine.analyze(
                [
                    intelligence,
                    intelligence,
                ]
            )
        )


        threat_actor = (
            self.actor_engine.analyze(
                intelligence
            )
        )


        graph = (
            self.graph_engine.ingest_intelligence(
                intelligence
            )
        )


        memory = (
            self.memory.remember(
                intelligence,
                {
                    "decision":
                    "investigate",

                    "confidence":
                    intelligence.get(
                        "risk",
                        {}
                    ).get(
                        "score",
                        0
                    )
                }
            )
        )



        result = FusionResult(

            indicator=indicator,

            risk=intelligence.get(
                "risk",
                {}
            ),

            correlation=correlation,

            campaign=campaign,

            threat_actor=threat_actor,

            graph=graph,

            memory=[
                memory
            ],

            recommendation={

                "action":
                "continue investigation",

                "priority":
                intelligence.get(
                    "risk",
                    {}
                ).get(
                    "risk",
                    "unknown"
                )
            }

        )



        return result.to_dict()