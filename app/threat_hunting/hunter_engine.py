from datetime import datetime

from .hypothesis_generator import HypothesisGenerator
from .query_hunter import QueryHunter
from .anomaly_detector import AnomalyDetector
from .hunting_campaign import HuntingCampaign
from .hunt_validator import HuntValidator
from .hunt_reporter import HuntReporter
from .hunting_memory import HuntingMemory


class ThreatHunterEngine:

    def __init__(self):
        self.hypothesis = HypothesisGenerator()
        self.query = QueryHunter()
        self.anomaly = AnomalyDetector()
        self.campaign = HuntingCampaign()
        self.validator = HuntValidator()
        self.reporter = HuntReporter()
        self.memory = HuntingMemory()

    def hunt(self, threat):

        hypotheses = self.hypothesis.generate(threat)

        queries = self.query.build(threat)

        anomalies = self.anomaly.detect(threat)

        campaign = self.campaign.create(threat)

        validation = self.validator.validate(
            hypotheses
        )

        report = self.reporter.generate(
            threat,
            anomalies
        )

        self.memory.store(threat)

        return {
            "status": "completed",
            "threat": threat,
            "hypothesis": hypotheses,
            "queries": queries,
            "anomalies": anomalies,
            "campaign": campaign,
            "validation": validation,
            "report": report,
            "created_at": datetime.utcnow().isoformat()
        }