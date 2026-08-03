from datetime import datetime

from .conversation_manager import ConversationManager
from .investigation_assistant import InvestigationAssistant
from .explanation_engine import ExplanationEngine
from .recommendation_engine import RecommendationEngine
from .query_assistant import QueryAssistant
from .copilot_memory import CopilotMemory
from .copilot_logger import CopilotLogger



class SecurityCopilotEngine:


    def __init__(self):

        self.conversation = ConversationManager()

        self.investigation = InvestigationAssistant()

        self.explanation = ExplanationEngine()

        self.recommendation = RecommendationEngine()

        self.query = QueryAssistant()

        self.memory = CopilotMemory()

        self.logger = CopilotLogger()



    def assist(self, incident):


        conversation = self.conversation.manage(
            incident
        )


        investigation = self.investigation.assist(
            incident
        )


        explanation = self.explanation.explain(
            incident
        )


        recommendations = self.recommendation.recommend(
            incident
        )


        queries = self.query.generate(
            incident
        )


        memory = self.memory.store(
            incident
        )


        log = self.logger.log(
            incident
        )


        return {

            "status":
                "completed",

            "incident":
                incident,

            "conversation":
                conversation,

            "investigation":
                investigation,

            "explanation":
                explanation,

            "recommendations":
                recommendations,

            "queries":
                queries,

            "memory":
                memory,

            "log":
                log,

            "created_at":
                datetime.utcnow().isoformat()
        }