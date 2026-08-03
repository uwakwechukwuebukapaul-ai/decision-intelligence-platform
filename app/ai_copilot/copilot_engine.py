from datetime import datetime

from .prompt_manager import PromptManager
from .analyst_assistant import AnalystAssistant
from .incident_explainer import IncidentExplainer
from .query_assistant import QueryAssistant
from .report_assistant import ReportAssistant
from .recommendation_assistant import RecommendationAssistant
from .copilot_memory import CopilotMemory
from .copilot_logger import CopilotLogger



class AICopilotEngine:


    def __init__(self):

        self.prompt = PromptManager()
        self.analyst = AnalystAssistant()
        self.explainer = IncidentExplainer()
        self.query = QueryAssistant()
        self.report = ReportAssistant()
        self.recommendation = RecommendationAssistant()
        self.memory = CopilotMemory()
        self.logger = CopilotLogger()



    def assist(self, incident):


        return {


            "status":
                "completed",


            "incident":
                incident,


            "prompt":
                self.prompt.build_prompt(
                    incident
                ),


            "analyst_assistance":
                self.analyst.assist(
                    incident
                ),


            "incident_explanation":
                self.explainer.explain(
                    incident
                ),


            "query_generation":
                self.query.generate(
                    incident
                ),


            "report_generation":
                self.report.generate(
                    incident
                ),


            "recommendations":
                self.recommendation.recommend(
                    incident
                ),


            "memory":
                self.memory.store(
                    incident
                ),


            "log":
                self.logger.log(
                    incident
                ),


            "created_at":
                datetime.utcnow().isoformat()

        }