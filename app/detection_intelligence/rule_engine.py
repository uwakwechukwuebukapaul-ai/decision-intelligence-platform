class RuleEngine:


    def evaluate(self, event):

        rules = []

        if event.get("indicator"):
            rules.append("Malicious Indicator Detection")


        if event.get("severity") == "critical":
            rules.append("Critical Threat Detection")


        if event.get("identity"):
            rules.append("Identity Risk Detection")


        if event.get("asset"):
            rules.append("Asset Exposure Detection")


        return rules