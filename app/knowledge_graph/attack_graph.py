from datetime import datetime


class AttackGraph:

    def build(self, incident):

        return {
            "framework": "MITRE ATT&CK",
            "attack_path": [
                "Initial Access",
                "Execution",
                "Persistence",
                "Impact"
            ],
            "incident": incident,
            "timestamp": datetime.utcnow().isoformat()
        }