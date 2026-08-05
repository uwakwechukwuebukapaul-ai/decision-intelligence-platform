class ResponseCoordinator:
    """
    Coordinates autonomous SOC response activities.
    """

    def __init__(self):
        self.actions = []

    def execute_response(self, incident):
        action = {
            "incident": incident,
            "status": "response_planned"
        }

        self.actions.append(action)

        return action

    def get_actions(self):
        return self.actions