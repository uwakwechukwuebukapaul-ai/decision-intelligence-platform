from datetime import datetime


class CognitiveMemory:


    def __init__(self):

        self.memory_store = {

            "previous_decisions":
                0,

            "learning_patterns":
                [],

            "intelligence_history":
                []

        }



    def build_memory_context(
        self,
        user_id,
        consensus_result
    ):


        self.memory_store["previous_decisions"] += 1


        self.memory_store["learning_patterns"].append(

            consensus_result.get(
                "final_recommendation"
            )

        )


        self.memory_store["intelligence_history"].append(

            datetime.utcnow().isoformat()

        )



        return {


            "user_id":

                user_id,


            "memory_status":

                "active",


            "memory_cycles":

                self.memory_store[
                    "previous_decisions"
                ],


            "learned_patterns":

                self.memory_store[
                    "learning_patterns"
                ],


            "historical_intelligence":

                self.memory_store[
                    "intelligence_history"
                ],


            "memory_confidence":

                95

        }