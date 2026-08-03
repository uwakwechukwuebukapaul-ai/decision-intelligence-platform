from datetime import datetime


class AlertTuner:


    def optimize(self,event):

        return {

            "false_positive_reduction":
                "enabled",

            "severity_adjustment":
                "critical",

            "priority":
                "high",

            "timestamp":
                datetime.utcnow().isoformat()

        }