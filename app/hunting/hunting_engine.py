"""
Sentinel DNA Threat Hunting Engine

Proactive investigation engine.
"""


from .hunt_repository import HuntRepository
from .hunt_schema import create_hunt_result
from .rules import HUNT_RULES



class HuntingEngine:


    def __init__(self):

        self.repository = HuntRepository()



    def hunt(
        self,
        indicator: str
    ):


        findings = []


        severity = "low"


        if any(
            tld in indicator
            for tld in [
                ".xyz",
                ".top",
                ".click",
                ".ru"
            ]
        ):

            findings.append(

                {
                    "rule":
                        "suspicious_domain",

                    "indicator":
                        indicator,

                    "message":
                        HUNT_RULES[
                            "suspicious_domain"
                        ][
                            "description"
                        ]

                }

            )

            severity = "high"



        result = create_hunt_result(

            query=indicator,

            findings=findings,

            severity=severity

        )


        return self.repository.save(
            result
        )