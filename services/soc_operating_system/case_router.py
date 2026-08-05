from datetime import datetime
import uuid


class CaseRouter:
    """
    Routes alerts into investigation cases.
    """

    def __init__(self):
        self.cases = []

    def route(self, alert):

        case = {
            "case_id": f"INC-{uuid.uuid4().hex[:8]}",
            "alert_id": alert["alert_id"],
            "severity": alert["severity"],
            "assigned_team": self.assign_team(alert),
            "status": "open",
            "created_at": datetime.utcnow().isoformat(),
        }

        self.cases.append(case)

        return case

    def assign_team(self, alert):

        severity = alert.get("severity")

        if severity == "critical":
            return "incident-response"

        if severity == "high":
            return "threat-hunting"

        return "soc-analyst"