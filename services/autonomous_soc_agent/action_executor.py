class ActionExecutor:
    """
    Executes approved SOC actions.
    """

    def execute(
        self,
        action
    ):

        supported_actions = {

            "collect evidence":
                "Evidence collection initiated",

            "contain asset":
                "Asset containment recommended",

            "block indicator":
                "Indicator blocking recommended"

        }


        result = supported_actions.get(

            action.lower(),

            "Action requires analyst approval"

        )


        return {

            "action":
                action,

            "result":
                result,

            "execution_status":
                "completed"

        }