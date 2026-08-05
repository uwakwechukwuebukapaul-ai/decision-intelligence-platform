from datetime import datetime


class SLAEngine:
    """
    Tracks SOC response commitments.
    """

    SLA_TARGETS = {
        "critical": 15,
        "high": 60,
        "medium": 240,
        "low": 480,
    }

    def evaluate(self, case):

        severity = case.get("severity", "medium")

        return {
            "case_id": case["case_id"],
            "response_target_minutes": self.SLA_TARGETS.get(
                severity,
                240
            ),
            "evaluated_at": datetime.utcnow().isoformat(),
            "status": "within_target",
        }