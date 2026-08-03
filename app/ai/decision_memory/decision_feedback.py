from datetime import datetime


class DecisionFeedback:
    """
    Decision Feedback Layer

    Responsibilities:
    - Record decision outcomes
    - Measure success/failure
    - Create learning signals
    """


    def __init__(self):

        self.feedback_history = []



    def record_outcome(
        self,
        decision_id,
        outcome,
        success
    ):

        feedback = {

            "decision_id":
                decision_id,


            "outcome":
                outcome,


            "success":
                success,


            "created_at":
                datetime.utcnow().isoformat()

        }


        self.feedback_history.append(
            feedback
        )


        return {

            "status":
                "recorded",


            "feedback":
                feedback

        }



    def get_feedback(
        self,
        decision_id=None
    ):


        if decision_id:


            results = [

                item

                for item in self.feedback_history

                if item["decision_id"] == decision_id

            ]


        else:


            results = self.feedback_history



        return {

            "count":
                len(results),


            "feedback":
                results

        }



    def success_rate(self):


        total = len(
            self.feedback_history
        )


        if total == 0:

            return {

                "success_rate":
                    0

            }


        successful = len(

            [

                item

                for item in self.feedback_history

                if item["success"]

            ]

        )


        return {

            "total":
                total,


            "successful":
                successful,


            "success_rate":
                round(
                    (successful / total) * 100,
                    2
                )

        }