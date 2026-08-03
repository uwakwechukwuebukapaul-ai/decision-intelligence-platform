from datetime import datetime


class RuleGenerator:

    def generate(self, threat):

        return {
            "rule_name": "AI Generated Detection Rule",
            "description": threat,
            "logic": [
                "Detect suspicious behavior",
                "Analyze indicators",
                "Identify malicious activity"
            ],
            "severity": "high",
            "created_at": datetime.utcnow().isoformat()
        }