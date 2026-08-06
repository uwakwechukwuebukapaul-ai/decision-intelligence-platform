from datetime import datetime


class ActionExecutor:


    def execute(
        self,
        action,
        context
    ):

        result = {

            "action": action,

            "indicator": context.get(
                "indicator"
            ),

            "status": "completed",

            "executed_at":
                datetime.utcnow().isoformat()

        }


        return result



    def execute_actions(
        self,
        actions,
        context
    ):

        results = []


        for action in actions:

            results.append(

                self.execute(
                    action,
                    context
                )

            )


        return results