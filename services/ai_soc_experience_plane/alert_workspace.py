class AlertWorkspace:
    """
    Sentinel DNA alert analyst workspace.

    Provides:
    - alert queue management
    - alert review workflow
    - analyst alert actions
    """

    def __init__(self):
        self.alerts = []


    def create_alert(self, alert):

        record = {
            "alert": alert,
            "status": "new",
            "priority": "unknown"
        }

        self.alerts.append(record)

        return record


    def assign_alert(self, alert_id, analyst):

        for item in self.alerts:

            if item.get("alert") == alert_id:
                item["analyst"] = analyst
                item["status"] = "assigned"
                return item

        return None


    def update_status(self, alert_id, status):

        for item in self.alerts:

            if item.get("alert") == alert_id:
                item["status"] = status
                return item

        return None


    def list_alerts(self):

        return self.alerts