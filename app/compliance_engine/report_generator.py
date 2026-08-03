from datetime import datetime


class ReportGenerator:

    def generate(self, incident):

        return {
            "incident": incident,
            "report_type": "Enterprise Compliance Report",
            "sections": [
                "Incident Summary",
                "Evidence Review",
                "Control Assessment",
                "Compliance Mapping",
                "Recommendations"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }