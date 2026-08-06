"""
Sentinel DNA Response Engine

SOAR decision execution layer.
"""


from .playbooks.containment import ContainmentPlaybook
from .playbook_engine import PlaybookEngine



class ResponseEngine:


    def __init__(self):

        self.playbook_engine = PlaybookEngine()

        self.containment = ContainmentPlaybook()



    def respond(
        self,
        decision: dict
    ):


        if decision.get("decision") == "contain":


            return self.containment.execute(

                decision.get(
                    "indicator",
                    "unknown"
                )

            )


        return {


            "status":
                "no_action",


            "reason":
                "Decision does not require automation"

        }