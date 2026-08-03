from datetime import datetime


class HypothesisGenerator:

    def generate(self, threat):

        hypotheses = []

        text = threat.lower()

        if "ransomware" in text:
            hypotheses.extend([
                "Possible ransomware execution",
                "Possible data encryption activity",
                "Possible lateral movement"
            ])

        if "powershell" in text:
            hypotheses.append(
                "Suspicious PowerShell execution"
            )

        if not hypotheses:
            hypotheses.append(
                "Unknown threat behavior requiring investigation"
            )

        return {
            "hypotheses": hypotheses,
            "count": len(hypotheses),
            "timestamp": datetime.utcnow().isoformat()
        }