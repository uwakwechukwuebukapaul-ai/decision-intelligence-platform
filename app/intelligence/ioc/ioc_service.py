"""
Sentinel DNA - IOC Service

Enterprise IOC intelligence service.

Responsibilities:
- Parse indicators
- Classify IOC type
- Perform risk analysis
- Provide backward-compatible lookup API
"""

from __future__ import annotations


from app.intelligence.ioc.indicator_parser import (
    IndicatorParser,
)


from app.intelligence.ioc.risk_analyzer import (
    RiskAnalyzer,
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



    def analyze(
        self,
        indicator: str,
    ) -> dict:
        """
        Analyze an IOC indicator.

        Enterprise response format.
        """


        parsed = self.parser.parse(
            indicator
        )


        risk = self.risk_analyzer.analyze(
            parsed
        )


        return {

            "indicator": indicator,

            "type": parsed.get(
                "type"
            ),

            "risk": risk,

        }



    def lookup(
        self,
        indicator: str,
    ) -> dict:
        """
        Legacy compatible IOC lookup.

        Preserves old IOC scoring contract
        while keeping the new intelligence model.
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