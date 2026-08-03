from datetime import datetime


class RootCauseAnalyzer:

    def analyze(self, incident):

        return {
            "root_cause":
                "Unauthorized execution leading to ransomware deployment",
            "attack_chain":
                [
                    "Execution",
                    "Privilege Abuse",
                    "Impact"
                ],
            "timestamp": datetime.utcnow().isoformat()
        }