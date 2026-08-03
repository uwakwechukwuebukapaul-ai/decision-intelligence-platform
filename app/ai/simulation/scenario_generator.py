from datetime import datetime


class ScenarioGenerator:
    """
    Generates possible strategic scenarios.
    """


    def generate(
        self,
        mission,
        intelligence
    ):

        scenarios = []


        scenarios.append(
            {
                "scenario":
                    "Execute current strategy",

                "mission":
                    mission,

                "intelligence":
                    intelligence
            }
        )


        scenarios.append(
            {
                "scenario":
                    "Delay execution and gather more data",

                "mission":
                    mission,

                "intelligence":
                    intelligence
            }
        )


        return {

            "count":
                len(scenarios),

            "scenarios":
                scenarios,

            "timestamp":
                datetime.utcnow().isoformat()

        }