class ScenarioEngine:
    """
    Builds cyber attack scenarios.
    """


    def create(
        self,
        name,
        conditions=None
    ):

        return {

            "scenario": name,

            "conditions": conditions or {},

            "events": [

                "reconnaissance",

                "initial_access",

                "execution",

                "impact"

            ],

            "status": "scenario_created"

        }