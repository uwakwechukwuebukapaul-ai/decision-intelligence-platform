from datetime import datetime


class BehaviorHunter:


    def analyze(self, event):

        behaviors = []


        if "powershell" in event.lower():

            behaviors.append(
                "Command execution"
            )


        if "ransomware" in event.lower():

            behaviors.append(
                "Encryption activity"
            )


        return {

            "behaviors":
                behaviors,

            "risk":
                "high",

            "timestamp":
                datetime.utcnow().isoformat()

        }