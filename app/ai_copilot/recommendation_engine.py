from datetime import datetime


class RecommendationEngine:

    def recommend(self, incident):

        if "ransomware" in incident.lower():

            actions = [
                "Execute containment workflow",
                "Isolate affected systems",
                "Block malicious indicators",
                "Begin forensic investigation"
            ]

        else:

            actions = [
                "Continue monitoring",
                "Collect additional evidence"
            ]


        return {
            "recommendations": actions,
            "priority": "critical",
            "timestamp": datetime.utcnow().isoformat()
        }