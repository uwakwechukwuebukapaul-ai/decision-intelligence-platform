from datetime import datetime


class BehaviorAnalyzer:


    def analyze(self, event):

        patterns = []

        text = event.lower()

        if "powershell" in text:
            patterns.append(
                "Command execution"
            )

        if "ransomware" in text:
            patterns.append(
                "Encryption behavior"
            )


        return {

            "patterns":
                patterns,

            "risk":
                "high"
                if patterns
                else "low",

            "timestamp":
                datetime.utcnow().isoformat()

        }