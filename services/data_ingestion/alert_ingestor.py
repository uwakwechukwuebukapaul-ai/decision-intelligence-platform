class AlertIngestor:
    """
    Handles incoming security alerts.
    """

    def ingest_alert(self, alert):

        return {
            "alert_received": True,
            "severity": alert.get(
                "severity",
                "unknown"
            ),
            "alert": alert
        }