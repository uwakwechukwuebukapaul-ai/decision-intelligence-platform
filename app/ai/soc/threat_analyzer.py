from datetime import datetime



class ThreatAnalyzer:


    def analyze(
        self,
        evidence
    ):


        risk_score = 0

        threats = []



        for item in evidence:


            text = item.lower()



            if "phishing" in text:

                risk_score += 30

                threats.append(
                    "Phishing activity detected"
                )



            if "malware" in text:

                risk_score += 40

                threats.append(
                    "Malware indicator detected"
                )



            if "credential" in text:

                risk_score += 30

                threats.append(
                    "Credential compromise risk"
                )



        if risk_score >= 70:

            severity = "critical"

        elif risk_score >= 40:

            severity = "high"

        else:

            severity = "low"



        return {


            "risk_score":
                risk_score,


            "severity":
                severity,


            "threats":
                threats,


            "timestamp":
                datetime.utcnow().isoformat()

        }