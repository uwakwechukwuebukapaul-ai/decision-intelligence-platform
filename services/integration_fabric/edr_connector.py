class EDRConnector:
    """
    Endpoint Detection and Response connector.
    """

    def __init__(self):
        self.name = "EDR"

    def collect_alerts(self):
        return {
            "connector": self.name,
            "alerts": []
        }

    def isolate_host(self, hostname):
        return {
            "action": "isolate_host",
            "target": hostname,
            "status": "queued"
        }