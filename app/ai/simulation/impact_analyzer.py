from datetime import datetime



class ImpactAnalyzer:



    def analyze(
        self,
        scenario,
        roi
    ):


        impact = "low"



        if roi["automation_gain"] >= 80:

            impact = "transformational"


        elif roi["automation_gain"] >= 50:

            impact = "significant"



        return {


            "security_impact":
                impact,


            "analyst_workload_reduction":
                roi["automation_gain"],


            "business_value":
                "Improved SOC efficiency and faster incident response",


            "timestamp":
                datetime.utcnow().isoformat()

        }