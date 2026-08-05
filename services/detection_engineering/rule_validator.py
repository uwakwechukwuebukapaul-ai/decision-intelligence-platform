class RuleValidator:
    """
    Detection quality validation engine.
    """

    def validate(self, rule):

        issues = []

        if not rule.get("name"):
            issues.append(
                "Missing rule name"
            )

        if not rule.get("logic"):
            issues.append(
                "Missing detection logic"
            )

        return {
            "valid": len(issues) == 0,
            "issues": issues
        }