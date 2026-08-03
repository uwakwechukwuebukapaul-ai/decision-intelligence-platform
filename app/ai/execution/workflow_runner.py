from datetime import datetime


class WorkflowRunner:


    def run(
        self,
        actions
    ):

        results = []


        for action in actions:

            results.append({

                "action_id":
                    action["action_id"],

                "objective":
                    action["objective"],

                "status":
                    "completed",

                "completed_at":
                    datetime.utcnow().isoformat()

            })


        return {

            "executed":
                len(results),

            "results":
                results

        }