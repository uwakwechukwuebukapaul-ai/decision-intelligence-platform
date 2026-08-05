from .analyst_workspace import AnalystWorkspace
from .copilot_engine import CopilotEngine
from .investigation_dashboard import InvestigationDashboard
from .case_interface import CaseInterface
from .alert_workspace import AlertWorkspace
from .executive_dashboard import ExecutiveDashboard
from .visualization_engine import VisualizationEngine
from .experience_orchestrator import ExperienceOrchestrator


class AISOCExperiencePlane:
    """
    Sentinel DNA analyst experience layer.

    Provides:
    - SOC analyst workspace
    - AI Copilot
    - dashboards
    - case interaction
    - visualization
    """

    def __init__(self):

        self.analyst_workspace = AnalystWorkspace()
        self.copilot = CopilotEngine()
        self.investigation_dashboard = InvestigationDashboard()
        self.case_interface = CaseInterface()
        self.alert_workspace = AlertWorkspace()
        self.executive_dashboard = ExecutiveDashboard()
        self.visualization = VisualizationEngine()
        self.orchestrator = ExperienceOrchestrator()


    def status(self):

        return {
            "component": "AI SOC Experience Plane",
            "status": "healthy"
        }