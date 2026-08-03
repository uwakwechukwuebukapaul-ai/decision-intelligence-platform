from datetime import datetime


class SignatureEngine:


    def match(self, event):

        indicators = []

        keywords = [
            "ransomware",
            "malware",
            "powershell"
        ]

        for keyword in keywords:

            if keyword in event.lower():
                indicators.append(keyword)


        return {

            "indicators":
                indicators,

            "matched":
                len(indicators) > 0,

            "timestamp":
                datetime.utcnow().isoformat()

        }