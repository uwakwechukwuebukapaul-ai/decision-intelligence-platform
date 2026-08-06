class IncidentManager:

    def create_incident(self, data):

        severity = data.get(
            "severity",
            "medium"
        )

        if severity == "critical":
            priority = "critical"

        elif severity == "high":
            priority = "high"

        else:
            priority = "normal"

        return {
            "incident_id": data.get("incident_id"),
            "indicator": data.get("indicator"),
            "severity": severity,
            "priority": priority,
            "status": "triaged"
        }

    def update_status(self, incident, status):

        incident["status"] = status

        return incident