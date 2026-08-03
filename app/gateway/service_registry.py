from datetime import datetime


class ServiceRegistry:
    """
    Registers and manages Sentinel DNA internal services.
    """

    def __init__(self):

        self.services = {
            "soc_engine": "available",
            "threat_intelligence": "available",
            "detection_engine": "available",
            "incident_response": "available",
            "threat_hunting": "available",
            "copilot": "available",
            "autonomous_brain": "available"
        }


    def get_services(self):

        return {
            "services": self.services,
            "count": len(self.services),
            "timestamp": datetime.utcnow().isoformat()
        }


    def check_service(self, name):

        return {
            "service": name,
            "status": self.services.get(
                name,
                "unknown"
            ),
            "timestamp": datetime.utcnow().isoformat()
        }