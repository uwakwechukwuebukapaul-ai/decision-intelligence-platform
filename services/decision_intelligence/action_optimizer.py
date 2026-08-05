class ActionOptimizer:

    def optimize(self, strategy):

        actions = {

            "respond":
                "execute automated response",

            "investigate":
                "launch investigation workflow",

            "monitor":
                "continue observation",

            "observe":
                "collect additional intelligence"
        }


        return actions.get(
            strategy,
            "no action"
        )