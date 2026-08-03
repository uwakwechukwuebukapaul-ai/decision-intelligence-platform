from datetime import datetime


class DecisionPipeline:



    def build(
        self,
        research,
        prediction,
        planning,
        execution,
        investment,
        executive
    ):


        return {


            "research":
                research,


            "prediction":
                prediction,


            "planning":
                planning,


            "execution":
                execution,


            "investment":
                investment,


            "executive":
                executive,


            "created_at":
                datetime.utcnow().isoformat()

        }