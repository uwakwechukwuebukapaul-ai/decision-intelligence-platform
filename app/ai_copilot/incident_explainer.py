from datetime import datetime


class IncidentExplainer:

    def explain(self, incident):

        return {
            "summary":
                f"Security incident detected: {incident}",

            "explanation":
                "The activity indicates possible malicious execution and impact behavior.",

            "timestamp":
                datetime.utcnow().isoformat()
        }