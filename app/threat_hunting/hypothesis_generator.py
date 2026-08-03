from datetime import datetime


class HypothesisGenerator:


    def generate(self, intelligence):


        text = str(intelligence).lower()


        hypotheses=[]


        if "ransomware" in text:

            hypotheses.append(
                "Threat actor may have gained initial access before encryption activity"
            )


        if "phishing" in text:

            hypotheses.append(
                "Compromised credentials may be used for unauthorized access"
            )


        if not hypotheses:

            hypotheses.append(
                "Unknown threat behaviour requires investigation"
            )


        return {

            "hypotheses": hypotheses,

            "count": len(hypotheses),

            "timestamp":
                datetime.utcnow().isoformat()

        }