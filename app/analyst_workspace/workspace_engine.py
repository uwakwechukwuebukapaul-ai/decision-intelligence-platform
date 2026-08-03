from datetime import datetime

from .incident_view import IncidentView
from .dashboard_builder import DashboardBuilder
from .threat_visualizer import ThreatVisualizer
from .copilot_interface import CopilotInterface
from .analyst_actions import AnalystActions
from .workspace_memory import WorkspaceMemory
from .workspace_logger import WorkspaceLogger


class AnalystWorkspaceEngine:

    def __init__(self):

        self.incident_view = IncidentView()
        self.dashboard = DashboardBuilder()
        self.visualizer = ThreatVisualizer()
        self.copilot = CopilotInterface()
        self.actions = AnalystActions()
        self.memory = WorkspaceMemory()
        self.logger = WorkspaceLogger()


    def open_workspace(self, incident):

        view = self.incident_view.build(incident)

        dashboard = self.dashboard.create(
            incident
        )

        graph = self.visualizer.visualize(
            incident
        )

        copilot = self.copilot.assist(
            incident
        )

        actions = self.actions.available(
            incident
        )

        memory = self.memory.store(
            incident
        )

        log = self.logger.record(
            incident
        )


        return {

            "status": "workspace_ready",

            "incident": incident,

            "incident_view": view,

            "dashboard": dashboard,

            "threat_visualization": graph,

            "copilot": copilot,

            "analyst_actions": actions,

            "memory": memory,

            "log": log,

            "created_at": datetime.utcnow().isoformat()

        }