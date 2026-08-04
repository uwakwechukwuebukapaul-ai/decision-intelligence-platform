class ResponseExecutor:

    def run(self, actions):

        executed = []

        for action in actions:

            executed.append(
                {
                    "action": action,
                    "status": "executed"
                }
            )

        return executed