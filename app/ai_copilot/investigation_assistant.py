from datetime import datetime


class InvestigationAssistant:
    """
    Helps analysts investigate incidents.
    """


    def assist(
        self,
        incident
    ):

        return {

            "incident":
                incident,


            "investigation_steps":

                [

                    "Collect evidence",

                    "Analyze indicators of compromise",

                    "Review user activity",

                    "Map attacker behaviour",

                    "Determine containment strategy"

                ],


            "timestamp":
                datetime.utcnow().isoformat()

        }