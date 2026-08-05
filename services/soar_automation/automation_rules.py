class AutomationRules:
    """
    Determines when automation should execute.
    """

    def __init__(self):

        self.rules = [
            {
                "condition": "critical_risk",
                "action": "auto_containment"
            },
            {
                "condition": "high_confidence_ioc",
                "action": "block_indicator"
            }
        ]

    def evaluate(self, context):

        matches = []

        for rule in self.rules:

            if rule["condition"] in str(context):

                matches.append(rule)

        return matches