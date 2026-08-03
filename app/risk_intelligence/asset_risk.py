from datetime import datetime


class AssetRisk:

    def analyze(self, event):

        text = event.lower()

        score = 20

        if "server" in text:
            score += 20

        if "database" in text:
            score += 20

        return {
            "asset": "Enterprise Asset",
            "score": min(score, 40),
            "criticality": "high",
            "timestamp": datetime.utcnow().isoformat()
        }