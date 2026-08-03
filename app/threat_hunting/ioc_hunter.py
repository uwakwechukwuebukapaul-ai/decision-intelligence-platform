from datetime import datetime


class IOCHunter:


    def search(self, event):

        matches = []


        if "malicious" in event.lower():

            matches.append(
                "Suspicious indicator detected"
            )


        return {

            "matched_indicators":
                matches,

            "status":
                "completed",

            "timestamp":
                datetime.utcnow().isoformat()

        }