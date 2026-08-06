from datetime import datetime

from .pipeline_schema import PipelineResult
from .pipeline_repository import PipelineRepository

from app.investigation import IntelligenceFusionEngine
from app.decision import DecisionEngine
from app.response import ResponseEngine
from app.threat_intelligence import IntelligenceEngine
from app.detection import DetectionEngine
from app.correlation import CorrelationEngine
from app.ueba import UEBAEngine


class PipelineEngine:

    def __init__(self):

        self.repository = PipelineRepository()

        self.investigation = IntelligenceFusionEngine()
        self.intelligence = IntelligenceEngine()
        self.detection = DetectionEngine()
        self.correlation = CorrelationEngine()
        self.ueba = UEBAEngine()

        self.decision = DecisionEngine()
        self.response = ResponseEngine()


    def execute(self, incident):

        incident_id = incident.get(
            "incident_id",
            "UNKNOWN"
        )

        indicator = incident.get(
            "indicator"
        )


        stages = []


        # Threat Intelligence
        threat = self.intelligence.analyze(
            indicator
        )
        stages.append(
            "threat_intelligence"
        )


        # Detection
        detection = self.detection.analyze(
            indicator
        )
        stages.append(
            "detection"
        )


        # Correlation
        correlation = self.correlation.correlate(
            {
                "incident_id": incident_id,
                "indicator": indicator
            }
        )

        stages.append(
            "correlation"
        )


        # Investigation Fusion
        investigation = self.investigation.analyze(
            incident_id
        )

        stages.append(
            "investigation"
        )


        # Decision
        decision = self.decision.decide(
            investigation
        )

        stages.append(
            "decision"
        )


        # Response Automation
        response = self.response.respond(
            decision | {
                "indicator": indicator
            }
        )

        stages.append(
            "response"
        )


        result = PipelineResult(

            incident_id=incident_id,

            status="completed",

            stages_completed=stages,

            intelligence={
                "threat": threat,
                "detection": detection,
                "correlation": correlation
            },

            decision=decision,

            response=response
        )


        return self.repository.save(
            result
        )