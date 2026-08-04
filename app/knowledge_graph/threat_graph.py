from datetime import datetime


class ThreatGraph:

    def analyze(self, event):

        return {
            "threat_entities": [
                "Ransomware Operator",
                "Malware Family",
                "Attack Technique"
            ],
            "risk": "critical",
            "event": event,
            "timestamp": datetime.utcnow().isoformat()
        }