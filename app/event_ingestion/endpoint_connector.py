from datetime import datetime


class EndpointConnector:


    def connect(self):

        return {

            "sources":
                [
                    "EDR",
                    "XDR",
                    "Endpoint Logs"
                ],

            "status":
                "connected",

            "timestamp":
                datetime.utcnow().isoformat()

        }