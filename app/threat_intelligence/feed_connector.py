from datetime import datetime


class FeedConnector:


    def lookup(self, event):

        return {

            "sources":
                [
                    "Threat Intelligence Feeds",
                    "Malware Database",
                    "IOC Repository"
                ],

            "matches":
                True,

            "timestamp":
                datetime.utcnow().isoformat()

        }