from datetime import datetime

from .incident_view import IncidentView
from .threat_view import ThreatView
from .risk_dashboard import RiskDashboard
from .investigation_view import InvestigationView
from .analytics_view import AnalyticsView
from .dashboard_memory import DashboardMemory
from .dashboard_logger import DashboardLogger



class SOCDashboardEngine:


    def __init__(self):

        self.incidents = IncidentView()

        self.threats = ThreatView()

        self.risk = RiskDashboard()

        self.investigation = InvestigationView()

        self.analytics = AnalyticsView()

        self.memory = DashboardMemory()

        self.logger = DashboardLogger()



    def generate(self, incident):


        incident_view = self.incidents.generate(
            incident
        )


        threat_view = self.threats.generate(
            incident
        )


        risk_view = self.risk.calculate(
            incident
        )


        investigation_view = self.investigation.generate(
            incident
        )


        analytics_view = self.analytics.generate(
            incident
        )


        dashboard_data = {

            "incident":
                incident_view,

            "threats":
                threat_view,

            "risk":
                risk_view,

            "investigation":
                investigation_view,

            "analytics":
                analytics_view

        }


        memory = self.memory.store(
            dashboard_data
        )


        log = self.logger.log(
            incident
        )


        return {

            "status":

                "completed",

            "dashboard":

                dashboard_data,

            "memory":

                memory,

            "log":

                log,

            "created_at":

                datetime.utcnow().isoformat()
        }