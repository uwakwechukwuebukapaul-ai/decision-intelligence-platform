from datetime import datetime


class RequestRouter:
    """
    Routes requests to the correct intelligence service.
    """

    def route(self, request):

        text = str(request).lower()


        if "ransomware" in text:
            destination = "incident_response"

        elif "ioc" in text or "threat actor" in text:
            destination = "threat_intelligence"

        elif "detect" in text or "alert" in text:
            destination = "detection_engine"

        else:
            destination = "autonomous_brain"


        return {

            "request": request,

            "destination":
                destination,

            "timestamp":
                datetime.utcnow().isoformat()
        }