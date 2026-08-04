from datetime import datetime


class ResponseCoordinator:


    def prepare(self,decision):

        return {


            "actions":[

                "Validate threat",

                "Contain affected systems",

                "Block malicious indicators",

                "Collect forensic evidence",

                "Start recovery workflow"

            ],


            "decision":
                decision["decision"],


            "status":
                "ready",


            "timestamp":
                datetime.utcnow().isoformat()

        }