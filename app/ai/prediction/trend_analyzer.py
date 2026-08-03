from datetime import datetime


class TrendAnalyzer:


    def analyze(
        self,
        knowledge
    ):

        trends = []


        for item in knowledge:

            text = item.lower()


            if "ai" in text:

                trends.append(
                    "Artificial intelligence adoption trend"
                )


            if "security" in text:

                trends.append(
                    "Cybersecurity demand trend"
                )


            if "automation" in text:

                trends.append(
                    "Automation growth trend"
                )


        if not trends:

            trends.append(
                "General market trend detected"
            )


        return {

            "trends": trends,

            "trend_count": len(trends),

            "timestamp":
                datetime.utcnow().isoformat()

        }