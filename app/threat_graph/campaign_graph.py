from datetime import datetime


class CampaignGraph:


    def build(self, event):

        return {

            "campaign": "Unknown Ransomware Campaign",

            "nodes": [
                "Threat Actor",
                "Malware",
                "Target Asset"
            ],

            "relationship":
                "actor-controls-campaign",

            "timestamp":
                datetime.utcnow().isoformat()
        }