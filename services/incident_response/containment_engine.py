class ContainmentEngine:

    def execute(self, actions):

        containment_actions = []

        for action in actions:

            if action in [
                "isolate_host",
                "block_indicator",
                "disable_account"
            ]:

                containment_actions.append(
                    {
                        "action": action,
                        "result": "contained"
                    }
                )

        return containment_actions