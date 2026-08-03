from datetime import datetime


class RiskAnalyzer:


    def analyze(self, intelligence):


        risks = []


        if intelligence:

            risks.append(
                "Enterprise cybersecurity market is highly competitive"
            )


            risks.append(
                "Trust and compliance requirements may slow adoption"
            )


            risks.append(
                "Large security vendors have existing market presence"
            )


        risk_score = 30


        return {


            "risk_score":
                risk_score,


            "risk_level":
                "medium",


            "risks":
                risks,


            "timestamp":
                datetime.utcnow().isoformat()

        }