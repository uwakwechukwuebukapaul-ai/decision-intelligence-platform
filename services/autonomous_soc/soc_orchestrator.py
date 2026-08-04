from .analyst_agent import AnalystAgent
from .investigation_planner import InvestigationPlanner

from services.agent_manager import AgentManager
from services.agents import (
    ThreatHunterAgent,
    IncidentCommanderAgent,
    DetectionEngineerAgent,
    ReportAgent
)


class SOCOrchestrator:
    """
    Autonomous SOC coordination layer.

    Controls AI security agents and investigation workflows.
    """

    def __init__(self):

        self.analyst = AnalystAgent()

        self.planner = InvestigationPlanner()

        self.agent_manager = AgentManager()


        self.register_agents()


    def register_agents(self):

        self.agent_manager.register(
            "threat_hunter",
            ThreatHunterAgent()
        )


        self.agent_manager.register(
            "incident_commander",
            IncidentCommanderAgent()
        )


        self.agent_manager.register(
            "detection_engineer",
            DetectionEngineerAgent()
        )


        self.agent_manager.register(
            "report_agent",
            ReportAgent()
        )


    def investigate(
        self,
        event
    ):
        """
        Execute autonomous SOC investigation.
        """


        investigation_plan = self.planner.create_plan(
            event
        )


        analyst_result = self.analyst.analyze(
            event
        )


        agent_results = self.agent_manager.execute_all(
            event,
            investigation_plan
        )


        return {

            "event":
                event,


            "investigation_plan":
                investigation_plan,


            "analyst_analysis":
                analyst_result,


            "agent_results":
                agent_results,


            "status":
                "autonomous_soc_completed"

        }