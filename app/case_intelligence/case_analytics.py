from datetime import datetime


class CaseAnalytics:
    """
    Generates SOC case intelligence metrics.
    """


    def analyze(self, cases):

        total = len(cases)

        critical = len(
            [
                c for c in cases
                if c.get("severity") == "critical"
            ]
        )

        return {
            "total_cases": total,
            "critical_cases": critical,
            "risk_level":
                "high" if critical else "normal",
            "generated_at":
                datetime.utcnow().isoformat()
        }