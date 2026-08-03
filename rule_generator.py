from datetime import datetime


class RuleGenerator:

    def generate(self, threat):

        return {
            "rule_name": "AI Generated Threat Detection Rule",
            "description": threat,
            "logic": [
                "Monitor suspicious execution",
                "Detect abnormal behavior",
                "Correlate security events"
            ],
            "severity": "critical",
            "timestamp": datetime.utcnow().isoformat()
        }