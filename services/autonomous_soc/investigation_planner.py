class InvestigationPlanner:
    """
    Generates SOC investigation workflows.
    """


    def create_plan(
        self,
        incident
    ):


        steps = [

            "collect incident evidence",

            "identify affected assets",

            "extract indicators of compromise",

            "map attacker techniques",

            "evaluate containment actions"

        ]


        return steps