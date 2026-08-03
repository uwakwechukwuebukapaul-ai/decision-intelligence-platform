from datetime import datetime



class ScenarioEngine:



    def create_scenario(
        self,
        environment
    ):


        if environment == "manual_soc":


            return {

                "model":
                    "Manual SOC",

                "alerts_per_day":
                    1000,

                "automation":
                    0,

                "investigation_time_minutes":
                    45

            }



        if environment == "ai_assisted_soc":


            return {

                "model":
                    "AI Assisted SOC",

                "alerts_per_day":
                    1000,

                "automation":
                    60,

                "investigation_time_minutes":
                    15

            }



        if environment == "autonomous_soc":


            return {

                "model":
                    "Autonomous SOC",

                "alerts_per_day":
                    1000,

                "automation":
                    90,

                "investigation_time_minutes":
                    5

            }



        return {

            "model":
                "Unknown",

            "automation":
                0

        }