from datetime import datetime


class ThreatKnowledge:
    """
    Security threat intelligence knowledge base.
    """

    def analyze(self, entities):

        threats = []

        for entity in entities:

            if entity["type"] == "Threat":

                threats.append(
                    {
                        "threat": entity["name"],
                        "risk": "high"
                    }
                )

        return {
            "identified_threats": threats,
            "threat_score": min(
                100,
                len(threats) * 30
            ),
            "timestamp": datetime.utcnow().isoformat()
        }