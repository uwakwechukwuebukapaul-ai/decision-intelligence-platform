from datetime import datetime


class FalsePositiveAnalyzer:

    def analyze(self, threat):

        return {

            "false_positive_risk":
                "medium",

            "optimization": [
                "Add user context",
                "Add asset criticality",
                "Increase event correlation"
            ],

            "timestamp":
                datetime.utcnow().isoformat()
        }