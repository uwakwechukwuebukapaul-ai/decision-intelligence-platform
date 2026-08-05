class AttackPathGenerator:
    """
    Generates possible attacker paths.
    """


    def generate(
        self,
        initial_vector,
        objective
    ):

        return {

            "status": "path_generated",

            "initial_vector": initial_vector,

            "objective": objective,

            "path": [

                {
                    "stage": "entry",

                    "technique": initial_vector

                },

                {
                    "stage": "movement",

                    "technique": "lateral_movement"

                },

                {
                    "stage": "objective",

                    "technique": objective

                }

            ]

        }