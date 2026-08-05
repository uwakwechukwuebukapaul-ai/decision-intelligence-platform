class InvestigationModel:
    """
    Investigation intelligence data model.
    """

    def create_case(self, event):

        return {
            "event": event,
            "status": "investigation_created",
            "severity": self.calculate_severity(event)
        }


    def calculate_severity(self, event):

        text = event.lower()

        critical_keywords = [
            "ransomware",
            "data breach",
            "credential theft",
            "privilege escalation"
        ]

        for keyword in critical_keywords:
            if keyword in text:
                return "critical"

        return "medium"