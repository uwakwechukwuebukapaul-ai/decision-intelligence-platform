from datetime import datetime


class NetworkConnector:


    def connect(self):

        return {

            "sources":
                [
                    "Firewall",
                    "IDS",
                    "Proxy"
                ],

            "status":
                "connected",

            "timestamp":
                datetime.utcnow().isoformat()

        }