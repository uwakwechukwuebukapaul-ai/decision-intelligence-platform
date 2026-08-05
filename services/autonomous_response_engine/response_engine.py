class ResponseEngine:
    """
    Core response decision engine.
    """

    def generate_plan(self, incident):

        return {
            "incident": incident,
            "actions": [
                "analyze threat",
                "contain affected asset",
                "collect evidence"
            ]
        }


    def prioritize(self, actions):

        return actions