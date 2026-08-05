class PriorityEngine:

    def calculate(self, risk):

        level = risk.get("risk_level", "low")

        priorities = {
            "critical": "P1",
            "high": "P2",
            "medium": "P3",
            "low": "P4"
        }

        return priorities.get(level, "P4")