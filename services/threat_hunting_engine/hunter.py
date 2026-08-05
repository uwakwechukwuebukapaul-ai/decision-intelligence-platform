from .hunt_strategy import HuntStrategy
from .query_builder import QueryBuilder
from .anomaly_detector import AnomalyDetector


class ThreatHunter:
    """
    Autonomous Sentinel DNA threat hunting engine.
    """

    def __init__(self):

        self.strategy = HuntStrategy()

        self.query_builder = QueryBuilder()

        self.anomaly_detector = AnomalyDetector()



    def hunt(
        self,
        event
    ):

        strategies = self.strategy.generate(
            event
        )


        queries = []


        for strategy in strategies:

            queries.append(
                self.query_builder.build(strategy)
            )


        findings = self.anomaly_detector.analyze(
            [
                event
            ]
        )


        risk = "low"


        for finding in findings:

            if finding["risk"] == "critical":
                risk = "critical"

            elif finding["risk"] == "high":
                risk = "high"


        return {

            "status":
            "hunt_completed",

            "event":
            event,

            "strategies":
            strategies,

            "queries":
            queries,

            "findings":
            findings,

            "risk":
            risk

        }