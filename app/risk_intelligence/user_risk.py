from datetime import datetime


class UserRisk:

    def analyze(self, event):

        score = 10

        text = event.lower()

        if "account" in text or "credential" in text:
            score = 30

        return {
            "user": "Unknown User",
            "score": score,
            "behavior": "Suspicious activity analysis",
            "timestamp": datetime.utcnow().isoformat()
        }