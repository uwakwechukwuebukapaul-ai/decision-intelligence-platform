class AlertWorkspace:

    def __init__(self):
        self.alerts = []


    def add_alert(self, alert):

        self.alerts.append(alert)

        return {
            "alert": alert,
            "status": "queued"
        }


    def list_alerts(self):

        return self.alerts