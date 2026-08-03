from datetime import datetime


class TacticMapper:


    def map(self, event):

        tactics = []


        if "powershell" in event.lower():

            tactics.append(
                "Execution"
            )


        if "ransomware" in event.lower():

            tactics.append(
                "Impact"
            )


        return {

            "tactics":
                tactics,

            "timestamp":
                datetime.utcnow().isoformat()
        }