class AssignmentEngine:
    """
    Assigns incidents to SOC analysts.
    """


    def __init__(self):

        self.team = [

            "SOC Analyst 1",

            "SOC Analyst 2",

            "Threat Hunter"

        ]

        self.index = 0



    def assign(
        self
    ):

        analyst = self.team[
            self.index
        ]


        self.index = (
            self.index + 1
        ) % len(self.team)


        return analyst