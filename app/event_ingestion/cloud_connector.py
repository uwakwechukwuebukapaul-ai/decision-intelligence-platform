from datetime import datetime


class CloudConnector:


    def connect(self):

        return {

            "providers":
                [
                    "AWS",
                    "Azure",
                    "Google Cloud"
                ],

            "status":
                "connected",

            "timestamp":
                datetime.utcnow().isoformat()

        }