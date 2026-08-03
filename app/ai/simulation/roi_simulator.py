from datetime import datetime



class ROISimulator:



    def calculate(
        self,
        scenario
    ):


        automation = scenario.get(
            "automation",
            0
        )


        savings = automation * 1.5


        efficiency = automation + 10



        return {


            "automation_gain":
                automation,


            "estimated_cost_reduction_percent":
                savings,


            "operational_efficiency":
                efficiency,


            "timestamp":
                datetime.utcnow().isoformat()

        }