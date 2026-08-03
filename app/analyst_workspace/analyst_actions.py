from datetime import datetime


class AnalystActions:


    def available(self, incident):

        return {

            "actions":

            [

                "Investigate",

                "Contain",

                "Start Hunt",

                "Create Report",

                "Escalate"

            ],

            "approval":

                "required",

            "timestamp":

                datetime.utcnow().isoformat()

        }