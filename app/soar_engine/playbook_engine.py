from datetime import datetime


class PlaybookEngine:

    def generate(self, incident):

        return {
            "playbook": "Ransomware Response Playbook",
            "steps": [
                "Validate incident",
                "Collect evidence",
                "Isolate affected systems",
                "Block malicious indicators",
                "Start recovery workflow"
            ],
            "incident": incident,
            "status": "generated",
            "timestamp": datetime.utcnow().isoformat()
        }