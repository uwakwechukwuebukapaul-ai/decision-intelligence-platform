from datetime import datetime


class PatternRecognition:

    def analyze(self, event):

        patterns = []

        keywords = {
            "ransomware": "Data encryption behavior",
            "powershell": "Command execution behavior",
            "phishing": "Credential theft behavior",
            "malware": "Malicious software behavior"
        }

        for key, value in keywords.items():

            if key.lower() in event.lower():
                patterns.append(value)


        return {
            "event": event,
            "patterns_detected": patterns,
            "risk": "high" if patterns else "low",
            "timestamp": datetime.utcnow().isoformat()
        }