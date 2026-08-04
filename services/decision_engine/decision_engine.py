from .decision_model import DecisionModel


class DecisionEngine:
    """
    Converts intelligence into autonomous decisions.

    Supports:
    - evaluate()
    - decide() compatibility interface

    Used by:
    - Sentinel Core Pipeline
    - Autonomous Orchestrator
    - Response Engine
    """


    def decide(
        self,
        intelligence
    ):
        """
        Pipeline compatibility wrapper.
        """

        return self.evaluate(
            intelligence
        )



    def evaluate(
        self,
        intelligence
    ):

        if hasattr(
            intelligence,
            "to_dict"
        ):

            intelligence = intelligence.to_dict()



        risk = intelligence.get(
            "risk",
            {}
        )


        risk_level = risk.get(
            "risk_level",
            "unknown"
        )


        risk_score = risk.get(
            "risk_score",
            0
        )



        if risk_level == "critical" or risk_score >= 90:

            return DecisionModel(

                decision="contain_immediately",

                priority="critical",

                actions=[

                    "isolate affected systems",

                    "disable compromised accounts",

                    "collect forensic evidence"

                ],

                reasoning={

                    "risk_level": risk_level,

                    "risk_score": risk_score,

                    "trigger":
                        "critical threat detected"

                }

            ).to_dict()



        if risk_score >= 50:

            return DecisionModel(

                decision="investigate",

                priority="high",

                actions=[

                    "collect additional telemetry",

                    "review affected assets"

                ],

                reasoning={

                    "risk_score": risk_score

                }

            ).to_dict()



        return DecisionModel(

            decision="monitor",

            priority="low",

            actions=[

                "continue observation"

            ],

            reasoning={

                "risk_score": risk_score

            }

        ).to_dict()