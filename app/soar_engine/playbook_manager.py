from datetime import datetime


class PlaybookManager:

    def select(self, incident):

        return {
            "playbook": "Ransomware Response Playbook",
            "steps": [
                "Validate incident",
                "Isolate affected assets",
                "Block indicators",
                "Collect evidence",
                "Recover systems"
            ],
            "incident": incident,
            "timestamp": datetime.utcnow().isoformat()
        }