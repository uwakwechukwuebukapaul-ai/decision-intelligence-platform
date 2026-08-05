class AutonomousController:

    def __init__(self):
        self.mode = "autonomous"

    def evaluate(self, event):
        return {
            "controller": "AutonomousController",
            "event": event,
            "decision": "route_for_analysis"
        }

    def set_mode(self, mode):
        self.mode = mode

        return {
            "mode": self.mode
        }