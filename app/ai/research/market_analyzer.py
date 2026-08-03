from datetime import datetime


class MarketAnalyzer:


    def analyze(self, evidence):


        score = 50


        if len(evidence) >= 3:

            score += 30


        if any(
            "automation" in item.lower()
            for item in evidence
        ):

            score += 10


        return {

            "market_score":
                min(score,95),


            "market_signal":
                "Strong AI SOC automation opportunity",


            "timestamp":
                datetime.utcnow().isoformat()

        }