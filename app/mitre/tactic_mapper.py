class TacticMapper:

    def map(self, technique):

        mappings = {

            "T1583.001": "Resource Development",

            "T1595": "Reconnaissance",

        }

        return mappings.get(
            technique,
            "Unknown"
        )