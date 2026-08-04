class IndicatorMatcher:

    def match(self, event):
        indicators = []

        keywords = [
            "ransomware",
            "powershell",
            "malware",
            "phishing",
            "credential"
        ]

        for keyword in keywords:
            if keyword.lower() in event.lower():
                indicators.append(keyword)

        return indicators