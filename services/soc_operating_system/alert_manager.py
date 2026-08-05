from datetime import datetime
import uuid


class AlertManager:
    """
    Handles SOC alert intake and normalization.
    """

    def __init__(self):
        self.alerts = []

    def ingest(self, alert):
        normalized = {
            "alert_id": f"ALT-{uuid.uuid4().hex[:8]}",
            "severity": alert.get("severity", "medium"),
            "source": alert.get("source", "unknown"),
            "description": alert.get("description", ""),
            "status": "new",
            "created_at": datetime.utcnow().isoformat(),
        }

        self.alerts.append(normalized)

        return normalized

    def list_alerts(self):
        return self.alerts