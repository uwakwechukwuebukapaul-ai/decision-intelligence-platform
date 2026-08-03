from datetime import datetime


class BehaviorBaseline:


    def analyze(self, event):

        behaviors = []

        if "powershell" in event.lower():
            behaviors.append(
                "Command execution"
            )

        if "ransomware" in event.lower():
            behaviors.append(
                "Encryption behavior"
            )


        return {

            "detected_behaviors": behaviors,

            "baseline_status":
                "abnormal"
                if behaviors
                else "normal",

            "timestamp":
                datetime.utcnow().isoformat()

        }