from datetime import datetime


class ReportGenerator:
    """
    Generates SOC investigation reports.
    """

    def create(self, incident):

        return {
            "generated_at": datetime.utcnow().isoformat(),
            "incident": incident,
            "summary": "Security investigation report generated.",
            "sections": {
                "impact": "Under analysis",
                "timeline": [],
                "recommendations": []
            }
        }