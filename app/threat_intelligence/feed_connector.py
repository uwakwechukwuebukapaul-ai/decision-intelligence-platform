from datetime import datetime


class FeedConnector:


    def enrich(self, event):

        return {

            "sources": [

                "Threat Intelligence Feeds",

                "Malware Intelligence",

                "IOC Databases"

            ],

            "matches": [

                "Ransomware activity",

                "Known attacker behavior"

            ],

            "timestamp": datetime.utcnow().isoformat()

        }