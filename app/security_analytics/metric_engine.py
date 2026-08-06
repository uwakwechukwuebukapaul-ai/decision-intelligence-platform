class MetricEngine:


    def calculate(self, analysis):

        score = analysis["score"]


        if score >= 80:

            severity = "critical"

        elif score >= 60:

            severity = "high"

        elif score >= 40:

            severity = "medium"

        else:

            severity = "low"


        return {

            "score": score,

            "severity": severity

        }