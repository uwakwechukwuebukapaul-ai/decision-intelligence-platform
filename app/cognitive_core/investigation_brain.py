from datetime import datetime
import uuid


class InvestigationBrain:

    def build_context(self, event):

        return {
            "context_id": f"CTX-{uuid.uuid4().hex[:8].upper()}",
            "event": event,
            "incident_type": self.identify_incident(event),
            "asset_context": self.identify_assets(event),
            "attack_context": self.identify_attack(event),
            "timestamp": datetime.utcnow().isoformat()
        }


    def identify_incident(self, event):

        event = event.lower()

        if "ransomware" in event:
            return "Ransomware Incident"

        if "phishing" in event:
            return "Phishing Incident"

        return "Security Incident"


    def identify_assets(self, event):

        assets = []

        keywords = [
            "server",
            "database",
            "endpoint",
            "cloud"
        ]

        for item in keywords:
            if item in event.lower():
                assets.append(item)

        return assets or ["Unknown Asset"]


    def identify_attack(self, event):

        attacks = []

        if "powershell" in event.lower():
            attacks.append("Command Execution")

        if "ransomware" in event.lower():
            attacks.append("Impact Operation")

        return attacks