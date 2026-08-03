from datetime import datetime


class ResponseOrchestrator:


    def recommend(self, alert):


        actions = []


        if alert["severity"] == "critical":

            actions = [

                "Isolate affected endpoint",

                "Block malicious indicators",

                "Start incident response workflow",

                "Notify security leadership"

            ]


        else:

            actions = [

                "Monitor activity",

                "Collect additional evidence"

            ]



        return {

            "recommended_actions":
                actions,

            "approval_required":
                alert["severity"] == "critical",

            "timestamp":
                datetime.utcnow().isoformat()

        }