from datetime import datetime


class DetectionEvolution:
    """
    Evolves detection rules using intelligence feedback.
    """

    def __init__(self):
        self.rules = []

    def evolve_rule(self, rule_name, improvement):
        rule = {
            "rule": rule_name,
            "improvement": improvement,
            "created": datetime.utcnow().isoformat()
        }

        self.rules.append(rule)

        return rule

    def analyze_detection_gaps(self, findings):
        return {
            "gaps_found": len(findings),
            "recommendation": "generate_detection_logic"
        }

    def list_evolved_rules(self):
        return self.rules