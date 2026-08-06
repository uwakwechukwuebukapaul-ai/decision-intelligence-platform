import uuid

from .reasoning_engine import ReasoningEngine
from .recommendation_engine import RecommendationEngine
from .copilot_repository import CopilotRepository
from .copilot_schema import CopilotRecord, timestamp



class CopilotEngine:


    def __init__(self):

        self.reasoning = ReasoningEngine()

        self.recommendations = RecommendationEngine()

        self.repository = CopilotRepository()



    def investigate(self, context):


        findings = self.reasoning.analyze(
            context
        )


        actions = self.recommendations.generate(
            context
        )


        summary = (
            "Security investigation generated "
            "using correlated intelligence signals"
        )


        attack_story = (
            "Threat activity was correlated with "
            "available asset, identity and IOC context"
        )


        record = CopilotRecord(

            copilot_id=
            f"COP-{uuid.uuid4().hex[:8].upper()}",

            incident_id=
            context.get("incident_id"),

            summary=
            summary,

            risk_explanation=
            findings,

            attack_story=
            attack_story,

            recommendations=
            actions,

            confidence=0.96,

            created_at=
            timestamp()
        )


        self.repository.save(
            record.to_dict()
        )


        return record.to_dict()