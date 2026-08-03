from datetime import datetime


class TacticMapper:

    def map(self, techniques):

        tactics = []

        names = str(techniques)

        if "PowerShell" in names:
            tactics.append("Execution")

        if "Encrypted" in names:
            tactics.append("Impact")

        if "Credential" in names:
            tactics.append("Credential Access")

        if not tactics:
            tactics.append("Unknown")

        return {
            "tactics": tactics,
            "framework": "MITRE ATT&CK",
            "timestamp": datetime.utcnow().isoformat()
        }