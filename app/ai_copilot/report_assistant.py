from datetime import datetime


class ReportAssistant:

    def generate(self, incident):

        return {

            "report_sections": [
                "Incident Overview",
                "Technical Findings",
                "Threat Analysis",
                "Business Impact",
                "Recommendations"
            ],

            "report_type":
                "AI Generated SOC Report",

            "timestamp":
                datetime.utcnow().isoformat()
        }