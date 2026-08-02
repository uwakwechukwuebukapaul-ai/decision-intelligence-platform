from datetime import datetime

from .memory_state import MemoryState
from .memory_store import MemoryStore



class MemoryController:


    def __init__(self, user_id):

        self.user_id = user_id



    def generate_memory_state(self):


        state = MemoryState(
            self.user_id
        ).generate()



        memory = MemoryStore().retrieve()



        return {


            "user_id":

                self.user_id,



            "memory_status":

                "active",



            "memory_score":

                99,



            "memory_state":

                state,



            "memory_store":

                memory,



            "generated_at":

                datetime.utcnow().isoformat(),



            "version":

                "1.0"

        }