from datetime import datetime


class DashboardBuilder:


    def create(self, incident):

        return {

            "dashboard":

            "SOC Analyst Dashboard",

            "metrics":

            {

                "risk_score": 100,

                "severity": "critical",

                "status": "active",

                "investigation": "running"

            },

            "timestamp":

                datetime.utcnow().isoformat()

        }