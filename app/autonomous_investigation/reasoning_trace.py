"""
Sentinel DNA Reasoning Trace

Stores explainable AI investigation decisions.
"""


from datetime import datetime



class ReasoningTrace:



    def __init__(self):

        self.events = []



    def add(
        self,
        stage: str,
        reasoning: str,
    ):


        event = {


            "stage":

                stage,


            "reasoning":

                reasoning,


            "timestamp":

                datetime.utcnow().isoformat(),

        }


        self.events.append(
            event
        )


        return event



    def export(self):

        return self.events