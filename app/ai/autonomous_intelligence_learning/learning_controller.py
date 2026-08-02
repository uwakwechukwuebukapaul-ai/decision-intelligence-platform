from datetime import datetime

from .learning_state import LearningState
from .learning_engine import LearningEngine
from .knowledge_processor import KnowledgeProcessor


class LearningController:


    def __init__(self, user_id):

        self.user_id = user_id



    def generate_learning_cycle(self):


        state = LearningState(
            self.user_id
        ).generate()



        learning = LearningEngine().process()



        knowledge = KnowledgeProcessor().analyze()



        return {


            "user_id":

                self.user_id,


            "learning_status":

                "active",


            "learning_score":

                99,


            "learning_state":

                state,


            "learning_engine":

                learning,


            "knowledge_processing":

                knowledge,


            "generated_at":

                datetime.utcnow().isoformat(),


            "version":

                "1.0"

        }