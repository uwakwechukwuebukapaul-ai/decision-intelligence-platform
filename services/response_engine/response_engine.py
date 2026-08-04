from .response_model import ResponseModel


class ResponseEngine:
    """
    Converts decisions into autonomous response plans.
    """


    def execute(
        self,
        decision
    ):

        decision_type = decision.get(
            "decision",
            "monitor"
        )


        priority = decision.get(
            "priority",
            "low"
        )


        actions = decision.get(
            "actions",
            []
        )


        if decision_type == "contain_immediately":

            return ResponseModel(

                response_type="containment",

                priority=priority,

                actions=actions,

                execution_state="ready",

                metadata={

                    "automation":
                        True,

                    "approval_required":
                        False

                }

            ).to_dict()



        if decision_type == "investigate":

            return ResponseModel(

                response_type="investigation",

                priority=priority,

                actions=actions,

                execution_state="ready",

                metadata={

                    "automation":
                        False,

                    "approval_required":
                        True

                }

            ).to_dict()



        return ResponseModel(

            response_type="monitoring",

            priority=priority,

            actions=actions,

            execution_state="planned",

            metadata={

                "automation":
                    False

            }

        ).to_dict()