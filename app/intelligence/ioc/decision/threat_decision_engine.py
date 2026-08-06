"""
Sentinel DNA

IOC Threat Decision Engine

Responsible for converting IOC intelligence
into security decisions.
"""

from __future__ import annotations



class ThreatDecisionEngine:
    """
    Determines whether IOC intelligence
    requires investigation action.
    """



    def decide(
        self,
        intelligence: dict,
    ) -> dict:
        """
        Generate threat decision.
        """


        risk = intelligence.get(
            "risk",
            {},
        )


        reputation = intelligence.get(
            "reputation",
            {},
        )


        score = risk.get(
            "score",
            0,
        )


        reputation_status = reputation.get(
            "reputation",
            "unknown",
        )


        decision = {

            "action": "monitor",

            "severity": "low",

            "confidence": 0,

            "reason": "No significant threat indicators",

        }



        if score >= 60 or reputation_status == "suspicious":

            decision = {

                "action": "create_case",

                "severity": "high",

                "confidence": reputation.get(
                    "confidence",
                    70,
                ),

                "reason":
                    "Suspicious IOC requires investigation",

            }



        elif score >= 30:

            decision = {

                "action": "investigate",

                "severity": "medium",

                "confidence": 60,

                "reason":
                    "IOC requires analyst review",

            }



        return decision