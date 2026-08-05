from datetime import datetime

from .alert_manager import AlertManager
from .case_router import CaseRouter
from .sla_engine import SLAEngine
from .soc_metrics import SOCMetrics


class SOCManager:
    """
    Central operating layer for Sentinel DNA SOC operations.

    Coordinates:
    - Alerts
    - Cases
    - Routing
    - SLA tracking
    - SOC metrics
    """

    def __init__(self):
        self.alert_manager = AlertManager()
        self.case_router = CaseRouter()
        self.sla_engine = SLAEngine()
        self.metrics = SOCMetrics()

    def process_alert(self, alert):
        alert_result = self.alert_manager.ingest(alert)

        case = self.case_router.route(alert_result)

        sla = self.sla_engine.evaluate(case)

        self.metrics.record_case(case)

        return {
            "status": "processed",
            "alert": alert_result,
            "case": case,
            "sla": sla,
            "timestamp": datetime.utcnow().isoformat(),
        }

    def health(self):
        return {
            "service": "SOC Operating System",
            "status": "healthy",
            "components": {
                "alert_manager": "active",
                "case_router": "active",
                "sla_engine": "active",
                "metrics": "active",
            },
        }