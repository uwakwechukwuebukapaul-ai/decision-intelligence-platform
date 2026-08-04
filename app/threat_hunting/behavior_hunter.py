from datetime import datetime


class BehaviorHunter:

    def analyze(self, event):

        behaviors = []

        if "powershell" in event.lower():
            behaviors.append("Command and Scripting Interpreter")

        if "ransomware" in event.lower():
            behaviors.append("Encryption Activity")

        return {
            "identified_behaviors": behaviors,
            "risk": "critical" if behaviors else "medium",
            "timestamp": datetime.now().isoformat()
        }