"""
Sentinel DNA - Investigation Timeline
"""


from datetime import datetime



class InvestigationTimeline:


    def __init__(self):

        self.events = []



    def add_event(
        self,
        stage: str,
        message: str,
    ) -> dict:


        event = {

            "stage": stage,

            "message": message,

            "timestamp":
            datetime.utcnow().isoformat()

        }


        self.events.append(event)


        return event



    def get_events(self):

        return self.events