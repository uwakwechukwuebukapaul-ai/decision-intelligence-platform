"""
Sentinel DNA - IOC Service

Enterprise IOC intelligence service.

Responsibilities:
- Parse indicators
- Classify IOC type
- Perform risk analysis
- Perform reputation enrichment
- Provide backward-compatible lookup API
"""

from __future__ import annotations


from app.intelligence.ioc.indicator_parser import (
    IndicatorParser,
)


from app.intelligence.ioc.risk_analyzer import (
    RiskAnalyzer,
)


from app.intelligence.ioc.enrichment.reputation_engine import (
    ReputationEngine,
)



class IOCService:
    """
    IOC Intelligence Service.
    """


    def __init__(
        self,
    ):

        self.parser = IndicatorParser()

        self.risk_analyzer = RiskAnalyzer()

        self.reputation_engine = ReputationEngine()



    def analyze(
        self,
        indicator: str,
    ) -> dict:
        """
        Analyze an IOC indicator.

        Enterprise intelligence response.
        """


        parsed = self.parser.parse(
            indicator
        )


        # Risk analysis

        risk = self.risk_analyzer.analyze(
            {
                "type": parsed.get("type"),
                "value": parsed.get("indicator"),
            }
        )


        # Reputation enrichment

        reputation = self.reputation_engine.analyze(
            parsed
        )


        return {

            "indicator": indicator,

            "type": parsed.get(
                "type"
            ),

            "risk": risk,

            "reputation": reputation,

        }



    def lookup(
        self,
        indicator: str,
    ) -> dict:
        """
        Legacy compatible IOC lookup.

        Preserves previous scoring contract.
        """


        result = self.analyze(
            indicator
        )


        indicator_type = result.get(
            "type"
        )


        legacy_score_map = {

            "ip": 0,


            "domain": result.get(
                "risk",
                {}
            ).get(
                "score",
                0
            ),


            "unknown": 20,

        }


        result["risk_score"] = legacy_score_map.get(
            indicator_type,
            20,
        )


        return result