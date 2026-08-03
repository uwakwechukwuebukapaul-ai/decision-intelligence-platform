from datetime import datetime


class AttackNavigator:

    def generate(self, tactics):

        return {
            "navigator":
                "MITRE ATT&CK Navigator View",
            "attack_path":
                [
                    "Initial Access",
                    "Execution",
                    "Persistence",
                    "Impact"
                ],
            "mapped_tactics":
                tactics,
            "timestamp":
                datetime.utcnow().isoformat()
        }