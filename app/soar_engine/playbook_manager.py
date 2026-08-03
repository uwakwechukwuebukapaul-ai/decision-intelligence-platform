from datetime import datetime


class PlaybookManager:

    def select(self, incident):

        return {
            "playbook": "Ransomware Response Playbook",
            "incident": incident,
            "steps": [
                "Contain endpoint",
                "Collect evidence",
                "Block indicators",
                "Recover systems"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }