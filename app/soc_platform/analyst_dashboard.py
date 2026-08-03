from datetime import datetime


class AnalystDashboard:


    def __init__(self):

        self.metrics = {

            "active_incidents": 0,

            "risk_level": "normal"

        }



    def update(self, case, alert):


        self.metrics["active_incidents"] += 1

        self.metrics["risk_level"] = (
            alert["severity"]
        )


        return {

            "active_incidents":
                self.metrics["active_incidents"],

            "risk_level":
                self.metrics["risk_level"],

            "latest_case":
                case["case_id"],

            "timestamp":
                datetime.utcnow().isoformat()

        }