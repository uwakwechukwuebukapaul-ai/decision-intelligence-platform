"""
Audit Logger

Tracks autonomous intelligence decisions.
"""


from datetime import datetime, timezone



class AuditLogger:


    def __init__(self):

        self.events = []



    def record(
        self,
        action: str,
        details: dict,
    ):


        event = {

            "action": action,

            "details": details,

            "timestamp":
                datetime.now(
                    timezone.utc
                ).isoformat()

        }


        self.events.append(
            event
        )


        return event



    def history(self):

        return self.events