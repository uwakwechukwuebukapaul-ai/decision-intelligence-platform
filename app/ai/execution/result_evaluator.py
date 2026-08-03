from datetime import datetime


class ResultEvaluator:


    def evaluate(
        self,
        workflow
    ):

        completed = 0


        for result in workflow["results"]:

            if result["status"] == "completed":

                completed += 1


        success_rate = 0


        if workflow["executed"]:

            success_rate = round(
                (completed / workflow["executed"]) * 100,
                2
            )


        return {

            "success_rate":
                success_rate,

            "evaluation":
                "successful"
                if success_rate >= 80
                else "needs_improvement",

            "timestamp":
                datetime.utcnow().isoformat()

        }