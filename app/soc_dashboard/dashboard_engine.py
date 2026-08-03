from datetime import datetime

from .incident_view import IncidentView
from .threat_view import ThreatView
from .risk_visualizer import RiskVisualizer
from .ai_insights import AIInsights
from .metrics_engine import MetricsEngine
from .dashboard_memory import DashboardMemory



class DashboardEngine:
    """
    Sentinel DNA Enterprise SOC Command Center.
    """


    def __init__(self):

        self.incidents = IncidentView()

        self.threats = ThreatView()

        self.risk = RiskVisualizer()

        self.ai = AIInsights()

        self.metrics = MetricsEngine()

        self.memory = DashboardMemory()



    def generate(self, event):


        dashboard = {

            "status":
                "completed",

            "event":
                event,


            "incident_view":
                self.incidents.analyze(event),


            "threat_view":
                self.threats.analyze(event),


            "risk":
                self.risk.calculate(event),


            "ai_insights":
                self.ai.generate(event),


            "metrics":
                self.metrics.generate(),


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.memory.store(dashboard)


        return dashboard