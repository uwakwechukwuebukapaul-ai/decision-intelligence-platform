class ReputationEngine:

    HIGH_RISK_INDICATORS = [
        "ransomware",
        "malware",
        "credential",
        "powershell"
    ]

    CRITICAL_INDICATORS = [
        "data_exfiltration",
        "confirmed_breach",
        "active_encryption",
        "domain_controller_compromise"
    ]


    def evaluate(self, indicators):

        risk_score = 0


        for indicator in indicators:

            if indicator in self.HIGH_RISK_INDICATORS:
                risk_score += 40

            if indicator in self.CRITICAL_INDICATORS:
                risk_score += 70


        if risk_score >= 100:
            risk_level = "CRITICAL"

        elif risk_score >= 40:
            risk_level = "HIGH"

        elif risk_score >= 20:
            risk_level = "MEDIUM"

        else:
            risk_level = "LOW"


        return {
            "risk_level": risk_level,
            "risk_score": risk_score,
            "indicator_count": len(indicators)
        }