from datetime import datetime


class SIEMConnector:


    def connect(self):

        return {

            "platforms":
                [
                    "Microsoft Sentinel",
                    "Splunk",
                    "Elastic Security"
                ],

            "status":
                "connected",

            "timestamp":
                datetime.utcnow().isoformat()

        }