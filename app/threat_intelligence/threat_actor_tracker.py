from datetime import datetime


class ThreatActorTracker:


    def track(self,event):

        return {

            "actor":

                "Unknown Ransomware Operator",

            "behavior":

                [

                    "PowerShell execution",

                    "Enterprise targeting"

                ],

            "confidence":

                "high",

            "timestamp":

                datetime.utcnow().isoformat()

        }