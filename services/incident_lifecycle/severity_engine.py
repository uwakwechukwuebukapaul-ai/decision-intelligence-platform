class SeverityEngine:
    """
    Calculates incident severity.
    """


    def calculate(
        self,
        threat_data
    ):

        score = 0


        text = threat_data.lower()


        if "ransomware" in text:
            score += 90


        if "malware" in text:
            score += 50


        if "credential" in text:
            score += 40


        if "admin" in text:
            score += 30


        if score >= 80:

            return "critical"


        elif score >= 50:

            return "high"


        elif score >= 20:

            return "medium"


        return "low"