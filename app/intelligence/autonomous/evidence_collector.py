"""
Sentinel DNA - Autonomous Evidence Collector
"""


from __future__ import annotations



class EvidenceCollector:


    def collect(
        self,
        intelligence: dict,
    ) -> dict:


        return {

            "indicator":
                intelligence.get(
                    "indicator"
                ),

            "risk":
                intelligence.get(
                    "risk"
                ),

            "campaign":
                intelligence.get(
                    "campaign"
                ),

            "threat_actor":
                intelligence.get(
                    "threat_actor"
                ),

            "graph":
                intelligence.get(
                    "graph"
                ),

        }