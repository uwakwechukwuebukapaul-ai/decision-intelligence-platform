class RuleGenerator:

    def generate(self, patterns):

        rules = []

        for pattern in patterns:

            rules.append(
                {
                    "rule_name": f"Detect {pattern}",
                    "severity": "HIGH"
                }
            )

        return rules