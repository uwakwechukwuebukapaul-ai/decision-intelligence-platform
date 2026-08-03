from datetime import datetime


class DecisionLogger:


    def record(self, incident, actions):

        return {

            "event": "AI decision created",

            "incident": incident,

            "actions_logged": actions["actions"],

            "timestamp": datetime.utcnow().isoformat()

        }