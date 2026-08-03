from datetime import datetime


class ThreatGraph:
    """
    Creates intelligence relationships.
    """


    def build(
        self,
        indicator,
        actor
    ):

        return {

            "nodes":

                [

                    indicator,

                    actor

                ],


            "relationship":

                "associated_with",


            "timestamp":

                datetime.utcnow().isoformat()

        }