class EvidenceAnalyzer:
    """
    Autonomous evidence examination engine.
    """


    def analyze(self, evidence):

        text = evidence.lower()

        indicators = []

        keywords = [
            "powershell",
            "malware",
            "ransomware",
            "phishing",
            "credential"
        ]


        for keyword in keywords:

            if keyword in text:
                indicators.append(keyword)


        return {

            "evidence": evidence,

            "indicators": indicators,

            "confidence":
                "high" if indicators else "low"

        }