from datetime import datetime


class ThreatReasoner:

    def analyze(self, context):

        event = context["event"].lower()

        threats = []

        if "ransomware" in event:
            threats.append("Ransomware activity")

        if "powershell" in event:
            threats.append("PowerShell execution")

        return {
            "identified_threats": threats,
            "severity": "critical"
            if threats else "medium",
            "timestamp": datetime.utcnow().isoformat()
        }