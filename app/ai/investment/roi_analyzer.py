from datetime import datetime


class ROIAnalyzer:


    def analyze(self, market_signal):


        opportunities = []


        if market_signal:


            opportunities.append(
                "Growing cybersecurity automation demand"
            )


            opportunities.append(
                "Enterprise SOC efficiency improvement opportunity"
            )


            opportunities.append(
                "AI-native security investigation market gap"
            )


        return {


            "roi_score":
                85,


            "opportunities":
                opportunities,


            "growth_prediction":
                "Strong long-term potential",


            "timestamp":
                datetime.utcnow().isoformat()

        }