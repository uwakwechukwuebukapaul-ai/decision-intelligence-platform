from .conversation_engine import ConversationEngine
from .investigation_assistant import InvestigationAssistant
from .explanation_engine import ExplanationEngine
from .report_generator import ReportGenerator
from .recommendation_engine import RecommendationEngine


class AISOCCopilot:
    """
    Sentinel DNA AI SOC Copilot.

    Provides analyst-facing intelligence:
    - investigation assistance
    - alert explanation
    - recommendations
    - reporting
    """

    def __init__(self):
        self.conversation = ConversationEngine()
        self.investigation = InvestigationAssistant()
        self.explainer = ExplanationEngine()
        self.reporter = ReportGenerator()
        self.recommender = RecommendationEngine()

    def investigate(self, case):
        return self.investigation.analyze(case)

    def explain_alert(self, alert):
        return self.explainer.explain(alert)

    def recommend(self, context):
        return self.recommender.generate(context)

    def generate_report(self, incident):
        return self.reporter.create(incident)

    def chat(self, message, context=None):
        return self.conversation.process(
            message,
            context
        )