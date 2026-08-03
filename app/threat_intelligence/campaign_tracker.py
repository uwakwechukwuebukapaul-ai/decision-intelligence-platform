from datetime import datetime


class CampaignTracker:


    def identify(self,event):

        return {

            "campaign":

                "Ransomware Campaign",

            "phases":

                [

                    "Initial Access",

                    "Execution",

                    "Encryption",

                    "Impact"

                ],

            "timestamp":

                datetime.utcnow().isoformat()

        }