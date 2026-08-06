"""
Sentinel DNA

Threat Context Intelligence Engine

Provides contextual threat intelligence
around IOC indicators.
"""

from __future__ import annotations



class ThreatContextEngine:
    """
    Generates threat context.
    """


    def analyze(
        self,
        indicator: dict,
    ) -> dict:
        """
        Analyze threat context.
        """


        indicator_type = indicator.get(
            "type",
            "unknown",
        )


        context = {

            "category": "unknown",

            "confidence": 50,

            "signals": [],

        }


        if indicator_type == "domain":

            context.update(

                {

                    "category": "possible command_and_control",

                    "confidence": 60,

                    "signals": [

                        "domain indicator",

                    ],

                }

            )


        elif indicator_type == "ip":

            context.update(

                {

                    "category": "network indicator",

                    "confidence": 55,

                    "signals": [

                        "ip address indicator",

                    ],

                }

            )


        return context