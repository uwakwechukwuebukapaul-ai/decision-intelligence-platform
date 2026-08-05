class SOCMetrics:
    """
    SOC performance measurement engine.
    """

    def __init__(self):
        self.total_cases = 0
        self.severity_count = {}

    def record_case(self, case):

        self.total_cases += 1

        severity = case.get(
            "severity",
            "unknown"
        )

        self.severity_count[severity] = (
            self.severity_count.get(severity, 0) + 1
        )

    def summary(self):

        return {
            "total_cases": self.total_cases,
            "severity_distribution": self.severity_count,
        }