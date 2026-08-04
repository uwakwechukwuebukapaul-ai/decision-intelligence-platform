class PatternDetector:

    def detect(self, event):

        event_lower = event.lower()

        patterns = []

        indicators = {
            "powershell": "PowerShell execution",
            "ransomware": "Ransomware activity",
            "malware": "Malware indicator",
            "credential": "Credential access attempt",
            "database": "Database targeting"
        }

        for keyword, description in indicators.items():

            if keyword in event_lower:
                patterns.append(description)

        return patterns