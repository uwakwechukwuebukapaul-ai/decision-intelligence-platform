from datetime import datetime


class PlatformLogger:


    def record(self, alert, workflow):

        return {

            "event":

                "SOC investigation executed",

            "alert":

                alert,

            "workflow_status":

                workflow["status"],

            "timestamp":

                datetime.utcnow().isoformat()

        }