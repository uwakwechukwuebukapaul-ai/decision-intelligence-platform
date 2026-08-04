from datetime import datetime, timezone


class ExecutionTrace:

    def __init__(self):

        self.events = []


    def start(self, service):

        event = {
            "service": service,
            "event": "started",
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.events.append(event)

        return event


    def complete(self, service):

        event = {
            "service": service,
            "event": "completed",
            "timestamp": datetime.now(
                timezone.utc
            ).isoformat()
        }

        self.events.append(event)

        return event


    def list_events(self):

        return self.events