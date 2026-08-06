"""
Sentinel DNA - Investigation Pipeline State

Tracks investigation execution stages.
"""


from datetime import datetime



class PipelineState:


    def __init__(self):

        self.events = []



    def add(
        self,
        stage: str,
        message: str,
    ):

        event = {

            "stage": stage,

            "message": message,

            "timestamp":
            datetime.utcnow().isoformat()

        }


        self.events.append(event)


        return event



    def history(self):

        return self.events