from datetime import datetime, timezone

from .decision_model import DecisionModel


class DecisionEngine:
    """
    Converts intelligence into autonomous decisions.

    Central Sentinel DNA decision layer.

    Responsibilities:
    - evaluate threat intelligence
    - determine response priority
    - generate autonomous actions
    - maintain pipeline compatibility

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
        Compatibility wrapper.

        Existing pipelines call decide().
        """

        return self.evaluate(
            intelligence
        )



    def evaluate(
        self,
        intelligence
    ):
        """
        Evaluate intelligence and produce decision.
        """


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



        if (
            risk_level == "critical"
            or risk_score >= 90
        ):

            return self._critical_response(
                risk_level,
                risk_score
            )



        if risk_score >= 50:

            return self._investigation_response(
                risk_score
            )



        return self._monitor_response(
            risk_score
        )



    def _critical_response(
        self,
        risk_level,
        risk_score
    ):

        result = DecisionModel(

            decision="contain_immediately",

            priority="critical",

            actions=[

                "isolate affected systems",

                "disable compromised accounts",

                "collect forensic evidence"

            ],

            reasoning={

                "risk_level":
                    risk_level,

                "risk_score":
                    risk_score,

                "trigger":
                    "critical threat detected"

            }

        ).to_dict()


        result["created_at"] = datetime.now(
            timezone.utc
        ).isoformat()


        return result



    def _investigation_response(
        self,
        risk_score
    ):

        result = DecisionModel(

            decision="investigate",

            priority="high",

            actions=[

                "collect additional telemetry",

                "review affected assets"

            ],

            reasoning={

                "risk_score":
                    risk_score

            }

        ).to_dict()


        result["created_at"] = datetime.now(
            timezone.utc
        ).isoformat()


        return result



    def _monitor_response(
        self,
        risk_score
    ):

        result = DecisionModel(

            decision="monitor",

            priority="low",

            actions=[

                "continue observation"

            ],

            reasoning={

                "risk_score":
                    risk_score

            }

        ).to_dict()


        result["created_at"] = datetime.now(
            timezone.utc
        ).isoformat()


        return result