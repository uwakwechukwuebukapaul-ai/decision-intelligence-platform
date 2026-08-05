class IntelligenceRouter:
    """
    Routes investigation signals to the correct intelligence engines.
    """

    def __init__(self, registry):
        self.registry = registry


    def route(self, event):

        result = {
            "event": event,
            "routes": []
        }

        keywords = str(event).lower()

        if "malware" in keywords or "ransomware" in keywords:
            result["routes"].append("threat_intelligence")


        if "powershell" in keywords or "attack" in keywords:
            result["routes"].append("detection_engine")


        if "incident" in keywords:
            result["routes"].append("incident_response")


        if not result["routes"]:
            result["routes"].append("general_intelligence")


        return result