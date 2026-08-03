from datetime import datetime


class AnalystWorkflow:



    def assign(self, case):


        return {

            "assigned_team":
                "SOC Investigation Team",

            "priority":
                case["severity"],

            "workflow":

                [

                    "Analyze evidence",

                    "Validate threat",

                    "Contain incident",

                    "Document findings"

                ],

            "timestamp":
                datetime.utcnow().isoformat()

        }