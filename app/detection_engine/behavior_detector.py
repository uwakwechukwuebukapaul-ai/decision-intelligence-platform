from datetime import datetime


class BehaviorDetector:


    def analyze(self,event):

        behaviors=[]


        if "PowerShell" in event:

            behaviors.append(
                "Command Execution"
            )


        if "ransomware" in event.lower():

            behaviors.append(
                "Encryption Behavior"
            )


        return {

            "identified_behaviors":
                behaviors,

            "risk":
                "critical"
                if behaviors else "low",

            "timestamp":
                datetime.utcnow().isoformat()

        }