from datetime import datetime

from .alert_manager import AlertManager
from .case_orchestrator import CaseOrchestrator
from .investigation_orchestrator import InvestigationOrchestrator
from .response_orchestrator import ResponseOrchestrator
from .analyst_dashboard import AnalystDashboard


class SOCEngine:


    def __init__(self):

        self.alert_manager = AlertManager()

        self.case_manager = CaseOrchestrator()

        self.investigation = InvestigationOrchestrator()

        self.response = ResponseOrchestrator()

        self.dashboard = AnalystDashboard()



    def process(self, alert):


        alert_result = self.alert_manager.analyze(
            alert
        )


        case_result = self.case_manager.create(
            alert,
            alert_result
        )


        investigation_result = self.investigation.start(
            case_result
        )


        response_result = self.response.recommend(
            alert_result
        )


        dashboard_result = self.dashboard.update(
            case_result,
            alert_result
        )


        return {

            "status": "completed",

            "alert_management":
                alert_result,

            "case":
                case_result,

            "investigation":
                investigation_result,

            "response":
                response_result,

            "dashboard":
                dashboard_result,

            "created_at":
                datetime.utcnow().isoformat()

        }