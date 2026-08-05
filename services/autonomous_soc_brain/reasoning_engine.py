class ReasoningEngine:

    def analyze(self, event):

        keywords = []

        for word in [
            "ransomware",
            "malware",
            "powershell",
            "phishing",
            "credential"
        ]:
            if word in event.lower():
                keywords.append(word)

        return {
            "threat_indicators": keywords,
            "event_type": "security_event"
        }