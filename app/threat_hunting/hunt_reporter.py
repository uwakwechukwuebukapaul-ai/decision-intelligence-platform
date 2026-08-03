from datetime import datetime


class HuntReporter:

    def generate(self, threat, findings):

        return {
            "title":
                "Sentinel DNA Threat Hunting Report",
            "threat":
                threat,
            "findings":
                findings["findings"],
            "generated_at":
                datetime.utcnow().isoformat()
        }