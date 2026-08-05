from datetime import datetime


class RuleGenerator:
    """
    AI-assisted detection rule generator.
    """

    def generate(self, threat_behavior):
        return {
            "rule_id": f"DET-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
            "name": threat_behavior.get(
                "name",
                "Unknown Threat Detection"
            ),
            "description": threat_behavior.get(
                "description",
                ""
            ),
            "severity": threat_behavior.get(
                "severity",
                "medium"
            ),
            "logic": {
                "behavior": threat_behavior.get(
                    "behavior",
                    []
                )
            },
            "created_at": datetime.utcnow().isoformat()
        }