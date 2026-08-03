from datetime import datetime


class CampaignGraph:


    def track(self,event):

        return {

            "campaign":
                "Ransomware Campaign",

            "phases":[

                "Execution",

                "Encryption",

                "Impact"

            ],

            "timestamp":
            datetime.utcnow().isoformat()

        }