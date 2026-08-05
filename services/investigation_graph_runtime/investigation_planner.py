class InvestigationPlanner:
    """
    Builds investigation execution plans
    from generated hypotheses.
    """

    def __init__(self):
        self.status = "ready"

    def build(self, hypothesis):

        steps = []

        for item in hypothesis.get("hypotheses", []):

            steps.append(
                {
                    "action": "investigate",
                    "target": item,
                    "status": "pending"
                }
            )

        return {
            "steps": steps,
            "priority": self.calculate_priority(steps)
        }


    def calculate_priority(self, steps):

        if len(steps) >= 3:
            return "critical"

        if len(steps) > 0:
            return "high"

        return "low"