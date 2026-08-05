class DecisionCycle:
    """
    Autonomous SOC decision loop:

    Observe
    Understand
    Decide
    Act
    """

    def execute(
        self,
        event,
        intelligence
    ):

        return {

            "phase": [

                "observe",

                "understand",

                "decide",

                "act"

            ],

            "decision": self.make_decision(
                event
            ),

            "status": "decision_completed"

        }


    def make_decision(self,event):

        event_lower = event.lower()


        if "ransomware" in event_lower:

            return {

                "action":
                    "contain_host",

                "priority":
                    "critical"

            }


        if "powershell" in event_lower:

            return {

                "action":
                    "investigate_execution",

                "priority":
                    "high"

            }


        return {

            "action":
                "monitor",

            "priority":
                "medium"

        }