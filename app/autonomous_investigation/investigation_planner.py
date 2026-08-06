"""
Sentinel DNA Investigation Planner

Creates investigation steps from intelligence.
"""


class InvestigationPlanner:


    def create_plan(
        self,
        intelligence: dict,
    ):


        indicator = intelligence.get(
            "indicator",
            "unknown",
        )


        return {


            "indicator":

                indicator,


            "steps":

                [

                    {
                        "step": 1,
                        "action":
                            "Analyze indicator reputation",
                    },

                    {
                        "step": 2,
                        "action":
                            "Review threat context",
                    },

                    {
                        "step": 3,
                        "action":
                            "Map MITRE techniques",
                    },

                    {
                        "step": 4,
                        "action":
                            "Recommend analyst response",
                    },

                ],

            "status":

                "planned",

        }